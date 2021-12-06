import os                                       
# 删除图片文件
import cv2                                      
# 调用摄像头拍摄照片
import time
#设定拍照间隔

index = 1

# 调用摄像头拍摄照片
def get_photo():
    # 开启摄像头
    cap = cv2.VideoCapture(0)           
    # 将摄像头中的一帧图片数据保存
    f, frame = cap.read()      
    # 将图片保存为本地文件
    cv2.imwrite('photos/image'+str(index)+'.jpg', frame)    
    # 关闭摄像头
    cap.release()

flag = 3

while(flag>0):
    get_photo()
    time.sleep(0.5)
    flag = flag-1
    index = index + 1
    

