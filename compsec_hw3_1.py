# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:51:51 2018

@author: vignajeeth
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import timeit



def Encrypt_and_Decrypt(Modeno,bits):
    
    a = timeit.default_timer()
    key = get_random_bytes(int(bits/8))
    b = timeit.default_timer()
        
    Mode=[AES.MODE_CBC,AES.MODE_CTR]
    cipher = AES.new(key, Mode[Modeno])
    
    kb=open('1kb.bin','rb')
    Mb=open('1Mb.bin','rb')
    
    kb_cont=kb.read()
    Mb_cont=Mb.read()
    
    c = timeit.default_timer()
    ciphertext_kb=cipher.encrypt(kb_cont)
    d = timeit.default_timer()
    ciphertext_Mb=cipher.encrypt(Mb_cont)
    e = timeit.default_timer()
    
    cipher = AES.new(key, AES.MODE_CBC)
    
    f = timeit.default_timer()
    op_kb=cipher.decrypt(ciphertext_kb)
    g = timeit.default_timer()
    op_Mb=cipher.decrypt(ciphertext_Mb)
    h = timeit.default_timer()
    
    print("Time required for generating a key:                ",b-a)
    
    print("Time required for encrypting 1kb file:             ",d-c)
    print("Time required for encrypting 1Mb file:             ",e-d)
    
    print("Time required for decrypting 1kb file:             ",g-f)
    print("Time required for decrypting 1Mb file:             ",h-g)
    
    print("Encryption speed for 1kb file (seconds per byte):  ",(d-c)/1024)
    print("Encryption speed for 1Mb file (seconds per byte):  ",(e-d)/1024000)
    
    print("Decryption speed for 1kb file (seconds per byte):  ",(g-f)/1024)
    print("Decryption speed for 1Mb file (seconds per byte):  ",(h-g)/1024000)


Modeno=0
bits=128
Encrypt_and_Decrypt(Modeno,bits)	#Change parameters appropriately for the first three questions.


