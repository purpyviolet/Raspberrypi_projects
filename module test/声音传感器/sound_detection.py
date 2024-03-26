import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 定义声音传感器连接的GPIO引脚
sound_pin = 21

# 设置GPIO引脚为输入模式
GPIO.setup(sound_pin, GPIO.IN)

try:
    while True:
        # 读取声音传感器的状态
        sound_status = GPIO.input(sound_pin)

        # 输出声音传感器状态
        if sound_status:
            print("检测到声音！")
        else:
            print("安静")

        # 等待一段时间再次检查
        time.sleep(0.1)

except KeyboardInterrupt:
    # 如果用户按下Ctrl+C，则清理GPIO设置
    GPIO.cleanup()
