# Entry point
root_agent = sequential_pipeline_agent
```

## 💻 Running the Agent

This app is fully interactive — you don’t need to write any code to run it.

Just open the Replit app and use the built-in **chat interface** to enter a company name (e.g., `"Apple"` or `"Tesla"`). The agent pipeline will:

1. Resolve the stock ticker.
2. Fetch real-time data and financial insights.
3. Generate a full investment report in markdown format.

> 💬 The chat interface will display the markdown report directly in the console or browser output pane.

## 🌟 Highlights

This app has guided you through building and running a stock market research agent using Google ADK and Dappier. By combining real-time financial data, multi-agent workflows, and markdown generation, you’ve created a complete pipeline that transforms natural language input into a structured investment report.

Key tools utilized in this app include:

* **Google ADK**: A flexible framework that enables sequential and parallel agent orchestration, built around modular LLM-based agents for complex task automation.
* **Dappier**: A platform connecting LLMs to real-time, rights-cleared data across domains like finance, news, and web search. It delivers enriched, prompt-ready insights, empowering agents with verified and up-to-date information.
* **Gemini Models**: LLMs used to reason over financial data, extract metrics, benchmark competitors, and synthesize final markdown content.
* **Replit**: An interactive development and execution environment that makes it easy to deploy, test, and interact with the pipeline via chat interface.

This app can be adapted and expanded to support various other financial workflows such as:

* Portfolio monitoring
* Real-time earnings tracking
* Sector-specific investment dashboards
* Automated newsletter generation

It serves as a practical template for integrating LLMs and live data APIs into real-world financial research tools.