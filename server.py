# Import socket
import socket
import os
# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 9998) )

# Listen sebanyak jumlah backlog
sock.listen(10)

def getfilesize(filename):
    return os.stat(filename).st_size

while True :
    # Terima permintaan koneksi
    conn, client_addr = sock.accept()
    # Kirim data
    filename = input(str("Input your file : "))
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

    print("Done sending..")




