#!/usr/bin/env python
#===========================================================
# WE DECLARE LIBRERIES TO BE USED ON THIS PYTHON SCRIPT
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
#===========================================================
# WE INITIALIZE THE START VALUE ON THE VARIABLE FOR THE VALUE WE WILL GET FROM THE ROS NODE A
value = ""

#===========================================================
# WE DEFINE THE CALLBACK FUNCTION FOR THE BOOL VALUES (True - False) WHICH THE ROS NODE A IS GONNA PROVIDE
def callback(data):
	# rospy.get_caller_id() THIS RETURNS THE ROS NODE ID
	global value
	int_data = data.data
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido del nodo A: %s", data.data)
	if int_data <= 60:
		value = "BAJO"
	elif int_data > 60 and int_data <= 120:
		value = "MEDIO"
	elif int_data > 120 and int_data <= 180:
		value = "ALTO"
        
#===========================================================
# NOW WE DECLARE DE MAIN FUNCTION TO BE RUN SEVERAL TIMES WHILE WE RUN OUR PROJECT
def C():
	global value

	pubE = rospy.Publisher('CF', String, queue_size=10)

	rospy.init_node('C', anonymous=False)

	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
  		rospy.Subscriber("AC", Int8, callback)
  		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
  		pubE.publish(value)
  		rospy.loginfo("Enviando al nodo F:"+ value)
  		rate.sleep()
        
#===========================================================
# NOW WE DECLARE DE MAIN FUNCTION TO BE RUN SEVERAL TIMES WHILE WE RUN OUR PROJECT
if __name__ == '__main__':
	C()

    
   
