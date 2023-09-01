import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32, Float32MultiArray, Int8
from system_monitor_ros_msg.msg import SystemMonitor
import time
import psutil

class SystemNode(Node):
    def __init__(self):
        super().__init__('system_monitor_node')

        self.system_pub = self.create_publisher(SystemMonitor, 'system_monitor', 1)

        self.ros_node_state = self.declare_parameter('ros_node_state', False).value
        self.use_sensors_battery_state = self.declare_parameter('use_sensors_battery_state', False).value
        self.node_list = []

    def get_system_state(self):
        system_data = SystemMonitor()
        system_data.stamp = self.get_clock().now().to_msg()
        # system_data.time = self.get_clock().now().nanoseconds / 1e9
        system_data.cpu_count = psutil.cpu_count()
        system_data.cpu_percent = psutil.cpu_percent(percpu=False)
        system_data.current_cpu_freq = psutil.cpu_freq(percpu=False).current
        system_data.memory_total = float(psutil.virtual_memory().total)
        system_data.memory_percent = float(psutil.virtual_memory().percent)
        system_data.disk_usage_percent = psutil.disk_usage(path='/').percent
        temp = psutil.sensors_temperatures()
        for key, current_temp in temp.items():
            system_data.sensors_temperatures = current_temp[0].current
            break

        if self.use_sensors_battery_state:
            system_data.sensors_battery = psutil.sensors_battery()

        self.system_pub.publish(system_data)


def main(args=None):
    rclpy.init(args=args)
    systemnode = SystemNode()
    print("Start monitoring syatem!!")
    while rclpy.ok():
        systemnode.get_system_state()
        time.sleep(1.0)

    systemnode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
