import serial #导入模块
try:
    #端口， GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
   
    CLIport = serial.Serial('/dev/ttyACM0', 115200)
    # 写数据
    result=CLIport.write("test".encode("uft-8"))
    
    CLIport.close()#关闭串口

except Exception as e:
    print("---异常---： ",e)