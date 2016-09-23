# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import numpy as np
from numpy import sin,cos,sqrt


'''
2b) Rasterize a mesma curva definida no item anterior utilizando uma mostragem adaptativa espaçada de 1/||y'(t)||
'''

def amostragem_adaptativa(nome_arquivo):

    matriz_imagem = np.zeros((200,200), dtype=np.uint8)

    t = 0
    while t < 100:
        x = t*sin(t)
        y = t*cos(t)
        
        x = 199-int(x+99)
        y = int(y+99)
        
        matriz_imagem[x][y] = 255
        t = t + (1.0/sqrt((sin(t) + t*cos(t))**2 + (cos(t) - t*sin(t))**2))
    
    imagem_adaptativa = Image.fromarray(matriz_imagem)
    imagem_adaptativa.save(nome_arquivo)

amostragem_adaptativa('02_adaptativa.png')
