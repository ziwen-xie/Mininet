from mininet.link import Link,TCLink
from mininet.node import Node,Host,OVSSwitch,Controller
from mininet.net import Mininet,CLI
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.topolib import TreeTopo


class MyTopo( Topo ):
    
    def build( self ):

        # Add hosts and switches
        h1 = self.addHost( 'h1',ip = '128.197.128.9' )
        h2 = self.addHost( 'h2',ip = '128.197.128.10' )
        
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        #rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( h1, s1, bw='1m')
        self.addLink( s1,s2, bw='1m')
        self.addLink( s2,h2, bw='1m')
        
        
        #net.get('h1').setIP('')
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
