from mininet.link import Link,TCLink
from mininet.node import Node,Host,OVSSwitch,Controller
from mininet.net import Mininet,CLI
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.topolib import TreeTopo


class MyTopo( Topo ):
    
    def build( self ):

        # Add hosts and switches
        h1 = self.addHost( 'h1',ip = '10.0.0.101/8' )
        h2 = self.addHost( 'h2',ip = '10.0.0.102/8' )
        h3 = self.addHost( 'h3' ,ip = '10.0.0.103/8')
        h4 = self.addHost( 'h4',ip = '10.0.0.104/8' )
        Switch = self.addSwitch( 's1' )
        #rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( h1, Switch, bw=10, delay = '1ms' )
        self.addLink( h2,Switch, bw=10, delay = '1ms' )
        self.addLink( h3, Switch, bw=10, delay = '1ms' )
        self.addLink( h4,Switch, bw=10, delay = '1ms' )
        
        #net.get('h1').setIP('')
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
