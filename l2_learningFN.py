
"""
An L2 learning switch.
 

It installs
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
import time
import os
import sys
import subprocess
from datetime import datetime

log = core.getLogger()
 
# We don't want to flood immediately when a switch connects.
# Can be overriden on commandline.
_flood_delay = 0
 
counter = 0 
flag = 0

fileCounter = open("NumPkt_SNW_I0.001s_h2_h5_3.csv","a")
#fileCounter = open("NumPkt_count_SNw_I0.001s_h2_Only_3.csv","a")
#fileCounter = open("NumPkt_count_SNw_I0.01_h2_with_h4_3.csv","a")

fileCounter.write("Pkt_No        \t" + '\t Pkt Info       \t' + "     Time" + '\n')

""" Static route .......
"""
################################################################### 
#1:
switch0 = 0000000000000001
flow0msg = of.ofp_flow_mod()
flow0msg.cookie = 0
flow0msg.match.dl_type  = 0x800
flow0msg.match.nw_src = IPAddr("10.0.0.3")
flow0msg.match.nw_dst = IPAddr("10.0.0.2")
#--- TIMER----------
flow0msg.idle_timeout = 300
flow0msg.hard_timeout = 120
# ACTIONS---------------------------------
flow0out = of.ofp_action_output (port = 1)
flow0dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:02"))
flow0msg.actions = [flow0dstMAC, flow0out]
 
#2:
switch1 = 0000000000000001
flow1msg = of.ofp_flow_mod()
flow1msg.cookie = 0
flow1msg.match.dl_type  = 0x800
flow1msg.match.nw_src = IPAddr("10.0.0.2")
flow1msg.match.nw_dst = IPAddr("10.0.0.3")
#--- TIMER----------
flow1msg.idle_timeout = 300
flow1msg.hard_timeout = 120
# ACTIONS---------------------------------
flow1out = of.ofp_action_output (port = 2)
flow1dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:03"))
flow1msg.actions = [flow1dstMAC, flow1out]

#  ...............................
#11:
switch10 = 0000000000000001
flow10msg = of.ofp_flow_mod()
flow10msg.cookie = 0
flow10msg.match.dl_type  = 0x800
flow10msg.match.nw_src = IPAddr("10.0.0.5")
flow10msg.match.nw_dst = IPAddr("10.0.0.2")
#--- TIMER----------
flow10msg.idle_timeout = 300
flow10msg.hard_timeout = 120
# ACTIONS---------------------------------
flow10out = of.ofp_action_output (port = 1)
flow10dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:02"))
flow10msg.actions = [flow10dstMAC, flow10out]   
    
#12:
switch11 = 0000000000000001
flow11msg = of.ofp_flow_mod()
flow11msg.cookie = 0
flow11msg.match.dl_type  = 0x800
flow11msg.match.nw_src = IPAddr("10.0.0.2")
flow11msg.match.nw_dst = IPAddr("10.0.0.5")
#--- TIMER----------
flow11msg.idle_timeout = 300
flow11msg.hard_timeout = 120
# ACTIONS---------------------------------
flow11out = of.ofp_action_output (port = 3)
flow11dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:05"))
flow11msg.actions = [flow11dstMAC, flow11out]
#  ...............................

################################################################### 
#3:
switch2 = 0000000000000004
flow2msg = of.ofp_flow_mod()
flow2msg.cookie = 0
flow2msg.match.dl_type  = 0x800
flow2msg.match.nw_src = IPAddr("10.0.0.3")
flow2msg.match.nw_dst = IPAddr("10.0.0.2")
#--- TIMER----------
flow2msg.idle_timeout = 300
flow2msg.hard_timeout = 120
# ACTIONS---------------------------------
flow2out = of.ofp_action_output (port = 1)
flow2dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:02"))
flow2msg.actions = [flow2dstMAC, flow2out]
 
#4:
switch3 = 0000000000000004
flow3msg = of.ofp_flow_mod()
flow3msg.cookie = 0
flow3msg.match.dl_type  = 0x800
flow3msg.match.nw_src = IPAddr("10.0.0.2")
flow3msg.match.nw_dst = IPAddr("10.0.0.3")
#--- TIMER----------
flow3msg.idle_timeout = 300
flow3msg.hard_timeout = 120
# ACTIONS---------------------------------
flow3out = of.ofp_action_output (port = 2)
flow3dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:03"))
flow3msg.actions = [flow3dstMAC, flow3out]

#5:
switch4 = 0000000000000004
flow4msg = of.ofp_flow_mod()
flow4msg.cookie = 0
flow4msg.match.dl_type  = 0x800
flow4msg.match.nw_src = IPAddr("10.0.0.4")
flow4msg.match.nw_dst = IPAddr("10.0.0.3")
#--- TIMER----------
flow4msg.idle_timeout = 300
flow4msg.hard_timeout = 120
# ACTIONS---------------------------------
flow4out = of.ofp_action_output (port = 2)
flow4dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:03"))
flow4msg.actions = [flow4dstMAC, flow4out]
 
#6:
switch5 = 0000000000000004
flow5msg = of.ofp_flow_mod()
flow5msg.cookie = 0
flow5msg.match.dl_type  = 0x800
flow5msg.match.nw_src = IPAddr("10.0.0.3")
flow5msg.match.nw_dst = IPAddr("10.0.0.4")
#--- TIMER----------
flow5msg.idle_timeout = 300
flow5msg.hard_timeout = 120
# ACTIONS---------------------------------
flow5out = of.ofp_action_output (port = 3)
flow5dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:04"))
flow5msg.actions = [flow5dstMAC, flow5out]

######################################################
#7:
switch6 = 0000000000000006
flow6msg = of.ofp_flow_mod()
flow6msg.cookie = 0
flow6msg.match.dl_type  = 0x800
flow6msg.match.nw_src = IPAddr("10.0.0.3")
flow6msg.match.nw_dst = IPAddr("10.0.0.2")
#--- TIMER----------
flow6msg.idle_timeout = 300
flow6msg.hard_timeout = 120
# ACTIONS---------------------------------
flow6out = of.ofp_action_output (port = 1)
flow6dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:02"))
flow6msg.actions = [flow6dstMAC, flow6out]
 
#8:
switch7 = 0000000000000006
flow7msg = of.ofp_flow_mod()
flow7msg.cookie = 0
flow7msg.match.dl_type  = 0x800
flow7msg.match.nw_src = IPAddr("10.0.0.2")
flow7msg.match.nw_dst = IPAddr("10.0.0.3")
#--- TIMER----------
flow7msg.idle_timeout = 300
flow7msg.hard_timeout = 120
# ACTIONS---------------------------------
flow7out = of.ofp_action_output (port = 2)
flow7dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:03"))
flow7msg.actions = [flow7dstMAC, flow7out]

#9:
switch8 = 0000000000000006
flow8msg = of.ofp_flow_mod()
flow8msg.cookie = 0
flow8msg.match.dl_type  = 0x800
flow8msg.match.nw_src = IPAddr("10.0.0.3")
flow8msg.match.nw_dst = IPAddr("10.0.0.4")
#--- TIMER----------
flow8msg.idle_timeout = 300
flow8msg.hard_timeout = 120
# ACTIONS---------------------------------
flow8out = of.ofp_action_output (port = 1)
flow8dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:02"))
flow8msg.actions = [flow8dstMAC, flow8out]
 
#10:
switch9 = 0000000000000006
flow9msg = of.ofp_flow_mod()
flow9msg.cookie = 0
flow9msg.match.dl_type  = 0x800
flow9msg.match.nw_src = IPAddr("10.0.0.4")
flow9msg.match.nw_dst = IPAddr("10.0.0.3")
#--- TIMER----------
flow9msg.idle_timeout = 300
flow9msg.hard_timeout = 120
# ACTIONS---------------------------------
flow9out = of.ofp_action_output (port = 2)
flow9dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:03"))
flow9msg.actions = [flow9dstMAC, flow9out]
#####################################################

"""  Start of  static flows Delete  """

#####################################################
switch0 = 0000000000000001
msg1 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE_STRICT)
msg1.match.nw_src = IPAddr("10.0.0.3")
msg1.match.nw_dst = IPAddr("10.0.0.2")
msg1.match.dl_dst = EthAddr("00:00:00:00:00:02")
msg1.match.dl_type = 0x800   
msg1.match.in_port = 2
msg1.match.cookie = 0
 
switch1 = 0000000000000001
msg2 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE_STRICT)
msg2.match.nw_src = IPAddr("10.0.0.2")
msg2.match.nw_dst = IPAddr("10.0.0.3")
msg2.match.dl_dst = EthAddr("00:00:00:00:00:03")
msg2.match.dl_type = 0x800   
msg2.match.in_port = 1
msg2.match.cookie = 0

# .........................
switch10 = 0000000000000001
msg11 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg11.match.nw_src = IPAddr("10.0.0.5")
msg11.match.nw_dst = IPAddr("10.0.0.2")
msg11.match.dl_dst = EthAddr("00:00:00:00:00:02")
msg11.match.dl_type = 0x800
msg11.match.in_port = 3
msg11.match.cookie = 0

switch11 = 0000000000000001
msg12 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg12.match.nw_src = IPAddr("10.0.0.2")
msg12.match.nw_dst = IPAddr("10.0.0.5")
msg12.match.dl_dst = EthAddr("00:00:00:00:00:05")
msg12.match.dl_type = 0x800
msg12.match.in_port = 1
msg12.match.cookie = 0
# .........................

#####################################################
switch2 = 0000000000000004
msg3 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg3.match.nw_src = IPAddr("10.0.0.3")
msg3.match.dl_src = EthAddr("00:00:00:00:00:03")
msg3.match.nw_dst = IPAddr("10.0.0.2")
msg3.match.dl_dst = EthAddr("00:00:00:00:00:02")
msg3.match.dl_type = 0x800   
msg3.match.in_port = 2
msg3.match.cookie = 0
 
switch3 = 0000000000000004
msg4 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg4.match.nw_src = IPAddr("10.0.0.2")
msg4.match.dl_src = EthAddr("00:00:00:00:00:02")
msg4.match.nw_dst = IPAddr("10.0.0.3")
msg4.match.dl_dst = EthAddr("00:00:00:00:00:03")
msg4.match.dl_type = 0x800   
msg4.match.in_port = 1
msg4.match.cookie = 0

switch4 = 0000000000000004
msg5 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg5.match.nw_src = IPAddr("10.0.0.3")
msg5.match.dl_src = EthAddr("00:00:00:00:00:03")
msg5.match.nw_dst = IPAddr("10.0.0.4")
msg5.match.dl_dst = EthAddr("00:00:00:00:00:04")
msg5.match.dl_type = 0x800   
msg5.match.in_port = 2
msg5.match.cookie = 0
 
switch5 = 0000000000000004
msg6 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg6.match.nw_src = IPAddr("10.0.0.4")
msg6.match.dl_src = EthAddr("00:00:00:00:00:04")
msg6.match.nw_dst = IPAddr("10.0.0.3")
msg6.match.dl_dst = EthAddr("00:00:00:00:00:03")
msg6.match.dl_type = 0x800   
msg6.match.in_port = 3
msg6.match.cookie = 0
##################################################################

switch6 = 0000000000000006
msg7 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg7.match.nw_src = IPAddr("10.0.0.3")
msg7.match.dl_src = EthAddr("00:00:00:00:00:03")
msg7.match.nw_dst = IPAddr("10.0.0.2")
msg7.match.dl_dst = EthAddr("00:00:00:00:00:02")
msg7.match.dl_type = 0x800   
msg7.match.in_port = 2
msg7.match.cookie = 0
 
switch7 = 0000000000000006
msg8 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg8.match.nw_src = IPAddr("10.0.0.2")
msg8.match.dl_src = EthAddr("00:00:00:00:00:02")
msg8.match.nw_dst = IPAddr("10.0.0.3")
msg8.match.dl_dst = EthAddr("00:00:00:00:00:03")
msg8.match.dl_type = 0x800   
msg8.match.in_port = 1
msg8.match.cookie = 0

switch8 = 0000000000000006
msg9 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg9.match.nw_src = IPAddr("10.0.0.3")
msg9.match.dl_src = EthAddr("00:00:00:00:00:03")
msg9.match.nw_dst = IPAddr("10.0.0.4")
msg9.match.dl_dst = EthAddr("00:00:00:00:00:04")
msg9.match.dl_type = 0x800   
msg9.match.in_port = 2
msg9.match.cookie = 0
 
switch9 = 0000000000000006
msg10 = of.ofp_flow_mod(match=of.ofp_match(),command=of.OFPFC_DELETE)
msg10.match.nw_src = IPAddr("10.0.0.4")
msg10.match.dl_src = EthAddr("00:00:00:00:00:04")
msg10.match.nw_dst = IPAddr("10.0.0.3")
msg10.match.dl_dst = EthAddr("00:00:00:00:00:03")
msg10.match.dl_type = 0x800   
msg10.match.in_port = 1
msg10.match.cookie = 0
# end of delete static flow entry

##################################################################
class LearningSwitch (object):

    def __init__ (self, connection, transparent):
    # Switch we'll be adding L2 learning switch capabilities to
    self.connection = connection
    self.transparent = transparent
    # Our table
    self.macToPort = {}
     
    # We want to hear PacketIn messages, so we listen
    # to the connection
    connection.addListeners(self)
    # We just use this to know when to log a helpful message
    self.hold_down_expired = _flood_delay == 0
 
    #log.debug("Initializing LearningSwitch, transparent=%s",
    #          str(self.transparent))
 
  def _handle_PacketIn (self, event):
    """
    Handle packet in messages from the switch to implement above algorithm.
    """
    global counter
    pktInTime = datetime.now()

    packet = event.parsed
    counter += 1
    fileCounter.write(str(counter) + '\t' + str(packet) + '\t' + str(pktInTime) + '\n') ## Write Packet information and its arrival time on file

    def flood (message = None):
      """ Floods the packet """
      pktOutTime = datetime.now()
      fileCounter.write(str(counter) + '\t' + str(packet) + '\t' + str(pktOutTime) + '\n') ## Write Packet iformation and its departure time on file
      
      msg = of.ofp_packet_out()
      if time.time() - self.connection.connect_time >= _flood_delay:
        # Only flood if we've been connected for a little while...
 
        if self.hold_down_expired is False:
          # Oh yes it is!
          self.hold_down_expired = True
          log.info("%s: Flood hold-down expired -- flooding",
              dpid_to_str(event.dpid))
 
        if message is not None: log.debug(message)
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
      else:
        pass
        #log.info("Holding down flood for %s", dpid_to_str(event.dpid))
      msg.data = event.ofp
      msg.in_port = event.port
      self.connection.send(msg)
 
    self.macToPort[packet.src] = event.port # 1
    if packet.dst.is_multicast:
      flood() # 3a
    else:
      if packet.dst not in self.macToPort: # 4
        flood("Port for %s unknown -- flooding" % (packet.dst,)) # 4a
      else:
        port = self.macToPort[packet.dst]
        # 6
        log.debug("installing flow for %s.%i -> %s.%i" %(packet.src, event.port, packet.dst, port))
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet, event.port)
        msg.idle_timeout = 1
        msg.hard_timeout = 2
        msg.actions.append(of.ofp_action_output(port = port))
        msg.data = event.ofp # 6a
        self.connection.send(msg)
        global flag
        flag = 1
        ###############################################
        # SWITCH- ONE
        # Push flows to switch
        # Pull flow from switch
        if (event.dpid == 1 and msg.match.nw_src == "10.0.0.3" and msg.match.nw_dst == "10.0.0.2"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch0, flow0msg)
                core.openflow.sendToDPID(switch0, msg1)
            else: 
                core.openflow.sendToDPID(switch0, msg1)
        elif (event.dpid == 1 and msg.match.nw_src == "10.0.0.2" and msg.match.nw_dst == "10.0.0.3"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch1, flow1msg)
                core.openflow.sendToDPID(switch0, msg1)
            else: 
                core.openflow.sendToDPID(switch0, msg1)
        # ...............................
        elif (event.dpid == 1 and msg.match.nw_src == "10.0.0.5" and msg.match.nw_dst == "10.0.0.2"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch10, flow10msg)
                core.openflow.sendToDPID(switch10, msg11)
            else:
                core.openflow.sendToDPID(switch0, msg11)                                        
        elif (event.dpid == 1 and msg.match.nw_src == "10.0.0.2" and msg.match.nw_dst == "10.0.0.5"):
            if(msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch11, flow11msg)
                core.openflow.sendToDPID(switch11, msg12)
            else:
                core.openflow.sendToDPID(switch11, msg12)
        # ...............................        
        # SWIICH - FOUR
        # Push flows to switch
        # Pull flow from switch
        elif (event.dpid == 4 and msg.match.nw_src == "10.0.0.3" and msg.match.nw_dst == "10.0.0.2"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch2, flow2msg)
                core.openflow.sendToDPID(switch2, msg3)
            else: 
                core.openflow.sendToDPID(switch2, msg3)        
        elif (event.dpid == 4 and msg.match.nw_src == "10.0.0.2" and msg.match.nw_dst == "10.0.0.3"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch3, flow3msg)
                core.openflow.sendToDPID(switch3, msg4)
            else: 
                core.openflow.sendToDPID(switch3, msg4)                           
        elif (event.dpid == 4 and msg.match.nw_src == "10.0.0.4" and msg.match.nw_dst == "10.0.0.3"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch4, flow4msg)
                core.openflow.sendToDPID(switch4, msg5)
            else: 
                core.openflow.sendToDPID(switch4, msg5)            
        elif (event.dpid == 4 and msg.match.nw_src == "10.0.0.3" and msg.match.nw_dst == "10.0.0.4"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch5, flow5msg)            
                core.openflow.sendToDPID(switch5, msg6)
            else: 
                core.openflow.sendToDPID(switch5, msg6)
        # SWIICH - SIX
            # Push flows to switch 
            # Pull flow from switch
        elif (event.dpid == 6 and msg.match.nw_src == "10.0.0.3" and msg.match.nw_dst == "10.0.0.2"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch6, flow6msg)
                core.openflow.sendToDPID(switch6, msg7)
            else: 
                core.openflow.sendToDPID(switch6, msg7)
        elif (event.dpid == 6 and msg.match.nw_src == "10.0.0.2" and msg.match.nw_dst == "10.0.0.3"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch7, flow7msg)
                core.openflow.sendToDPID(switch7, msg8)
            else: 
                core.openflow.sendToDPID(switch7, msg8)            
        elif (event.dpid == 6 and msg.match.nw_src == "10.0.0.3" and msg.match.nw_dst == "10.0.0.4"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch8, flow8msg)
                core.openflow.sendToDPID(switch8, msg9)
            else: 
                core.openflow.sendToDPID(switch8, msg9)
        elif (event.dpid == 6 and msg.match.nw_src == "10.0.0.4" and msg.match.nw_dst == "10.0.0.3"):
            if (msg.idle_timeout == 0 or msg.hard_timeout ==0):
                core.openflow.sendToDPID(switch9, flow9msg)
                core.openflow.sendToDPID(switch9, msg10)
            else: 
                core.openflow.sendToDPID(switch9, msg10)
                
        print " Flow installed and removed ...."
        
        pktOutTime = datetime.now()
        fileCounter.write(str(counter) + '\t' + str(packet) + '\t' + str(pktOutTime) + '\n') ## Write Packet information and its departure time on file        
    ###############################################
            
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
  core.registerNew(l2_learning, str_to_bool(transparent)) 