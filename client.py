import numpy as np
import socket
import os
import cv2
n = 0

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi
sock.connect( ("127.0.0.1", 9998) )

def getfilesize(filename):
    return os.stat(filename).st_size

# Receive data dari client

#filename = "File Transfer"
#file = open(filename, 'wb')
#file_data = sock.recv(10485760)
#file.write(file_data)
#file.close()

#print("sukses")
try:
    print("Starting to read bytes..")
    buffer = sock.recv(1024)

    with open('hasil_'+str(n)+'.mp4', "wb") as video:
        n += 1
        i = 0
        while buffer:                
            video.write(buffer)
            print("buffer {0}".format(i))
            i += 1
            buffer = sock.recv(1024)

    
        cap = cv2.VideoCapture('hasil_0.mp4')
        while(1):
            ret, frame = cap.read()
            cv2.imshow('output',frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
                break

        cap.release()
        cv2.destroyAllWindows()
    
except KeyboardInterrupt:
    if sock:
        sock.close()
