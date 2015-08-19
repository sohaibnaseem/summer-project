#!/usr/bin/python

"""
Script
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
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8')
    s2 = net.addSwitch( 's2', listenPort=6634, mac='00:00:00:00:00:02' )
    s3 = net.addSwitch( 's3', listenPort=6635, mac='00:00:00:00:00:03' )
    h4 = net.addHost( 'h4', mac='00:00:00:00:00:04', ip='11.0.0.4/8')
    s5 = net.addSwitch( 's5', listenPort=6636, mac='00:00:00:00:00:05' )
    c6 = net.addController( 'c6', controller=RemoteController, ip='192.168.59.105', port=6633 )
    s7 = net.addSwitch( 's7', listenPort=6637, mac='00:00:00:00:00:07' )

    print "*** Creating links"
    net.addLink(s2, s3, 4, 4)
    net.addLink(s7, s3, 2, 3)
    net.addLink(s2, s7, 3, 1)
    net.addLink(s5, s3, 2, 2)
    net.addLink(h4, s3, 0, 1)
    net.addLink(s2, s5, 2, 1)
    net.addLink(h1, s2, 0, 1)

    print "*** Starting network"
    net.build()
    s7.start( [c6] )
    s3.start( [c6] )
    s5.start( [c6] )
    s2.start( [c6] )
    c6.start()



    
    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()


