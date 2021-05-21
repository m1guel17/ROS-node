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
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido de nodo H : %s", data.data)
	if string_data == "BBB":  #RULE1
		value = "B"
	if string_data == "BBM":  #RULE2
		value = "B"
	if string_data == "BBA":  #RULE3
		value = "M"
	if string_data == "BMB":  #RULE4
		value = "B"	
	if string_data == "BMM":  #RULE5
		value = "M"
	if string_data == "BMA":  #RULE6
		value = "M"
	if string_data == "BAB":  #RULE7
		value = "M"
	if string_data == "BAM":  #RULE8
		value = "M"
	if string_data == "BAA":  #RULE9
		value = "A"
	if string_data == "ABB":  #RULE10
		value = "M"
	if string_data == "ABM":  #RULE11
		value = "M"
	if string_data == "ABA":  #RULE12
		value = "A"
	if string_data == "AMB":  #RULE13
		value = "M"
	if string_data == "AMM":  #RULE14
		value = "M"	
	if string_data == "AMA":  #RULE15
		value = "A"
	if string_data == "AAB":  #RULE16
		value = "A"
	if string_data == "AAM":  #RULE17
		value = "A"
	if string_data == "AAA":  #RULE18
		value = "A"	
			
#===========================================================
def I():
	global value
	pubA = rospy.Publisher('IArduino', String, queue_size=10)
	rospy.init_node('I', anonymous=False)
	#rospy.spin()
	rate = rospy.Rate(0.5)
	while not rospy.is_shutdown():
		rospy.Subscriber("HI", String, callback)
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
		pubA.publish(value)
		rospy.loginfo("Enviando a la placa ARDUINO : " + value)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	I()
#===========================================================
