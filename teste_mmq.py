coef_teste_y1 = -0.0097
coef_teste_y2 = 0.0018
coef_teste_u0 = 0.0037
coef_teste_u1 = 0.6000

saida_teste_expandida = np.concatenate(([0.0, 0.0], saida_teste))
entrada_teste_expandida = np.concatenate(([0.0], entrada_teste))

quant_amostras_teste = len(saida_teste)
saida_estimada_teste = np.zeros_like(saida_teste)

for k in range(quant_amostras_teste):
    saida_estimada_teste[k] = (
        coef_teste_y1 * saida_teste_expandida[k + 1]
        + coef_teste_y2 * saida_teste_expandida[k]
        + coef_teste_u0 * entrada_teste_expandida[k + 1]
        + coef_teste_u1 * entrada_teste_expandida[k]
    )

emq_teste_mmq = np.mean((saida_teste - saida_estimada_teste) ** 2)
print(f"EMQ de Teste: {emq_teste_mmq:.6f}")

plt.figure(figsize=(16, 6))
plt.plot(tempo_teste, saida_teste, "o", label="dados de teste", alpha=0.6)
plt.plot(tempo_teste, saida_estimada_teste, label="ajuste MMQ", linewidth=2)
plt.text(0.95 * max(tempo_teste), 0.85 * max(saida_teste), f'EMQ = {emq_teste_mmq:.4f}')

texto_mmq_teste = (
    'Ajuste: ' +
    r'$y[n] = -0.0097\,y[n-1] + 0.0018\,y[n-2] + 0.0037\,u[n] + 0.6000\,u[n-1]$'
)

plt.text(
    0.015, 0.96, texto_mmq_teste,
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8)
)

plt.xlabel("Tempo")
plt.ylabel("Saída")
plt.title("MMQ - Teste")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()