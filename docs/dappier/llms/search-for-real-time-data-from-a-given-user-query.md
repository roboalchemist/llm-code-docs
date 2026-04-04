# Search for real time data from a given user query.
response = DappierToolkit().search_real_time_data(
    query="latest news on CAMEL AI"
)

print(response)
```

```
Here’s the latest buzz on CAMEL AI! 🐫✨

- At **AdventureX2024**, CAMEL AI clinched **first prize** in the Graph Track! 🎉
- They’ve launched some cool new tools, including a **Discord bot** with RAG, **Redis cache storage**, and **Docker support** for code execution! 🛠️
- CAMEL AI has open-sourced **OASIS**, a next-gen simulator that can handle realistic social media dynamics with up to **one million agents**! 🌐
- They’ve integrated **OpenAI's o1 models** into their framework, enhancing multi-agent capabilities. 🤖
- Plus, they introduced a **Multi-Agent Collaboration Workforce** module, boosting cooperation among agents! 🤝

For more updates, check out their Discord: [CAMEL AI Discord](http://discord.camel-ai.org). Exciting stuff happening! 🚀
```

🎉 **Dappier effortlessly retrieves the latest news on CAMEL AI, providing valuable data for AI integration!**

## 🤖🤖 Multi-Agent Role-Playing with CAMEL

*This section sets up a role-playing session where AI agents interact to accomplish a task using Dappier tool. We will guide the assistant agent in creating a dynamic travel plan by leveraging real-time weather data.*

```python Python theme={null}
from typing import List

from colorama import Fore

from camel.agents.chat_agent import FunctionCallingRecord
from camel.societies import RolePlaying
from camel.toolkits import FunctionTool
from camel.utils import print_text_animated
```

Defining the Task Prompt

```python Python theme={null}
task_prompt = """Generate a 2-day travel itinerary for New York tailored to the
real-time weather forecast for the upcoming weekend. Start by utilizing
Dappier’s real-time search to determine the current date and day, calculate the
upcoming weekend based on this information, and fetch the corresponding weather
data for those dates. Use the weather insights to craft the itinerary.
No additional actions are required.
"""
```

We will configure the assistant agent with tools for real-time weather data
retrieval.

```python Python theme={null}
dappier_tool = FunctionTool(DappierToolkit().search_real_time_data)

tool_list = [
    dappier_tool
]

assistant_model_config = ChatGPTConfig(
    tools=tool_list,
    temperature=0.0,
)
```

Setting Up the Role-Playing Session

```python Python theme={null}