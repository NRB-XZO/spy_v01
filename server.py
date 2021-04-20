import socket

host = "nrbnosafe@duckdns.org"
port = 1604

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket olusturuldu")

    s.bind((host, port)) 
    print("socket {} nolu porta baglandi".format(port))

    s.listen(5)      
    print("socket dinleniyor")
except socket.error as msg:
    print("Hata:",msg)

while True: 

   # Client ile baglanti kurulursa 
   c, addr = s.accept()      
   print('Gelen baglanti:', addr)
  
   komut = str(input("Komut:"))
   c.send(komut.encode('utf-8'))
   c.close()
