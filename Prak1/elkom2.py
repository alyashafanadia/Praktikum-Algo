# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 21:29:04 2022

@author: User
"""

import math

a1, a2 = input("Masukkan titik koordinat A : ").split(",")
b1, b2 = input("Masukkan titik koordinat B : ").split(",")

jarak = math.sqrt(((int(a2)-int(a1))**2)+((int(b2)-int(b1))**2))

print("Jarak dari titik A (", a1, ",", a2, ") ke titik B (", b1, ",", b2, ") adalah : ", jarak)
