#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import rospy
import rosnode
from std_msgs.msg import String
from std_msgs.msg import Float32, Float32MultiArray, Int8
import time
import psutil

try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

from system_monitor_ROS.msg import system_monitor

class SystemNode():
    def __init__(self):
        # Publisherの作成
        self.system_pub = rospy.Publisher('system_monitor',system_monitor,queue_size=1)
        # self.ros_node_monitor_pub = rospy.Publisher('ros')
        # system_monitor_msg = system_monitor()
        self.rosmaster = rospy.get_master()
        self.node_id = "/rosnode"
        # self.looprate = rospy.get_param("rate",1.0)
        self.ros_node_state = rospy.get_param("ros_node_state",True)
        self.use_sensors_battery_state = rospy.get_param("use_sensors_battery_state",False)
        self.node_list = []


    def get_system_state(self):
        system_data = system_monitor()
        #time
        system_data.time = rospy.get_time()
        #cpu
        system_data.cpu_count = psutil.cpu_count()
        # print(psutil.cpu_count())
        system_data.cpu_percent = psutil.cpu_percent(percpu=False)
        system_data.current_cpu_freq = psutil.cpu_freq(percpu=False).current
        # system_data.cpu_each_percent = psutil.cpu_percent(percpu=True)
        # system_data.current_each_cpu_freq = psutil.cpu_freq(percpu=True)
        
        #memory
        system_data.memory_total = psutil.virtual_memory().total
        system_data.memory_percent = psutil.virtual_memory().percent
        
        #disk
        system_data.disk_usage_percent = psutil.disk_usage(path='/').percent
        
        #sensors
        temp= psutil.sensors_temperatures()
        # print("temp",temp)
        for key ,current_temp in temp.items():
            system_data.sensors_temperatures  = current_temp[0].current
            # print(current_temp[0].current)
            break
        
        if self.use_sensors_battery_state:
            system_data.sensors_battery = psutil.sensors_battery()
        self.system_pub.publish(system_data)
        self.state()
    
    def get_rosnode_state(self,name,pid):
        self.name = name
        self.process = psutil.Process(pid=pid)
        self.process_cpu_percent = self.process.cpu_percent()
        self.process_mem_used = self.process.memory_info().rss
        self.process_mem_percent = self.process.memory_percent()
        print("Name:",self.name,"CPU_percent:",self.process_cpu_percent,"MEM_percent:",self.process_mem_percent)
    
    def state(self):
        self.node_list = rosnode.get_node_names()
        print(self.node_list)
        for nodename in self.node_list:
            nodeapi = rosnode.get_api_uri(master=self.rosmaster,caller_id=nodename,skip_cache=True)[2]
            # print(nodeapi)
            nodeproxy = ServerProxy(nodeapi)
            nodepid = rosnode._succeed(nodeproxy.getPid(self.node_id))
            # print("node pid :" ,nodepid)
            self.get_rosnode_state(nodename,nodepid)

if __name__ == '__main__':
    rospy.init_node('system_monitor_node')

    time.sleep(3.0)
    systemnode = SystemNode()

    while not rospy.is_shutdown():
        systemnode.get_system_state()
        rospy.sleep(1.0)