#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import String

motor1f = 11
motor1b = 12
motor2f = 13
motor2b = 15

def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(motor1f, GPIO.OUT)
        GPIO.setup(motor1b, GPIO.OUT)
        GPIO.setup(motor2f, GPIO.OUT)
	GPIO.setup(motor2b, GPIO.OUT)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'received  %s', data.data)

    if data.data == 'w':
      print 'Robot moving forward \n'
      GPIO.output(motor1f, GPIO.HIGH)
      GPIO.output(motor2f, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(motor1f, GPIO.LOW)
      GPIO.output(motor2f, GPIO.LOW)

    elif data.data == 's':
          print 'Robot moving backward \n'
          GPIO.output(motor1b, GPIO.HIGH)
          GPIO.output(motor2b, GPIO.HIGH)
          time.sleep(1)
          GPIO.output(motor1b, GPIO.LOW)
          GPIO.output(motor2b, GPIO.LOW)

    elif data.data == 'd':
          print 'Robot moving right \n'
          GPIO.output(motor1f, GPIO.HIGH)
          GPIO.output(motor2b, GPIO.HIGH)
          time.sleep(1)
          GPIO.output(motor1f, GPIO.LOW)
          GPIO.output(motor2b, GPIO.LOW)

    elif data.data == 'a':
          print 'Robot moving left \n'
          GPIO.output(motor1b, GPIO.HIGH)
          GPIO.output(motor2f, GPIO.HIGH)
          time.sleep(1)
          GPIO.output(motor1b, GPIO.LOW)
          GPIO.output(motor2f, GPIO.LOW)

def destroy():
        GPIO.output(motor1f, GPIO.LOW)
        GPIO.output(motor1b, GPIO.LOW)
        GPIO.output(motor2f, GPIO.LOW)
	GPIO.output(motor2b, GPIO.LOW)
	GPIO.cleanup()

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

   setup()
   listener()
   destroy()
