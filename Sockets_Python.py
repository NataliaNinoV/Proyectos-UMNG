# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 04:40:01 2021

@author: CristianFelipe
"""
from socket import *
import time

direccion=("192.168.1.50",8000)

cliente_socket=socket(AF_INET,SOCK_DGRAM)

cliente_socket.settimeout(1)

while(1):
    
    data="1"
    cliente_socket.sendto(data.encode(),direccion)
    
    try:
        
        rec_data,addr=cliente_socket.recvfrom(2048)
        grados=float(rec_data)*360/1024
        print("Los grados del potenciometro son: {0}".format(grados))
        
    except:
        
        print("Algo anda mal")
        
    time.sleep(2)
            
        