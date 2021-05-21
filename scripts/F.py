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
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido del nodo C : %s", data.data)
	if string_data == "BAJO":
		value = "B"
	if string_data == "MEDIO":
		value = "M"
	if string_data == "ALTO":
		value = "A"
#===========================================================
def F():
	global value
	pubH = rospy.Publisher('FH', String, queue_size=10)
	rospy.init_node('F', anonymous=False)
	#rospy.spin()
	rate = rospy.Rate(0.5)
	while not rospy.is_shutdown():
		rospy.Subscriber("CF", String, callback)
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
		pubH.publish(value)
		rospy.loginfo("Enviando al nodo H:  "+ value)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	F()
#===========================================================
