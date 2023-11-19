from socket import * 
from threading import *
from tkinter import *
from datetime import datetime  

client = socket(AF_INET, SOCK_STREAM)

ip = "SENİNIPV4ADRESİN"
port = 6666

client.connect((ip, port))

pencere = Tk()

pencere.title("Bağlandı: "+ ip +" "+ str(port))

message = Text(pencere, width=50)
message.grid(row =0, column=0, padx=10, pady=10,)

mesaj_giris = Entry(pencere, width=50)
mesaj_giris.insert(0, "Adınız *")

mesaj_giris.grid(row=1,column=0,
                 padx=10,pady=10,
                 )

mesaj_giris.focus() # hedef belirtme
mesaj_giris.selection_range(0, END)

def mesaj_gonder():
    istemci_mesaji = mesaj_giris.get()
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    message.insert(END, '\n' + 'Sen :'+ istemci_mesaji+'  Tarih: '+timestamp)
    client.send(istemci_mesaji.encode('utf8'))
    mesaj_giris.delete(0, END)
    
btn_msj_gonder = Button(pencere, text="Gönder", width=30, command=mesaj_gonder)
btn_msj_gonder.grid(row=2, column=0, pady=10,padx=10)


def gelen_msaj_kontrol():
    while True:
        server_msg = client.recv(1024).decode('utf8')
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        message.insert(END, '\n'+ server_msg+' Tarih: '+ timestamp)
        
recv_kontrol = Thread(target=gelen_msaj_kontrol)
recv_kontrol.daemon = True
recv_kontrol.start()

pencere.mainloop()
        
