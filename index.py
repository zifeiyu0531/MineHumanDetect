# encoding:utf-8
import base64
import urllib.request
import urllib.parse
import json

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EyeumTBoyz78MpcwQ0VArUfW&client_secret=Z8KkV6EdRwO3TD7c9WInrkdZSo0gSTng'

request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)

content = response.read()
content_dict = json.loads(content)
token = content_dict['access_token']

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"

# 二进制方式打开图片文件
f = open('test.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
params = urllib.parse.urlencode(params).encode("utf-8")

access_token = token
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print(content)

if __name__ == '__main__':
