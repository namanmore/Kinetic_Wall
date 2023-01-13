#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver myServo1 = Adafruit_PWMServoDriver(0x40); //DRIVER 1
Adafruit_PWMServoDriver myServo2 = Adafruit_PWMServoDriver(0x41); //DRIVER 2
Adafruit_PWMServoDriver myServo3 = Adafruit_PWMServoDriver(0x42); //DRIVER 3


#define SERVOMIN 150
#define SERVOMAX 600

uint8_t servonum1 = 0;
uint8_t servonum2 = 0;
uint8_t servonum3 = 0;
uint8_t numberOfServos1 = 16;
uint8_t numberOfServos2 = 16;
uint8_t numberOfServos3 = 16;

void setup() {
  Serial.begin(9600);
  myServo1.begin();
  myServo1.setPWMFreq(60);
  myServo2.begin();
  myServo2.setPWMFreq(60);
  myServo3.begin();
  myServo3.setPWMFreq(60);
  delay(10);
}

void loop() 
{
  // Runs all servos from 0 to 180 then 180 to 0 one by one
  while(servonum1<numberOfServos1)
  { 
    
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX/2; pulselen++){
    myServo1.setPWM(servonum1, 0, pulselen);
  }
  delay(500);
  for (uint16_t pulselen = SERVOMAX/2; pulselen > SERVOMIN; pulselen--){
    myServo1.setPWM(servonum1, 0, pulselen);
  }
  delay(500);
  servonum1 ++;
  }
  while(servonum2<numberOfServos2)
  { 
    
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++){
    myServo2.setPWM(servonum2, 0, pulselen);
  }
  delay(500);
  for (uint16_t pulselen = SERVOMAX; pulselen > SERVOMIN; pulselen--){
    myServo2.setPWM(servonum2, 0, pulselen);
  }
  delay(500);
  servonum2 ++;
  }
  while(servonum3<numberOfServos3)
  { 
    
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++){
    myServo3.setPWM(servonum3, 0, pulselen);
  }
  delay(500);
  for (uint16_t pulselen = SERVOMAX; pulselen > SERVOMIN; pulselen--){
    myServo3.setPWM(servonum3, 0, pulselen);
  }
  delay(500);
  servonum3 ++;
  }
  servonum1=0;
  servonum2=0;
  servonum3=0;
}
