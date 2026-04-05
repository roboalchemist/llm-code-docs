<!--
source: https://desearch.ai/docs/guide/integrations/function-calling-gpt
title: Function Calling with GPT - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# Function Calling with GPT - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/function-calling-gpt

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
Function Calling with GPT

This guide walks you through how to use OpenAI's tool calling feature to connect with Desearch, a powerful AI-driven search engine. We'll cover everything from setup to running live search queries through an LLM.

Function Calling with GPT

## Installation and Requirements

Start by installing the necessary Python packages:

PYTHON
pip install openai desearch_py rich

- openai: for communicating with OpenAI models
- desearch_py: to access Desearch search functionality
- rich: for colorful and structured terminal output

## Setting Environment Variables

Create a .env file in the root of your project with your API keys:

TEXT
OPENAI_API_KEY=your_openai_api_key
DESEARCH_API_KEY=your_desearch_api_key

You can get your API keys from:

- <Anchor label="OpenAI API Key" target="_blank" href="https://platform.openai.com/api-keys">OpenAI API Key</Anchor>
- <Anchor label="Desearch API Key" target="_blank" href="https://console.desearch.ai/api-keys">Desearch API Key</Anchor>

## What Is Tool Calling?

Tool calling allows OpenAI models to return structured calls to functions you define in your code.

Here’s a sample schema that defines how your tool is described to the model:

JSON
{
  "name": "desearch_search",
  "description": "Performs a search and returns relevant information.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query to run."
      }
    },
    "required": ["query"]
  }
}

OpenAI will return a function name and its parameters — you are responsible for executing the actual call in your code.

## Integrating Desearch as an OpenAI Tool

### Step 1: Initialize Your Clients

PYTHON
from dotenv import load_dotenv
from desearch_py import Desearch
from openai import OpenAI
import os

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
desearch = Desearch(api_key=os.getenv("DESEARCH_API_KEY"))

### Step 2: Define Tool Schema

PYTHON
TOOLS = [
  {
    "name": "desearch_search",
    "description": "Perform a web search and return relevant results.",
    "input_schema": {
      "type": "object",
      "properties": {
        "query": {
          "type": "string",
          "description": "The search term to use."
        }
      },
      "required": ["query"]
    }
  }
]

### Step 3: Define the System Prompt

PYTHON
SYSTEM_MESSAGE = {
  "role": "system",
  "content": "You are a smart assistant with access to a powerful search engine. Use the provided tool to help the user find answers."
}

### Step 4: Create the Desearch Function

PYTHON
def desearch_search(query: str) -> dict:
  return desearch.ai_search(
    prompt=query,
    tools=["twitter"],
    model="NOVA",
    date_filter="PAST_24_HOURS",
    streaming=False
  )

Step 5: Handle Tool Calls

PYTHON
def process_tool_calls(tool_calls, messages):
  for call in tool_calls:
    args = json.loads(call.function.arguments)
    if call.function.name == "desearch_search":
      results = desearch_search(**args)
      messages.append({
        "role": "tool",
        "content": str(results),
        "tool_call_id": call.id
      })
  return messages

Step 6: Build the Main Loop

PYTHON
def main():
  messages = [SYSTEM_MESSAGE]
  while True:
    user_input = Prompt.ask("🔎 What do you want to search for?")
    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages,
      tools=TOOLS
    )
    
    message = response.choices[0].message
    tool_calls = message.tool_calls

    if tool_calls:
      messages.append(message)
      messages = process_tool_calls(tool_calls, messages)
      messages.append({
        "role": "user",
        "content": "Use the search results to answer my last question."
      })

      final_response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
      )
      console.print(Markdown(final_response.choices[0].message.content))
    else:
      console.print(Markdown(message.content))
5. Run the App

Save your code as openai_search.py and ensure your .env file is in the same directory. Run the script:

PYTHON
python openai_search.py

You'll be prompted:

TEXT
What do you want to search for?

Type your query, and the assistant will use Desearch to find real-time answers.

What do you want to search for?: What is bittensor? Context updated with desearch_search (None): What is bittensor? Bittensor is a decentralized AI network designed to create a marketplace for machine learning models and AI training services. Unlike traditional AI systems, which are often restricted by centralized APIs or paywalls, Bittensor utilizes blockchain technology to allow open and permissionless participation in AI development. The primary aim is to democratize access to AI and build a collaborative ecosystem where contributors earn rewards for training and enhancing AI models. At its core, Bittensor functions as a decentralized marketplace where participants, referred to as miners, contribute computational resources to train machine learning models. In return, these miners earn TAO tokens as rewards. This structure fosters a competitive market based on incentives, encouraging ongoing innovation and improvement of AI technologies. Bittensor is characterized as a network of incentive-driven subnets rather than a traditional blockchain like Bitcoin or Ethereum. Each subnet acts as a competitive market for AI training, promoting a self-sustaining economy wherein AI models are continuously refined through collective contributions. The ecosystem aims to integrate AI with Web3 principles, emphasizing ownership, control, and open participation. By facilitating a decentralized AI marketplace, Bittensor seeks to drive innovation through collaborative effort and financial incentives, potentially leading to more diverse and powerful AI models. In summary, Bittensor represents an innovative approach to merging blockchain technology with AI training and marketplace dynamics, promoting a shift towards decentralized AI ownership and collaboration.

The assistant now responds using fresh information retrieved via Desearch, powered by GPT.

Full code
PYTHON
import json
import os

from dotenv import load_dotenv
from typing import Any, Dict
from desearch_py import Desearch
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
desearch = Desearch(api_key=os.getenv("DESEARCH_API_KEY"))

console = Console()

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "desearch_search",
            "description": "Perform a web search and return relevant results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search term to use.",
                    }
                },
                "required": ["query"],
            },
        },
    }
]

SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are a smart assistant with access to a powerful search engine. Use the provided tool to help the user find answers.",
}

def desearch_search(query: str) -> dict:
    return desearch.ai_search(
        prompt=query,
        tools=["twitter"],
        model="NOVA",
        date_filter="PAST_24_HOURS",
        streaming=False,
    )

def process_tool_calls(tool_calls, messages):
    for call in tool_calls:
        args = json.loads(call.function.arguments)
        if call.function.name == "desearch_search":
            results = desearch_search(**args)
            messages.append(
                {"role": "tool", "content": str(results), "tool_call_id": call.id}
            )
            console.print(
                f"[bold cyan]Context updated[/bold cyan] [i]with[/i] "
                f"[bold green]desearch_search ({args.get('mode')})[/bold green]: ",
                args.get("query"),
            )
    return messages

def main():
    messages = [SYSTEM_MESSAGE]
    while True:
        try:
            user_input = Prompt.ask("🔎 What do you want to search for?")
            messages.append({"role": "user", "content": user_input})

            response = openai.chat.completions.create(
                model="gpt-4o-mini", messages=messages, tools=TOOLS
            )

            message = response.choices[0].message
            tool_calls = message.tool_calls

            if tool_calls:
                messages.append(message)
                messages = process_tool_calls(tool_calls, messages)
                messages.append(
                    {
                        "role": "user",
                        "content": "Use the search results to answer my last question.",
                    }
                )

                final_response = openai.chat.completions.create(
                    model="gpt-4o-mini", messages=messages
                )
                console.print(Markdown(final_response.choices[0].message.content))
            else:
                console.print(Markdown(message.content))
        except Exception as e:
            console.print(f"[bold red]An error occurred:[/bold red] {str(e)}")

if __name__ == "__main__":
    main()

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
