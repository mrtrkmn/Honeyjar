#Honeypot Base Architecture

###config

    {
        "name": "<name of the virtual box>",
        "base": "<path to the base .ova or name of VM to clone>",
        "folder": "<where to store virtual machines>",
        "pcap_folder": "<location for saving pcap files>",
        "network_id": "<stores the network id - will be used for multiple computers on same network>",
        "uuid": "<stores UUID after creation>"
    }

###commandline arguments

python honeypot_base.py <config.json> arg1 arg2 ... 

- start
- stop
- restart
- create
- destroy
- recreate -> destroy and create
- auto -> Create if not created and start

###Global Variables
- self.config -> points to config file
- regex 
    - list vms
    - creating network

###Functions

####Base
- read_config
- check_file_exists
- debug
- execute_command

####Features
- check_exists -> check if virtualbox machine with that UUID exists, falls back to name
- create -> imports OVA file and specifies name
- destroy -> removes the VM
- recreate -> call destroy and then create
- apply_network -> apply network config - nat, host-only
- apply_pcap(pcap_name) -> sets name for pcap file
- start
    - starts the VM
- shutdown
    - shutdown the VM
- restart
    - restarts the vm

