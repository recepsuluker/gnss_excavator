#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose

def callback(data):
    rospy.loginfo("to received pose data from receiver3:\n%s", data)

def listener():
    rospy.init_node('pose_subscriber3', anonymous=True)
    rospy.Subscriber('/pose_data3', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

