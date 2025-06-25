#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_multiply, quaternion_inverse

def callback1(data):
    rospy.loginfo("Received pose data from receiver1")
    combined_data["pose1"] = data
    publish_combined_pose()

def callback2(data):
    rospy.loginfo("Received pose data from receiver2")
    combined_data["pose2"] = data
    publish_combined_pose()

def callback3(data):
    rospy.loginfo("Received pose data from receiver3")
    combined_data["pose3"] = data
    publish_combined_pose()

def average_poses(poses):
    avg_pose = Pose()
    
    # Average positions
    avg_pose.position.x = sum(p.position.x for p in poses) / len(poses)
    avg_pose.position.y = sum(p.position.y for p in poses) / len(poses)
    avg_pose.position.z = sum(p.position.z for p in poses) / len(poses)
    
    # Average orientations (quaternions)
    quaternions = [(
        p.orientation.x,
        p.orientation.y,
        p.orientation.z,
        p.orientation.w) for p in poses]
    
    avg_quaternion = [sum(q) / len(q) for q in zip(*quaternions)]
    avg_pose.orientation.x = avg_quaternion[0]
    avg_pose.orientation.y = avg_quaternion[1]
    avg_pose.orientation.z = avg_quaternion[2]
    avg_pose.orientation.w = avg_quaternion[3]
    
    return avg_pose

def publish_combined_pose():
    if all(key in combined_data for key in ["pose1", "pose2", "pose3"]):
        poses = [combined_data["pose1"], combined_data["pose2"], combined_data["pose3"]]
        combined_pose = average_poses(poses)
        rospy.loginfo("Combined pose:\n%s", combined_pose)
        pub.publish(combined_pose)

def listener():
    rospy.init_node('combined_node', anonymous=True)

    rospy.Subscriber('/pose_data1', Pose, callback1)
    rospy.Subscriber('/pose_data2', Pose, callback2)
    rospy.Subscriber('/pose_data3', Pose, callback3)

    rospy.spin()

if __name__ == '__main__':
    combined_data = {}
    pub = rospy.Publisher('/combined_pose', Pose, queue_size=10)
    listener()
