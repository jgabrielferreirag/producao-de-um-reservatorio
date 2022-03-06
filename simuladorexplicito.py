

import pandas as pd
import matplotlib.pyplot as plt

n = int(input("Numero de blocos: "))
qtd_poco = int(input("Numero de poços a serem perfurados: "))
poco = []
for i in range(qtd_poco):
    bloco = int(input("Qual bloco será perfurado: "))-1
    poco.append(bloco)
column_names = []
for x in range(n):
    column_names.append("Bloco {0}".format(x+1))

relatorio = pd.DataFrame(columns=column_names)


pressaoi = []
for i in range(n):
    pressaoi.append(float(input(f"Pressão do Bloco {i+1} (psi): ")))
    
T = int(input("Periodo em dias: "))
dt = int(input("Intervalo das medições em dias: "))
n2 = int(T/dt)
index_names = []
for x in range(n2):
    index_names.append("Dia {0}".format(x*dt))

relatorio = pd.DataFrame(columns=column_names, index=index_names)


dx = float(input("Comprimento de cada bloco (ft): "))
dy = float(input("Largura de cada bloco (ft): "))
dz = float(input("Profundidade de cada bloco (ft): "))
BL = float(input("Fator Volume de Formação (RB/STB): "))
BLst = float(input("Fator Volume de Formação Padrão (RB/STB): "))
cl = 3.5*10**(-6)  #(1/Psi)
kx = float(input("Permeabilidade (Darcy): "))
phi = float(input("Porosidade: "))
u = float(input("Viscosidade (cP): "))

Ayz = dy*dz  #Area Transversal (ft²)
Vtotal = dx*dy*dz  #Volume (ft³)
qlsc = float(input("Qual a vazão externa: "))  #(STB/D)
ac = 5.615

parametro1 = (ac*BLst*dt)/(Vtotal*phi*cl)
Bc = 1.127
parametro2 = (Bc*Ayz*kx)/(u*BL*dx)

comp = len(pressaoi)
for i in range(comp):
    relatorio.loc["Dia 0", "Bloco {0}".format(i+1)] = pressaoi[i]


for i in range(n2):
    pressaon = []
    for j in range(comp):
        if j in poco:
            if j == 0:
                px = pressaoi[j]+parametro1*qlsc+parametro1*(parametro2*pressaoi[j+1]-parametro2*pressaoi[j])
                pressaon.append(px)
            elif j == comp:
                px = pressaoi[j]+parametro1*qlsc+parametro1*(parametro2*pressaoi[j-1]-parametro2*pressaoi[j])
                pressaon.append(px)
            else:  
                px = pressaoi[j]+parametro1*qlsc+parametro1*(parametro2*pressaoi[j+1]-2*parametro2*pressaoi[j]+parametro2*pressaoi[j-1])
                pressaon.append(px)
        else:
            if j == 0:
                px = pressaoi[j]+parametro1*(parametro2*pressaoi[j+1]-parametro2*pressaoi[j])
                pressaon.append(px)
            elif j == comp-1:
                px = pressaoi[j]+parametro1*(parametro2*pressaoi[j-1]-parametro2*pressaoi[j])
                pressaon.append(px)
            else:
                px = pressaoi[j]+parametro1*(parametro2*pressaoi[j+1]-2*parametro2*pressaoi[j]+parametro2*pressaoi[j-1])
                pressaon.append(px)
    for j in range(comp):
        relatorio.loc["Dia {0}".format((i+1)*dt), "Bloco {0}".format(j+1)] = pressaon[j]
    pressaoi = pressaon


writer = pd.ExcelWriter("relatorio1exp.xlsx")
relatorio.to_excel(writer)
writer.save()


relatorio.index = relatorio.index.str.extract(r'(\d+)').astype(int).squeeze().tolist()
relatorio.plot().line()

plt.show()
