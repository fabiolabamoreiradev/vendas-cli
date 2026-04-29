# 📊 Vendas CLI

![Python](https://img.shields.io/badge/python-3.12-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Coverage](https://img.shields.io/badge/coverage-80%25+-brightgreen)

CLI em Python para processamento de arquivos CSV de vendas, com geração de relatórios em texto ou JSON.

---

## 🚀 Visão Geral

Este projeto foi desenvolvido com foco em:

- Código limpo e modular  
- Separação de responsabilidades  
- Testabilidade  
- Uso de bibliotecas padrão do Python  
- Cobertura de testes acima de 80%  

A aplicação lê um arquivo CSV contendo dados de vendas e gera relatórios consolidados.

---

## 🏗️ Arquitetura

vendas/
├── parser.py # Leitura e validação do CSV
├── core.py # Regras de negócio
├── output.py # Formatação de saída
└── cli.py # Interface de linha de comando


---

## 📥 Instalação

```bash
py -m pip install .

▶️ Uso
📄 CSV esperado
produto,quantidade,preco_unitario,data_venda
Camiseta,3,49.9,2026-01-10
Calça,2,99.9,2026-02-15
Tênis,1,199.9,2026-03-20

▶️ Executar
vendas-cli vendas.csv
🔄 JSON
vendas-cli vendas.csv --format json
📅 Filtro (opcional)
vendas-cli vendas.csv --start 2025-01-01 --end 2025-03-31
📊 Exemplo de saída
Texto
Relatório de Vendas
------------------------------
Camiseta            R$ 199.60
Calça               R$ 199.80
Tênis               R$ 199.90
------------------------------
TOTAL: R$ 599.30
MAIS VENDIDO: Camiseta
JSON
{
  "total_por_produto": {
    "Camiseta": 199.6
  },
  "total_geral": 199.6,
  "produto_mais_vendido": "Camiseta"
}
🧪 Testes

Executar:

py -m pytest

Cobertura:

py -m pytest --cov=vendas --cov-report=term-missing

Garantir mínimo:

py -m pytest --cov=vendas --cov-fail-under=80
⚠️ Tratamento de erros
Arquivo não encontrado
CSV vazio
Campos obrigatórios ausentes
Dados inválidos
🧠 Decisões Técnicas
Uso de bibliotecas padrão (csv, argparse, logging)
Separação de responsabilidades
Funções puras no core
Validação no parser
🔄 Melhorias futuras
Validação com Pydantic
Processamento em larga escala
API REST / interface web
Persistência em banco
👨‍💻 Autor

Projeto desenvolvido para desafio técnico Python Sênior.