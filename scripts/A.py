#!/usr/bin/env python
#===========================================================
# WE DECLARE LIBRERIES TO BE USED ON THIS PYTHON SCRIPT
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from std_msgs.msg import String

#===========================================================
# WE INITIALIZE THE START VALUES ON THE VARIABLES FOR THE INPUTS COMING FROM THE EXTERNAL WORLD
value_bool = False
value_int = 0
value_float = 0.0

#===========================================================
# WE DEFINE THE CALLBACK FUNCTION FOR THE BOOL VALUES (True - False) WHICH THE ARDUINO IS GONNA PROVIDE
def callbackbool(data_bool):
	global value_bool
	str_data_bool = data_bool.data         # WE GET THE BOOL VALUE AND WE STORE IT INTO A VARIBLE TO BE CLASSIFIED FOR THE TO-BE PUBLISHED VALUE
	rospy.loginfo(rospy.get_caller_id() + " | Bool Arduino : " + data_bool.data) # THIS LINE IS GONNA PRINT IN THE CONSOLE WHAT BOOL VALUE ARE WE GETTING FROM THE ARDUINO
	if str_data_bool == "True":            # IF THE VALUE GOT FROM ARDUINO IS A "True" (string type value) we set the value_bool VALUE TO True (A BOOLEAN VALUE TO BE SENT TO ROS NODE B)
		value_bool = True
	elif str_data_bool == "False":         # IF THE VALUE GOT FROM ARDUINO IS A "False" (string type value) we set the value_bool VALUE TO False (A BOOLEAN VALUE TO BE SENT TO ROS NODE B)
		value_bool = False
	else:                                  # WE STABLISH THE SET VALUE OF value_bool TO False, THIS IS BUILT THIS WAY SO WE DONT JUMP UP THE MAIN EXIT FROM ROS NODE I
		value_bool = False

#===========================================================
# WE DEFINE THE CALLBACK FUNCTION FOR THE INTEGER VALUES [10 - 70] WHICH THE ARDUINO IS GONNA PROVIDE
def callbackint(data_int):
	global value_int
	str_data_int = data_int.data                               # WE GET THE INTEGER VALUE AND WE STORE IT INTO A VARIBLE TO BE CLASSIFIED FOR THE TO-BE PUBLISHED VALUE
	rospy.loginfo(rospy.get_caller_id() + " | Int Arduino : " + str(data_int.data)) # THIS LINE IS GONNA PRINT IN THE CONSOLE WHAT INTEGER VALUE ARE WE GETTING FROM THE ARDUINO
	value_int = str_data_int                                   # WE STORE THE VALUE FROM THE ARDUINO INTO A VARIBLE READY TO USE FOR ROS NODE A

#===========================================================
# WE DEFINE THE CALLBACK FUNCTION FOR THE FLOAT VALUES [0.00 - 180.00] WHICH THE ARDUINO IS GONNA PROVIDE
def callbackfloat(data_float):
	global value_floa
	str_data_float = data_float.data                           # WE GET THE FLOAT VALUE AND WE STORE IT INTO A VARIBLE TO BE CLASSIFIED FOR THE TO-BE PUBLISHED VALUE
	rospy.loginfo(rospy.get_caller_id() + " | Float Arduino : " + str(data_float.data)) # THIS LINE IS GONNA PRINT IN THE CONSOLE WHAT FLOAT VALUE ARE WE GETTING FROM THE ARDUINO
	value_float = str_data_float                               # WE STORE THE VALUE FROM THE ARDUINO INTO A VARIBLE READY TO USE FOR ROS NODE A
    
#===========================================================
# NOW WE DECLARE DE MAIN FUNCTION TO BE RUN SEVERAL TIMES WHILE WE RUN OUR PROJECT
def A():

    global value_bool                                          # WE DECLARE THE value_bool, value_int, float_int INTO GLOBAL, THIS DUE TO THIS VARIABLE IS FIRST DECLARED AND CALLED INTO A FUNCTION OUT OF THE MAIN ONE
    global value_int
    global value_float

    pubB = rospy.Publisher('AB', Bool, queue_size=10)           # HERE WE DECLARE WHAT OUR ROS TOPIC IS GONNA BE CALLED, TO PUT IT INTO SIMPLE WORDS, IT'S GONNA BE HOW OUR CONVERSATION CALLED
    pubC = rospy.Publisher('AC', Int8, queue_size=10)
    pubD = rospy.Publisher('AD', Float32, queue_size=10)
	
    rospy.init_node('A', anonymous=False)                      # WE INITIALIZE THE ROS NODE A AND WE RUN IT INTO ANON ANONYMOUS WAY, WE SET IT THIS WAY BECAUSE THIS IS A SIMPLE PROGRAM AND WE DON'T HAVE ROS NODES WITH THE SAME NAME
    rate = rospy.Rate(10)                                      # WE SET THE FRECUENCY OF THE PUBLISHING RATE
    
    while not rospy.is_shutdown():
        data_str = "bool : " + str(value_bool) + " | int : " + str(value_int) + " | float : " + str(value_float) # WE DECLARE OUR STRING DATA TO PRINT IT IN THE CONSOLE
        rospy.Subscriber("ArduinoBool", String, callbackbool)  # WE SUSCRIBE TO ROS TOPICS SET BY THE ARDUINO 
        rospy.Subscriber("ArduinoInt", Int8, callbackint)
        rospy.Subscriber("ArduinoFloat", Float32, callbackfloat)
        rospy.loginfo(data_str)
        pubB.publish(value_bool)
        pubC.publish(value_int)
        pubD.publish(value_float)
        rate.sleep()
        

        
#===========================================================
# 
if __name__ == '__main__':
	try:
		A()
	except rospy.ROSInterruptException:
		pass
