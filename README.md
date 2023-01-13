# Kinetic-Wall
All the supporting codes for Kinectic Wall project

This Repository conatins scripts that will make the Kinetic-Wall work

## Dependencies  

* Python with libraries required for this project  
* Raspberry Pi with i2c enabled  
* Microsoft Kinect for Xbox 360  
* Pca9685 Servo Driver   

## Understanding the working
  
The PCA9685 module works on i2c and the way in which you send data is important.
To be able to use the different modules, you need to set a different I2C address for each board and this is done
using the six-address selection solderable pads (A0 – A5) where you have to connect these pads depending on the  
address you like to give a specific board. Refer the image here
<p align="center">
  <img src="https://github.com/namanmore/Kinetic_Wall/blob/main/README_files/PCA9685.jpg" />
</p>  
The connections are straightforward so not going into that.

## Running the Codes  

The files in the *Working_Codes/Socket* directory are the ones needed to make things work.  
* *laptop_run* -> Code which will run the Kinect and send pixel data after appropriate filtering over Socket to Raspberry Pi  

* *rpi_run* -> Code which will run on the rpi, this will receive the data and actuate all the servos on the Kinetic Wall  

## Extra Files   

The file in the *Working_Codes/Kinect* directory is to visualize and adjust the depth filtering using a GUI  
The files in the *Working_Codes/Arduino* directory is to use Arduino to actuate all the servos of Kinetic Wall according to the user's need 
The files in the *Others* directory contains files which were made initially while testing. Can be used as reference
