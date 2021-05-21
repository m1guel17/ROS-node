#!/usr/bin/env python
#===========================================================
import rospy
from std_msgs.msg import String
#import numpy as np
#import skfuzzy as fuzz
#from skfuzzy import control as ctrl
value = ""
value2 = ""
value3 = ""
#===========================================================
#def fuzzy():
# Bool Bajo o Alto
# Int [0 - 1023] = [0 - 180]
# Float [0 - 255]
 #bool_data = ctrl.Antecedent(np.arange(0, 1, 0.5), 'BOOL') #quality
 #int_data = ctrl.Antecedent(np.arange(0, 180, 0.5), 'INT') #service
 #float_data = ctrl.Antecedent(np.arange(0.0, 180.0, 0.5), 'FLOAT') #quality

 #pwm = ctrl.Consequent(np.arange(0, 255, 0.5), 'PWM') #tip  
#
 #bool_data['B'] = fuzz.trapmf(bool_data.universe, [0.0, 0.0, 0.25, 0.5])
 #bool_data['A'] = fuzz.trapmf(bool_data.universe, [0.5, 0.75, 1.0, 1.0])
###############
#
# int_data['B'] = fuzz.trapmf(int_data.universe, [0, 0, 30, 60])
 #int_data['M'] = fuzz.trapmf(int_data.universe, [60, 80, 100, 120])
# int_data['A'] = fuzz.trapmf(int_data.universe, [120, 140, 160, 180])
#################
#
 #float_data['B'] = fuzz.trapmf(int_data.universe, [0.0, 0.0, 30.0, 60.0])
 #float_data['M'] = fuzz.trapmf(int_data.universe, [60.0, 80.0, 100.0, 120.0])
 #float_data['A'] = fuzz.trapmf(int_data.universe, [120.0, 140.0, 160.0, 180.0])
#################
#
 #pwm['B'] = fuzz.trapmf(pwm.universe, [0, 0, 51, 85])
 #pwm['M'] = fuzz.trimf(pwm.universe, [85, 127.5, 170])
 #pwm['A'] = fuzz.trapmf(pwm.universe, [170, 204, 255, 255])
 ##bool_data.view()
 ##int_data.view()
 ##pwm.view() 
#
 #rule1 = ctrl.Rule(bool_data['B'] | int_data['B'] | float_data['B'], pwm['B'])
 #rule2 = ctrl.Rule(bool_data['B'] | int_data['B'] | float_data['M'], pwm['B'])
 #rule3 = ctrl.Rule(bool_data['B'] | int_data['B'] | float_data['A'], pwm['M'])
#
 #rule4 = ctrl.Rule(bool_data['B'] | int_data['M'] | float_data['B'], pwm['B'])
 #rule5 = ctrl.Rule(bool_data['B'] | int_data['M'] | float_data['M'], pwm['M'])
 #rule6 = ctrl.Rule(bool_data['B'] | int_data['M'] | float_data['A'], pwm['M'])
#
 #rule7 = ctrl.Rule(bool_data['B'] | int_data['A'] | float_data['B'], pwm['M'])
 #rule8 = ctrl.Rule(bool_data['B'] | int_data['A'] | float_data['M'], pwm['M'])
 #rule9 = ctrl.Rule(bool_data['B'] | int_data['A'] | float_data['A'], pwm['A'])
#
 #rule10 = ctrl.Rule(bool_data['A'] | int_data['B'] | float_data['B'], pwm['M'])
 #rule11 = ctrl.Rule(bool_data['A'] | int_data['B'] | float_data['M'], pwm['M'])
 #rule12 = ctrl.Rule(bool_data['A'] | int_data['B'] | float_data['A'], pwm['A'])
#
 #rule13 = ctrl.Rule(bool_data['A'] | int_data['M'] | float_data['B'], pwm['M'])
 #rule14 = ctrl.Rule(bool_data['A'] | int_data['M'] | float_data['M'], pwm['M'])
 #rule15 = ctrl.Rule(bool_data['A'] | int_data['M'] | float_data['A'], pwm['A'])
#
 #rule16 = ctrl.Rule(bool_data['A'] | int_data['A'] | float_data['B'], pwm['A'])
 #rule17 = ctrl.Rule(bool_data['A'] | int_data['A'] | float_data['M'], pwm['A'])
 #rule18 = ctrl.Rule(bool_data['A'] | int_data['A'] | float_data['A'], pwm['A'])
#
 #pwm_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15,   Vrule16, rule17, rule18])
# pwm_s = ctrl.ControlSystemSimulation(pwm_ctrl)
#
# pwm_s.input['BOOL'] =  1
# pwm_s.input['INT'] = 120
# pwm_s.input['FLOAT'] = 120.0
# pwm_s.compute()
# pwm.view(sim=pwm_s)
#print(pwm_s.output['VOLTAGE'])

def callback(data):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo 
	global value
	string_dataE = data.data	
	rospy.loginfo(rospy.get_caller_id() + "  Dato recibido del nodo E :" + data.data)
	if string_dataE == "B":
		value = "B"
	else:
		value = "A"
def callback2(data2):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo 
	global value2
	string_dataF = data2.data	
	rospy.loginfo(rospy.get_caller_id() + "  Dato recibido del nodo F :" + data2.data)
	if string_dataF == "B":
		value2 = "B"
		
	if string_dataF == "M":
		value2 = "M"
		
	if string_dataF == "A":
		value2 = "A"
	
def callback3(data3):
	# rospy.get_caller_id() = esto devuelve identificacion del nodo 
	global value3
	string_dataG = data3.data	
	rospy.loginfo(rospy.get_caller_id() + "  Dato recibido del nodo G :" + data3.data)
	if string_dataG == "B":
		value3 = "B"
	elif string_dataG == "M":
		value3 = "M"
	elif string_dataG == "A":
		value3 = "A"			
		
#===========================================================
def H():
	global value
	pubI = rospy.Publisher('HI', String, queue_size=10)	
	rospy.init_node('H', anonymous=False)
	#rospy.spin()
	rate = rospy.Rate(0.2)
	while not rospy.is_shutdown():
		rospy.Subscriber("EH", String, callback)
		rospy.Subscriber("FH", String, callback2)
		rospy.Subscriber("GH", String, callback3)
		#data_str = "DATO RECIBIDO " + data.data + "LO QUE IMPRIMO ES : " + value
		pubI.publish(value + value2 + value3)
		rospy.loginfo("Enviando al nodo I: (E: "+ value + ") + (F: " + value2 + ") + (G: "+ value3 + ")")
		rate.sleep()
#===========================================================
if __name__ == '__main__':
	H()
#===========================================================
