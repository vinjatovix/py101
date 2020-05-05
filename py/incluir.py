# -*- coding: utf-8 -*-
"""
Created on Sun May  3 04:33:39 2020

@author: vinja
"""


fichero = open('rec.txt','at')
edad = input('Cual es tu edad?')

fichero.write(f'\n{edad}')

fichero.close()




