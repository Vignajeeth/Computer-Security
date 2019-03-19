
#from Crypto.Random import get_random_bytes


#key = get_random_bytes(16)
from Crypto.Cipher import AES
import timeit



message=b'qwertyuiopasdfgh'
key=b'1234567890123456'
Hardware=[]
Software=[]
Ratio=[]

for i in range(7):
	k=10**i
	a = timeit.default_timer()
	for j in range(k):
		Cipher=AES.new(key,AES.MODE_ECB,use_aesni=False)
		Ciphertext=Cipher.encrypt(message)
	b = timeit.default_timer()

	#fm=Cipher.decrypt(Ciphertext)
	#print(fm)


	c = timeit.default_timer()
	for j in range(k):
		Cipher=AES.new(key,AES.MODE_ECB,use_aesni=True)
		Ciphertext=Cipher.encrypt(message)
	d = timeit.default_timer()

	#fm1=Cipher.decrypt(Ciphertext)
	#print(fm1)
	print("Software AES for ",i,"th power of 10 :	",b-a)
	print("Hardware AES for ",i,"th power of 10 :	",d-c)
	Hardware.append(d-c)
	Software.append(b-a)
	Ratio.append((b-a)/(d-c))

import matplotlib.pyplot as plt
ivalues=[0,1,2,3,4,5,6]
plt.ylabel('Ratio of Time Taken')
plt.xlabel('Magnitudes of 10')
plt.title('AES Hardware vs Software')
#plt.plot(ivalues,Hardware,'r',label='Hardware')
#plt.plot(ivalues,Software,'b',label='Software')
plt.plot(ivalues,Ratio,'g')
#plt.legend()
plt.show()

