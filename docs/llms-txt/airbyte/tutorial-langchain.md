# Source: https://docs.airbyte.com/ai-agents/tutorials/quickstarts/tutorial-langchain.md

# Agent connector tutorial: LangChain

Copy Page

In this tutorial, you'll create a new Python project with uv, add a LangChain agent, equip it to use one of Airbyte's agent connectors, and use natural language to explore your data. This tutorial uses GitHub, but if you don't have a GitHub account, you can use one of Airbyte's other agent connectors and perform different operations.

## Overview[​](#overview "Direct link to Overview")

This tutorial is for AI engineers and other technical users who work with data and AI tools. You can complete it in about 15 minutes.

The tutorial assumes you have basic knowledge of the following tools, but most software engineers shouldn't struggle with anything that follows.

* Python and package management with uv
* LangChain and LangGraph
* GitHub, or a different third-party service you want to connect to

## Before you start[​](#before-you-start "Direct link to Before you start")

Before you begin this tutorial, ensure you have the following.

* [Python](https://www.python.org/downloads/) version 3.13 or later
* [uv](https://github.com/astral-sh/uv)
* A [GitHub personal access token](https://github.com/settings/tokens). For this tutorial, a classic token with `repo` scope is sufficient.
* An [OpenAI API key](https://platform.openai.com/api-keys). This tutorial uses OpenAI, but LangChain supports other LLM providers if you prefer.

## Part 1: Create a new Python project[​](#part-1-create-a-new-python-project "Direct link to Part 1: Create a new Python project")

In this tutorial you initialize a basic Python project to work in. However, if you have an existing project you want to work with, feel free to use that instead.

Create a new project using uv:

```
uv init my-langchain-agent --app
cd my-langchain-agent
```

This creates a project with the following structure:

```
my-langchain-agent/
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
└── README.md
```

You create `.env` and `uv.lock` files in later steps, so don't worry about them yet.

## Part 2: Install dependencies[​](#part-2-install-dependencies "Direct link to Part 2: Install dependencies")

Install the GitHub connector, LangChain with OpenAI support, and LangGraph for the agent runtime:

```
uv add airbyte-agent-github langchain langchain-openai langgraph
```

This command installs:

* `airbyte-agent-github`: The Airbyte agent connector for GitHub, which provides type-safe access to GitHub's API.
* `langchain`: The LangChain framework core.
* `langchain-openai`: LangChain's OpenAI integration for chat models.
* `langgraph`: The LangGraph agent runtime, which provides a `create_react_agent` function for building tool-calling agents.

The GitHub connector also includes `python-dotenv`, which you can use to load environment variables from a `.env` file.

## Part 3: Import LangChain and the GitHub agent connector[​](#part-3-import-langchain-and-the-github-agent-connector "Direct link to Part 3: Import LangChain and the GitHub agent connector")

1. Create an `agent.py` file for your agent definition:

   ```
   touch agent.py
   ```

2. Add the following imports to `agent.py`:

   agent.py

   ```
   import os
   import json

   from dotenv import load_dotenv
   from langchain_core.tools import tool
   from langchain_openai import ChatOpenAI
   from langgraph.prebuilt import create_react_agent
   from airbyte_agent_github import GithubConnector
   from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig
   ```

   These imports provide:

   * `os` and `json`: Access environment variables and serialize connector results.
   * `load_dotenv`: Load environment variables from your `.env` file.
   * `tool`: LangChain's decorator for converting a function into a tool.
   * `ChatOpenAI`: LangChain's OpenAI chat model integration.
   * `create_react_agent`: LangGraph's function for creating a ReAct agent that can call tools.
   * `GithubConnector`: The Airbyte agent connector that provides type-safe access to GitHub's API.
   * `GithubPersonalAccessTokenAuthConfig`: The authentication configuration for the GitHub connector using a personal access token.

## Part 4: Add a .env file with your secrets[​](#part-4-add-a-env-file-with-your-secrets "Direct link to Part 4: Add a .env file with your secrets")

1. Create a `.env` file in your project root and add your secrets to it. Replace the placeholder values with your actual credentials.

   .env

   ```
   GITHUB_ACCESS_TOKEN=your-github-personal-access-token
   OPENAI_API_KEY=your-openai-api-key
   ```

   warning

   Never commit your `.env` file to version control. If you do this by mistake, rotate your secrets immediately.

2. Add the following line to `agent.py` after your imports to load the environment variables:

   agent.py

   ```
   load_dotenv()
   ```

   This makes your secrets available via `os.environ`. LangChain's `ChatOpenAI` automatically reads `OPENAI_API_KEY` from the environment, and you'll use `os.environ["GITHUB_ACCESS_TOKEN"]` to configure the connector in the next section.

## Part 5: Configure your connector and agent[​](#part-5-configure-your-connector-and-agent "Direct link to Part 5: Configure your connector and agent")

Now that your environment is set up, add the following code to `agent.py` to create the GitHub connector and LangChain agent.

### Define the connector[​](#define-the-connector "Direct link to Define the connector")

Define the agent connector for GitHub. It authenticates using your personal access token.

agent.py

```
connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(
        token=os.environ["GITHUB_ACCESS_TOKEN"]
    )
)
```

### Define the tool[​](#define-the-tool "Direct link to Define the tool")

Create an async function that wraps the connector's `execute` method as a LangChain tool. The `@tool` decorator converts the function into a LangChain tool, and `@GithubConnector.tool_utils` automatically generates a comprehensive tool description from the connector's metadata. This tells the agent what entities are available (issues, pull requests, repositories, etc.), what actions it can perform on each entity, and what parameters each action requires.

agent.py

```
@tool
@GithubConnector.tool_utils
async def github_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute GitHub connector operations."""
    result = await connector.execute(entity, action, params or {})
    return json.dumps(result, default=str)
```

### Define the agent[​](#define-the-agent "Direct link to Define the agent")

Create a LangChain chat model and a LangGraph ReAct agent:

agent.py

```
llm = ChatOpenAI(model="gpt-4o")
agent = create_react_agent(llm, [github_execute])
```

* `ChatOpenAI(model="gpt-4o")` creates an OpenAI chat model. You can use a different model by changing the model string. For example, use `"gpt-4o-mini"` to lower costs. LangChain also supports [other providers](https://python.langchain.com/docs/integrations/chat/) like Anthropic and Google.
* `create_react_agent` creates a ReAct agent that reasons about which tools to call based on the user's input.

## Part 6: Run your project[​](#part-6-run-your-project "Direct link to Part 6: Run your project")

Now that your agent is configured with tools, update `main.py` and run your project.

1. Update `main.py`. This code creates a simple chat interface in your command line tool and allows your agent to remember your conversation history between prompts.

   main.py

   ```
   import asyncio
   from agent import agent

   async def main():
       print("GitHub Agent Ready! Ask questions about GitHub repositories.")
       print("Type 'quit' to exit.\n")

       history = []

       while True:
           prompt = input("You: ")
           if prompt.lower() in ("quit", "exit", "q"):
               break
           history.append({"role": "user", "content": prompt})
           result = await agent.ainvoke({"messages": history})
           response = result["messages"][-1].content
           history = result["messages"]
           print(f"\nAgent: {response}\n")

   if __name__ == "__main__":
       asyncio.run(main())
   ```

2. Run the project.

   ```
   uv run main.py
   ```

### Chat with your agent[​](#chat-with-your-agent "Direct link to Chat with your agent")

The agent waits for your input. Once you prompt it, the agent decides which tools to call based on your question, fetches the data from GitHub, and returns a natural language response. Try prompts like:

* "List the 10 most recent open issues in airbytehq/airbyte"
* "What are the 10 most recent pull requests that are still open in airbytehq/airbyte?"
* "Are there any open issues that might be fixed by a pending PR?"

The agent has basic message history within each session, and you can ask followup questions based on its responses.

### Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

If your agent fails to retrieve GitHub data, check the following:

* **HTTP 401 errors**: Your `GITHUB_ACCESS_TOKEN` is invalid or expired. Generate a new token and update your `.env` file.
* **HTTP 403 errors**: Your `GITHUB_ACCESS_TOKEN` doesn't have the required scopes. Ensure your token has `repo` scope for accessing repository data.
* **OpenAI errors**: Verify your `OPENAI_API_KEY` is valid, has available credits, and won't exceed rate limits.

## Summary[​](#summary "Direct link to Summary")

In this tutorial, you learned how to:

* Set up a new Python project with uv
* Add LangChain, LangGraph, and Airbyte's GitHub agent connector to your project
* Configure environment variables and authentication
* Create a LangChain tool from the GitHub connector
* Build a ReAct agent with LangGraph and use natural language to interact with GitHub data

## Next steps[​](#next-steps "Direct link to Next steps")

* Add more agent connectors to your project. Explore other agent connectors in the [Airbyte agent connectors catalog](/ai-agents/connectors/.md) to give your agent access to more services like Stripe, HubSpot, and Salesforce.

* Consider how you might like to expand your agent's capabilities. For example, you might want to trigger effects like sending a Slack message or an email based on the agent's findings. You aren't limited to the capabilities of Airbyte's agent connectors. You can use other libraries and integrations to build an increasingly robust agent ecosystem.
