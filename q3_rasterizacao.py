# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import numpy as np
from numpy import sin,cos,sqrt


'''
3) Rasterize a região U definida por:
   U = ( x,y ) tais que:
         x + y > 1
         ( x , y ) pertence ao disco de raio 1 e centro (0,1)
         ( x, y ) pertence ao disco de raio 1 e centro (1,0)
 Janela [ 0,1 ] x [ 0,1 ]

'''

def rasteriza(nome_arquivo):

    matriz_imagem = np.zeros((200,200), dtype=np.uint8)
    
    for i in range(0,200):
        for j in range(0,200):
            x = i/200
            y = j/200

            if (x + y) > 1 and (x**2 + (y-1)**2) < 1 and ((x-1)**2 + y**2) < 1:
                matriz_imagem[199-i][j] = 255
                
    imagem_rasterizada = Image.fromarray(matriz_imagem)
    imagem_rasterizada.save(nome_arquivo)

rasteriza('03_rasterizada.png')
