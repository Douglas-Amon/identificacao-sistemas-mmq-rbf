# Teste da RBF
matriz_rbf_teste = np.zeros((len(x2), len(centros_rbf)))

for i in range(matriz_rbf_teste.shape[0]):
    for j in range(matriz_rbf_teste.shape[1]):
        matriz_rbf_teste[i, j] = np.exp(
            -(1 / (2 * sigma_rbf**2)) * (abs(x2[i] - centros_rbf[j])**2)
        )

saida_rbf_teste = matriz_rbf_teste @ pesos_rbf

# Ajustando tamanhos para evitar erro de índice
tamanho_minimo = min(len(tempo_teste), len(saida_teste), len(saida_rbf_teste))

tempo_teste_ajustado = tempo_teste[:tamanho_minimo]
saida_teste_ajustada = saida_teste[:tamanho_minimo]
saida_rbf_teste_ajustada = saida_rbf_teste[:tamanho_minimo]

emq_rbf_teste = np.mean((saida_teste_ajustada - saida_rbf_teste_ajustada) ** 2)
print(emq_rbf_teste)

texto_rbf = (
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
plt.plot(tempo_teste_ajustado, saida_teste_ajustada, 'o', label='y(t) teste')
plt.plot(tempo_teste_ajustado, saida_rbf_teste_ajustada, label='y estimado RBF')

plt.text(
    0.01, 0.95, texto_rbf,
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(boxstyle="round,pad=0.5", facecolor='linen', alpha=0.9)
)

plt.xlabel('Tempo')
plt.ylabel('Saída')
plt.title('RBF - Teste')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()