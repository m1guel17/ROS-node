#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>

//#include <TimerOne.h>

#include <Servo.h>
Servo myservo;
int val = 0;

ros::NodeHandle  nh;

std_msgs::String msg;
std_msgs::String bool_value;
std_msgs::Int16 int_value;
std_msgs::Float32 float_value;

ros::Publisher pub_bool("ArduinoBool", &bool_value);
ros::Publisher pub_int("ArduinoInt", &int_value);
ros::Publisher pub_float("ArduinoFloat", &float_value);

int int_pot = A6;
float val_pot_int_f;
int val_pot_int;
int float_pot = A7;
int aux;
int aux2;
float val_pot_float;

const int button = 4;

String holder;

//void messageCb( const std_msgs::Empty& toggle_msg){
  //digitalWrite(13, HIGH-digitalRead(13));   // blink the led
//}
void Imessage( const std_msgs::String& value){
  holder = value.data; // B - M -A 
  if(holder == "B"){
    val = 15;
  } else if(holder == "M"){
    val = 90;
  } else if(holder == "A"){
    val = 15;
  }
}

ros::Subscriber<std_msgs::String> sub("IArduino", Imessage );

void setup(){
  nh.initNode();
  nh.advertise(pub_bool);
  nh.advertise(pub_int);
  nh.advertise(pub_float);
  nh.subscribe(sub);
  myservo.attach(9);
  pinMode(13, OUTPUT);
  pinMode(A6, INPUT);
  pinMode(A7, INPUT);
  pinMode(4, INPUT);
  //Serial.begin(9600);//
}

void loop(){
  val_pot_int = analogRead(int_pot);
  //val_pot_int_f = (180.00 * aux2)/ 1023.00;
  //val_pot_int = (int)val_pot_int_f;
  val_pot_int = map(val_pot_int, 0, 1023, 10, 170);
  if (val_pot_int < 1){
    val_pot_int = 0;
    }else if(val_pot_int > 175){
      val_pot_int = 180;
      }
  aux = analogRead(float_pot);
  val_pot_float = (180.00 * aux)/ 1023.00;
  if(digitalRead(button)==1){
    bool_value.data = "True";
    digitalWrite(13, HIGH);
    //int_value.data = 75;
    //float_value.data = 150.42;
    }else{
    bool_value.data = "False";
    digitalWrite(13, LOW);
    //int_value.data = 32;
    //float_value.data = 110.21;
    }
  int_value.data = val_pot_int;
  float_value.data = val_pot_float;
  myservo.write(aux);
  delay(15);
  pub_bool.publish( &bool_value );
  pub_int.publish( &int_value );
  pub_float.publish( &float_value );
  nh.spinOnce();
  //Serial.print("Bool: ");//
  //Serial.print(digitalRead(button));//
  //Serial.print(" | Int: ");//
  //Serial.print(val_pot_int);//
  //Serial.print(" | Float: ");//
  //Serial.println(val_pot_float); //
  delay(100);
}
