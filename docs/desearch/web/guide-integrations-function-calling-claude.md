<!--
source: https://desearch.ai/docs/guide/integrations/function-calling-claude
title: Function Calling with Claude - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# Function Calling with Claude - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/function-calling-claude

---

Home
Guide
API Reference
SDKs
API Console
API Status
GitHub
Discord
Blog
Search guides...
⌘K
INTRODUCTION
Desearch AI
Desearch Console
Glossary
APIS
Desearch API
Desearch x Bittensor
API Keys
Authorization
Pricing and Billing
SDK
Desearch API SDK
Python SDK Specification
JavaScript SDK Specification
INTEGRATIONS
MCP
OpenAI Wrapper
Function Calling with GPT
Function Calling with Claude
RAG with LangChain x Desearch
RAG with LlmaIndex x Desearch
ElizaOs Agents with Desearch
CrewAI Agents with Desearch
Browser Use x Desearch
OpenClaw Agent with Desearch
Numinous SN6 × Desearch Integration
USE CASES
Search Engine Use Cases
AI-Driven Chat Use Cases
Intelligent Agent Task Automation
CAPABILITIES
X (Twitter) Queries
Function Calling with Claude

This guide shows how to integrate Anthropic’s Claude LLM with Desearch using Claude's Tool Use (function calling) feature. The integration lets Claude intelligently decide when to call Desearch’s AI search and return up-to-date web content.

Function Calling with Claude

## Installation and Environment Setup

Make sure you have <Anchor label="python3" target="_blank" href="https://www.python.org/doc/">python3</Anchor> and <Anchor label="pip" target="_blank" href="https://pip.pypa.io/en/stable/installation/">pip</Anchor> installed on your machine.

Install the required packages:

SHELL
pip install anthropic desearch_py rich python-dotenv

This installs:

- anthropic for Claude API calls
- desearch_py for Desearch AI search
- rich for better terminal output
- python-dotenv for loading environment variables

## API Key Setup

Create a .env file in your project root:

TEXT
ANTHROPIC_API_KEY=your_claude_api_key_here
DESEARCH_API_KEY=your_desearch_api_key_here

Get your keys from:

- <Anchor label="Anthropic Console" target="_blank" href="https://console.anthropic.com/settings/keys">Anthropic Console</Anchor>
- <Anchor label="Desearch Dashboard" target="_blank" href="https://console.desearch.ai/api-keys">Desearch Dashboard</Anchor>

Make sure to add .env to .gitignore to avoid leaking secrets.

## Understanding Tool Use in Claude

Claude can generate structured requests to call external tools you define.

Here's the tool schema you'll define for Claude:

JSON
{
  "name": "desearch_search",
  "description": "Perform a web search and return the most relevant data.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query to perform."
      }
    },
    "required": ["query"]
  }
}

When Claude detects the need to search, it will return something like:

JSON
{
  "type": "tool_use",
  "id": "toolu_xxx",
  "name": "desearch_search",
  "input": {"query": "latest news on AI regulation"}
}

You must handle this tool call and pass the query to Desearch in your own code.

## Using Desearch with Claude Tool Use

### Step 1: Initialize Clients

PYTHON
from dotenv import load_dotenv
import anthropic
import os
from desearch_py import Desearch

load_dotenv()

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
desearch = Desearch(api_key=os.getenv("DESEARCH_API_KEY"))

### Step 2: Define the Tool

PYTHON
TOOLS = [
    {
        "name": "desearch_search",
        "description": "Perform a web search and return relevant data.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to perform."
                }
            },
            "required": ["query"]
        }
    }
]

Step 3: System Prompt

PYTHON
SYSTEM_MESSAGE = "You are an assistant with access to an advanced AI search engine. Use the Desearch tool to help the user find up-to-date information."

Step 4: Define the Tool Function

PYTHON
def desearch_search(query: str) -> dict:
    return desearch.ai_search(
        prompt=query,
        tools=["twitter"],
        model="NOVA",
        date_filter="PAST_24_HOURS",
        streaming=False
    )

Step 5: Tool Call Handler

PYTHON
def process_tool_calls(tool_calls):
    search_results = []
    for tool_call in tool_calls:
        if tool_call.name == "desearch_search":
            args = tool_call.input
            results = desearch_search(**args)
            search_results.append(results)
    return search_results
4. Main Loop: Chat with Search Integration
PYTHON
from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown

console = Console()

def main():
    messages = []
    while True:
        try:
            user_input = Prompt.ask("[bold yellow]What do you want to search for?[/bold yellow]")
            messages.append({"role": "user", "content": user_input})

            response = claude.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                system=SYSTEM_MESSAGE,
                messages=messages,
                tools=TOOLS
            )

            tool_calls = [item for item in response.content if item.type == "tool_use"]

            if tool_calls:
                results = process_tool_calls(tool_calls)
                messages.append({"role": "assistant", "content": f"Search results: {results}"})
                messages.append({"role": "user", "content": "Summarize the findings and answer the original query."})
                
                followup = claude.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1024,
                    system=SYSTEM_MESSAGE,
                    messages=messages
                )

                final_response = followup.content[0].text
                console.print(Markdown(final_response))
                messages.append({"role": "assistant", "content": final_response})

            else:
                console.print(Markdown(response.content[0].text))
                messages.append({"role": "assistant", "content": response.content[0].text})

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
5. Run the Script

Save everything as claude_desearch.py. Then run it:

SHELL
python claude_desearch.py

You’ll be prompted like this:

SHELL
What do you want to search for?

✅ Sample Output

SHELL
What do you want to search for?: What is Bittensor?
Context updated with desearch_search:  What is Bittensor?
Bittensor is a decentralized machine learning network built on blockchain. It allows users to contribute AI models to a global marketplace and earn $TAO tokens. The system promotes open collaboration and aims to democratize access to AI infrastructure.
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
