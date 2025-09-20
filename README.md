# 🎯 Projeto 09 — Testes Unitários com LangChain

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&link=https://www.python.org/)](https://www.python.org/) 
[![LangChain](https://img.shields.io/badge/LangChain-Framework-orange)]() 
[![OpenAI](https://img.shields.io/badge/OpenAI-IA-red)]()   [![Pytest](https://img.shields.io/badge/Pytest-Testes-green)]()  

> Nono projeto do **Bootcamp Machine Learning** da [DIO](https://www.dio.me/) em parceria com a **BairesDev**.  
> Aplicação prática de um **agente de geração de testes unitários**, que recebe trechos de código Python e retorna automaticamente **arquivos de teste em Pytest**, utilizando **LangChain + GPT**.

---

## 📌 Sobre o Projeto

Esse projeto consiste em um **gerador automático de testes unitários**, desenvolvido em Python.  
A ideia é fornecer funções/módulos como entrada, e o agente (usando **LangChain** e **OpenAI API**) produz testes no formato **Pytest**.  

**Funcionalidades principais:**

- Receber código Python como entrada (funções ou arquivos).  
- Geração automática de testes unitários em `pytest`.  
- Execução dos testes e exibição dos resultados.  
- Organização modular: prompts, exemplos e testes.  

**Objetivos do projeto:**  

- 🤖 Demonstrar como **LangChain** pode auxiliar no desenvolvimento de software.  
- 🧪 Automatizar a criação de testes unitários.  
- ⚡ Integrar IA generativa ao fluxo de desenvolvimento Python.  

---

## 🛠️ Ferramentas utilizadas

Python 3.12 — Linguagem de implementação do projeto.

LangChain — Framework para construção de agentes e chains que orquestram chamadas a LLMs.

langchain-community — Extensões/integrações comunitárias para LangChain (quando aplicável).

OpenAI API (GPT) — LLM usado para gerar conteúdo dos testes a partir dos prompts.

python-dotenv — Carregamento seguro de variáveis de ambiente (ex.: OPENAI_API_KEY).

Pytest — Framework de testes utilizado para executar e validar os testes gerados.

---

## 📂 Estrutura do Projeto

```text
projeto-09-testes-unitarios-com-langchain
├── agent                   # Código principal do agente LangChain
│   ├── prompts             # Prompts utilizados para gerar os testes
│   │   └── test_prompt.txt
│   ├── __init__.py
│   ├── chains.py           # Definições de chains LangChain
│   └── utils.py            # Funções auxiliares
│
├── examples                # Exemplos de código Python
│   ├── __init__.py
│   └── soma.py             # Exemplo simples para teste
│
├── tests                   # Testes gerados ou escritos manualmente
│   └── test_soma.py
│
├── .env                    # Variáveis de ambiente (API Key da OpenAI)
├── LICENSE                 # Arquivo de licença MIT
├── main.py                 # Arquivo principal do projeto
├── requirements.txt        # Dependências do projeto
├── resultado_testes_soma.txt  # Exemplo de saída dos testes executados
└── README.md               # Este arquivo
```

---

## 📊 Exemplo de Uso
Exemplo de código em examples/soma.py:
```bash
def soma(a, b):
    return a + b
```
O agente gera automaticamente o arquivo tests/test_soma.py:
from examples.soma import soma
```bash
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
```
Execução do pytest (exemplo real no projeto):
```bash
============================= test session starts =============================
platform win32 -- Python 3.12.0, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\GitHub\DIO\Machine Learning - BairesDev\projeto-09-testes-unitarios-com-langchain
plugins: anyio-4.10.0, langsmith-0.4.28
collected 5 items

tests\test_soma.py ...FF                                                 [100%]

================================== FAILURES ===================================
__________________________ test_soma_falha_diferente __________________________

    def test_soma_falha_diferente():
>       assert soma(1, 2) != 3
E       assert 3 != 3
E        +  where 3 = soma(1, 2)

tests\test_soma.py:19: AssertionError
___________________________ test_soma_falha_excecao ___________________________

    def test_soma_falha_excecao():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

tests\test_soma.py:22: Failed
=========================== short test summary info ===========================
FAILED tests/test_soma.py::test_soma_falha_diferente - assert 3 != 3
FAILED tests/test_soma.py::test_soma_falha_excecao - Failed: DID NOT RAISE <c...
========================= 2 failed, 3 passed in 0.12s =========================
```

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/rodrigoulart/projeto-09-testes-unitarios-com-langchain.git

# Acesse a pasta do projeto
cd projeto-09-testes-unitarios-com-langchain

# Instale as dependências
pip install -r requirements.txt

# Configure sua chave da OpenAI no arquivo .env
# Exemplo:
# OPENAI_API_KEY=#SUA_CHAVE_AQUI
```

Rodar o agente:
```bash
python agent.py functions.py
```

Rodar os testes:
```bash
pytest tests/ -v
```

---

## 🧪 Mock de Testes (Opcional)

Se não tiver chave da OpenAI, é possível simular o comportamento:

Substitua o trecho que faz a chamada à API por um mock que retorna um test_*.py de exemplo.

Coloque os arquivos mock em examples/ ou tests/ e execute pytest normalmente.

---

## 📚 Conceitos Aplicados

LangChain → Framework para criar agentes baseados em LLMs.

OpenAI API → Utilizada para geração de testes automatizados.

Pytest → Biblioteca de testes unitários para Python.

Prompt Engineering → Uso de templates para guiar a IA na criação dos testes.

dotenv → Gerenciamento seguro de variáveis de ambiente.

---

## 🏆 Créditos

Desenvolvido por Rodrigo Moraes, como parte dos desafios do Bootcamp de Machine Learning da DIO em parceria com a BairesDev.

📎 Repositório: github.com/rodrigoulart/projeto-09-testes-unitarios-com-langchain
