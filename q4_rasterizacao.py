# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import numpy as np
from numpy import sin,cos,sqrt


'''
4 Rasterize a curva descrita implicitamente por F-1(0), onde F é definida por F(x,y) = y2 - x3 + x.  Janela: [-2, 2 ] x [-2, 2 ].
'''

def rasteriza(nome_arquivo):

    matriz_imagem = np.zeros((200,200), dtype=np.uint8)
    for i in range(0,200):
        for j in range(0,200):
            x = (i-0.5-100)/50
            y = (j-100)/50
            z1 = y**2 - x**3 + x
        
            x = (i+0.5-100)/50
            y = (j-100)/50
            z2 = y**2 - x**3 + x
        
            x = (i-100)/50
            y = (j-0.5-100)/50
            z3 = y**2 - x**3 + x
        
            x = (i-100)/50
            y = (j+0.5-100)/50
            z4 = y**2 - x**3 + x
        
            all_pos = z1 > 0 and z2 > 0 and z3 > 0 and z4 > 0 
            all_neg = z1 < 0 and z2 < 0 and z3 < 0 and z4 < 0 
            
            if  not (all_pos or all_neg):
                matriz_imagem[199-j][i] = 255
    imagem_rasterizada= Image.fromarray(matriz_imagem)
    imagem_rasterizada.save(nome_arquivo)
    
rasteriza('04_rasterizada.png')
