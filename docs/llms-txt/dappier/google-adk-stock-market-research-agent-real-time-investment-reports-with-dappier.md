# 🧠 Google ADK Stock Market Research Agent: Real-Time Investment Reports with Dappier
Source: https://docs.dappier.com/cookbook/recipes/google-adk-stock-market-researcher



You can explore this project live on Replit [here](https://replit.com/@dappier/Multi-Agent-Stock-Market-Research-or-Google-ADK-and-Dappier)

This Replit app demonstrates how to build a powerful stock market research agent using **Google ADK** and **Dappier**. By combining multi-agent workflows and real-time financial data, this project showcases a novel approach to generating investment-grade markdown reports for any public company.

In this app, you'll explore:

* **Google ADK (Agent Development Kit)**: A flexible framework by Google to build intelligent, multi-step agents capable of reasoning, decision-making, and orchestration using Gemini models.
* **Dappier**: A real-time data platform that connects LLMs to live, rights-cleared information across domains like finance, news, and web search. It enriches agent workflows with structured, prompt-ready data.
* **Gemini-Powered Agents**: Modular LLM agents designed to resolve ticker symbols, extract stock metrics, analyze peer companies, and generate comprehensive investment summaries.
* **Replit Deployment**: Run the complete multi-agent research pipeline in the browser using Replit, with secure environment variable support and real-time agent execution.

This app not only delivers a practical solution for real-time stock research but also serves as a reusable foundation for any financial analytics tool powered by AI and live data.

## 🚀 Live Demo

You can explore and test the full stock market research pipeline directly in your browser.

* 🔗 **Live Deployment**: [multi-agent-stock-market-research-or-google-adk-and-dap-dappier.replit.app](https://multi-agent-stock-market-research-or-google-adk-and-dap-dappier.replit.app)
  Run the full multi-agent workflow and get real-time investment reports by entering a company name.

* 🛠️ **Source Code**: [Replit Project](https://replit.com/@dappier/Multi-Agent-Stock-Market-Research-or-Google-ADK-and-Dappier)
  Fork the code, explore agent definitions, customize tool integrations, or extend the pipeline for your own use cases.

> 💡 You don’t need to install anything locally. Just open the link, input a company name (e.g., `"Apple"`), and receive a full markdown-formatted investment report — powered by Gemini models and Dappier’s real-time financial data.

## 📦 Installation

This app is built using [Replit](https://replit.com/), so you don't need to set up any local environment. Just fork or run the app directly in your browser.

However, if you're setting this up manually or adapting it outside Replit, install the required packages using `pip`:

```bash  theme={null}
pip install google-adk dappier
```

> ✅ **Note**: Replit automatically installs the packages listed in `replit.nix` or `pyproject.toml` (if used). You can also manually add packages from the **Packages** tab in the left sidebar.

Once dependencies are installed, you're ready to configure your API keys and begin running the agent workflow.

## 🔑 Setting Up API Keys

To run the stock market research agent, you'll need the following API keys:

* `GOOGLE_API_KEY` – For accessing Gemini models via Google ADK.
* `GOOGLE_GENAI_USE_VERTEXAI` – Set this to `"false"` to use Gemini on public API instead of Vertex AI.
* `DAPPIER_API_KEY` – To access real-time financial and web data from Dappier.

### 🔐 In Replit

1. Click the **🔒 Secrets** tab (lock icon) in the left sidebar.
2. Add the following environment variables:

| Key                         | Value                    |
| --------------------------- | ------------------------ |
| `GOOGLE_API_KEY`            | *(Your Google API Key)*  |
| `GOOGLE_GENAI_USE_VERTEXAI` | `false`                  |
| `DAPPIER_API_KEY`           | *(Your Dappier API Key)* |

You can get your API keys from the following sources:

* **Google API Key**: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
* **Dappier API Key**: [https://platform.dappier.com/profile/api-keys](https://platform.dappier.com/profile/api-keys)

> ⚠️ **Important**: Do not print your API keys or commit them to public repositories. Use environment variables or secret managers to handle credentials securely.

## 🔌 Real-Time Tools Powered by Dappier

Dappier provides real-time, rights-cleared data that powers different stages of the stock research workflow. In this app, we use two key tool functions:

1. **Web Search Tool** — For general queries like company overview, financial trends, and peer benchmarking.
2. **Stock Market Tool** — For structured stock market data such as price snapshots, ratios, volumes, and categorized news.

These are defined in the `tools.py` file and initialized using the Dappier Python SDK.

```python  theme={null}
from dappier import Dappier

client = Dappier()

def real_time_web_search(query: str) -> str:
    """
    Perform a real-time web search. Use this for general queries that do not include a specific stock ticker.
    """
    try:
        return client.search_real_time_data_string(
            query=query,
            ai_model_id="am_01j06ytn18ejftedz6dyhz2b15"
        )
    except Exception as e:
        return f"Error: {str(e)}"

def stock_market_data_search(query: str) -> str:
    """
    Fetch real-time stock market data. Use this tool only when querying with a stock ticker symbol.
    """
    try:
        return client.search_real_time_data_string(
            query=query,
            ai_model_id="am_01j749h8pbf7ns8r1bq9s2evrh"
        )
    except Exception as e:
        return f"Error: {str(e)}"
```

> 🧠 These tools power the agents in different stages of the pipeline based on the query type — general vs. ticker-specific.
> All data comes from Dappier’s trusted and rights-cleared data sources, ensuring accuracy and compliance.

## 🏷️ Ticker Resolution Agent

The first step in the stock research pipeline is to resolve the stock ticker symbol from a user-provided company name. This ensures downstream agents receive a valid ticker for accurate data retrieval.

We define a lightweight LLM agent using Google ADK's `LlmAgent`, powered by Gemini, and backed by **Dappier's real-time web search tool**.

```python  theme={null}
from google.adk.agents import LlmAgent
from datetime import datetime
from .tools import real_time_web_search

GEMINI_MODEL = "gemini-2.0-flash"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")