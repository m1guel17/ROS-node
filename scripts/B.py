#!/usr/bin/env python
#===========================================================
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
value = ""
#===========================================================
def callback(data):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo
	global value
	bool_data = data.data
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido del nodo A : %s", data.data)
	if bool_data == False:
		value = "BAJO"
	else:
		value = "ALTO"
#===========================================================
def B():
	global value
	pubE = rospy.Publisher('BE', String, queue_size=10)
	rospy.init_node('B', anonymous=False)
	#rospy.spin()
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		rospy.Subscriber("AB", Bool, callback)
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
		pubE.publish(value)
		rospy.loginfo("Enviando al nodo E : "+ value)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	B()
#===========================================================
