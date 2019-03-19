# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 01:22:06 2018

@author: vignajeeth
"""

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import timeit
# Create a new DSA key
def Question_G_and_H(keysize):
    
    kb=open('1kb.bin','rb')
    Mb=open('1Mb.bin','rb')
    
    kb_cont=kb.read()
    Mb_cont=Mb.read()

    a = timeit.default_timer()    
    key = DSA.generate(keysize)
    b = timeit.default_timer()
    
    publickey=key.publickey()
    
    hash_obj = SHA256.new(kb_cont)
    signer = DSS.new(key, 'fips-186-3')
    c = timeit.default_timer()
    signature = signer.sign(hash_obj)
    d = timeit.default_timer()
    pkey=DSS.new(publickey,'fips-186-3')
    
    try:
        e = timeit.default_timer()
        pkey.verify(hash_obj,signature)
        f = timeit.default_timer()
        valid = True
    except ValueError:
        valid = False
    print(valid)
    
    hash_obj = SHA256.new(Mb_cont)
    signer = DSS.new(key, 'fips-186-3')
    g = timeit.default_timer()
    signature = signer.sign(hash_obj)
    h = timeit.default_timer()
    pkey=DSS.new(publickey,'fips-186-3')
    
    try:
        i = timeit.default_timer()
        pkey.verify(hash_obj,signature)
        j = timeit.default_timer()
        valid = True
    except ValueError:
        valid = False
    print(valid)
    print()
    print("Key generation time:",b-a)
    print("Time to produce a signature for 1kb file:",d-c)
    print("Time to produce a signature for 1Mb file:",h-g)
    print("Time to verify a signature for 1kb file:",f-e)
    print("Time to verify a signature for 1Mb file:",j-i)
    print()
    print("Signature producing speed for 1kb file:",(d-c)/1024)
    print("Signature producing speed for 1Mb file:",(h-g)/1024000)
    print("Signature verifying speed for 1kb file:",(f-e)/1024)
    print("Signature verifying speed for 1Mb file:",(j-i)/1024000)

    
Question_G_and_H(2048)			# Change stuff for g and h


