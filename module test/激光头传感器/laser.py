import RPi.GPIO as GPIO
import time

# 设置GPIO引脚号
laser_pin = 21


def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(laser_pin, GPIO.OUT)  # 将GPIO引脚设置为输出模式


def loop():
    while True:
        # 开启激光
        GPIO.output(laser_pin, GPIO.HIGH)
        print("激光已开启！")
        time.sleep(1)  # 等待1秒

        # 关闭激光
        GPIO.output(laser_pin, GPIO.LOW)
        print("激光已关闭！")
        time.sleep(1)  # 等待1秒


def destroy():
    GPIO.cleanup()  # 清理GPIO设置


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

