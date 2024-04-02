import RPi.GPIO as GPIO
import time

ir_sensor_pin = 21  # 红外避障传感器连接的GPIO引脚


def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(ir_sensor_pin, GPIO.IN)  # 设置GPIO口为输入模式


def loop():
    while True:
        if GPIO.input(ir_sensor_pin) == GPIO.LOW:
            print("有物体遮挡红外线！")
        else:
            print("未检测到物体")

        time.sleep(0.1)  # 稍微延时一下，防止过于频繁读取传感器状态


def destroy():
    GPIO.cleanup()  # 清理GPIO设置


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
