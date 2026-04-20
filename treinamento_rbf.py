x1 = []
for i in range(2, len(t), 1):
    x1.append(y[i-1] + y[i-2] + u[i-1] + u[i-2] + np.sin(y[i-1]) + (u[i-1])**3)

print(x1, len(x1))

x2 = []
for i in range(2, len(t2), 1):
    x2.append(y2[i-1] + y2[i-2] + u2[i-1] + u2[i-2] + np.sin(y2[i-1]) + (u2[i-1])**3)

print(x2, len(x2))

u1 = u[2:]
u2 = u2[2:]
y1 = y[2:]
y2 = y2[2:]
t1 = t[2:]
t2 = t2[2:]

# =========================
# RBF - TREINAMENTO
# =========================
centros_rbf = np.linspace(min(x1), max(x1), 4)   # centros das funções de base radial
sigma_rbf = 5.0

print(centros_rbf)

matriz_rbf_treino = np.zeros((len(x1), len(centros_rbf)))

for i in range(matriz_rbf_treino.shape[0]):
    for j in range(matriz_rbf_treino.shape[1]):
        matriz_rbf_treino[i, j] = np.exp(
            -(1 / (2 * sigma_rbf**2)) * (abs(x1[i] - centros_rbf[j])**2)
        )

pesos_rbf = la.pinv(matriz_rbf_treino) @ y1
saida_rbf_treino = matriz_rbf_treino @ pesos_rbf

emq_rbf_treino = 0
for i in range(len(y1)):
    emq_rbf_treino += (y1[i] - saida_rbf_treino[i])**2
emq_rbf_treino /= len(y1)

print(emq_rbf_treino)

texto_rbf_treino = (
    'Ajuste:\n'
    'y_est = %.4f $\\phi_0(t)$ + %.4f $\\phi_1(t)$ + '
    '%.4f $\\phi_2(t)$ + %.4f $\\phi_3(t)$'
    % (
        pesos_rbf[0].item(),
        pesos_rbf[1].item(),
        pesos_rbf[2].item(),
        pesos_rbf[3].item()
    )
)

plt.figure(figsize=(16, 4))
plt.plot(t1, y1, label='saída real de treino')
plt.plot(t1, saida_rbf_treino, label='saída estimada RBF')
plt.xlabel('Tempo')
plt.ylabel('Saída')
plt.title('RBF - Treinamento')

plt.text(
    0.015, 0.95, texto_rbf_treino,
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(boxstyle="round,pad=0.5", facecolor='linen', alpha=0.95)
)

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

emq_rbf_treino = 0
for i in range(len(y1)):
    emq_rbf_treino += (y1[i] - saida_rbf_treino[i])**2
emq_rbf_treino /= len(y1)

print(emq_rbf_treino)

reta_rbf_treino = np.poly1d(np.polyfit(y1, saida_rbf_treino, 1))
eixo_reta_rbf = np.linspace(-5, 5, 500)

plt.figure(figsize=(16, 4))
plt.text(2.5, 3.0, 'EMQ = %.4f' % emq_rbf_treino)
plt.suptitle("Treinamento RBF", fontsize=18, y=0.95)
plt.plot(y1, saida_rbf_treino, 'o', label='amostras')
plt.plot(eixo_reta_rbf, reta_rbf_treino(eixo_reta_rbf), '-', color='red', label='reta de ajuste')
plt.grid(True)
plt.legend()
plt.show()