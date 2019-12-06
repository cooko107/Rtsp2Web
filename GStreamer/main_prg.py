'''\
This Simple program Demonstrates how to use G-Streamer and capture RTSP Frames in Opencv using Python
- Sahil Parekh
'''

import multiprocessing as mp
import time
import vid_streamv3 as vs
import cv2
import sys
from flask import Flask, request, Response
import numpy as np
import time

'''
Main class
'''

app = Flask(__name__)


class mainStreamClass:
    def __init__(self, url):

        # Current Cam
        self.camProcess = None
        self.cam_queue = None
        self.stopbit = None
        # self.camlink = 'rtsp://admin:xiolift123@192.168.13.106/h264/ch1/main/av_stream' #Add your RTSP cam link
        self.camlink = url  # Add your RTSP cam link
        self.framerate = 10
        excep_file = open('image/exception.jpg', 'rb')
        self.excep_frame = excep_file.read()
        excep_file.close()
        self.preframe = None
        self.lastTime = None

    def startMain(self):

        # set  queue size
        self.cam_queue = mp.Queue(maxsize=100)

        # get all cams
        time.sleep(3)

        self.stopbit = mp.Event()
        self.camProcess = vs.StreamCapture(self.camlink,
                                           self.stopbit,
                                           self.cam_queue,
                                           self.framerate)
        self.camProcess.start()

        # calculate FPS
        # lastFTime = time.time()

        # try:
        #     while True:

        #         if not self.cam_queue.empty():
        #             # print('Got frame')
        #             cmd, val = self.cam_queue.get()

        #             '''
        #             #calculate FPS
        #             diffTime = time.time() - lastFTime`
        #             fps = 1 / diffTime
        #             # print(fps)

        #             '''
        #             lastFTime = time.time()

        #             # if cmd == vs.StreamCommands.RESOLUTION:
        #             #     pass #print(val)

        #             if cmd == vs.StreamCommands.FRAME:
        #                 if val is not None:
        #                     print(val.shape)
        #                     # cv2.imshow('Cam: ' + self.camlink, val)
        #                     # cv2.waitKey(1)

        # except KeyboardInterrupt:
        #     print('Caught Keyboard interrupt')

        # except:
        #     e = sys.exc_info()
        #     print('Caught Main Exception')
        #     print(e)

        # self.stopCamStream()
        # cv2.destroyAllWindows()

    def __del__(self):
        print('++++++++ video release')
        self.stopCamStream()

    def stopCamStream(self):
        print('in stopCamStream')

        if self.stopbit is not None:
            self.stopbit.set()
            try:
                while not self.cam_queue.empty():
                    try:
                        _ = self.cam_queue.get()
                    except:
                        break
                    self.cam_queue.close()
                self.camProcess.join()
            except Exception as e:
                raise e

    def get_frame(self):
        # 一帧一帧捕获视频
        time.sleep(0.05)
        if not self.cam_queue.empty():
            cmd, val = self.cam_queue.get()
            if cmd == vs.StreamCommands.FRAME:
                if val is not None:
                    print(val.shape)
                    flag, jpg = cv2.imencode('.jpg', val)
                    self.preframe = np.array(jpg).tostring()
                    self.lastTime = time.time()
                    return np.array(jpg).tostring()
            else:
                print('cmd not right')
                return self.excep_frame
        else:
            print('empty')
            if self.lastTime is None or time.time() - self.lastTime > 60:
                return self.excep_frame
            else:
                return self.preframe


class Video(object):

    def resize(self, frame):
        h, w = frame.shape[0], frame.shape[1]
        return cv2.resize(frame, (int(500 * w / h), 500))


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
    v = mainStreamClass(url)
    v.startMain()
    return Response(gen(v), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run('0.0.0.0', 50010, threaded=True)

# if __name__ == "__main__":
#     mc = mainStreamClass()
#     mc.startMain()