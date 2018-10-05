# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
## problème 16
def solve(n):
    p=str(2**n)
    somme=0
    for i in p :
        somme=somme+int(i)
    return somme

assert solve(15)==26   

            
