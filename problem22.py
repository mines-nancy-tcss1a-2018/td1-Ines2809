# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:20:42 2018

@author: saaif1u
"""
## problème 22
def read():
    fichier=open('p022_names.txt','r')
    for ligne in fichier:
        chaine=ligne
        fichier.close()
        l=chaine.split(',')
        return l


def solve22():
    liste=[]
    l=read()
    for k in l:
        liste=liste.append(k)
        liste=sorted(liste)  # dès lors, la liste est triée
    lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    somme_score=0
    for mot in liste:  # pour chaque mot dans la liste
        mot=str(mot)  # on le transforme en chaine de caracteres
        somme=0
        for i in mot:   # on veut déterminer le rang de chaque lettre de chaque mot grâce à la boucle while
            s=1
            while i != lettres[s]:
                s=s+1
            somme=somme+s  # somme des nombres correspondants aux lettres
    score=somme*(int(mot)+1)
    somme_score=somme_score+score
    return somme_score
            
print (solve(22))       
                
        
        
        
        
        
        
    