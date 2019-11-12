# -*- coding:utf-8 -*-
import cv2
import numpy as np
import requests
import json
import base64

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EyeumTBoyz78MpcwQ0VArUfW&client_secret=Z8KkV6EdRwO3TD7c9WInrkdZSo0gSTng'
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.get(host)
if response:
    access_token = response.json()["access_token"]
    print(access_token)
    request_url = request_url + "?access_token=" + access_token
else:
    print(response.json())

camera = cv2.VideoCapture(0) # 参数0表示第一个摄像头
# camera = cv2.VideoCapture("test.avi") # 从文件读取视频

# 判断视频是否打开
if (camera.isOpened()):
    print('Open')
else:
    print('Fail to open!')

# # 测试用,查看视频size
# size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
#        int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# print 'size:'+repr(size)

rectangleCols = 30
while True:
    grabbed, frame_lwpCV = camera.read() # 逐帧采集视频流
    if not grabbed:
        break
    cv2.imwrite("1.jpg", frame_lwpCV)

    f = open('1.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())

    gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY) # 转灰度图
    frame_data = np.array(gray_lwpCV)  # 每一帧循环存入数组
    box_data = frame_data[:, 400:400+rectangleCols] # 取矩形目标区域
    pixel_sum = np.sum(box_data, axis=1) # 行求和q
    length = len(gray_lwpCV)
    x = range(length)

    # 画目标区域
    lwpCV_box = cv2.rectangle(frame_lwpCV, (400, 0), (430, length), (0, 255, 0), 2)
    cv2.imshow('lwpCVWindow', frame_lwpCV) # 显示采集到的视频流
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    break
camera.release()
cv2.destroyAllWindows()