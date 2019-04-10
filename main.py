import serial
import time
scale=serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=1)

#flush input buffer just in case
scale.flushInput()

#open pipe
scalepipe = open('/dev/shm/scalepipe','w')

try:

   while True:
       #do we have something on the serial port
       if scale.inWaiting() > 0 :
          #ok read until cariage return or timeout
          info = scale.readline().decode('utf-8')
          #send it to pipe
          print(info)
          scalepipe.write(info)
          scalepipe.flush()
       else:
          #add a delay to reduce cpu usage
          time.sleep(0.001)


except KeyboardInterrupt:
       scalepipe.close()
       print('done')