# TREINAMENTO DO MMQ
quant_amostras_treino = len(saida_treino)

saida_treino_expandida = np.concatenate(([0.0, 0.0], saida_treino))
entrada_treino_expandida = np.concatenate(([0.0], entrada_treino))

reg_saida_k1 = saida_treino_expandida[1:quant_amostras_treino + 1]
reg_saida_k2 = saida_treino_expandida[0:quant_amostras_treino]
reg_entrada_k0 = entrada_treino_expandida[1:quant_amostras_treino + 1]
reg_entrada_k1 = entrada_treino_expandida[0:quant_amostras_treino]

matriz_normal = np.array([
    [reg_saida_k1.T @ reg_saida_k1, reg_saida_k1.T @ reg_saida_k2, reg_saida_k1.T @ reg_entrada_k0, reg_saida_k1.T @ reg_entrada_k1],
    [reg_saida_k2.T @ reg_saida_k1, reg_saida_k2.T @ reg_saida_k2, reg_saida_k2.T @ reg_entrada_k0, reg_saida_k2.T @ reg_entrada_k1],
    [reg_entrada_k0.T @ reg_saida_k1, reg_entrada_k0.T @ reg_saida_k2, reg_entrada_k0.T @ reg_entrada_k0, reg_entrada_k0.T @ reg_entrada_k1],
    [reg_entrada_k1.T @ reg_saida_k1, reg_entrada_k1.T @ reg_saida_k2, reg_entrada_k1.T @ reg_entrada_k0, reg_entrada_k1.T @ reg_entrada_k1]
])

vetor_normal = np.array([
    [reg_saida_k1.T @ saida_treino],
    [reg_saida_k2.T @ saida_treino],
    [reg_entrada_k0.T @ saida_treino],
    [reg_entrada_k1.T @ saida_treino]
])

parametros_mmq = la.solve(matriz_normal, vetor_normal)
coef_y1, coef_y2, coef_u0, coef_u1 = parametros_mmq.flatten()

saida_estimada_treino = np.zeros_like(saida_treino)

for k in range(quant_amostras_treino):
    saida_estimada_treino[k] = (
        coef_y1 * saida_treino_expandida[k + 1]
        + coef_y2 * saida_treino_expandida[k]
        + coef_u0 * entrada_treino_expandida[k + 1]
        + coef_u1 * entrada_treino_expandida[k]
    )

plt.figure(figsize=(16, 6))
plt.plot(tempo_treino, saida_treino, "o", label="dados de treino", alpha=0.6)
plt.plot(tempo_treino, saida_estimada_treino, "r" ,label="ajuste MMQ", linewidth=2)

texto_mmq_treino = (
    f'Ajuste: y[n] = {coef_y1:.4f}y[n-1] + {coef_y2:.4f}y[n-2] + '
    f'{coef_u0:.4f}u[n] + {coef_u1:.4f}u[n-1]'
)

plt.text(
    0.015, 0.96, texto_mmq_treino,
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8)
)

plt.xlabel("Tempo")
plt.ylabel("Saída")
plt.title("MMQ - Treinamento")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

print("coef_y1 =", coef_y1)
print("coef_y2 =", coef_y2)
print("coef_u0 =", coef_u0)
print("coef_u1 =", coef_u1)

reta_ajuste = np.poly1d(np.polyfit(saida_treino, saida_estimada_treino, 1))
eixo_reta = np.linspace(-3, 3, 500)

emq_treino = np.mean((saida_treino - saida_estimada_treino) ** 2)
print(f"EMQ de Treinamento: {emq_treino:.6f}")

plt.figure(figsize=(14, 4))
plt.suptitle("Erro de treinamento", fontsize=18, y=0.95)
plt.plot(saida_treino, saida_estimada_treino, 'o', label='amostras')
plt.plot(eixo_reta, reta_ajuste(eixo_reta), 'g-', label='reta de ajuste')
plt.text(2.5, 2.7, 'EMQ = %.4f' % emq_treino)
plt.grid(True)
plt.legend()
plt.show()