import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 设置触发和回声引脚
TRIG = 20
ECHO = 21

# 设置TRIG为输出，ECHO为输入
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # 确保触发引脚是低电平
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    # 产生一个10微秒的高电平脉冲到TRIG引脚
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10微秒
    GPIO.output(TRIG, False)

    # 保存发送脉冲的时间和接收回声的时间
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # 计算脉冲的持续时间
    pulse_duration = pulse_end - pulse_start

    # 使用声速（34300厘米/秒）计算距离，并将其除以2，因为声音要走来回的路程
    distance = pulse_duration * 34300 / 2

    # 四舍五入到两位小数
    distance = round(distance, 2)

    # 返回测量到的距离
    return distance

try:
    while True:
        dist = measure_distance()
        print("Measured Distance = {:.2f} cm".format(dist))
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
