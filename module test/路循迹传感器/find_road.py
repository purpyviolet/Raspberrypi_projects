import RPi.GPIO as GPIO
import time

# 定义路循迹传感器连接的引脚
sensor_pin = 21  # 假设传感器连接到GPIO引脚21上


def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(sensor_pin, GPIO.IN)  # 将传感器引脚设置为输入模式


def read_sensor():
    # 读取传感器状态
    sensor_value = GPIO.input(sensor_pin)
    return sensor_value


def loop():
    while True:
        sensor_data = read_sensor()
        if sensor_data == GPIO.LOW:
            print("传感器状态: 检测到线路")
        else:
            print("传感器状态: 未检测到线路")

        time.sleep(0.1)  # 每隔0.1秒读取一次传感器状态


def destroy():
    GPIO.cleanup()  # 清理GPIO设置


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

