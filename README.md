# identificacao-sistemas-mmq-rbf

# 📊 Modelagem de Sistemas com MMQ e RBF

Projeto desenvolvido para a Unidade 2 da disciplina **ECT-33401 - Computação Numérica (UFRN)**.

O objetivo é modelar um sistema dinâmico a partir de dados experimentais utilizando dois métodos:

* 📐 Mínimos Quadrados (MMQ)
* 🧠 Redes de Base Radial (RBF)

---

## 🚀 Funcionalidades

✔ Leitura de dados experimentais
✔ Modelagem com MMQ (linear)
✔ Modelagem com RBF (não linear)
✔ Avaliação com erro quadrático médio (EMQ)
✔ Comparação entre modelo real e estimado
✔ Validação com entrada degrau

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

```id="5k4l7g"
📁 projeto
 ├── dados_01.dat   # dados de treino
 ├── dados_02.dat   # dados de teste
 ├── main.py        # código principal
 └── README.md
```

---

## ▶️ Como executar

1. Clone o repositório:

```id="b7c1z0"
git clone https://github.com/seu-usuario/modelagem-sistemas-mmq-rbf.git
```

2. Baixe os arquivos de dados

Baixe os arquivos fornecidos pelo professor:

dados_01.dat
dados_02.dat

E coloque ambos na mesma pasta do código (main.py).

📌 Exemplo de estrutura correta:

📁 identificacao-sistemas-mmq-rbf
 ├── dados_01.dat
 ├── dados_02.dat
 ├── main.py
 └── README.md

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

Douglas Amon-
Universidade Federal do Rio Grande do Norte (UFRN)

---

## ⭐ Possíveis melhorias

* Ajuste automático de σ (sigma)
* Otimização do número de centros
* Interface gráfica
* Comparação com outros métodos (ex: redes neurais)

---
