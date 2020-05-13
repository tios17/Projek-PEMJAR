# Import socket
import socket
import os
import threading
# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 1934) )

# Listen sebanyak jumlah backlog
sock.listen(10)

def getfilesize(filename):
    return os.stat(filename).st_size

def handle_thread(conn):
    try :
        while True :
            data = conn.recv(100)
            data = data.decode('ascii')
            filename = str(data)
            print (filename)
            
            #filename = input(str("Input your file : "))
            #file = open(filename , 'rb')
            #size = getfilesize(filename)
            #data_file = file.read(size)
            #conn.send(data_file)

            #print ('Total File',size)    
            #print("Sukses")
    
            with open(filename, "rb") as video:
                buffer = video.read()
                #print(buffer)
                conn.send(buffer)
                conn.close()

    except (socket.error, KeyboardInterrupt):
        print("Done sending..")

try :
    while True :
        # Terima permintaan koneksi
        conn, client_addr = sock.accept()
        clientThread = threading.Thread(target=handle_thread, args=(conn,))
        clientThread.start()

except KeyboardInterrupt :
        print("Server mati")


    # Kirim data
    
       
    




