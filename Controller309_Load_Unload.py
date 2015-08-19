# Copyright 2011 James McCauley
#
# This file is part of POX.
#
# POX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# POX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with POX.  If not, see <http://www.gnu.org/licenses/>.

"""
An L2 learning switch.

It is derived from one written live for an SDN crash course.
It is somwhat similar to NOX's pyswitch in that it installs
exact-match rules for each flow.
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
from pox.lib.addresses import EthAddr, IPAddr
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.arp import arp
from pox.lib.packet.ipv4 import ipv4
from pox.lib.recoco import Timer
import time

log = core.getLogger()

# We don't want to flood immediately when a switch connects.
# Can be overriden on commandline.
_flood_delay = 0


"""  
Static routes part -- START ----
This Part is executed later  in the code (at the end) in def launch part
with the line core.callDelayed (5, install_flows) 
"""

#1: 
switch0 = 0000000000000002
flow0msg = of.ofp_flow_mod() 
flow0msg.cookie = 0 
flow0msg.match.dl_type  = 0x800
flow0msg.match.nw_dst = IPAddr("10.0.0.1")
#--- TIMER----------
flow0msg.idle_timeout = 10
flow0msg.hard_timeout = 30
# ACTIONS---------------------------------
flow0out = of.ofp_action_output (port = 1)
flow0dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:01"))
flow0msg.actions = [flow0dstMAC, flow0out] 

#2: 
switch1 = 0000000000000002
flow1msg = of.ofp_flow_mod() 
flow1msg.cookie = 0 
flow1msg.priority = 10
flow1msg.match.dl_type  = 0x800
flow1msg.match.nw_proto = 6
flow1msg.match.tp_src = 80
#--- TIMER----------
flow1msg.idle_timeout = 10  
flow1msg.hard_timeout = 30
# ACTIONS---------------------------------
flow1out = of.ofp_action_output (port = 3)
flow1msg.actions = [flow1out] 

#3: 
switch2 = 0000000000000002
flow2msg = of.ofp_flow_mod() 
flow2msg.cookie = 0 
flow2msg.priority = 10
flow2msg.match.dl_type  = 0x800
flow2msg.match.nw_proto = 6
flow2msg.match.tp_src = 22
#--- TIMER----------
flow2msg.idle_timeout = 10  
flow2msg.hard_timeout = 30
# ACTIONS---------------------------------
flow2out = of.ofp_action_output (port = 2)
flow2msg.actions = [flow2out] 

#4: 
switch3 = 0000000000000002
flow3msg = of.ofp_flow_mod() 
flow3msg.cookie = 0 
flow3msg.priority = 1
flow3msg.match.dl_type  = 0x800
flow3msg.match.nw_dst = IPAddr("11.0.0.4")
#--- TIMER----------
flow3msg.idle_timeout = 10  
flow3msg.hard_timeout = 30
# ACTIONS---------------------------------
flow3out = of.ofp_action_output (port = 4)
flow3msg.actions = [flow3out] 

#5: 
switch4 = 0000000000000003
flow4msg = of.ofp_flow_mod() 
flow4msg.cookie = 0 
flow4msg.match.dl_type  = 0x800
flow4msg.match.nw_dst = IPAddr("11.0.0.4")
#--- TIMER----------
flow4msg.idle_timeout = 10  
flow4msg.hard_timeout = 30
# ACTIONS---------------------------------
flow4out = of.ofp_action_output (port = 1)
flow4dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:04"))
flow4msg.actions = [flow4dstMAC, flow4out] 

#6: 
switch5 = 0000000000000003
flow5msg = of.ofp_flow_mod() 
flow5msg.cookie = 0 
flow5msg.priority = 10
flow5msg.match.dl_type  = 0x800
flow5msg.match.nw_proto = 6
flow5msg.match.tp_dst = 80
#--- TIMER----------
flow5msg.idle_timeout = 10  
flow5msg.hard_timeout = 30
# ACTIONS---------------------------------
flow5out = of.ofp_action_output (port = 3)
flow5msg.actions = [flow5out] 

#7: 
switch6 = 0000000000000003
flow6msg = of.ofp_flow_mod() 
flow6msg.cookie = 0 
flow6msg.priority = 10
flow6msg.match.dl_type  = 0x800
flow6msg.match.nw_proto = 6
flow6msg.match.tp_dst = 22
#--- TIMER----------
flow6msg.idle_timeout = 10  
flow6msg.hard_timeout = 30
# ACTIONS---------------------------------
flow6out = of.ofp_action_output (port = 2)
flow6msg.actions = [flow6out] 

#8: 
switch7 = 0000000000000003
flow7msg = of.ofp_flow_mod() 
flow7msg.cookie = 0 
flow7msg.priority = 1
flow7msg.match.dl_type  = 0x800
flow7msg.match.nw_dst = IPAddr("10.0.0.1")
#--- TIMER----------
flow7msg.idle_timeout = 10  
flow7msg.hard_timeout = 30
# ACTIONS---------------------------------
flow7out = of.ofp_action_output (port = 4)
flow7msg.actions = [flow7out] 

#9: 
switch8 = 0000000000000005
flow8msg = of.ofp_flow_mod() 
flow8msg.cookie = 0 
flow8msg.match.dl_type  = 0x800
flow8msg.match.nw_dst = IPAddr("10.0.0.1")
#--- TIMER----------
flow8msg.idle_timeout = 10  
flow8msg.hard_timeout = 30
# ACTIONS---------------------------------
flow8out = of.ofp_action_output (port = 1)
flow8msg.actions = [flow8out] 

#10: 
switch9 = 0000000000000005
flow9msg = of.ofp_flow_mod() 
flow9msg.cookie = 0 
flow9msg.match.dl_type  = 0x800
flow9msg.match.nw_dst = IPAddr("11.0.0.4")
#--- TIMER----------
flow9msg.idle_timeout = 10  
flow9msg.hard_timeout = 30
# ACTIONS---------------------------------
flow9out = of.ofp_action_output (port = 2)
flow9msg.actions = [flow9out] 

#11: 
switch10 = 0000000000000007
flow10msg = of.ofp_flow_mod() 
flow10msg.cookie = 0 
flow10msg.match.dl_type  = 0x800
flow10msg.match.nw_dst = IPAddr("10.0.0.1")
#--- TIMER----------
flow10msg.idle_timeout = 10  
flow10msg.hard_timeout = 30
# ACTIONS---------------------------------
flow10out = of.ofp_action_output (port = 1)
flow10msg.actions = [flow10out] 

#12: 
switch11 = 0000000000000007
flow11msg = of.ofp_flow_mod() 
flow11msg.cookie = 0 
flow11msg.match.dl_type  = 0x800
flow11msg.match.nw_dst = IPAddr("11.0.0.4")
#--- TIMER----------
flow11msg.idle_timeout = 10  
flow11msg.hard_timeout = 30
# ACTIONS---------------------------------
flow11out = of.ofp_action_output (port = 2)
flow11msg.actions = [flow11out] 

def install_flows(): 
   log.info("    *** Installing static flows... ***")
   # Push flows to switches
   core.openflow.sendToDPID(switch0, flow0msg)
   core.openflow.sendToDPID(switch1, flow1msg)
   core.openflow.sendToDPID(switch2, flow2msg)
   core.openflow.sendToDPID(switch3, flow3msg)
   core.openflow.sendToDPID(switch4, flow4msg)
   core.openflow.sendToDPID(switch5, flow5msg)
   core.openflow.sendToDPID(switch6, flow6msg)
   core.openflow.sendToDPID(switch7, flow7msg)
   core.openflow.sendToDPID(switch8, flow8msg)
   core.openflow.sendToDPID(switch9, flow9msg)
   core.openflow.sendToDPID(switch10, flow10msg)
   core.openflow.sendToDPID(switch11, flow11msg)
   log.info("    *** Static flows installed. ***")

"""  
Static routes part -- END ----
"""
def dpid_to_mac (dpid):
  return EthAddr("%012x" % (dpid & 0xffFFffFFffFF,))

class LearningSwitch (object):
  def __init__ (self, connection, transparent):
    # Switch we'll be adding L2 learning switch capabilities to
    self.connection = connection
    self.transparent = transparent

    # Our table
    self.macToPort = {} # This table is for each switch (connection) registered in class l2_learning  Down in the code.
    # We want to hear PacketIn messages, so we listen to the connection
    connection.addListeners(self)

    # We just use this to know when to log a helpful message
    self.hold_down_expired = _flood_delay == 0

    def _handle_PacketIn (self, event):
    """
    Handle packet in messages from the switch to implement above algorithm.
    """

    packet = event.parsed
    inport = event.port

    self.macToPort[packet.src] = event.port # 1

    if packet.type == packet.ARP_TYPE:
        if packet.payload.opcode == arp.REQUEST:
            arp_reply = arp()			
            arp_reply.hwsrc = dpid_to_mac(event.dpid)
            arp_reply.hwdst = packet.src
            arp_reply.opcode = arp.REPLY
            arp_reply.protosrc = packet.payload.protodst
            arp_reply.protodst = packet.payload.protosrc
            ether = ethernet()
            ether.type = ethernet.ARP_TYPE
            ether.dst = packet.src
            ether.src = dpid_to_mac(event.dpid)
            ether.payload = arp_reply
            msg = of.ofp_packet_out()
            msg.data = ether.pack()
            msg.actions.append(of.ofp_action_output(port = of.OFPP_IN_PORT))
            msg.in_port = inport
            event.connection.send(msg)
	
    else:
      if packet.dst not in self.macToPort: # 4
      else:
        port = self.macToPort[packet.dst]
        if port == event.port: # 5
          # 5a
          log.warning("Same port for packet from %s -> %s on %s.%s.  Drop."
              % (packet.src, packet.dst, dpid_to_str(event.dpid), port))
          drop(10)
          return
        # 6
        log.debug("installing flow for %s.%i -> %s.%i" %
                  (packet.src, event.port, packet.dst, port))
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet, event.port)
        msg.idle_timeout = 10 #Seconds that the flow in recorded in the Switch.  If no activity in this time-gap, the flow is deleted.
        msg.hard_timeout = 30
        msg.actions.append(of.ofp_action_output(port = port))
        msg.data = event.ofp # 6a
        self.connection.send(msg)
        ###############################################
        # SWITCH- TWO
        # Push flows to switch
        # Pull flow from switch
        if (event.dpid == 2 and match.nw_dst == "10.0.0.1"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch0, flow0msg)                
        elif (event.dpid == 2 and match.nw_proto == 6 and match.tp_src == 80):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch1, flow1msg)                
        elif (event.dpid == 2 and match.nw_proto == 6 and match.tp_src == 25):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch2, flow2msg)                    
        elif (event.dpid == 2 and match.nw_dst == "11.0.0.4"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch3, flow3msg)            
        ###############################################
        # SWITCH- THREE
        # Push flows to switch
        # Pull flow from switch
        elif (event.dpid == 3 and match.nw_dst == "11.0.0.4"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch4, flow4msg)       
        elif (event.dpid == 3 and match.nw_proto == 6 and match.tp_src == 80):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch5, flow5msg)        
        elif (event.dpid == 3 and match.nw_proto == 6 and match.tp_src == 25):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch6, flow6msg)        
        elif (event.dpid == 3 and match.nw_dst == "10.0.0.1"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch7, flow7msg)        
        ###############################################
        # SWITCH- FIVE
        # Push flows to switch
        # Pull flow from switch                                
        elif (event.dpid == 5 and match.nw_dst == "10.0.0.1"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch8, flow8msg)
        
        elif (event.dpid == 5 and match.nw_dst == "11.0.0.4"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch9, flow9msg)
        ###############################################
        # SWITCH- SEVEN
        # Push flows to switch
        # Pull flow from switch                                
        elif (event.dpid == 7 and match.nw_dst == "10.0.0.1"):
            core.openflow.sendToDPID(switch10, flow10msg)            
        elif (event.dpid == 7 and match.nw_dst == "11.0.0.4"):
            core.openflow.sendToDPID(switch11, flow11msg)              

class l2_learning (object):
  """
  Waits for OpenFlow switches to connect and makes them learning switches.
  """
  def __init__ (self, transparent):
    core.openflow.addListeners(self)
    self.transparent = transparent

  def _handle_ConnectionUp (self, event):
    log.debug("Connection %s" % (event.connection,))
    LearningSwitch(event.connection, self.transparent)

def launch (transparent=False, hold_down=_flood_delay):
  """
  Starts an L2 learning switch.
  """
  try:
    global _flood_delay
    _flood_delay = int(str(hold_down), 10)
    assert _flood_delay >= 0
  except:
    raise RuntimeError("Expected hold-down to be a number")
  Timer(10, install_flows, recurring = True ) 
  core.registerNew(l2_learning, str_to_bool(transparent))