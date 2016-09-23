# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import numpy as np
from numpy import sin,cos,sqrt

'''
############ 1)  Rasterize uma circunferência de centro (0,0) e raio unitário. Pede-se que sejam apresentadas duas soluções, na primeira a circunferência deve ser descrita paramétricamente, e na segunda deve ser descrita implicitamente. Janela: [-1,1] x [-1, 1].

'''

def circunferencia_parametrica(nome_arquivo):    

    matriz_imagem = np.zeros((200,200), dtype=np.uint8)
    for t in range(0,360):
        #passando pra radianos
        x = cos(t*np.pi/180)
        y = sin(t*np.pi/180)
        
        #transladando pra caber na Janela(matriz): [-1,1] x [-1, 1]
        x = int(x*100+99)
        y = int(y*100+99)
        
        #valor da cor do pixel
        matriz_imagem[x][y] = 255
    #obtendo a imagem a partir da matriz montada    
    imagem_circunferencia = Image.fromarray(matriz_imagem)
    #salvando a imagem
    imagem_circunferencia.save(nome_arquivo)

circunferencia_parametrica('01_parametrica.png')
