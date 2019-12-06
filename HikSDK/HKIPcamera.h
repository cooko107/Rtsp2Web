//HKIPcamera.h
#include <opencv2/opencv.hpp>
using namespace cv;

void init(char* ip, char* usr, char* password);
Mat getframe();
void release();