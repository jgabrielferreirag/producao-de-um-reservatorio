# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:11:06 2021

@author: joao_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


n=int(input("Numero de blocos: "))
qtdpoço=int(input("Numero de poços a serem perfurados: "))
poços=[]
for i in range(qtdpoço):
    bloco=int(input("Qual bloco será perfurado: "))-1
    poços.append(bloco)
column_names=[]
for x in range(n):
    column_names.append("Bloco {0}".format(x+1))

relatorio=pd.DataFrame(columns=column_names)

    
pressaoi=[]
for i in range(n):
    pressaoi.append(float(input("Pressão do Bloco {0}: ".format(i+1))))
    
T=int(input("Periodo em dias: "))
dt=int(input("Intervalo das medições em dias: "))
n2=int(T/dt)
index_names=[]
for x in range(n2):
    index_names.append("Dia {0}".format(x*dt))

relatorio=pd.DataFrame(columns=column_names, index=index_names)

   
dx=float(input("Comprimento em ft: "))
dy=float(input("Largura em ft: "))
dz=float(input("Profundidade em ft: "))
BL=float(input("Fator Volume de Formação em RB/STB: "))
BLst=float(input("Fator Volume de Formação Padrão em RB/STB: "))
cl=3.5*10**(-6) #(1/Psi)
kx=float(input("Permeabilidade em Darcy: "))
phi=float(input("Porosidade: "))
u=float(input("Viscosidade em cp: "))

Ayz=dy*dz #Area Transversal (ft²)
Vtotal=dx*dy*dz #Volume (ft³)
qlsc=float(input("Qual a vazão externa: ")) #(STB/D)
ac=5.615

parametro1=(Vtotal*phi*cl)/(ac*BLst*dt)

Bc=1.127
parametro2=(Bc*Ayz*kx)/(u*BL*dx)


comp=len(pressaoi)
for i in range(comp):
    relatorio.loc["Dia 0","Bloco {0}".format(i+1)]=pressaoi[i]
    
matriz1=[[0]*n for x in range(n)]


for i in range(n):
    lista=[]
    if i+1==1:
        matriz1[i][i]=-(parametro2+parametro1)
        matriz1[i][i+1]=parametro2
    elif i+1==n:
        matriz1[i][i-1]=parametro2
        matriz1[i][i]=-(parametro2+parametro1)
    else:
        matriz1[i][i]=-(2*parametro2+parametro1)
        matriz1[i][i+1]=parametro2
        matriz1[i][i-1]=parametro2

A=np.array(matriz1)
for k in range(n2):
    pressao2=[[0]*1 for x in range(n)]
    for i in range(n):
        if i in poços:
            pressao2[i]=-(qlsc+parametro1*pressaoi[i])
        else:
            pressao2[i]=-(parametro1*pressaoi[i])
    B=np.array(pressao2)
    X=np.linalg.inv(A).dot(B)
    for j in range(comp):
        relatorio.loc["Dia {0}".format((k+1)*dt),"Bloco {0}".format(j+1)]=X[j]
    pressaoi=X


writer=pd.ExcelWriter("relatorio1imp.xlsx")
relatorio.to_excel(writer)
writer.save()

relatorio.index = relatorio.index.str.extract(r'(\d+)').astype(int).squeeze().tolist()
relatorio.plot().line()

plt.show()
