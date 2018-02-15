#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import subprocess
import json 
import time
import sys
import os
import re

class honeypot_base(object):
    def __init__(self):
        #Validate arguments
        if len(sys.argv) != 3:
            print("Invalid arguments!")
            self.print_help()
            sys.exit()

        #get arguments
        self.config_file = sys.argv[1]
        self.argument = sys.argv[2]

        #Print init message
        self.log_string("Initialzed honeypot_base with config file - "+str(self.config_file)+" and arguments "+str(self.argument))

        #lists to check validtaion of arguments and config file
        self.valid_arg = ['start', 'stop', 'restart', 'create', 'destroy', 'recreate', 'auto']
        self.valid_config = ['name', 'base', 'base_folder', 'pcap_file', 'network_id', 'uuid']

        ##commands that we can use!
        #general
        self.cmd_clone = 'clonevm {0} --name {1} --basefolder "{2}"'
        self.cmd_import = 'import {0} --vsys 0 --vmname {1}'
        self.cmd_register = 'registervm "{0}"'
        self.cmd_delete = 'unregistervm {0} --delete'
        self.cmd_list_vms = 'list vms'
        #power
        self.cmd_list_running = 'list runningvms'
        self.cmd_start = 'startvm {0} --type headless'
        self.cmd_stop = 'controlvm {0} acpipowerbutton'
        self.cmd_stop_force = 'controlvm {0} poweroff'
        self.cmd_reset = 'controlvm {0} reset'
        #network
        self.cmd_list_hostonly = 'list hostonlyifs'
        self.cmd_create_hostonly = 'hostonlyif create'
        self.cmd_set_hostonly = 'modifyvm {0} --hostonlyadapter{1} {2}'
        self.cmd_network_nic = 'modifyvm {0} --nic{1} {2}'
        self.cmd_network_nictype = 'modifyvm {0} --nictype{1} {2}'
        self.cmd_network_pcap = 'modifyvm {0} --nictrace{1} on --nictracefile{1} "{2}"'

        #regular expressions to use!
        self.re_list = re.compile('\"([^\"]+)\" {([^}]+)}')
        #Did only catch ONE line..
        #self.re_list_hostonly = re.compile('^Name:\s+([A-z0-9]+)')
        self.re_list_hostonly = re.compile('Name:\s+(vboxnet[0-9]+)')
        self.re_create_hostonly = re.compile('\'([^\']+)\'')

        #Default value for config, and init it!!
        self.config = False

        #Initial validate and setup
        #read and validate config file
        if self.read_config() == False:
            self.log_string("Could not read config file..")
            sys.exit()
        
        #validate arguments
        if self.validate_argument() == False:
            self.log_string("Invalid argument given...")
            sys.exit()

        self.start()

    def log_string(self, log):
	str_time = time.strftime("%d-%m-%Y - %H:%M:%S");
	logStr = str_time+" "+log;
	print(logStr);
	return

    def print_help(self):
        print("Usage: python honeypot_base.py <config-file> <start|stop|restart|create|destroy|recreate|auto>")
        return True

    def start(self):
        if self.argument == 'start':
            self.vm_apply_pcap()
            self.vm_start()
        elif self.argument == 'stop':
            self.vm_stop()
        elif self.argument == 'restart':
            self.vm_stop()
            self.vm_apply_pcap()
            self.vm_start()
        elif self.argument == 'create':
            self.vm_create()
            self.vm_apply_network()
            self.vm_apply_pcap()
        elif self.argument == 'destroy':
            self.vm_destroy()
        elif self.argument == 'recreate':
            self.vm_destroy()
            self.vm_create()
            self.vm_apply_network()
            self.vm_apply_pcap()
        elif self.argument == 'auto':
            self.log_string("What did this do again?")
        else:
            self.log_string("WHAT!")
            return False

        return True

    def check_file(self, path):
        return os.path.isfile(path)

    def check_folder(self, path):
        return os.path.folder(path)

    def validate_argument(self):
        if self.argument not in self.valid_arg:
            self.log_string(self.argument+' is not a valid argument')
            return False
        return True

    def validate_config(self, config_json):
        #keep track of all the field (we require 1:1)
        found = 0
        #loop over config_json
        for key in config_json:
            if key not in self.valid_config:
                self.log_string(key+' is not a valid config key!')
                return False
            else:
                found += 1

        if len(self.valid_config) != found:
            self.log_string("Failed to find all fields in config!")
            return False

        return True

    def read_config(self):
        if self.check_file(self.config_file) == False:
            return False

        f = open(self.config_file, "r")
        data = f.read()
        f.close()

        try:
            config_data = json.loads(data)
        except:
            return False

        #check if valid config
        if self.validate_config(config_data) == False:
            return False

        self.config = config_data
        return True

    def update_config(self, key, value):
        if key not in self.valid_config:
            self.log_string("Not a valid key...? Stop this!")
            return False

        #update our config
        self.config[key] = value

        f = open(self.config_file, "w")
        f.write(json.dumps(self.config, indent=4, sort_keys=True))
        f.close()
        
        return True


    def execute(self, command):
        self.log_string("Trying to execute command - "+command)
        #append vboxmanage to all commands
        command = 'vboxmanage '+command
        try:
            output = subprocess.check_output(command, shell=True)                       
        except subprocess.CalledProcessError as grepexc:
            print("Error executing command: ", grepexc.returncode, grepexc.output)
            sys.exit()
            return False

        return output

    def vm_list(self, cmd, check_uuid = True, check_name = False):
        output = self.execute(cmd)
        if output == False:
            self.log_string("Could not execute command!")
            return False

        matches = self.re_list.findall(output)

        if len(matches) < 1:
            return False

        for match in matches:
            #check the uuid
            if check_uuid == True and match[1] == self.config['uuid']:
                return match
            if check_name == True and match[0] == self.config['name']:
                return match
        
        return False 

    def vm_exists(self):
        if self.vm_list(self.cmd_list_vms) != False:
            return True
        
        self.log_string("VM does not exists...")
        return False

    def vm_running(self):
        if self.vm_list(self.cmd_list_running) != False:
            return True

        self.log_string("VM is not turned on")
        return False

    def vm_start(self):
        if self.vm_exists() == False:
            return False

        if self.vm_running():
            self.log_string("VM already running, skipping")
            return True

        output = self.execute(self.cmd_start.format(self.config['uuid']))

        if "successfully started" in output:
            self.log_string("Starting VM!")
            return True

        self.log_string("Could not start VM!")
        return False

    def vm_stop(self):
        if self.vm_exists() == False:
            return False

        if self.vm_running() == False:
            self.log_string("VM already stopped, skipping")
            return True

        output = self.execute(self.cmd_stop_force.format(self.config['uuid']))

        if len(output) > 0 and '100%' not in output:
            self.log_string("Failed to stop VM!")
            return False

        self.log_string("Stopped vm!")
        return True 

    def vm_hostonly_exists(self, network_id):
        output = self.execute(self.cmd_list_hostonly)

        if output == False:
            return False

        networks = self.re_list_hostonly.findall(output)

        if networks == None:
            return False

        for network in networks:
            if network == network_id:
                return True

        return False

    def vm_hostonly_create(self):
        output = self.execute(self.cmd_create_hostonly)

        if output == False:
            return False

        match = self.re_create_hostonly.search(output)

        if match == None:
            self.log_string("Failed to create network")
            return False

        return match.group(1)

    def vm_apply_network(self):
        if self.vm_exists() == False:
            self.log_string("VM does not exists...")
            return False

        #make sure that it isn't running..
        if self.vm_running() == True:
            self.log_string('VM must not be running when chaning config..')
            return False

        #check if we need to create a hostonly one, or it exists...
        if len(self.config["network_id"]) < 1:
            self.log_string("Creating new host-only network")
            network = self.vm_hostonly_create()
            time.sleep(0.1)
            if network == False:
                self.log_string("Failed to create network")
                return False
            self.log_string("Created network - "+network)
            self.update_config("network_id", network)
        else:
            if self.vm_hostonly_exists(self.config['network_id']) == False:
                self.log_string("Hostonly network does not exists - "+str(self.config['network_id']))
                return False

        #Set all interfaces to none (1-4) - so we know what is connected...
        for nic in range(1,5):
            output = self.execute(self.cmd_network_nic.format(self.config['uuid'], str(nic), "none"))
            time.sleep(0.1)
            if len(output) > 0:
                self.log_string("Failed to set network interface to none...")
                return False

        #Set interface 1 to nat
        output = self.execute(self.cmd_network_nic.format(self.config['uuid'], "1", "nat"))
        time.sleep(0.1)

        if len(output) > 0:
            self.log_string("Failed to set nic1 to NAT")
            return False

        #set hardware type for interface 1
        output = self.execute(self.cmd_network_nictype.format(self.config['uuid'], "1", "82540EM"))
        time.sleep(0.1)

        if len(output) > 0:
            self.log_string("Failed to set type for nic1")
            return False

        #set nic 2 to hostonly
        output = self.execute(self.cmd_network_nic.format(self.config['uuid'], "2", "hostonly"))
        time.sleep(0.1)

        if len(output) > 0:
            self.log_string("Failed to set nic2 to host-only")
            return False

        #set hardware type for interface 2
        output = self.execute(self.cmd_network_nictype.format(self.config['uuid'], "2", "82540EM"))
        time.sleep(0.1)

        if len(output) > 0:
            self.log_string("Failed to set type for nic2")
            return False

        #set host-only network id
        output = self.execute(self.cmd_set_hostonly.format(self.config['uuid'], "2", self.config['network_id'])) 
        time.sleep(0.1)

        if len(output) > 0:
            self.log_string("Failed to set hostonly network - "+self.config['network_id']+" for nic2")
            return False

        return True

    def vm_apply_pcap(self):
        if self.vm_exists() == False:
            self.log_string("VM does not exists...")
            return False

        #make sure that it isn't running..
        if self.vm_running() == True:
            self.log_string('VM must not be running when chaning config..')
            return False

        output = self.execute(self.cmd_network_pcap.format(self.config['uuid'], '1', self.config['pcap_file']))

        if len(output) > 0:
            self.log_string("Could not specify pcap location")
            return False

        return True
    
    def vm_destroy(self):
        #check if machine exists
        if self.vm_exists() == False:
            self.log_string("Machine does not exist")
            return False

        #make sure that it isn't running..
        if self.vm_running() == True:
            self.log_string('VM must not be running when deleting..')
            return False

        output = self.execute(self.cmd_delete.format(self.config['uuid']))

        if len(output) > 0 and '100%' not in output:
            self.log_string("Failed to delete :-")
            return False

        #lets update the config real quick...
        self.update_config('uuid', '')

        return True

    def vm_create(self):
        #check if machine exists
        if self.vm_exists():
            self.log_string("Machine exists, destroy before creating it!")
            return False

        #check if a UUID is already set, if so say
        if len(self.config['uuid']) > 0:
            self.log_string('Already a UUID, how?')
            return False

        #check if vm with that name exists exists
        if self.vm_list(self.cmd_list_vms, check_uuid = False, check_name=True) != False:
            self.log_string('VM with that name already exists..?')
            return False

        #check if .ova or we need to clone
        if self.config['base'][-4:] == ".ova" or self.config['base'][-4:] == ".ovf":
            self.log_string("PLEASE STOP!")
            return False
            #does the file exist??
            if self.check_file(self.config['base']) == False:
                self.log_string("File does not exist for importing?")
                return False

            self.log_string("Importing ova/ovf file - "+str(self.config['base'])+" - might take a while...")
            output = self.execute(self.cmd_import.format(self.config['base'], self.config['name'], self.config['base_folder']))

            if "Successfully imported" not in output:
                self.log_string("Failed to import image...")
                return False
        #we are cloning I guess?
        else:
            #check if it exists
            if self.vm_list(self.cmd_list_vms, check_uuid = True, check_name = True) != False:
                self.log_string("Cannot clone from computer that does not exists")
                return False
            self.log_string("Clonning machine - "+str(self.config['base'])+" into "+str(self.config['name']+"- might take a while"))
            output = self.execute(self.cmd_clone.format(self.config['base'], self.config['name'], self.config['base_folder']))

            if "successfully cloned" not in output:
                self.log_string("Failed to clone machine")
                return False

            #register the VM...
            output = self.execute(self.cmd_register.format(self.config['base_folder']+self.config['name']+'/'+self.config['name']+'.vbox'))
            print(output)

            if 'error' in output:
                self.log_string("Failed to clone machine...")
                return False

        #get UUID and update
        vm_info = self.vm_list(self.cmd_list_vms, check_uuid = False, check_name = True)

        if vm_info == False:
            self.log_string("Failed to find cloned vm in machines...")
            return False

        self.update_config('uuid', vm_info[1])

        return True

#init our class
x = honeypot_base()
#x.vm_apply_network()
#x.vm_apply_pcap("frederikstop.pcap")
#x.vm_create()
#x.vm_hostonly_create()
#x.vm_exists()
#x.vm_start()
