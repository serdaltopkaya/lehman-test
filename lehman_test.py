#!/usr/bin/python

import random
ss=raw_input("sayiyi kendiniz girmek istiyormusunuz (e/h)")
if ss=="e":
    p=int(raw_input("sayiyi giriniz: "))
else:   
    p=(random.randrange(1,10))*2**128
exp=((p-1)/2)
j=0
y="e"

def modpow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent & 1 == 1: # sayi tek ise
            result = (result * base) % modulus
        exponent = exponent >> 1 #sayiyi 2 ye bol
        base = (base * base) % modulus
    return result

while(y!="h"):
    a=random.randrange(1,p)
    result1=modpow(a,exp,p)
    if result1==1 or (p-result1)==1:
        j=j+1
        print j,". denemede  ", p, "sayisi  %",100*(1/(float(2**j))), "oraninda asal olmama ihtimali var"

    else :
        j=j+1
        print p, "sayisi ", j, ". denemede asal olmadigi tespit edildi "
        break
    y=str(raw_input("devam etmek istiyormusunuz (e\h)"))
