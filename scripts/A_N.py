#!/usr/bin/env python
#===========================================================
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from std_msgs.msg import String

value_bool = False
value_int = 0
value_float = 0.0
#===========================================================
def callbackbool(data_bool):
	global value_bool
	str_data_bool = data_bool.data
	rospy.loginfo(rospy.get_caller_id() + " | Bool Arduino : " + data_bool.data)
	if str_data_bool == "True":
		value_bool = True
	elif str_data_bool == "False":
		value_bool = False
	else:
		value_bool = False

def callbackint(data_int):
	global value_int
	str_data_int = data_int.data
	rospy.loginfo(rospy.get_caller_id() + " | Int Arduino : " + str(data_int.data))
	value_int = str_data_int

def callbackfloat(data_float):
	global value_float
	str_data_float = data_float.data
	rospy.loginfo(rospy.get_caller_id() + " | Float Arduino : " + str(data_float.data))
	value_float = str_data_float

#===========================================================
def A_N():
	global value_bool
	global value_int
	global value_float
	pubB = rospy.Publisher('AB', Bool, queue_size=10)
	pubC = rospy.Publisher('AC', Int8, queue_size=10)
	pubD = rospy.Publisher('AD', Float32, queue_size=10)
	rospy.init_node('A_N', anonymous=False)
#===========================================================
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		data_str = "bool : " + str(value_bool) + " | int : " + str(value_int) + " | float : " + str(value_float)
		rospy.Subscriber("ArduinoBool", String, callbackbool)
		rospy.Subscriber("ArduinoInt", Int8, callbackint)
		rospy.Subscriber("ArduinoFloat", Float32, callbackfloat)
		rospy.loginfo(data_str)
		pubB.publish(value_bool)
		pubC.publish(value_int)
		pubD.publish(value_float)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	try:
		A_N()
	except rospy.ROSInterruptException:
		pass
#===========================================================
"""
#!/usr/bin/env python
#===========================================================
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from std_msgs.msg import String

intPublished = 75
floatPublished = 150.36
boolPublished = False
value = ""
#===========================================================
def callback(data):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo
	global value
	str_data = data.data
	rospy.loginfo(rospy.get_caller_id() + " | Dato recibido del Arduino : %s", data.data)
	value = str_data
#===========================================================
def A_():
	global value
	pubB = rospy.Publisher('AB', Bool, queue_size=10)
	pubC = rospy.Publisher('AC', Int8, queue_size=10)
	pubD = rospy.Publisher('AD', Float32, queue_size=10)
	rospy.init_node('A_', anonymous=False)
#===========================================================
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		data_str = "bool : " + str(boolPublished) + " | int : " + str(intPublished) + " | str : " + str(floatPublished)
		rospy.Subscriber("ArduinoAint", String, callback)
		rospy.loginfo(data_str)
		pubB.publish(boolPublished)
		pubC.publish(intPublished)
		pubD.publish(floatPublished)
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	try:
		A_()
	except rospy.ROSInterruptException:
		pass
#===========================================================

"""
