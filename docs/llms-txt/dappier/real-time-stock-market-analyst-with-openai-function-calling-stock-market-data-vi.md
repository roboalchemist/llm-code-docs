# 🛠️ Real-Time Stock Market Analyst with OpenAI Function Calling + Stock Market Data via Dappier
Source: https://docs.dappier.com/cookbook/recipes/open-ai-function-calling-stock-analyst



You can also check this cookbook in Colab [here](https://colab.research.google.com/drive/1DQGn4lKY1ioV3C0cSpvPCkkPlcQGNCf6?usp=sharing).

This notebook demonstrates how to set up and leverage OpenAI Function Calling combined with Dappier for detailed stock market analysis. By integrating real-time trading data and automated function execution, this notebook walks you through a practical approach to generating intelligent, up-to-date investment strategies.

In this notebook, you'll explore:

* **OpenAI Function Calling**: A powerful feature that enables large language models to automatically detect and invoke external tools to accomplish tasks in a structured and contextual manner.
* **Dappier**: A platform connecting LLMs to real-time, rights-cleared data from trusted sources, specializing in domains like finance, web search, and news. It delivers enriched, prompt-ready data, empowering AI with verified and up-to-date information for diverse applications.
* **Stock Market Analysis**: A real-world use case where the assistant reasons over live stock price changes, breaking news, and trade volume in the last 24 hours to deliver a comprehensive financial analysis and investment strategy for a selected company.

This setup not only demonstrates a flexible architecture for building intelligent financial assistants but also serves as a foundation for developing other real-world applications requiring real-time information retrieval, structured tool use, and contextual decision-making.

Here’s the **Video Walkthrough** section, following the same format and tone as the original:

***

## 📺 Video Walkthrough

Prefer watching? Here’s a video version of this notebook:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ry6hOHit__s?si=0m046ETmBnwdFQr2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

***

## 📦 Installation

Install the required packages:

```bash  theme={null}
!pip install openai dappier
```

***

## 🔑 Setting Up API Keys

You'll need to set up your API keys for OpenAI, Dappier.\
This ensures that the tools can interact with external services securely.

You can go to [here](https://platform.dappier.com/profile/api-keys) to get API Key from Dappier with **free** credits.

```python Python theme={null}
import os
from getpass import getpass