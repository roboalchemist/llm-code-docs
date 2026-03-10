# 🧠 Google ADK Dynamic Travel Planner: Real-Time Itineraries with Dappier
Source: https://docs.dappier.com/cookbook/recipes/google-adk-dynamic-travel-planner



You can explore this project live on Replit [here](https://replit.com/@dappier/Dynamic-Travel-Planner-or-Google-ADK-and-Dappier)

This Replit app demonstrates how to build a powerful travel planning agent using **Google ADK** and **Dappier**. By combining multi-agent workflows and real-time location-based data, this project showcases a novel approach to generating personalized, markdown-formatted itineraries for any city and date.

In this app, you'll explore:

* **Google ADK (Agent Development Kit)**: A flexible framework by Google to build intelligent, multi-step agents capable of reasoning, decision-making, and orchestration using Gemini models.
* **Dappier**: A real-time data platform that connects LLMs to live, rights-cleared information across domains like local attractions, dining, events, and web search. It enriches agent workflows with structured, prompt-ready data.
* **Gemini-Powered Agents**: Modular LLM agents designed to generate multi-day travel plans based on user preferences, travel dates, and real-time search.
* **Replit Deployment**: Run the complete multi-agent itinerary generation pipeline in the browser using Replit, with secure environment variable support and real-time agent execution.

This app not only delivers a practical solution for dynamic travel planning but also serves as a reusable foundation for any location-aware assistant powered by AI and live data.

## 📦 Installation

This app is built using [Replit](https://replit.com/), so you don't need to set up any local environment. Just fork or run the app directly in your browser.

However, if you're setting this up manually or adapting it outside Replit, install the required packages using `pip`:

```bash  theme={null}
pip install google-adk dappier
```

> ✅ **Note**: Replit automatically installs the packages listed in `replit.nix` or `pyproject.toml` (if used). You can also manually add packages from the **Packages** tab in the left sidebar.

## 🔑 Setting Up API Keys

To run the dynamic travel planner agent, you'll need the following API keys:

* `GOOGLE_API_KEY` – For accessing Gemini models via Google ADK.
* `GOOGLE_GENAI_USE_VERTEXAI` – Set this to `"false"` to use Gemini on public API instead of Vertex AI.
* `DAPPIER_API_KEY` – To access real-time travel and web data from Dappier.

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

Dappier provides real-time, rights-cleared data that powers different stages of the itinerary generation workflow. In this app, we use a single tool function:

1. **Real-Time Travel Planner Tool** — For generating structured itineraries based on location, date, number of days, and user interests.

This tool is defined in the `tools.py` file and initialized using the Dappier Python SDK.

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
```

> 🧠 This tool powers the core agent that dynamically generates the travel itinerary using structured, real-time data from Dappier’s travel content sources.
> All data is fresh, localized, and sourced from rights-cleared platforms to ensure safety and compliance.

## 🧾 Input Resolution Agent

Extracts destination, start date, and number of travel days from user input. If any field is missing, it prompts the user to provide the missing information.

```python  theme={null}
from google.adk.agents import LlmAgent
from datetime import datetime

GEMINI_MODEL = "gemini-2.0-flash"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")