# ROS-Nodes
The scripts on this GitHub repository are part of a lab to get you started on ROS nodes. Practice with three "flavors" of nodes and arduino communication. All documentation has been taken from the ROS website and can be found there. I highly recommend installing Arduino first and arduino ros serial node to work with it.

# Lab's Structure
ROS works with Nodes as its core. Everything ROS is capable of doing goes mainly into a node. On this lab we work with 10 nodes, all of them work in a two way information path where they listen and talk to one to three Nodes via "Topic". Nine of this Nodes work on python  and the last one work on Arduino.
---
# Definitions
- Publisher: the publisher, also called "talker", node will continually broadcast a message.
- Suscriber: the suscriber, also called "listener", node will continually be looking for a message.
- Topic: it refers to how we name our "conversation" between two or more nodes

# Working Principles
We have 9 Nodes which are gonna execute a fuzzy logic taking the 3 inputs we give to them via Arduino (2 analog readings and 1 digital reading)
* ROS NODE A: is gonna take the 3 values from the arduino and is gonna split them into variables ready to send them to ROS Nodes B, C and D.
* ROS NODE B: is gonna take the bool value from the arduino splitted by ROS NODE A and gonna assign a value according to it.
* ROS NODE C: is gonna take one of the analog values (int) from the arduino splitted by ROS NODE A and gonna assign a value according to it and the value is gonna be sent in a string to ROS NODE E.
* ROS NODE D:is gonna take one of the analog values (turned into float by **map** function) from the arduino splitted by ROS NODE A and gonna assign a value according to it and the value is gonna be sent in a string to ROS NODE F.
* ROS NODE E, F and G: takes the string value sent by ROS NODE B and gonna execute a fuzzy logic according to what said string value was and is gonna send a **char** to ROS NODE H
* ROS NODE H: takes those 3 **char** values from ROS NODES E, F and G and execute a last fuzzy logic to designate the last value which is gonna be sent to ROS NODE I.
* ROS NODE I: take the last value from ROS NODE H and send a value back to the Arduino so we could dim the light from the LED. (LED is gonna represent the velocity set for a motor which we lack of)

![image](https://user-images.githubusercontent.com/63883454/119090090-c7b81c00-b9d0-11eb-98af-c560a55d8e0e.png)

# Executing Procedure
1.  We have an Arduino Nano wired to two potentiometer along with a button, these three are gonna stablish two analog values and a boolean one. We also have an output, in these case is gonna be an LED which is gonna provide us information with its brightness according to the inputs and the logic behind the ROS Nodes.
2.  We run the nine ROS nodes written in python one by one on the ubuntu terminals. 
4.  We start the ROS serial arduino node.
5.  We could see which message is sent and received with the command:
```
rostopic <<Insert rostopic>>
```
# Developers behind this
*   FLORES SIERRA MIGUEL ESTEBAN
*   JEAN FRANCO GONZALES LEYVA
*   HERNANDEZ OLAVE GERSON
