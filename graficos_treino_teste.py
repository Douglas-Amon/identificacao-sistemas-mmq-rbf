import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import butter, sosfiltfilt


dados_treino = np.loadtxt('dados_01.dat')
tempo_treino = dados_treino[:, 0]
entrada_treino = dados_treino[:, 1]
saida_treino = dados_treino[:, 2]

plt.figure(figsize=(12, 4))
plt.plot(tempo_treino, saida_treino, lw=2, alpha=0.5, label='dados de treino')
plt.legend(loc='upper right', bbox_to_anchor=(0.98, 0.99))
plt.grid(True)
plt.show()

dados_teste = np.loadtxt('dados_02.dat')
tempo_teste = dados_teste[:, 0]
entrada_teste = dados_teste[:, 1]
saida_teste = dados_teste[:, 2]

plt.figure(figsize=(12, 4))
plt.plot(tempo_teste, saida_teste, lw=2, alpha=0.5, label='dados de teste')
plt.legend(loc='upper right', bbox_to_anchor=(0.98, 0.99))
plt.grid(True)
plt.show()

![grafico](treino_teste.png)
