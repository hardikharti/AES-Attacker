import random	
import sys
sys.path.append('./')

from functions import *

key = 0x2b7e151628aed2a6abf7158809cf4f3c
print("key :"),
print(key)
print("\n")

a=[]
b=[]
c=[]
d=[]

for i in range(256):
	a.append(i)
	b.append(i)
	c.append(i)
	d.append(i)

random.shuffle(b)
random.shuffle(c)
random.shuffle(d)

plain_text = [[0, 0, 0, 0] for _ in range(4)]
plain_text2 = [[0, 0, 0, 0] for _ in range(4)]
for ii in range(256):
    for jj in range(ii+1,256):
        for kk in range(256):
            for ll in range(kk+1,256):
                for i in range(256):
                    for j in range(i+1,256):
                        for k in range(256):
                            for l in range(k+1,256):
                                print("plaintext1")
                                print(a[ii],b[kk],c[i],d[k])
                                print("plaintext2")
                                print(a[jj],b[ll],c[j],d[l])
                                # ToDo : Make this assignment random 
                                plain_text2[0][0] = a[ii]
                                plain_text2[1][1] = b[kk]
                                plain_text2[2][2] = c[i]
                                plain_text2[3][3] = d[k]
                                plain_text[0][0] = a[jj]
                                plain_text[1][1] = b[ll]
                                plain_text[2][2] = c[j]
                                plain_text[3][3] = d[l]
                                p2 = encrypt(key, plain_text)
                                p1 = encrypt(key, plain_text2)

                                if(p2[0][0] == p1[0][0] and p2[1][3] == p1[1][3] and p2[2][2] == p1[2][2] and p2[3][1] == p1[3][1] and plain_text != plain_text2):
                                        print("found")
                                        gp1 = plain_text
                                        gp2 = plain_text2
                                        i = 255
                                        ii = 255
                                        j = 255
                                        jj = 255
                                        k = 255
                                        kk = 255
                                        l = 255
                                        ll = 255
                                        # print(p1, p2)

# good pairs are found
# print(gp1,gp2)
key_try = [[0, 0, 0, 0] for _ in range(4)]
for i in range(256):
    for j in range(256):
        for k in range(256):
            for l in range(256):
                key_try[1][1] = k
                key_try[2][2] = j
                key_try[3][3] = i
                key_try[0][0] = l
                xp = encrypttoround1(key_try, gp1)
                yp = encrypttoround1(key_try, gp2)
                zp = xp
                wp = yp
                zp[1][0] = yp[1][0]
                zp[3][0] = yp[3][0]
                wp[1][0] = xp[1][0]
                wp[3][0] = xp[1][0]
                p3 = encryptfrom1(key_try, zp)
                p4 = encryptfrom1(key_try, wp)
                if(p3[0][0] == p4[0][0] and p3[1][3] == p4[1][3] and p3[2][2] == p4[2][2] and p3[3][1] == p4[3][1]):
                    print(key_try)
                    print("SUCCESS")
