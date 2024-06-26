import RPi.GPIO as GPIO
import time

tilt_pin = 21  # 倾斜传感器连接的GPIO引脚


def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(tilt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置GPIO口为输入模式，启用上拉电阻


def loop():
    while True:
        if GPIO.input(tilt_pin) == GPIO.LOW:
            print("物体倾斜！")
        else:
            print("物体平稳")

        time.sleep(0.1)  # 稍微延时一下，防止过于频繁读取传感器状态


def destroy():
    GPIO.cleanup()  # 清理GPIO设置


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

