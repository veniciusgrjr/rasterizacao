# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import numpy as np
from numpy import sin,cos,sqrt
'''
    1)  Rasterize uma circunferência de centro (0,0) e raio unitário. Pede-se que sejam apresentadas duas soluções, na primeira a circunferência deve ser descrita paramétricamente, e na segunda deve ser descrita implicitamente. Janela: [-1,1] x [-1, 1].
'''

def circinferencia_implicita(nome_arquivo):

    matriz_imagem = np.zeros((201,201), dtype=np.uint8)
    for i in range(0,201):
        for j in range(0,201):
            x = (i-0.5-100)/100
            y = (j-100)/100
            z1 = x**2+y**2-1
        
            x = (i+0.5-100)/100
            y = (j-100)/100
            z2 = x**2+y**2-1
        
            x = (i-100)/100
            y = (j-0.5-100)/100
            z3 = x**2+y**2-1
        
            x = (i-100)/100
            y = (j+0.5-100)/100
            z4 = x**2+y**2-1
        
            all_pos = z1 > 0 and z2 > 0 and z3 > 0 and z4 > 0 
            all_neg = z1 < 0 and z2 < 0 and z3 < 0 and z4 < 0 
        
            if  not (all_pos or all_neg):
                    matriz_imagem[i][j] = 255
    imagem_circunferencia = Image.fromarray(matriz_imagem)
    imagem_circunferencia.save(nome_arquivo)
circinferencia_implicita('01_implicita.png')
