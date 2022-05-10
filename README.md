# MIninet Command

h1 python -m http.server 80 &

## create topo
### add host & ip
``` python

h1 = self.addHost( 'h1',ip = '10.0.0.101/8' )
Switch = self.addSwitch( 's1' )


```
### add link& delay
```python
self.addLink( h1, Switch, bw=10, delay = '1ms' )
```

## run topo
```sh
sudo mn --custom test1.py --topo mytopo

```
## use xterm
```sh
xterm h1 h2 h3 h4
```

## TCP
### create server 
monitor result every 1s
```sh
iperf -s -p 5566 
```
### start tcp 
for a transmission duration of 15s
```sh
iperf -c 10.0.0.2 -p 5566 -t 2
```
## UDP
server side
```sh
iperf -s -p 5003 -u
```
client side
```sh
iperf -c 10.0.0.2 -u -p 5003 -t 2
```


## iperf
`-p,--port` the port for server to listen and for client to connect. default is 5201 
UDP port: 5003
TCP port: 5566
`-f` format. have `k` = Kbits/sec; `K` = KBytes/s; `m` = Mbits/s, `M`= MBytes/s
`-i` report interval
`-F` filename
`--logfile file`  output to log
### server side
`-s` server
### client side
`-c --client host` connect to host
`--sctp` use SCTP
`-u` use UDP
`-b` set bandwidth
`-t` transmission time
`-n` num of buffers
`-k` num of blocks/packets
`-l` length
`-4` only use ipv4
`-6` only use ipv6
`-S --tos n` type of service:
1. `IPTOS_LOWDELAY`, TOS # = `0x10`
2. `IPTOS_THROUGHPUT`, TOS# = `0x08`
3. `IPTOS_RELIABILITY`, TOS# = `0x04`
4. `IPTOS_LOWCOST`, TOS# = `0x02`





# Docker
## Start a container
```sh
> sudo docker run -it --name ec441 ubuntu /bin/bash
```

### execute exist container
directly start in docker (not recommend, cannot use previous command)
or
```bash
> sudo docker exec -it ec544 /bin/bash
```

---
## File transfer
### write a file
```sh
> echo "hello!" > hello.txt
```
### Transfer file
open a new terminal and start the container
```sh
> sudo docker start ec544
ec544
```
see the session ID
```sh
> sudo docker container ls
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES

11xxxxxxxx   ubuntu    "/bin/bash"   20 minutes ago   Up 20 minutes             ec544
```
transfer files
```sh
> sudo docker cp 1134444df4:/hello.txt ~/Desktop/hello.txt
```

---
# Mininet
### headers
``` python
from mininet.link import Link,TCLink
from mininet.node import Node,Host,OVSSwitch,Controller
from mininet.net import Mininet,CLI
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.topolib import TreeTopo

```

### sample code
``` python
from mininet_basics import *
h1 = Host( 'h1' )                                                                                                     
h2 = Host( 'h2' )                                                                                                     
s1 = OVSSwitch( 's1', inNamespace=False )                                                                             
c0 = Controller( 'c0', inNamespace=False )                                                                            
Link( h1, s1 )                                                                                                        
Link( h2, s1 )                                                                                                        
h1.setIP( '10.1/8' )                                                                                                  
h2.setIP( '10.2/8' )                                                                                                  
c0.start()                                                                                                            
s1.start( [ c0 ] )                                                                                                    
print(h1.cmd( 'ping -c1', h2.IP() ) )                                                                                  
s1.stop()                                                                                                             
c0.stop()
```
### sample topology
```python
#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo)
    net.start()
    print( "Dumping host connections" )
    dumpNodeConnections(net.hosts)
    print( "Testing network connectivity" )
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
```

`addSwitch()`: adds a switch to a `Topo` and returns the switch name
`addHost()`: adds a host to a `Topo` and returns the host name
`addLink()`: adds a bidirectional link to `Topo` (and returns a link key, but this is not important). Links in Mininet are bidirectional unless noted otherwise.
`start()`: starts your network
`pingAll()`: tests connectivity by trying to have all nodes ping each other

`stop()`: stops your network

`net.hosts`: all the hosts in a network

`dumpNodeConnections()`: dumps connections to/from a set of nodes.

`setLogLevel( 'info' | 'debug' | 'output' )`: set Mininet's default output level; 'info' is recommended as it provides useful information.

# Wireshark
## concepts
### IP
``` bash
> ifconfig
```
`inet` is the IP address
 IP addresses are provided by ISP, they are (1) static (2)dynamic
`eth0` wire connection
`eth1` Wi-Fi
### Port
ftp: 421 (file transfer protocol)
http: 443
dns: 53 (domain names to ip address)
``` bash
> ping google.com
PING google.com (142.250.72.110) 56(84) bytes of data.
```
#### show all the ports
``` bash
> nmap localhost
```
**start web service**
``` bash
> service httpd start
```
 listen on port 80
### MAC
media access control address
hardware: network card
can use `ifconfig` to see

### Layers
1. physical
2. data link: decoding/encoding; flow control $ synchronizing frames
	- mac
	- llc: logical link control
3. network: switching and routing, addressingg, error handling, packet sequencing
4. transport: tcp
5. session:
6. presentation: convert data into suitable form for application
7. application: things in wireshark 
## wireshark
### installation
search for wireshark versions
```bash
> yum search wireshark
```
search for system
```bash
uname -a
```
### turn an interface down
```bash
> ifconfig wlp2s0 down
> ifconfig wlp2s0 up
```
### filters
``` bash
ip.src == 10.0.0.1
```
&& and
|| or
tcp
udp
udp.port == 53 || tcp.port == 53(filter DNS)
icmp

#### ip address
ip.src == xx.xxx
ip.dst == 
ip.addr

#### port
tcp.srcport == 
tcp.dstport ==
tcp.port == 
udp.port ==

### find ip address
```bash
tshark -nr input.pcap -q -z ip_hosts,tree | find "Addresses"
```
or 
statistics--> ipv4 packages



