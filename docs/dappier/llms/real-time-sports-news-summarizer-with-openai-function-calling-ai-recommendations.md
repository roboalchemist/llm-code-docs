# 🛠️ Real-Time Sports News Summarizer with OpenAI Function Calling + AI Recommendations via Dappier
Source: https://docs.dappier.com/cookbook/recipes/open-ai-function-calling-sports-summarizer



You can also check this cookbook in Colab [here](https://colab.research.google.com/drive/1GAhPgnU8vIjQYVheqohvVAXMMAxjTcWO?usp=sharing).

This notebook demonstrates how to set up and leverage OpenAI Function Calling combined with Dappier's AI Recommendations API for summarizing real-time sports news. By integrating AI-curated content and automated function execution, this notebook walks you through a practical approach to generating concise, up-to-date summaries of trending sports stories.

In this notebook, you'll explore:

* **OpenAI Function Calling**: A powerful feature that enables large language models to automatically detect and invoke external tools to accomplish tasks in a structured and contextual manner.
* **Dappier AI Recommendations**: A capability that provides real-time, AI-powered content recommendations from trusted sources, delivering rich contextual articles based on the latest news and natural language queries.
* **Sports News Summarization**: A real-world use case where the assistant retrieves the latest sports news and generates a human-readable summary for quick consumption.

This setup not only demonstrates a flexible architecture for building intelligent news summarization assistants but also serves as a foundation for developing other real-world applications requiring live content curation, structured tool use, and contextual response generation.

***

## 📺 Video Walkthrough

Prefer watching? Here’s a video version of this notebook:

<iframe width="560" height="315" src="https://www.youtube.com/embed/q9IjtaubWrU?si=H1nDb-FiA9mOiDDW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

***

## 📦 Installation

Install the required packages:

```bash  theme={null}
!pip install openai dappier
```

***

## 🔑 Setting Up API Keys

You'll need to set up your API keys for OpenAI and Dappier.\
This ensures that the tools can interact with external services securely.

You can go to [here](https://platform.dappier.com/profile/api-keys) to get API Key from Dappier with **free** credits.

```python Python theme={null}
import os
from getpass import getpass