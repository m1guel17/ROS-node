#!/usr/bin/env python
#===========================================================
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
value = ""
#===========================================================
def callback(data):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo
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
def C():
	global value
	pubE = rospy.Publisher('CF', String, queue_size=10)
	rospy.init_node('C', anonymous=False)
	#rospy.spin()
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		rospy.Subscriber("AC", Int8, callback)
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
		pubE.publish(value)
		rospy.loginfo("Enviando al nodo F:"+ value)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	C()
#===========================================================
    
    

