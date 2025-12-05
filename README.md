# Trabalho Final - Recuperação da Informação (2025/2)

Este repositório contém a análise comparativa entre dados reais de mercado (State of Data Brazil) e vagas coletadas via Web Scraping.

## 📂 Estrutura do Projeto
- `src/coleta`: Scripts utilizados para baixar dados do Kaggle e raspar vagas do Python.org.
- `src/limpeza`: Scripts de tratamento e padronização dos textos.
- `data/`: Contém os datasets brutos (raw) e processados.
- `docs/`: Relatório final em PDF gerado a partir da análise.
- `notebooks/`: Jupyter Notebook com o código do Modelo de Recuperação (TF-IDF) e visualizações.

## 🚀 Como Executar
1. O projeto requer as bibliotecas listadas (pandas, sklearn, matplotlib, seaborn).
2. Para visualizar a análise completa, acesse o arquivo `Relatorio_Final.pdf` na pasta `docs` (ou `data/raw`).
3. O código fonte principal está no notebook `notebooks/Relatorio_Final.ipynb`.

## 📊 Resumo
Foi aplicado um modelo vetorial (TF-IDF) para recuperar vagas relevantes baseadas em termos de busca, comparando o perfil das vagas com o perfil dos profissionais do Data Hackers.
