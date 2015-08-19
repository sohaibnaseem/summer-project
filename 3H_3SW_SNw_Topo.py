#!/usr/bin/python
 
"""
Script for 3 hosts and 3switches 
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, OVSLegacyKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
 
def topology():
    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
 
    print "*** Creating nodes"
    s1 = net.addSwitch( 's1', listenPort=6634, mac='00:00:00:00:00:01' )
    s4 = net.addSwitch( 's4', listenPort=6635, mac='00:00:00:00:00:04' )
    s6 = net.addSwitch( 's6', listenPort=6636, mac='00:00:00:00:00:06' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.0.3/8' )
    h4 = net.addHost( 'h4', mac='00:00:00:00:00:04', ip='10.0.0.4/8' )
    #c7 = net.addController( 'c5', controller=RemoteController, ip='127.0.0.1', port=6633 )
    c7 = net.addController( 'c5', controller=RemoteController, ip='192.168.59.105', port=6633 )
         
 
    print "*** Creating links"
    net.addLink(s1, h2, 1, 0)
    net.addLink(s1, s4, 2, 1)
    net.addLink(s4, h4, 3, 0)
    net.addLink(s4, s6, 2, 1)
    net.addLink(s6, h3, 2, 0)    
 
    print "*** Starting network"
    net.build()
    s1.start( [c7] )
    s4.start( [c7] )
    s6.start( [c7] )
    c7.start()
 
    print "*** Running CLI"
    CLI( net )
 
    print "*** Stopping network"
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
