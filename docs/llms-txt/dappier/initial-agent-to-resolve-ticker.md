# --- Initial Agent to Resolve Ticker ---
ticker_resolution_agent = LlmAgent(
    name="TickerResolutionAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, take a user-provided company name and use real-time web search to resolve its stock ticker symbol.
Return only the stock ticker symbol in uppercase.
""",
    description="Resolves stock ticker symbol from company name.",
    tools=[real_time_web_search],
    output_key="ticker_symbol"
)
```

> 🎯 This agent ensures the entire pipeline starts with an accurate stock symbol, derived from the latest web data.
> Dappier is used here to ensure up-to-date resolution, especially for lesser-known or recently listed companies.

Perfect — we'll now begin documenting the **individual agents**, one at a time, starting with the **Ticker Resolution Agent**.

## 🏷️ Ticker Resolution Agent

The first step in the stock research pipeline is to resolve the stock ticker symbol from a user-provided company name. This ensures downstream agents receive a valid ticker for accurate data retrieval.

We define a lightweight LLM agent using Google ADK's `LlmAgent`, powered by Gemini, and backed by **Dappier's real-time web search tool**.

```python  theme={null}
from google.adk.agents import LlmAgent
from datetime import datetime
from .tools import real_time_web_search

GEMINI_MODEL = "gemini-2.0-flash"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")