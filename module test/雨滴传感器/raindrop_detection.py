import RPi.GPIO as GPIO
import time

rain_pin = 21  # 雨滴传感器连接的GPIO引脚


def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(rain_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置GPIO口为输入模式，启用上拉电阻


def loop():
    while True:
        if GPIO.input(rain_pin) == GPIO.LOW:
            print("检测到雨滴！")
        else:
            print("未检测到雨滴")

        time.sleep(1)  # 稍微延时一下，防止过于频繁读取传感器状态


def destroy():
    GPIO.cleanup()  # 清理GPIO设置


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

