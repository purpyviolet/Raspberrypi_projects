import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 定义震动传感器连接的GPIO引脚
vibration_pin = 21

# 设置GPIO引脚为输入模式
GPIO.setup(vibration_pin, GPIO.IN)

try:
    while True:
        # 读取震动传感器的状态
        vibration_status = GPIO.input(vibration_pin)

        # 输出震动传感器状态
        if vibration_status:
            print("震动！")
        else:
            print("安静")

        # 等待一段时间再次检查
        time.sleep(0.1)

except KeyboardInterrupt:
    # 如果用户按下Ctrl+C，则清理GPIO设置
    GPIO.cleanup()
