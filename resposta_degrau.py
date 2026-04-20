quant_pontos_degrau = 100
tempo_degrau = np.arange(quant_pontos_degrau)
entrada_degrau = np.ones(quant_pontos_degrau)
saida_degrau = np.zeros(quant_pontos_degrau)

for k in range(2, quant_pontos_degrau):
    reg_saida_1 = saida_degrau[k - 1]
    reg_saida_2 = saida_degrau[k - 2]
    reg_entrada_0 = entrada_degrau[k]
    reg_entrada_1 = entrada_degrau[k - 1]

    base_rbf_0 = np.exp(-(1 / (2 * sigma_rbf**2)) * (reg_saida_1 - centros_rbf[0])**2)
    base_rbf_1 = np.exp(-(1 / (2 * sigma_rbf**2)) * (reg_saida_2 - centros_rbf[1])**2)
    base_rbf_2 = np.exp(-(1 / (2 * sigma_rbf**2)) * (reg_entrada_0 - centros_rbf[2])**2)
    base_rbf_3 = np.exp(-(1 / (2 * sigma_rbf**2)) * (reg_entrada_1 - centros_rbf[3])**2)

    vetor_bases = np.array([base_rbf_0, base_rbf_1, base_rbf_2, base_rbf_3])
    saida_degrau[k] = vetor_bases @ pesos_rbf

plt.figure(figsize=(14, 6))
plt.plot(tempo_degrau, saida_degrau, "-b", label="resposta ao degrau RBF", linewidth=2)
plt.title("Resposta ao Degrau - RBF")
plt.xlabel("Amostra")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()