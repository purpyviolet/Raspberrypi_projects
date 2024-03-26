import RPi.GPIO as GPIO
import time

# 使用BCM GPIO引脚编号
GPIO.setmode(GPIO.BCM)

# 设置GPIO 21引脚为输入，并启用内部上拉电阻
# （假设低电平表示暗，高电平表示亮）
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # 读取传感器状态
        sensor_value = GPIO.input(21)

        if sensor_value == 0:
            print("光线检测：亮")
        else:
            print("光线检测：暗")

        # 每秒检测一次
        time.sleep(1)

except KeyboardInterrupt:
    # 捕获Ctrl+C，清理资源后退出
    GPIO.cleanup()
