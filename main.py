# # zad1
# A=[x-1 for x in range (1,11)]
# print('zbiór a: ',A)
# B=[4**x for x in range (0,7)]
# print('zbiór b: ',B)
# C=[x for x in B if x%2==0]
# print('zbiór c :',C)
#
# zad2
#
# import random
# lista=[]
# a=0
# while a<10:
#      a+=1
#      lista.append(random.randint(0,50))
# A=[x for x in lista if x%2==0]
# print('lista losowa: \n',lista,'lista parzystych elementów: \n',A)
#
# zad3
# #
# produkty={'maliny':'kg','arbuzy':'szt','pomarańcze':'kg','cukierki':'kg','pączki':'szt'}
# produktySzt=[produkty.values() if value=='szt']
# print(produktySzt)
#
# zad4
#
# def czyProst(a,b,c):
#     if a**2+b**2==c**2:
#         print('trójkąt jest prostokątny')
#     else:
#         print('trójkąt nie jest prostokątny')
# print(czyProst(2,2,4))
#
# zad5
#
# def poletrapez(a=1,b=1,h=1):
#     return((a+b)/h)
# print(poletrapez())
# print(poletrapez(a=4,b=3,h=6))
#
# zad6
#
# def iloczynciag(a=1,b=4,ile=10):
#     i=1
#     while i<=ile:
#         a*=b
#         i+=1
#     return(a)
# print(iloczynciag())
#
# zad9
#
import ciągi.arytmetyczne
import ciągi.geometryczne
print(ciągi.arytmetyczne.nWyraz())
print(ciągi.arytmetyczne.suma())
print(ciągi.geometryczne.nWyraz())
print(ciągi.arytmetyczne.suma())