#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def main():

    rospy.init_node("turtle_circle_node")


    # 从 ros param 读取参数
    linear_speed = rospy.get_param(
        "~linear_speed", 2.0)

    angular_speed = rospy.get_param(
        "~angular_speed", 1.0)


    pub = rospy.Publisher(
        "/turtle1/cmd_vel",
        Twist,
        queue_size=10)


    rate = rospy.Rate(10)


    while not rospy.is_shutdown():

        msg = Twist()

        msg.linear.x = linear_speed
        msg.angular.z = angular_speed

        pub.publish(msg)

        rate.sleep()



if __name__ == "__main__":
    main()
