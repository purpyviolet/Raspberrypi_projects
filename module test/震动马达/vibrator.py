import RPi.GPIO as GPIO
import time

# 定义震动马达模块连接的引脚
motor_pin = 21  # 假设震动马达模块连接到GPIO引脚21上

def setup():
    GPIO.setmode(GPIO.BCM)  # 设置GPIO模式为BCM
    GPIO.setup(motor_pin, GPIO.OUT)  # 将震动马达引脚设置为输出模式

def vibrate(duration):
    # 控制震动马达模块震动一段时间
    GPIO.output(motor_pin, GPIO.HIGH)  # 开启震动
    time.sleep(duration)  # 持续震动指定的时间
    GPIO.output(motor_pin, GPIO.LOW)  # 关闭震动

def loop():
    while True:
        # 持续震动1秒钟
        vibrate(1)
        time.sleep(1)  # 停止震动1秒钟，然后再次震动

def destroy():
    GPIO.cleanup()  # 清理GPIO设置

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
