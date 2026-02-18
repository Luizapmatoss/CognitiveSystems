# 🧠 Sistema de Monitoramento Cognitivo

Projeto desenvolvido para coleta e análise de tempos de reação simples, com foco em monitoramento cognitivo e análise estatística comportamental.

---

## 📌 Objetivo

Este sistema tem como finalidade:

- Medir tempo de reação simples
- Armazenar dados em banco SQLite
- Calcular estatísticas descritivas
- Identificar e remover outliers
- Permitir comparação entre participantes reais

O projeto simula um experimento cognitivo básico utilizado em estudos de psicologia e neurociência.

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- SQLite3
- Biblioteca `statistics`
- Git/GitHub para versionamento

---

## 🧪 Como Funciona

1. O sistema coleta dados do participante:
   - Nome ou código
   - Idade
   - Gênero
   - Profissão
   - Variáveis comportamentais (sono, cafeína, exercício, etc.)

2. O experimento executa 20 tentativas de tempo de reação.

3. Cada tentativa:
   - Aguarda intervalo aleatório (entre 2 e 5s)
   - Solicita que o usuário pressione ENTER
   - Mede tempo de reação em milissegundos
   - Salva no banco de dados

4. Ao final da sessão:
   - Outliers são filtrados automaticamente
   - Estatísticas são calculadas:
     - Média
     - Desvio padrão
     - Variância
     - Valor mínimo
     - Valor máximo
     - Quantidade de outliers removidos

---

## 📊 Critério de Filtragem de Outliers

Os seguintes valores são removidos automaticamente:

- Tempos menores que 100 ms (antecipação)
- Tempos maiores que 600 ms (distração)

Este critério segue padrões comuns em estudos de tempo de reação simples.

---


---

## ▶️ Como Executar

1. Clone o repositório:
git clone https://github.com/seuusuario/CognitiveSystems.git

2. Acesse a pasta:
cd CognitiveSystems

3. Execute:
python main.py

---

## 📈 Possíveis Expansões Futuras

- Geração automática de gráficos
- Regressão linear
- Interface gráfica
- Exportação para CSV
- Análise longitudinal por participante

---

## ⚠️ Aviso

Este projeto possui finalidade acadêmica e experimental.
Não possui valor diagnóstico clínico.

---

## 👩‍💻 Autora

Luiza Matos  
Estudante de Ciência da Computação  
Projeto acadêmico de Sistemas Cognitivos
