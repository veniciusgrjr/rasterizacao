# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import numpy as np
from numpy import sin,cos,sqrt


'''
2a) Rasterize a curva  definida parametricamente por  y(t) = (tsen(t), tcos(t)) ,0 < t < 100. Utilize uma amostragem uniforme espaçada de 0,1 na rasterização.

'''

def amostragem_uniforme(nome_arquivo):

    matriz_imagem = np.zeros((200,200), dtype=np.uint8)
    for t in range(0,1000):
        # aplicando a equação da curva
        t = t/10
        x = t*sin(t)
        y = t*cos(t)
        
        # mapeando 200x200
        x = 199-int(x+99)
        y = int(y+99)
        
        #montando a imagem
        matriz_imagem[x][y] = 255
    imagem_uniforme = Image.fromarray(matriz_imagem)
    imagem_uniforme.save(nome_arquivo)
    
amostragem_uniforme('02_uniforme.png')
