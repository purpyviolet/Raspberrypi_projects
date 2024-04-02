import RPi.GPIO as GPIO
import time

flame_sensor_pin = 21  # 火焰传感器连接的GPIO引脚


def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(flame_sensor_pin, GPIO.IN)  # 设置GPIO口为输入模式


def loop():
    while True:
        if GPIO.input(flame_sensor_pin) == GPIO.LOW:
            print("检测到火焰！")
        else:
            print("未检测到火焰")

        time.sleep(1)  # 稍微延时一下，防止过于频繁读取传感器状态


def destroy():
    GPIO.cleanup()  # 清理GPIO设置


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

s