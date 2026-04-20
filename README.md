# 📊 Modelagem de Sistemas com MMQ e RBF

Projeto desenvolvido para a Unidade 2 da disciplina **ECT-33401 - Computação Numérica (UFRN)**.

O objetivo é modelar um sistema dinâmico a partir de dados experimentais utilizando dois métodos:

* 📐 Mínimos Quadrados (MMQ)
* 🧠 Redes de Base Radial (RBF)

---

## 🚀 Funcionalidades

* ✔ Leitura de dados experimentais
* ✔ Modelagem com MMQ (linear)
* ✔ Modelagem com RBF (não linear)
* ✔ Avaliação com erro quadrático médio (EMQ)
* ✔ Comparação entre modelo real e estimado
* ✔ Validação com entrada degrau

---

## 🧠 Metodologia

### 🔹 1. MMQ (Mínimos Quadrados)

Modelo linear baseado em regressão:

$$
y[n] = a_1 y[n-1] + a_2 y[n-2] + b_1 u[n] + b_2 u[n-1]
$$

* Ajuste via sistema normal
* Avaliação por EMQ
* Aplicação em treino e teste

---

### 🔹 2. RBF (Radial Basis Function)

Modelo não linear utilizando funções gaussianas:

$$
\phi(x) = e^{-\frac{(x - c)^2}{2\sigma^2}}
$$

* Definição de centros
* Construção da matriz de ativação
* Ajuste dos pesos via pseudo-inversa

---

## 📂 Estrutura do Projeto

```
📁 identificacao-sistemas-mmq-rbf
 ├── dados_01.dat
 ├── dados_02.dat
 ├── graficos_treino_teste.py
 ├── treinamento_mmq.py
 ├── treinamento_rbf.py
 ├── teste_mmq.py
 ├── teste_rbf.py
 ├── resposta_degrau.py
 └── README.md
```

---

## ▶️ Como executar

### ⚠️ Importante

O projeto está dividido em vários arquivos.
Para executar corretamente, é necessário **unir todos os códigos em um único arquivo**, seguindo a ordem:

1. `graficos_treino_teste.py`
2. `treinamento_mmq.py`
3. `treinamento_rbf.py`
4. `teste_mmq.py`
5. `teste_rbf.py`
6. `resposta_degrau.py`

📌 Após juntar, salve como:

```bash
main.py
```

---

### 1. Clone o repositório

```bash
git clone https://github.com/Douglas-Amon/identificacao-sistemas-mmq-rbf.git
cd identificacao-sistemas-mmq-rbf
```

---

### 2. Verifique os arquivos de dados

Os arquivos devem estar na mesma pasta:

```
dados_01.dat
dados_02.dat
```

---

### 3. Execute o código

```bash
python main.py
```

---

## 📊 Resultados

* O MMQ apresentou bom desempenho para comportamento linear
* A RBF apresentou melhor adaptação a não linearidades
* A validação com degrau mostrou maior robustez da RBF

---

## 📌 Tecnologias utilizadas

* Python 3
* NumPy
* Matplotlib
* SciPy

---

## 👨‍💻 Autor

Douglas Amon
Universidade Federal do Rio Grande do Norte (UFRN)

---

## ⭐ Possíveis melhorias

* Ajuste automático de σ (sigma)
* Otimização do número de centros
* Interface gráfica
* Comparação com outros métodos (ex: redes neurais)

---
