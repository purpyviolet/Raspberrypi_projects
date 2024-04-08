# encoding:utf-8
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
CLK = 20  # 时钟引脚
DIO = 21  # 数据引脚
segdata = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]  # 0-9
segdatadp = [0xbf, 0x86, 0xdb, 0xcf, 0xe6, 0xed, 0xfd, 0x87, 0xff, 0xef]  # 带小数点的0-9


# 发送起始位，时钟为高的时候，数据线需要一个高低的跳变
def tm1637_start():
    GPIO.output(CLK, 1)
    GPIO.output(DIO, 1)
    GPIO.output(DIO, 0)
    GPIO.output(CLK, 0)


# 发送停止位，数据线拉低，时钟线由低到高的跳变，产生一个停止信号给TM1637
def tm1637_stop():
    GPIO.output(DIO, 0)
    GPIO.output(CLK, 0)
    GPIO.output(CLK, 1)
    GPIO.output(DIO, 1)


# 写位
def write_bit(bit):
    GPIO.output(CLK, 0)
    if bit:
        GPIO.output(DIO, 1)
    else:
        GPIO.output(DIO, 0)
    GPIO.output(CLK, 1)


# 写字节（8个二进制位的发送）
def write_byte(data):
    for i in range(8):
        write_bit((data >> i) & 0x01)
    GPIO.output(CLK, 0)
    GPIO.output(DIO, 1)
    GPIO.output(CLK, 1)
    GPIO.setup(DIO, GPIO.IN)
    while GPIO.input(DIO):
        pass
    GPIO.setup(DIO, GPIO.OUT)


# 写命令，写命令只有一个参数，就是命令本身
def write_command(cmd):
    tm1637_start()
    write_byte(cmd)
    tm1637_stop()


# 写数据，两个参数，第一个参数数据写入的位置，第二个参数要写入的数据内容
def write_data(addr, data):
    tm1637_start()
    write_byte(addr)
    write_byte(data)
    tm1637_stop()


# 显示时间：时分
def time_display(hour_shi, hour_ge, min_shi, min_ge, f_dp):
    write_command(0x40)  # 写数据
    write_command(0x44)  # 固定地址
    write_data(0xc0, segdata[int(hour_shi)])  # 时的十位
    if f_dp:
        write_data(0xc1, segdatadp[int(hour_ge)])  # 时的个位，带小数点
    else:
        write_data(0xc1, segdata[int(hour_ge)])  # 分的十位
    write_data(0xc2, segdata[int(min_shi)])  # 分的个位
    write_data(0xc3, segdata[int(min_ge)])  # 分的个位
    write_command(0x88)  # 显示开


def tm1637_init():
    GPIO.setup(CLK, GPIO.OUT)
    GPIO.setup(DIO, GPIO.OUT)


# main函数
if __name__ == '__main__':
    tm1637_init()  # 初始化数码管
    while True:
        now_time = time.localtime(time.time())  # 获取当前时间
        hour_shi = now_time.tm_hour // 10  # 时的十位
        hour_ge = now_time.tm_hour % 10  # 时的个位
        min_shi = now_time.tm_min // 10  # 分的十位
        min_ge = now_time.tm_min % 10  # 分的个位
        second = now_time.tm_sec
        dp_flag = second % 2 == 0  # 判断奇偶性
        time_display(hour_shi, hour_ge, min_shi, min_ge, dp_flag)
        time.sleep(1)  # 每秒更新一次数码管显示

