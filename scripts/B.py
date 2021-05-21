#!/usr/bin/env python
#===========================================================
# WE DECLARE LIBRERIES TO BE USED ON THIS PYTHON SCRIPT
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool

#===========================================================
# WE INITIALIZE THE START VALUE ON THE VARIABLE FOR THE VALUE WE WILL GET FROM THE ROS NODE A
value = ""

#===========================================================
# WE DEFINE THE CALLBACK FUNCTION FOR THE BOOL VALUES (True - False) WHICH THE ROS NODE A IS GONNA PROVIDE
def callback(data):
	# rospy.get_caller_id() THIS RETURNS THE ROS NODE ID
	global value
	bool_data = data.data
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido del nodo A : %s", data.data)
	if bool_data == False:
		value = "BAJO"
	else:
		value = "ALTO"
        
#===========================================================
# NOW WE DECLARE DE MAIN FUNCTION TO BE RUN SEVERAL TIMES WHILE WE RUN OUR PROJECT
def B():
    global value                                              # WE DECLARE THE value INTO GLOBAL, THIS DUE TO THIS VARIABLE IS FIRST DECLARED AND CALLED INTO A FUNCTION OUT OF THE MAIN ONE
	
    pubE = rospy.Publisher('BE', String, queue_size=10)       # HERE WE DECLARE WHAT OUR ROS TOPIC IS GONNA BE CALLED, TO PUT IT INTO SIMPLE WORDS, IT'S GONNA BE HOW OUR CONVERSATION CALLED
	
    rospy.init_node('B', anonymous=False)                     # WE INITIALIZE THE ROS NODE B AND WE RUN IT INTO ANON ANONYMOUS WAY, WE SET IT THIS WAY BECAUSE THIS IS A SIMPLE PROGRAM AND WE DON'T HAVE ROS NODES WITH THE SAME NAME

    rate = rospy.Rate(1)                                      # WE SET THE FRECUENCY OF THE PUBLISHING RATE
    
    while not rospy.is_shutdown():
        rospy.Subscriber("AB", Bool, callback)                # WE SUSCRIBE TO ROS TOPICS SET ROS NODE A
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
        pubE.publish(value)                                   # WE PUBLISH INTO THE SET ROS TOPIC OUR CORRESPONDANT VALUE
        rospy.loginfo("Enviando al nodo E : "+ value)         # WE PRINT OUR STRING DATA SO WE COULD BE AWARE OF WHAT OUR NODE IS GETTING AND PROCESSING
        rate.sleep()
        
#===========================================================
# OUR MAIN LOOP TRY AND EXCEPT IN CASE OF AN ERROR
if __name__ == '__main__':
	B()
