import RPi.GPIO as GPIO
import time

# 定义土壤湿度传感器连接的引脚
digital_pin = 21  # 数字输出（DO）连接的GPIO引脚
analog_pin = 20  # 模拟输出（AO）连接的GPIO引脚


def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(digital_pin, GPIO.IN)  # 设置数字输出引脚为输入模式
    GPIO.setup(analog_pin, GPIO.IN)  # 设置模拟输出引脚为输入模式


def read_analog():
    # 读取模拟输出的电压值
    analog_value = GPIO.input(analog_pin)
    return analog_value


def read_digital():
    # 读取数字输出的状态
    digital_value = GPIO.input(digital_pin)
    return digital_value


def loop():
    while True:
        # 读取模拟输出值
        analog_data = read_analog()
        print("模拟输出值:", analog_data)

        # 读取数字输出状态
        digital_data = read_digital()
        if digital_data == GPIO.LOW:
            print("数字输出: 湿润")
        else:
            print("数字输出: 干燥")

        time.sleep(1)  # 每隔1秒读取一次传感器数据


def destroy():
    GPIO.cleanup()  # 清理GPIO设置


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

