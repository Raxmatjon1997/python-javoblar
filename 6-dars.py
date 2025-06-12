# -*- coding: utf-8 -*-
"""
Created on Wed May 28 19:18:39 2025

@author: Рахматжон
"""
#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

#son=int(input("Istalgan sonni kiriting \n>>>"))
#kvdrt=son**2
#kub=son**3
#print(str(son)+" ning kvadrati "+str(kvdrt)+" ga teng") 
#print(str(son)+" ning kubi "+str(kub)+" ga teng")


#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
#yosh=int(input("Yoshingiz nechida? \n>>>"))
#t_yil=2025-yosh
#print("Siz "+str(t_yil)+" da tug'ilgansiz")


#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning 
#yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
a=float(input("1-sonni kiriting:"))
b=float(input("2-sonni kiriting:"))
yigindi=a+b
ayirma=a-b
kopaytma=a*b
bolinma=a/b

print(str(a)+"+"+str(b)+"="+str(yigindi))
print(str(a)+"-"+str(b)+"="+str(ayirma))
print(str(a)+"*"+str(b)+"="+str(kopaytma))
print(str(a)+"/"+str(b)+"="+str(bolinma))

