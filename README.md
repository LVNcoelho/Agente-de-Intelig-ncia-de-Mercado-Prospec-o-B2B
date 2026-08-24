# 🔍 LeadScout AI — Agente de Inteligência de Mercado & Prospecção B2B

> **Automação híbrida com Selenium e Gemini 2.5 Flash para varredura de oportunidades na web, redes sociais e diagnóstico de vendas em tempo real.**

O **LeadScout AI** é uma solução de inteligência comercial criada para acelerar a prospecção B2B de PMEs e novos empreendimentos. O sistema realiza varreduras automatizadas no Google — rastreando desde páginas oficiais até perfis no **Instagram, Facebook e portais regionais** —, utilizando o **Gemini 2.5 Flash** para analisar os dados e gerar relatórios completos com **diagnóstico de oportunidade digital**.

---

## 📑 Índice

* [💡 Estratégia & Valor de Negócio](#-estratégia--valor-de-negócio)
* [🛠️ Tech Stack & Escolhas Arquiteturais](#-tech-stack--escolhas-arquiteturais)
* [🔄 Fluxo de Funcionamento](#-fluxo-de-funcionamento)

---

## 💡 Estratégia & Valor de Negócio

* **Mapeamento Multicanais (Web & Social Media):** O algoritmo de captura identifica pegadas digitais em variados canais (notícias, Instagram, Facebook, diretórios locais), mapeando onde o lead está ativo.
* **Análise Contextual de Leads:** Em vez de apenas extrair nomes e telefones, a IA analisa a presença digital capturada e gera um diagnóstico customizado, indicando exatamente a dor do cliente e por que ele precisa de automação ou serviços digitais.
* **Eficiência no Funil de Vendas:** Reduz drasticamente as horas gastas por consultores e SDRs na fase manual de pesquisa e qualificação de mercado.
* **Alta Adaptabilidade:** Permite ajustar os alvos de busca para qualquer nicho de mercado (clínicas, lojas, restaurantes, eventos) e região geográfica em poucos segundos.

---

## 🛠️ Tech Stack & Escolhas Arquiteturais

| Tecnologia | Função | Motivo da Escolha Estratégica |
| :--- | :--- | :--- |
| **Python 3** | Linguagem Core | Ecossistema robusto e flexível para automação web e integração com APIs de Inteligência Artificial. |
| **Selenium WebDriver** | Scraping & Coleta | Execução em navegador automatizado para raspagem resiliente de dados em tempo real no Google e redes sociais. |
| **Google Gemini 2.5 Flash** | Inteligência Analytic | Modelo multimodal de resposta rápida que atua como analista de mercado, interpretando dados brutos e gerando saídas estruturadas. |
| **Google GenAI SDK** | Comunicação com IA | SDK oficial para comunicação direta, performática e segura com os modelos Gemini. |

---

## 🔄 Fluxo de Funcionamento

```text
[ Configuração de Nicho/Região ] ──► [ Robô Selenium (Google & Redes Sociais) ]
                                                       │
                                              (Links & Dados Brutos)
                                                       │
                                                       ▼
[ Relatório de Oportunidades ] ◄──── [ Gemini 2.5 Flash (Analista B2B) ]
