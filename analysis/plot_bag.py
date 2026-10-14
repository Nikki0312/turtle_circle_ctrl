#!/usr/bin/env python3

import rosbag
import matplotlib.pyplot as plt


bag = rosbag.Bag("../bag/circle_data.bag")


t = []
vx = []
wz = []

x = []
y = []

start = None


for topic, msg, time in bag.read_messages():

    if start is None:
        start = time.to_sec()

    current_time = time.to_sec() - start


    if topic == "/turtle1/cmd_vel":

        t.append(current_time)
        vx.append(msg.linear.x)
        wz.append(msg.angular.z)


    elif topic == "/turtle1/pose":

        x.append(msg.x)
        y.append(msg.y)


bag.close()



# 线速度曲线

plt.figure()

plt.plot(t, vx)

plt.xlabel("Time(s)")
plt.ylabel("Linear velocity")

plt.title("Linear Velocity")

plt.grid()

plt.show()



# 角速度曲线

plt.figure()

plt.plot(t, wz)

plt.xlabel("Time(s)")
plt.ylabel("Angular velocity")

plt.title("Angular Velocity")

plt.grid()

plt.show()



# 轨迹曲线

plt.figure()

plt.plot(x, y)

plt.xlabel("x")

plt.ylabel("y")

plt.title("Turtle Trajectory")

plt.axis("equal")

plt.grid()

plt.show()
