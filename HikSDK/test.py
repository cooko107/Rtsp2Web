# -*- coding:utf8 -*-
import sys

sys.path.append('/workspace/HikStream')
import HKIPcamera
import time
import numpy as np

ip = str('10.19.31.30')  #摄像头IP地址，要和本机IP在同一局域网
name = str('88888888')       #管理员用户名
pw = str('xiolift123')      #管理员密码
HKIPcamera.init(ip, name, pw)
while True:
    fram = HKIPcamera.getframe()
    print(fram)
    # frame = np.array(fram)
    # print(frame.shape)
#HKIPcamera.release()
#time.sleep(5