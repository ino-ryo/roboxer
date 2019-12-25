
import serial
import getch

def main():
    #with serial.Serial('/dev/cu.usbserial-AI05UAD9', 9600,timeout = 1)  as sr:
    with serial.Serial('/dev/ttyACM0', 115200,timeout = 1)  as sr:
    #with serial.Serial('/dev/ttyUSB1', 115200,timeout = 1)  as sr:
        while True:
            
            key = ord(getch.getch())
            if key == 119:
                flag=bytes('w','utf-8')
                sr.write(flag)
            elif key==97:
                flag=bytes('a','utf-8')
                sr.write(flag)
            elif key==115:
                flag=bytes('s','utf-8')
                sr.write(flag)
            elif key==100:
                flag=bytes('d','utf-8')
                sr.write(flag)
            elif key==120:
                flag=bytes('x','utf-8')
                sr.write(flag)
            elif key==113:
                flag=bytes('q','utf-8')
                sr.write(flag)
            elif key==101:
                flag=bytes('e','utf-8')
                sr.write(flag)
            elif key==27:
                break
            #int_data = sr.read()
            #if(int_data < bytes(100)):
                #int_data = int.from_bytes(int_data , 'big')
            #print(int_data)
            #print("\n")
        #ESC押されたらおわり
        sr.close() 
if __name__  == "__main__":
    main()
