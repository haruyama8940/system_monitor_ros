# system_monitor_ROS
このリポジトリは，システムの状態を監視を目的としたROSノードです．  
大まかに下記の情報が取得できます．
1. システム全体のCPUやメモリの状態，温度
2. rosnodeごとのcpu及びメモリ使用率 

# Dependencies
- ros nodetic  
- python3系及びそれに対応したバーションの[psutil](https://psutil.readthedocs.io/en/latest/#)

# Install
```
pip3 install psutil
```
```
git clone https://github.com/haruyama8940/system_monitor_ROS
```
# Run
```
 roslaunch system_monitor_ROS system_monitor_ROS.launch 
```
