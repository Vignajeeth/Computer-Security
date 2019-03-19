# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 05:07:31 2018

@author: vignajeeth
"""
def Question_D():
    from Crypto.Hash import SHA256
    from Crypto.Hash import SHA512
    from Crypto.Hash import SHA3_256
    
    import timeit
    
    kb=open('1kb.bin','rb')
    Mb=open('1Mb.bin','rb')
    
    kb_cont=kb.read()
    Mb_cont=Mb.read()
    
    #________SHA 256__________
    sha256k = SHA256.new()
    a = timeit.default_timer()
    sha256k.update(kb_cont)
    b = timeit.default_timer()
    print (sha256k.hexdigest())
    
    sha256M = SHA256.new()
    c = timeit.default_timer()
    sha256M.update(Mb_cont)
    d = timeit.default_timer()
    print (sha256M.hexdigest())
    
    #________SHA 512__________
    sha512k = SHA512.new()
    e = timeit.default_timer()
    sha512k.update(kb_cont)
    f = timeit.default_timer()
    print (sha512k.hexdigest())
    
    sha512M = SHA512.new()
    g = timeit.default_timer()
    sha512M.update(Mb_cont)
    h = timeit.default_timer()
    print (sha512M.hexdigest())
    
    
    #________SHA3 256_________
    sha3256k = SHA3_256.new()
    i = timeit.default_timer()
    sha3256k.update(kb_cont)
    j = timeit.default_timer()
    print (sha3256k.hexdigest())
    
    sha3256M = SHA3_256.new()
    k = timeit.default_timer()
    sha3256M.update(Mb_cont)
    l = timeit.default_timer()
    print (sha3256M.hexdigest())
    print()
    print()
    print("Time required to compute a hash using SHA256 for 1kb file:  ",b-a)
    print("Time required to compute a hash using SHA256 for 1Mb file:  ",d-c)
    print("Time required to compute a hash using SHA512 for 1kb file:  ",f-e)
    print("Time required to compute a hash using SHA512 for 1Mb file:  ",h-g)
    print("Time required to compute a hash using SHA3-256 for 1kb file:",j-i)
    print("Time required to compute a hash using SHA3-256 for 1Mb file:",l-k)
    print()
    print("Hash speed using SHA256 for 1kb file (seconds per byte):  ",(b-a)/1024)
    print("Hash speed using SHA256 for 1Mb file (seconds per byte):  ",(d-c)/1024000)
    print("Hash speed using SHA512 for 1kb file (seconds per byte):  ",(f-e)/1024)
    print("Hash speed using SHA512 for 1Mb file (seconds per byte):  ",(h-g)/1024000)
    print("Hash speed using SHA3-256 for 1kb file (seconds per byte):",(j-i)/1024)
    print("Hash speed using SHA3-256 for 1Mb file (seconds per byte):",(l-k)/1024000)





#----- e and f ------



def Question_E_and_F(keysize):    
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    
    import timeit
    
    kb=open('1kb.bin','rb')
    Mb=open('1Mb.bin','rb')
    
    kb_cont=kb.read()
    Mb_cont=Mb.read()
    
    a = timeit.default_timer()
    key = RSA.generate(keysize)
    b = timeit.default_timer()
    
    f = open('key.pem','wb')
    f.write(key.export_key('PEM'))
    f.close()
    
    cipher = PKCS1_OAEP.new(key)
    
    KB=[]
    KBC=[]
    KBC_op=[]
    for i in range(0,1024,128):    
        KB.append(kb_cont[i:i+128])
    #ciphertext = cipher.encrypt(kb_cont)
    
    MB=[]
    MBC=[]
    MBC_op=[]
    for i in range(0,1024000,200):
        MB.append(Mb_cont[i:i+200])
    
    c = timeit.default_timer()
    for i in KB:
        KBC.append(cipher.encrypt(i))
    d = timeit.default_timer()
    for i in MB:
        MBC.append(cipher.encrypt(i))
    e = timeit.default_timer()
    
    #cipher = PKCS1_OAEP.new(key)
    
    for i in KBC:
        KBC_op.append(cipher.decrypt(i))
    f = timeit.default_timer()
    
    for i in MBC:
        MBC_op.append(cipher.decrypt(i))
    g = timeit.default_timer()
    
    
        
    print("Time required for generating a key:                ",b-a)
    
    print("Time required for encrypting 1kb file:             ",d-c)
    print("Time required for encrypting 1Mb file:             ",e-d)
    
    print("Time required for decrypting 1kb file:             ",f-e)
    print("Time required for decrypting 1Mb file:             ",g-f)
    
    print("Encryption speed for 1kb file (seconds per byte):  ",(d-c)/1024)
    print("Encryption speed for 1Mb file (seconds per byte):  ",(e-d)/1024000)
    
    print("Decryption speed for 1kb file (seconds per byte):  ",(f-e)/1024)
    print("Decryption speed for 1Mb file (seconds per byte):  ",(g-f)/1024000)

#Question_D()				# Uncomment for question d
Question_E_and_F(3072)			# Change parameters appropriately forquestion e and f

