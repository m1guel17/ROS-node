# ROS-node
The scripts on this GitHub repository are part of a lab to get you started on ROS nodes. Practice with three "flavors" of nodes and arduino communication. All documentation has been taken from the ROS website and can be found there. I highly recommend installing Arduino first and arduino ros serial node to work with it.

# Lab's Structure
ROS works with Nodes as its core. Everything ROS is capable of doing goes mainly into a node. On this lab we work with 10 nodes, all of them work in a two way information path where they listen and talk to one to three Nodes via "Topic". Nine of this Nodes work on python  and the last one work on Arduino.

# Definitions
- Publisher: the publisher, also called "talker", node will continually broadcast a message.
- Suscriber: the suscriber, also called "listener", node will continually be looking for a message.
- Topic: it refers to how we name our "conversation" between two or more nodes
![image](https://user-images.githubusercontent.com/63883454/119089801-56786900-b9d0-11eb-91e8-09440887e6c1.png)

# Working Principles
1.  We have an Arduino Nano wired to two potentiometer along with a button, these three are gonna stablish two analog values and a boolean one. We also have an output, in these case is gonna be an LED which is gonna provide us information with its brightness according to the inputs and the logic behind the ROS Nodes.
2.  We run the nine ROS nodes written in python one by one on the ubuntu terminals. 
4.  We start the ROS serial arduino node.
5.  We could see which message is sent and received with the command:
```
rostopic <<Insert rostopic>>
```
# Developers behind this
*   FLORES SIERRA MIGUEL ESTEBAN
*   HERNANDEZ OLAVE GERSON
