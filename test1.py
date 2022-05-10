from mininet.link import Link,TCLink
from mininet.node import Node,Host,OVSSwitch,Controller
from mininet.net import Mininet,CLI
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.topolib import TreeTopo


class MyTopo( Topo ):
    
    def build( self ):

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        Switch = self.addSwitch( 's1' )
        #rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( h1, Switch )
        self.addLink( h2,Switch )
        self.addLink( h3, Switch )
        self.addLink( h4,Switch )
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
