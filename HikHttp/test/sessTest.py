
from threading import Thread
import time
import sys
sys.path.append('/workspace/xo_rtsp_server')
from utils import HikHttp


def run_th(client, round, i):
    for _ in range(round):
        frame = client.get_frame()
        print(i, 'get frame')
        time.sleep(1)


if __name__ == '__main__':
    c1 = HikHttp.HikClient('http://10.19.7.103', 'admin', 'admin', timeout=2)
    c2 = HikHttp.HikClient('http://10.19.7.103', 'admin', 'admin', timeout=2)
    t1 = Thread(target=run_th, args=(c1, 100, 1))
    t2 = Thread(target=run_th, args=(c2, 20, 2))
    # t1.daemon = True
    # t2.daemon = True
    t1.start()
    t2.start()
