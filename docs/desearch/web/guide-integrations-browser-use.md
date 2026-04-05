<!--
source: https://desearch.ai/docs/guide/integrations/browser-use
title: Browser Use x Desearch - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# Browser Use x Desearch - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/browser-use

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
Browser Use x Desearch

browser-use is a powerful framework for running autonomous browser agents. This guide shows how to integrate Desearch as a custom tool for your agents, enabling them to perform advanced web and social media searches. You'll learn how to:

Build custom tools in browser-use powered by Desearch
Configure agents to use those tools
Create agents that automate searches and write outputs in the browser
🚀 browser-use Example: Bittensor Article Writer

This guide demonstrates how to build a browser-use agent that searches Twitter for posts about “Bittensor” and writes an article using the results.

1. Install Dependencies

Use pip to install the required libraries.

BASH
pip install browser-use desearch-py python-dotenv
2. Configure Environment Variables

Set your Desearch API key in your .env file so your agent can authenticate with the Desearch API.

DESEARCH_API_KEY=your_api_key_here
3. Build the Desearch Tool

We create a custom tool that connects browser-use to the Desearch SDK. It runs searches based on parameters your agent provides.

PYTHON
from browser_use import Controller, ActionResult
from desearch_py import Desearch
from pydantic import BaseModel, Field
import os

controller = Controller()

class BasicTwitterSearchToolInput(BaseModel):
    query: str = Field(description="The Twitter search query.")

@controller.action(
    "Use the Basic Twitter Search tool to perform a search.",
    param_model=BasicTwitterSearchToolInput,
)
def run_basic_twitter_search(params: BasicTwitterSearchToolInput) -> str:
    query = params.query
    """Use the tool synchronously."""
    api_key = os.getenv("DESEARCH_API_KEY")
    if not api_key:
        raise ValueError("DESEARCH_API_KEY environment variable not set.")

    desearch = Desearch(api_key=api_key)
    try:
        result = desearch.basic_twitter_search(query=query)
        return ActionResult(extracted_content=result.__str__())
    except Exception as e:
        return f"An error occurred while calling Desearch: {str(e)}"

4. Create the Agent

Import browser-use modules and configure your agent.

PYTHON
from browser_use import Agent
from browser_use.llm import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

task = (
    "Go to https://www.onlinenotepad.io/ "
    "and write an article about 'Bittensor' using tweets found via the search tool."
)

agent = Agent(
    task=task,
    llm=ChatOpenAI(model="gpt-4o"),
    use_vision=False,
    max_failures=2,
    controller=controller,
    max_actions_per_step=1,
)
5. Run the Agent

Finally, execute the agent asynchronously:

PYTHON
import asyncio

async def run():
    await agent.run()

if __name__ == "__main__":
    asyncio.run(run())
6. Output

When your agent runs, it navigates to an online notepad and writes an article using data fetched from Desearch. For example:

Article Title: Bittensor and Its Growing Impact on AI Bittensor is creating buzz on Twitter as a decentralized network for machine learning. Users discuss how it rewards contributors and builds an open AI ecosystem. Several tweets highlight its innovative economic incentives and potential to democratize AI research. As interest grows, Bittensor is gaining more traction among developers and AI enthusiasts looking for decentralized alternatives to traditional cloud providers. Stay tuned for more insights on how Bittensor might shape the future of decentralized intelligence!
🔗 Further Reading
browser-use Quickstart
Desearch Python SDK
🎉 Conclusion

By integrating Desearch into browser-use, you can build agents that research topics, analyze social media, and automate writing—all directly inside a browser session!

An example project using this integration is available here: Desearch for browser-use on GitHub

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
