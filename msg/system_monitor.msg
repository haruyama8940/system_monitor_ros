#----------time-----------
#Header header
float64 time
#-----------cpu-----------
#cpu core
#psutil.cpu_count
int8 cpu_count

#representing the current system-wide CPU utilization as a percentage
#psutil.cpu_percent()
float32 cpu_percent

#cpu crequency
#psutil.cpu_freq()
float32 current_cpu_freq

#each cpu percentage
#psutil.cpu_percent(precpu=True)
# float32[] cpu_each_percent

#cpu crequency
#psutil.cpu_freq(precpu=True)
# float32[] current_each_cpu_freq

#-----------memory-----------
#psutil.virtual_memory().total
float32 memory_total
#psutil.virtual_memory().percent
float32 memory_percent

#-----------disk-------------
#psutil.disk_usage(path='/').percent
float32 disk_usage_percent

#-----------sensors----------
#psutil.sensors_temperatures()
float32 sensors_temperatures
#psutil.sensors_battery()
float32 sensors_battery

#ROS node list
string[] rosnode_list

