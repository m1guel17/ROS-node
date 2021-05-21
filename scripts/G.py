#!/usr/bin/env python
#===========================================================
import rospy
from std_msgs.msg import String
value = ""
#===========================================================
def callback(data):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo B
	global value
	string_data = data.data
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido del nodo D : %s", data.data)
	if string_data == "BAJO":
		value = "B"
	if string_data == "MEDIO":
		value = "M"
	if string_data == "ALTO":
		value = "A"
#===========================================================
def G():
	global value
	pubH = rospy.Publisher('GH', String, queue_size=10)
	rospy.init_node('G', anonymous=False)
	#rospy.spin()
	rate = rospy.Rate(0.5)
	while not rospy.is_shutdown():
		rospy.Subscriber("DG", String, callback)
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
		pubH.publish(value)
		rospy.loginfo("Enviando al nodo H:  "+ value)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	G()
#===========================================================
