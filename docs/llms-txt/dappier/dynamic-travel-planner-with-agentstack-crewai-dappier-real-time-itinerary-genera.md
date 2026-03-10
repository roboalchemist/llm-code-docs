# 🖇️ Dynamic Travel Planner with AgentStack, CrewAI & Dappier: Real-Time Itinerary Generation Using Multi-Agent AI
Source: https://docs.dappier.com/cookbook/recipes/agentstack-dynamic-travel-planner



This developer-focused cookbook demonstrates how to build and run a local multi-agent itinerary planner using **AgentStack**, **CrewAI**, and **Dappier**, powered by **OpenAI** and monitored via **AgentOps**. The setup guides you through generating structured travel itineraries based on real-time weather, live events, and hotel deals for a given city and date.

In this tutorial, you'll explore:

* **AgentStack**: A CLI-first framework for rapidly scaffolding AI agent workflows, generating agents, tasks, and tools with seamless CrewAI integration.
* **CrewAI**: A lightweight multi-agent orchestration engine, perfect for managing sequential or collaborative task execution between agents.
* **Dappier**: A platform that connects LLMs to real-time, rights-cleared data from trusted sources, specializing in domains like web search, finance, and travel. It delivers enriched, prompt-ready data, empowering AI with verified and up-to-date information for diverse applications.
* **OpenAI**: A leading provider of advanced AI models capable of natural language understanding, contextual reasoning, and content generation. It enables intelligent, human-like interactions and supports a wide range of applications across various domains.
* **AgentOps**: Track and analyze the running of CrewAI agents with full visibility into cost, token usage, execution traces, and replays.

This setup not only demonstrates a practical application of AI-driven travel planning but also provides a flexible framework that can be adapted to other real-world scenarios requiring real-time data integration from Dappier, multi-agent collaboration, and contextual reasoning.

## 📦 Project Initialization and Setup

To get started, we'll use the `agentstack` CLI to scaffold a fully functional multi-agent project. This command generates the base project structure, config files, virtual environment, and a ready-to-customize `crew.py` file with support for tools like Dappier and frameworks like CrewAI.

### Step 1: Initialize the Project

Run the following command in your terminal:

```bash  theme={null}
agentstack init dynamic_travel_planner
```

This will generate a folder named `dynamic_travel_planner` with the complete project structure.

### Step 2: Move Into the Project

```bash  theme={null}
cd dynamic_travel_planner
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