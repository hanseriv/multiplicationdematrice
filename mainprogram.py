"""
user : Jean TROUSSIER
Date : Jeudi 19 septembre
Obj : multiplication matriciel (fichier principal)
"""
import fonctioncalculmatriciel as fcm
a = [[4,5,6],[5,6,8],[7,8,9]]
b = [[8,2,4],[9,1,2],[]]
flag = 0
if fcm.Are_they_matrix(a) == False or fcm.Are_they_matrix(b) ==False:
    print ("non matrix array")
    flag = 1
if fcm.mult_possible(a,b) == False:
    print("non multiplicative matrix")
    flag = 1
if flag != 1 :
    print(fcm.multiplication(a,b))
