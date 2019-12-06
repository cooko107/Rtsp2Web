from flask import Flask, request, Response
import cv2
import numpy as np
import time
# from hikvisionapi import Client
from utils import HikHttp

app = Flask(__name__)


camera_list = []

class Video(object):
    """Read the camera through opencv"""

    def __init__(self, url):

        excep_file = open('image/exception.jpg', 'rb')
        self.excep_frame = excep_file.read()
        excep_file.close()
        self.hik = False
        self.get_info(url)



    def __del__(self):
        print('++++++++ video release')
        self.cap.release()
        # self.cam.release()

    def get_info(self, url):
        main_info = url.split('/')[2]
        if len(main_info.split('@')) > 1:
            username, pwd = main_info.split('@')[0].split(':')[0], main_info.split('@')[0].split(':')[1]
            host = main_info.split('@')[1].split(':')[0]
            self.cam = HikHttp.HikClient('http://' + host, username, pwd, timeout=2)
            self.hik = True
        self.cap = cv2.VideoCapture(url)


    def resize(self, frame):
        h, w = frame.shape[0], frame.shape[1]
        return cv2.resize(frame, (int(500 * w / h), 500))


    def get_frame(self):
        # 一帧一帧捕获视频
        if not self.hik:
            flag, frame = self.cap.read()
            if not flag:
                return self.excep_frame
            else:
                frame = self.resize(frame)
                flag, jpg = cv2.imencode('.jpg', frame)
                return np.array(jpg).tostring()
        try:
            response = self.cam.get_frame()
            return response.content
        except Exception as e:
            print('error happend', e)
            self.hik = False
            return self.excep_frame


def gen(camera):
    """Video stream generation function"""

    while True:
        frame = camera.get_frame()
        # time.sleep(0.01)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/index', methods=['get', 'post'])
def index():
    url = request.values.get('url')
    print(url)
    v = Video(url)
    return Response(gen(v), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run('0.0.0.0', 50010, threaded=True)
