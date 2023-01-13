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
int pulse1 = 210; //45 degrees
int pulse2 = 305; //90 degrees
int pulselen = 210;   //Set your desired angle to set all the servos at
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
  while (servonum1 < numberOfServos1)
  {

    myServo1.setPWM(servonum1, 0, pulselen);
    servonum1 ++;
  }
  while (servonum2 < numberOfServos2)
  {
    myServo2.setPWM(servonum2, 0, pulselen);
    servonum2 ++;
  }
  while (servonum3 < numberOfServos3)
  {
    myServo3.setPWM(servonum3, 0, pulselen);
    servonum3 ++;
  }
  servonum1 = 0;
  servonum2 = 0;
  servonum3 = 0;
}
