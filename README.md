# ROS-node
The scripts on this GitHub repository are part of a lab to get you started on ROS nodes. Practice with three "flavors" of nodes and arduino communication. All documentation has been taken from the ROS website and can be found there. I highly recommend installing Arduino first and arduino ros serial node to work with it.

# Lab's Structure
ROS works with Nodes as its core. Everything ROS is capable of doing goes mainly into a node. On this lab we work with 10 nodes, all of them work in a two way information path where they listen and talk to one to three Nodes via "Topic". Nine of this Nodes work on python  and the last one work on Arduino.

# Definitions
- Publisher: the publisher, also called "talker", node will continually broadcast a message.
- Suscriber: the suscriber, also called "listener", node will continually be looking for a message.
- Topic: it refers to how we name our "conversation" between two or more nodes

# Working Principles
