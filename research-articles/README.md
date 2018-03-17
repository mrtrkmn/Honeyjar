#### This directory contains : 
1. Investigated and Highlighted Network Analysis Articles 
2. Libraries and its implementation with their explanations will be added during the process. 
3. (Could contain) some .PCAP files which are given as example.

### Features which can be used on implementation of ML 

- __Protocol Types__  
- __Request size__ (of a request in network)
- __Evil bit__ (can be looked at here)
- __Valid protocol requests__ (is it valid or not. it can give hint for an anomaly based irregular behavior.)
- __TCP Header__ (IPv4 Header security flag)
- __Source IP Address__
- __Source PORT number__
- __Destination IP Address__
- __Destination PORT Number__
- __Transaction Protocol__
- __State__ (Indicates to the state and its dependent protocol, e.g. ACC, CLO, CON, ECO, ECR, FIN, INT, MAS, PAR, REQ, RST, TST, TXD, URH, URN, and (-) (if not used state))
- __Source to destination transaction bytes__
- __Destination to source transaction bytes__
- __TTL (DEST <-> SRC)__
- __Retransmitted or drooped packets (DEST <-> SRC)__
- __Used Service__(http, ftp, smtp, ssh, dns, ftp-data ,irc  and (-) if not much used service)
- __Source bits per second__
- __Destination bits per second__
- __Source to destination packet count__
- __Destination to source packet count__
- __Timestamp__
- __TCP connection setup time(SYN <-> SYN_ACK)__
- __Number of GET/POST methods__
- __Number of Attemps(username/password attemps in an FTP session)__
- __Number of connection to same : dest/src/port__
- __Duration of the flow__
- __Average number of bytes per packet__
- __Packet per sec__
- __TCP flags__
- __Number of SYN/ACK/FIN/RST/SynAck/PushAck packets__

*_NOTE:_*   __<->__   _*sign indicates that this feature should be investigated in both sides such as TTL(DEST <->SRC) means time to live value from source to destination and destination to source.*_



### Machine Learning Mind Map

![Machine Learning Mind Map](https://raw.githubusercontent.com/ahmetturkmen/Honeyjar/master/research-articles/MachineLearningAlgorithms.png?token=AM-9YUGeTtph9CAJlCMRz4fSiVRGTn1Uks5asqUgwA%3D%3D)


### Ports Associated With Trojans & Malwares

<table x-use-null-cells &lt;col cellspacing="0" class="whs4">
<col>
<col>
<col>
<col>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs6">
<p class="whs7">Port Number</td>
<td colspan="1" rowspan="1" class="whs8">
<p class="whs7">Trojan Name</td>
<td colspan="1" rowspan="1" class="whs8">
<p class="whs7">Port Number</td>
<td colspan="1" rowspan="1" class="whs9">
<p class="whs7">Trojan Name</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>23432</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Asylum</td>
<td colspan="1" rowspan="1" class="whs11">
<p>31338</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Net Spy</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>31337</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Back Orifice</td>
<td colspan="1" rowspan="1" class="whs11">
<p>31339</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Net Spy</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>18006</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Back Orifice 2000</td>
<td colspan="1" rowspan="1" class="whs11">
<p>139</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Nuker</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>12349</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Bionet</td>
<td colspan="1" rowspan="1" class="whs11">
<p>44444</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Prosiak</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>6667</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Bionet</td>
<td colspan="1" rowspan="1" class="whs11">
<p>8012</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Ptakks</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>80</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Codered</td>
<td colspan="1" rowspan="1" class="whs11">
<p>7597</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Qaz</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>21</td>
<td colspan="1" rowspan="1" class="whs11">
<p>DarkFTP</td>
<td colspan="1" rowspan="1" class="whs11">
<p>4000</td>
<td colspan="1" rowspan="1" class="whs11">
<p>RA</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>3150</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Deep Throat</td>
<td colspan="1" rowspan="1" class="whs11">
<p>666</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Ripper</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>2140</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Deep Throat</td>
<td colspan="1" rowspan="1" class="whs11">
<p>1026</td>
<td colspan="1" rowspan="1" class="whs11">
<p>RSM</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>10048</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Delf</td>
<td colspan="1" rowspan="1" class="whs11">
<p>64666</td>
<td colspan="1" rowspan="1" class="whs11">
<p>RSM</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>23</td>
<td colspan="1" rowspan="1" class="whs11">
<p>EliteWrap</td>
<td colspan="1" rowspan="1" class="whs11">
<p>22222</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Rux</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>6969</td>
<td colspan="1" rowspan="1" class="whs11">
<p>GateCrash</td>
<td colspan="1" rowspan="1" class="whs11">
<p>11000</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Senna Spy</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>7626</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Gdoor</td>
<td colspan="1" rowspan="1" class="whs11">
<p>113</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Shiver</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>10100</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Gift</td>
<td colspan="1" rowspan="1" class="whs11">
<p>1001</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Silencer</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>21544</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Girl Friend</td>
<td colspan="1" rowspan="1" class="whs11">
<p>3131</td>
<td colspan="1" rowspan="1" class="whs11">
<p>SubSari</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>7777</td>
<td colspan="1" rowspan="1" class="whs11">
<p>GodMsg</td>
<td colspan="1" rowspan="1" class="whs11">
<p>1243</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Sub Seven</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>6267</td>
<td colspan="1" rowspan="1" class="whs11">
<p>GW Girl</td>
<td colspan="1" rowspan="1" class="whs11">
<p>6711</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Sub Seven</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>25</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Jesrto</td>
<td colspan="1" rowspan="1" class="whs11">
<p>6776</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Sub Seven</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>25685</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Moon Pie</td>
<td colspan="1" rowspan="1" class="whs11">
<p>27374</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Sub Seven</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>68</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Mspy</td>
<td colspan="1" rowspan="1" class="whs11">
<p>6400</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Thing</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs10">
<p>1120</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Net Bus</td>
<td colspan="1" rowspan="1" class="whs11">
<p>12345</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Valvo line</td></tr>
<tr valign="top" class="whs5">
<td colspan="1" rowspan="1" class="whs12">
<p>7300</td>
<td colspan="1" rowspan="1" class="whs13">
<p>Net Spy</td>
<td colspan="1" rowspan="1" class="whs13">
<p>1234</td>
<td colspan="1" rowspan="1" class="whs11">
<p>Valvo line</td></tr>
</table>

_Taken from : http://docs.trendmicro.com/all/ent/officescan/v10.5/en-us/osce_10.5_olhcl/osce_topics/what_are_trojan_ports_.htm_


__Practical Tools to make PCAP file analysis__

- https://github.com/caesar0301/awesome-pcaptools


__TCP Three-Way Handshake__
 - This is important to understand
 - Network scans use parts of the handshake to get responses 
 - First, client sends a synchronization packet.This is called SYN packet
 - This is used to synchronize sequence numbers
 - If the server accepts, it responds with a SYN ACK 
 - Then, the client responds with an acknowledgement, a session begins and socket created. 

__In case of Service Refueses__
- It refuses a SYN packet with an RST and an ICMP Destination Unreachable packet. 
- No response may mean a firewall.
- Host may try again with another SYN packet

__Normal TCP Traffic__
- It begins with a three-way handshake 
- Client initiates the conversation by requesting to have a session with the server
- 

__Ping Sweep__

- A series of packets is sent to identify live hosts 
- Sends series of package out to identify live hosts on the network
- Waits for the respond and knows whih hosts are alive.

__Port Scan__

- Identifies listening TCP and UDP ports on a live target system looking for services

__Network Mapping__

- Identifies the topoloy and creates a map 

__OS Fingerprinting__

- Determines a target's OS based on response

__Nmap__

- Network scanning tool includes a variety of scan types 
    - Finds live hosts
    - Identifies listening services 
    - Evades intrusion detection systems
- Sends specially crafted packets to various ports
- Identifies the OS based on specific behavior
    - Windows size and time to live (TTL ) value



