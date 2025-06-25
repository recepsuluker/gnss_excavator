#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose

def callback(data):
    rospy.loginfo("to received pose data from receiver1:\n%s", data)

def listener():
    rospy.init_node('pose_subscriber1', anonymous=True)
    rospy.Subscriber('/pose_data1', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()


