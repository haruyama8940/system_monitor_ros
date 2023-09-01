# system_monitor_ROS
このリポジトリは，システム状態の監視を目的としたROS 2ノードです．  
大まかに下記の情報が取得できます．
1. システム全体のCPUやメモリの状態，温度
2. rosnodeごとのcpu及びメモリ使用率

# Publish
- system_monitor
  独自定義のメッセージファイルを使用したトピックです．
  以下の情報が含まれています
  - float64 time　　
    システム測定時の時刻を示します　　
  - int8 cpu_count　　
    システム内の論理コアを取得します　　
  - float32 cpu_percent　　
    CPUの使用率を取得します　　
  - float32 current_cpu_freq　　
    CPUの現在の動作周波数を取得します　　
  - float32 memory_total　　
    システム全体で使用可能なメモリを取得します　　
  - float32 memory_percent　　
    システムのメモリ使用率を取得します　　
  - float32 disk_usage_percent　　
    ディスク全体の使用率を取得します　　
  - float32 sensors_temperatures　　
    現在のCPU温度を取得します
  - ~~float32 sensors_battery~~　　
    ~~現在のバッテリー容量を取得します~~　　
  - ~~string[] rosnode_list~~　　
    ~~起動中のROSノードを取得します~~　　

# Dependencies
- ros2  
- python3系及びそれに対応したバーションの[psutil](https://psutil.readthedocs.io/en/latest/#)

# Install
```
pip3 install psutil
```
```
git clone https://github.com/haruyama8940/system_monitor_ros -b ros2-devel
git clone https://github.com/haruyama8940/system_monitor_ros_msg

```
# Run
```
 ros2 run system_monitor_ros system_monitor 
```
