# 🖇️ Stock Market Research with AgentStack, CrewAI & Dappier: Real-Time Investment Intelligence using Multi-Agent AI
Source: https://docs.dappier.com/cookbook/recipes/agentstack-stock-market-researcher



This developer-focused cookbook demonstrates how to build and run a local multi-agent investment research system using **AgentStack**, **CrewAI**, and **Dappier**, powered by **OpenAI** and monitored via **AgentOps**. The setup guides you through generating structured investment reports from real-time financial and company data.

In this tutorial, you'll explore:

* **AgentStack**: A CLI-first framework for rapidly scaffolding AI agent workflows, generating agents, tasks, and tools with seamless CrewAI integration.
* **CrewAI**: A lightweight multi-agent orchestration engine, perfect for managing sequential or collaborative task execution between agents.
* **Dappier**: A platform that connects LLMs to real-time, rights-cleared data sources like stock market data, web search, and financial news.
* **OpenAI**: A powerful language model provider, enabling natural language understanding, real-time reasoning, and content generation.
* **AgentOps**: A monitoring tool to track, replay, and analyze agent runs with detailed visibility into agent reasoning and tool use.

This guide walks you through creating a **local, production-grade AI research agent system** to analyze companies like Amazon, generate investment snapshots, and compile markdown-formatted financial reports — all grounded in **real-time market data** from Dappier.

> 🛠️ All tasks and agents in this cookbook are generated using `agentstack` commands and executed in a Python project on your local machine. No notebooks, no server setup required.

## 📦 Project Initialization and Setup

To get started, we'll use the `agentstack` CLI to scaffold a fully functional multi-agent project. This command generates the base project structure, config files, virtual environment, and a ready-to-customize `crew.py` file with support for tools like Dappier and frameworks like CrewAI.

### Step 1: Initialize the Project

Run the following command in your terminal:

```bash  theme={null}
agentstack init stock_market_research
```

This will generate a folder named `stock_market_research` with the complete project structure.

### Step 2: Move Into the Project

```bash  theme={null}
cd stock_market_research
```

### Step 3: Activate the Virtual Environment

Activate the virtual environment created by `agentstack`:

```bash  theme={null}
source .venv/bin/activate
```

If you're using a Windows terminal, use:

```bash  theme={null}
.venv\Scripts\activate
```

> ✅ You now have a fully bootstrapped multi-agent AI project using AgentStack and CrewAI.

## 🔑 Setting Up API Keys

To enable real-time data access and AI reasoning, you’ll need API keys for the following services:

* **OpenAI** – for LLM-powered reasoning and summarization
* **Dappier** – for real-time stock market data and web search
* **AgentOps** – for run monitoring and debugging

These keys are stored in the `.env` file created during project initialization.

### Step 1: Open the `.env` file

Inside your project root, open `.env` and update it with your API keys:

```env  theme={null}