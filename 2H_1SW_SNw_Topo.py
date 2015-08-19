#!/usr/bin/python
 
"""
Script for create topology using two hosts and one switch
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
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8' )
    h5 = net.addHost( 'h5', mac='00:00:00:00:00:05', ip='10.0.0.5/8' )
    #c7 = net.addController( 'c7', controller=RemoteController, ip='127.0.0.1', port=6633 )
    c7 = net.addController( 'c7', controller=RemoteController, ip='192.168.59.105', port=6633 )
         
 
    print "*** Creating links"
    net.addLink(s1, h5, 3, 0)
    net.addLink(s1, h2, 1, 0)
 
    print "*** Starting network"
    net.build()
    s1.start( [c7] )
    c7.start()
 
    print "*** Running CLI"
    CLI( net )
 
    print "*** Stopping network"
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
