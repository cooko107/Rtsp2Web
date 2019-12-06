## 1. rtsp2html5
### 优点: cpu占用低
### 缺点: 延迟高
### 参考链接: <https://github.com/ralphhughes/Rtsp2Html5>
### 依赖: nodejs ffmpeg

####原代码里填的是固定值，我稍微改造了一下，改成传递一个rtsp流地址然后去获取流


## 2. rtsp->nginx->rtmp
### 优点: cpu占用低
### 缺点: 延迟高，不能动态传流
### 依赖: nginx ffmpeg
### 参考链接: <https://blog.csdn.net/zx763/article/details/83002528>

#### 配置文件就不贴了，我不太喜欢这种方式，因为每次都要开个ffmpeg命令很麻烦，而且我尝试过 延迟还是高的 


## 3. opencv
### 优点: cpu占用高
### 缺点: 延迟低
### 依赖: opencv flask(或其他服务框架)
### 参考链接: <https://www.cnblogs.com/arkenstone/p/7159615.html>

#### cpu占用高，开多了是个问题


## 4. 海康http接口
### 优点: cpu占用低，延迟低
### 缺点: 帧数低,有http接口才可
### 依赖: hikvisionapi flask(或其他服务框架)
### 参考链接: <https://pypi.org/project/hikvisionapi/>

#### 帧数不高，一次http访问大概在0.15s左右，然后我碰到的问题是linux下，开两个窗口，然后关闭其中一个，另一个就会timeout，windows下不会有这个问题，不知道为何

## 5. gstream
### 优点: 延迟低
### 缺点: cpu占用一般
### 依赖: gstreamer flask(或其他服务框架)
### 参考链接: <https://github.com/sahilparekh/GStreamer-Python>

#### 延迟低(针对rtsp流，非实际)，cpu占用还行，比较推荐，但实际部署中发现部分rtsp流读不了，会报错，不知为何


## 6. 海康sdk
### 参考链接: <https://blog.csdn.net/ustczhang/article/details/79030715>
#### 原文用codeblocks编译的,因为我没有gui，所以写成了setup.py文件,编译通过了，信息显示登录和取流也成功了，但是出现error happend，c++较弱,没有继续调试。