'''
@Copyright (C): 2010-2019, Shenzhen Yahboom Tech
@Author: Malloy.Yuan
@Date: 2019-07-17 10:10:02
@LastEditors: Malloy.Yuan
@LastEditTime: 2019-09-17 17:54:19
'''
#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import string
import serial

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

class ServoSerial:
    
    __servo_1_min = 600
    __servo_1_max = 3600
    __servo_2_min = 1300
    __servo_2_max = 4095
    
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyTHS1", 115200, timeout = 0.001)
        print ("serial Open!")
    
    def __del__(self):
        self.ser.close()
        print ("serial Close!")

    def Servo_serial_control(self, index, angle):
        pack1 = 0xff
        pack2 = 0xff
        id = index
        len = 0x07
        cmd = 0x03
        addr = 0x2A
        #Keep the servo pulse of the servo within a safe range
        if index == 1:
            if angle<self.__servo_1_min:
                angle=self.__servo_1_min
            elif angle>self.__servo_1_max:
                angle = self.__servo_1_max
        elif index == 2:
            if angle<self.__servo_2_min:
                angle=self.__servo_2_min
            elif angle>self.__servo_2_max:
                angle=self.__servo_2_max

        pos_H = (angle >> 8) & 0x00ff
        pos_L = angle & 0x00ff
        
        time_H = 0x00   # time = 500ms Decomposed into two
        time_L = 0x0A
        checknum = (~(id + len + cmd + addr + pos_H + pos_L + time_H + time_L)) & 0xff
        print(checknum)
        data = [pack1, pack2, id, len, cmd, addr, pos_H, pos_L, time_H, time_L, checknum]
        print(bytes(data))
        self.ser.write(bytes(data))

    def Servo_serial_double_control(self, index_1, angle_1, index_2, angle_2):
        pack1 = 0xff
        pack2 = 0xff
        id = 0xFE
        id_1 = index_1
        id_2 = index_2
        len = 0x0E
        cmd = 0x83
        addr1 = 0x2A
        addr2 = 0x04
        #Keep the servo pulse of the servo within a safe range
        if angle<self.__servo_1_min:
            angle=self.__servo_1_min
        elif angle>self.__servo_1_max:
            angle = self.__servo_1_max

        if angle<self.__servo_2_min:
            angle=self.__servo_2_min
        elif angle>self.__servo_2_max:
            angle=self.__servo_2_max

        pos1_H = (angle_1 >> 8) & 0x00ff
        pos1_L = angle_1 & 0x00ff

        pos2_H = (angle_2 >> 8) & 0x00ff
        pos2_L = angle_2 & 0x00ff
        
        time1_H = 0x00   # time = 10ms Decomposed into two
        time1_L = 0x0A

        time2_H = 0x00   # time = 10ms Decomposed into two
        time2_L = 0x0A

        checknum = (~(id + len + cmd + addr1 + addr2 + id_1 + pos1_H + pos1_L + time1_H + time1_L + id_2 + pos2_H + pos2_L + time2_H + time2_L)) & 0xff
        print(checknum)
        data = [pack1, pack2, id, len, cmd, addr1, addr2, id_1, pos1_H, pos1_L, time1_H, time1_L, id_2, pos2_H, pos2_L, time2_H, time2_L, checknum]
        print(bytes(data))
        self.ser.write(bytes(data))

	
	
	
	
	
	
