# Projeto MLOps – Previsão de Preço de Diamantes

Este repositório faz parte da disciplina **MLOps – Running ML in Production Environments**.

O objetivo do projeto é mostrar, passo a passo, como evoluir de um fluxo manual em notebooks para um projeto de Machine Learning organizado, reprodutível e pronto para automação, seguindo boas práticas de MLOps.

---

## Contexto até aqui

Na **Aula 1**, trabalhamos com um fluxo típico de ciência de dados:

- EDA em notebook  
- Treino e inferência manual  
- Uso inicial do MLflow para registrar experimentos  

Esse fluxo funciona, mas não escala e não é fácil de repetir.

Na **Aula 2**, o foco foi **organizar o projeto e estruturar o ciclo de dados**, preparando o terreno para automação e evolução do pipeline nas próximas aulas.

---

## O que foi feito na Aula 2

Nesta etapa, o projeto passou por uma reorganização importante:

- Criação de um repositório GitHub  
- Estruturação do projeto em pastas claras  
- Separação da lógica de dados em um módulo Python  
- Criação de um ponto único para carregar e dividir os dados  
- Integração do notebook com o código do projeto  

O notebook deixou de ser responsável por toda a lógica de dados e passou a **consumir funções reutilizáveis**.

---

## Estrutura atual do projeto

```text
impacta_mlops/
│
├── notebooks/
│   └── eda_diamonds.ipynb
│
├── src/
│   └── data.py
│
├── app/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Módulo de dados

O arquivo `src/data.py` centraliza a lógica relacionada aos dados:

- carregamento do dataset `diamonds` do seaborn  
- separação de features e target  
- divisão em treino e teste  

Isso garante que todos usem **o mesmo processo de preparação**, evitando inconsistências entre notebooks e scripts.

---

## Uso no notebook

O notebook agora utiliza diretamente o módulo de dados:

```python
from src.data import train_test_split_diamonds

X_train, X_test, y_train, y_test = train_test_split_diamonds()
```

Com isso:

- a lógica de dados fica centralizada  
- o notebook fica mais simples  
- o código se torna reutilizável  
- o projeto começa a ganhar reprodutibilidade  

---

## Ambiente de desenvolvimento

Recomenda-se o uso de ambiente virtual.

Criar e ativar o ambiente:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---
