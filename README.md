# turtle_circle_ctrl

ROS Noetic 小乌龟圆周运动控制实验


## 1. 实验环境

- Ubuntu 20.04
- ROS Noetic
- Python3


## 2. 功能介绍

本package实现：

1. 通过ROS节点发布速度控制小乌龟旋转运动；
2. 支持ROS参数配置线速度和角速度；
3. 使用launch文件启动；
4. 使用rosbag记录速度和位姿数据；
5. 使用Python程序分析bag数据。


## 3. 编译

```bash
cd ~/catkin_ws

catkin_make

source devel/setup.bash
