# 🧩 Smart Content Curator with LangChain + Dappier MCP using `mcp-use`
Source: https://docs.dappier.com/cookbook/recipes/mcp-use-news-letter



This cookbook demonstrates how to build a real-time, LLM-powered **content curation assistant** using **LangChain**, **Dappier MCP**, and the lightweight **`mcp-use`** client. You’ll walk through creating a **Smart Content Curator** that fetches structured, AI-generated content recommendations across a variety of rich lifestyle and news domains — including **sports**, **lifestyle**, **pet care**, **planet-friendly living**, and **local news** — and presents them in clean, markdown-ready summaries.

In this cookbook, you’ll explore:

* **LangChain + OpenAI**: A flexible framework for developing LLM-based agents with tool calling, memory, and decision-making capabilities.
* **Dappier MCP**: A Model Context Protocol server that connects your LLM agents to **real-time, AI-powered tools** — including dynamic recommendations, live summaries, and category-specific insights.
* **AI Recommendations**: Use domain-specific AI models like **iHeartDogs**, **iHeartCats**, **GreenMonster**, and **WISH-TV AI** to pull curated content from verified sources such as *One Green Planet*, *Home Life Media*, and *WISH-TV*, tailored for responsible media, animal lovers, environmentalists, and local news readers.
* **mcp-use**: A minimal Python client for integrating any MCP server using `stdio` or `http`, ideal for rapid prototyping and production.
* **Content Curation Assistant**: A production-ready use case that outputs structured, high-quality summaries from live data — perfect for newsletters, editorial pipelines, or content automation dashboards.

Explore all available AI data models via the [Dappier Marketplace](https://marketplace.dappier.com/marketplace).

## 📦 Installation

To get started, install the required tools and dependencies:

***

**Step 1: Install `uv` (required to run the Dappier MCP server)**

**macOS / Linux**:

```bash  theme={null}
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows**:

```bash  theme={null}
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

***

**Step 2: Create a Virtual Environment (Recommended)**

Create and activate a virtual environment to isolate dependencies.

**macOS / Linux**:

```bash  theme={null}
python3 -m venv venv
source venv/bin/activate
```

**Windows**:

```bash  theme={null}
python -m venv venv
venv\Scripts\activate
```

***

**Step 3: Install Python Packages**

Install the necessary Python dependencies including LangChain and `mcp-use`.

```bash  theme={null}
pip install langchain-openai mcp-use python-dotenv
```

## 🔑 Setting Up API Keys

You’ll need API keys for both **Dappier** and **OpenAI** to authenticate your requests and access tools.

***

**Dappier API Key**

Visit [Dappier](https://platform.dappier.com/profile/api-keys) to generate your API key. Dappier provides free credits to help you get started.

You can set the API key as an environment variable in your terminal:

```bash  theme={null}
export DAPPIER_API_KEY=your-dappier-api-key
```

Or include it in a `.env` file at the root of your project:

```env  theme={null}
DAPPIER_API_KEY=your-dappier-api-key
```

***

**OpenAI API Key**

Go to [OpenAI](https://platform.openai.com/account/api-keys) to retrieve your API key.

Set it in your terminal:

```bash  theme={null}
export OPENAI_API_KEY=your-openai-api-key
```

Or include it in your `.env` file:

```env  theme={null}
OPENAI_API_KEY=your-openai-api-key
```

In your Python script, load the `.env` file:

```python Python Python theme={null}
from dotenv import load_dotenv

load_dotenv()
```

## ⚙️ Import Dependencies

Start by importing the required modules to build the content curation agent. This includes components from `mcp-use`, LangChain, and environment configuration.

```python Python theme={null}
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
```

These imports enable:

* Loading environment variables using `dotenv`
* Running asynchronous workflows with `asyncio`
* Accessing OpenAI models through LangChain
* Interacting with the Dappier MCP server using `mcp-use` to retrieve AI-powered content recommendations

## 📝 Define User Input

We’ll collect a natural language query from the user, allowing them to request **multiple types of content** in a single prompt — for example, “Give me today’s top sports and lifestyle stories” or “What’s new in pet care and the green planet space?”.

```python Python theme={null}
def get_user_input():
    query = input("What kind of curated content are you interested in? You can combine multiple topics (e.g., sports and lifestyle, pet care and green planet): ").strip()
    return query
```

## 🛰️ Run the Agent with Dappier MCP

This function sets up the MCP agent using `mcp-use`, formulates a content curation query, and executes it using Dappier’s AI-powered recommendation tools.

```python Python theme={null}
async def run_content_curator(query: str):
    # Load environment variables
    load_dotenv()

    # Retrieve API key
    api_key = os.getenv("DAPPIER_API_KEY")
    if not api_key:
        raise ValueError("DAPPIER_API_KEY is not set")

    # MCPClient configuration using stdio transport (via uvx dappier-mcp)
    config = {
        "mcpServers": {
            "dappier": {
                "command": "uvx",
                "args": ["dappier-mcp"],
                "env": {
                    "DAPPIER_API_KEY": api_key
                }
            }
        }
    }

    # Create MCP client and LLM
    client = MCPClient.from_dict(config)
    llm = ChatOpenAI(model="gpt-4o")

    # Create the agent
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        # Formulate prompt
        full_prompt = f"""
        Act as a smart content curator. Use Dappier’s AI-powered tools to fetch the latest articles and recommendations based on this query: "{query}"

        For each topic:
        - Retrieve high-quality, AI-recommended articles
        - Provide a brief summary for each
        - Format everything as a clean, readable markdown newsletter

        Output structure:
        - Group articles by topic
        - Use markdown formatting (e.g., headlines, bullet points, bold)
        - Include direct links to sources where available
        """

        print("\n" + "-" * 40)
        print(f"Running content curation for: {query}")
        print("\n=== Response ===\n")

        result = await agent.run(full_prompt, max_steps=30)
        print(result)

    finally:
        # Clean up sessions
        if client.sessions:
            await client.close_all_sessions()
```

## 🚦 Initialize and Launch the Workflow

The `main()` function collects the user’s natural language request and runs the content curation workflow using `mcp-use` and Dappier MCP.

```python Python theme={null}
async def main():
    query = get_user_input()
    await run_content_curator(query)
```

To start the agent, run the main function using `asyncio`:

```python Python theme={null}
if __name__ == "__main__":
    asyncio.run(main())
```

```json  theme={null}
What kind of curated content are you interested in? You can combine multiple topics (e.g., sports and lifestyle, pet care and green planet): Please fetch latest content from sports, lifestyle and wishtv and present them in a blog format 

----------------------------------------
Running content curation for: Please fetch latest content from sports, lifestyle and wishtv and present them in a blog format

=== Response ===

[04/23/25 14:13:56] INFO     Processing request of type ListToolsRequest                                                                        server.py:534
                    INFO     Processing request of type ListToolsRequest                                                                        server.py:534
[04/23/25 14:13:58] INFO     Processing request of type CallToolRequest                                                                         server.py:534
[04/23/25 14:14:00] INFO     HTTP Request: POST https://api.dappier.com/app/v2/search?data_model_id=dm_01j0pb465keqmatq9k83dthx34 "HTTP/1.1   _client.py:1025
                             200 OK"                                                                                                                         
                    INFO     Processing request of type CallToolRequest                                                                         server.py:534
[04/23/25 14:14:01] INFO     HTTP Request: POST https://api.dappier.com/app/v2/search?data_model_id=dm_01j0q82s4bfjmsqkhs3ywm3x6y "HTTP/1.1   _client.py:1025
                             200 OK"                                                                                                                         
                    INFO     Processing request of type CallToolRequest                                                                         server.py:534
[04/23/25 14:14:02] INFO     HTTP Request: POST https://api.dappier.com/app/v2/search?data_model_id=dm_01jagy9nqaeer9hxx8z1sk1jx6 "HTTP/1.1   _client.py:1025
                             200 OK"