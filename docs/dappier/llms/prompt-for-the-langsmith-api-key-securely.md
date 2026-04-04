# Prompt for the LangSmith API key securely
langsmith_api_key = getpass('Enter your API key: ')
os.environ["LANGSMITH_API_KEY"] = langsmith_api_key
os.environ["LANGSMITH_TRACING"] = "true"
```

## 🛰️ Access Real Time Data with Dappier Tool

The DappierRealTimeSearchTool is a powerful tool designed to empower AI applications with real-time, up-to-date information across diverse domains such as news, weather, travel, and financial markets. By integrating seamlessly with LangChain, it enables developers to retrieve and process real-time data efficiently. Key features include access to the latest news, weather updates, travel deals, financial news, stock prices, and AI-enhanced insights for accurate and fast information retrieval. With its easy-to-use API and customizable parameters, the tool is ideal for building dynamic, data-driven applications that require real-time intelligence.

In this section, we will search for the latest news related to Langchain as an example. Explore a wide range of data models in our marketplace at [marketplace.dappier.com](https://marketplace.dappier.com). For list of all parameters supported for Dappier retriever visit [Dappier docs](https://docs.dappier.com/integrations/langchain-integration#parameters-3).

```python Python theme={null}
from langchain_dappier import DappierRealTimeSearchTool

tool = DappierRealTimeSearchTool()

response = tool.invoke({"query": "Latest news on Langchain AI"})

print(response)
```

```json  theme={null}
Here’s the latest on Langchain AI:

1. **Interrupt Conference**: LangChain is hosting the "Interrupt: The AI Agent Conference"! 🎉 It's a great opportunity to dive deep into AI agents and their applications.

2. **New Evals Framework**: They’ve introduced a new way to run evaluations using LangSmith's Pytest and Vitest/Jest, making it easier for developers to assess performance. 🧪

3. **Funding Success**: LangChain recently secured $25 million in funding to enhance their platform, focusing on supporting the full lifecycle of Large Language Models (LLMs). 🚀

4. **Growing Adoption of AI Agents**: A recent report revealed that 78% of companies plan to implement AI agents soon, with 51% already using them in production. Mid-sized companies are leading the charge at 63%. 📈

5. **Hugging Face Collaboration**: There’s a new partnership with Hugging Face, allowing users to run thousands of AI models locally for free! 🤖

Exciting developments ahead for LangChain!
```

🎉 **Dappier effortlessly retrieves the latest on Langchain AI, providing valuable data for AI integration!**

## 📈💰 Real-Time Market Insights & Trading Strategies

*This section sets up an automated workflow where LangChain and the DappierRealTimeSearchTool collaborate to generate real-time market insights and trading strategies. We will guide the system in retrieving real-time financial news and stock trends, leveraging OpenAI models to analyze data and craft dynamic, actionable trading recommendations.*

```python Python theme={null}
from langchain.chat_models import init_chat_model
from langchain_dappier import DappierRealTimeSearchTool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
import json
```

Define the task prompt

```python Python theme={null}
TASK_PROMPT = """
Generate a Stock Trading Strategy for the US Market, Tailored to Real-Time
Financial News and Stock Trends. Follow These Steps:

Fetch Current Financial News:
Retrieve the latest financial news in the US using Dappier real-time search to
identify market-moving events, economic updates, or sector-specific
developments.

Fetch Stock Trends:
Retrieve the latest stock market trends in the US using Dappier real-time
search to analyze price movements, volume changes, and sector performance.

Select Top 5 Stocks:
Based on the financial news and stock trends, pick the top 5 stocks that show
strong potential for growth or stability. Include an analysis of why these
stocks were chosen.

Design a Trading Strategy:
Create a dynamic trading strategy tailored to the selected stocks.
Include details such as:

Entry and exit points

Risk management techniques (e.g., stop-loss levels)

Time horizon (short-term, medium-term, or long-term)

Sector diversification (if applicable)

How current financial news and trends influence the strategy.

Final Response:
The final response should include:

A summary of the latest financial news and stock trends.

The top 5 selected stocks with analysis.

A detailed trading strategy with actionable steps.
"""
```

Here we set up our language model and the Dappier real-time search tool. For list of all parameters supported for Dappier retriever visit [Dappier docs](https://docs.dappier.com/integrations/langchain-integration#parameters-3). Explore a wide range of data models in our marketplace at [marketplace.dappier.com](https://marketplace.dappier.com).

```python Python theme={null}