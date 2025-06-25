#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose

def read_pose_from_file(file_path):
    # assuming the values for pose
    pose = Pose()
    pose.position.x = 0.0
    pose.position.y = 0.0
    pose.position.z = 0.0
    pose.orientation.x = 0.0
    pose.orientation.y = 0.0
    pose.orientation.z = 0.0
    pose.orientation.w = 1.0
    return pose

def talker():
    pub = rospy.Publisher('/pose_data1', Pose, queue_size=10)
    rospy.init_node('pose_publisher1', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    file_path = '/home/gnss/rtkrcv_ant0.conf'
    
    while not rospy.is_shutdown():
        pose = read_pose_from_file(file_path)
        rospy.loginfo(pose)
        pub.publish(pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

