# -*- coding:utf-8 -*-
import cv2
import requests
import base64

def getPhoto():
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EyeumTBoyz78MpcwQ0VArUfW&client_secret=Z8KkV6EdRwO3TD7c9WInrkdZSo0gSTng'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.get(host)
    if response:
        access_token = response.json()["access_token"]
        print("access_token:" + access_token)
        request_url = request_url + "?access_token=" + access_token
    else:
        print(response.json())
    camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头
    # camera = cv2.VideoCapture("test.avi") # 从文件读取视频

    # 判断视频是否打开
    if (camera.isOpened()):
        print('Open')
    else:
        print('Fail to open!')

    while True:
        grabbed, frame_lwpCV = camera.read()  # 逐帧采集视频流
        if not grabbed:
            break
        cv2.imwrite("1.jpg", frame_lwpCV)

        f = open('1.jpg', 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            response = response.json()
            print(response)

        for people in response["person_info"]:
            print(people["location"])
            q1 = int(people["location"]["left"])
            q2 = int(people["location"]["top"])
            w1 = int(people["location"]["left"] + people["location"]["width"])
            w2 = int(people["location"]["top"] + people["location"]["height"])
            cv2.rectangle(frame_lwpCV, (q1, q2), (w1, w2), (0, 255, 0), 2)

        if response["person_num"] > 0:
            cv2.imwrite("2.jpg", frame_lwpCV)  # 将处理好的祯以图片格式写入文件

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
    return frame_lwpCV


if __name__ == '__main__':
    getPhoto()
