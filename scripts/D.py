#!/usr/bin/env python
#===========================================================
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
value = ""
#===========================================================
def callback(data):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo B
	global value
	float_data = data.data
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido del nodo A: %s", data.data)
	if float_data <= 60.0:
		value = "BAJO"
	elif float_data > 60.0 and float_data <= 120.0:
		value = "MEDIO"
	elif float_data > 120.0 and float_data <= 180.0:
		value = "ALTO"
#===========================================================
def D():
	global value
	pubE = rospy.Publisher('DG', String, queue_size=10)
	rospy.init_node('D', anonymous=False)
	#rospy.spin()
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		rospy.Subscriber("AD", Float32, callback)
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
		pubE.publish(value)
		rospy.loginfo("Enviando al nodo G:"+ value)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	D()
#===========================================================
