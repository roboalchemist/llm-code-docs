# 🛠️ Dynamic Travel Planner with OpenAI Function Calling + Real-Time Insights via Dappier
Source: https://docs.dappier.com/cookbook/recipes/open-ai-function-calling-travel-assistant



You can also check this cookbook in Colab [here](https://colab.research.google.com/drive/1N9UBTgc3rhBi0y7GqhBxt6DM7izfpEaf?usp=sharing)

This notebook demonstrates how to set up and leverage OpenAI Function Calling combined with Dappier for dynamic travel planning. By integrating real-time data and automated function execution, this notebook walks you through a practical approach to creating adaptive travel plans.

In this notebook, you'll explore:

* **OpenAI Function Calling**: A powerful feature that enables large language models to automatically detect and invoke external tools to accomplish tasks in a structured and contextual manner.
* **Dappier**: A platform connecting LLMs to real-time, rights-cleared data from trusted sources, specializing in domains like web search, weather, and commerce. It delivers enriched, prompt-ready data, empowering AI with verified and up-to-date information for diverse applications.
* **Dynamic Travel Planning**: A real-world use case where the assistant reasons over live data to generate a customized 2-day itinerary for New York City based on the latest news, weather, and hotel deals.

This setup not only demonstrates a flexible architecture for building intelligent assistants but also serves as a foundation for developing other real-world applications requiring real-time information retrieval, structured tool use, and contextual decision-making.

## 📺 Video Walkthrough

Prefer watching? Here’s a video version of this notebook:

<iframe width="560" height="315" src="https://www.youtube.com/embed/XHfsooz3Dlk?si=HaOwBBBBR294E4FJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

***

## 📦 Installation

Install the required packages:

```bash  theme={null}
!pip install openai dappier
```

***

## 🔑 Setting Up API Keys

You'll need to set up your API keys for OpenAI, Dappier.
This ensures that the tools can interact with external services securely.

You can go to [here](https://platform.dappier.com/profile/api-keys) to get API Key from Dappier with **free** credits.

```python Python theme={null}
import os
from getpass import getpass