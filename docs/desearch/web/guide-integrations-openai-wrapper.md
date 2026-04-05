<!--
source: https://desearch.ai/docs/guide/integrations/openai-wrapper
title: OpenAI Wrapper - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# OpenAI Wrapper - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/openai-wrapper

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
OpenAI Wrapper

Power your OpenAI chat completions with an intuitive Desearch wrapper that automates search.

Desearch provides a AI search and retrieval ecosystem designed for building RAG (Retrieval-Augmented Generation) applications. By leveraging multi-source information from the X and web, Desearch delivers precise, current data to enhance your LLM outputs.

Effective RAG implementation requires more than basic search functionality. It demands intelligent query generation, multi-source integration, and contextual understanding. The Desearch OpenAI wrapper addresses these challenges with a single line of code, transforming any OpenAI chat completion into a comprehensive Desearch-powered RAG system.

Get Started
1. Installation

Install the Desearch and OpenAI Python libraries:

BASH
pip install openai desearch-py
2. Set Up Clients

Import and initialize the Desearch and OpenAI clients with your API keys:

PYTHON
from openai import OpenAI
from desearch_py import Desearch

openai = OpenAI(api_key='YOUR_OPENAI_API_KEY')

desearch = Desearch(api_key='YOUR_DESEARCH_API_KEY')
3. Enhance Your OpenAI Client

Use the Desearch.wrap method to enhance your existing OpenAI client with advanced RAG capabilities:

PYTHON
desearch_openai = desearch.wrap(openai)
4. Make Enhanced API Calls

The wrapped client maintains the familiar OpenAI interface while automatically augmenting completions with relevant search results from multiple sources:

PYTHON
completion = desearch_openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What are the latest developments in quantum computing?"}]
)

print(completion.choices[0].message.content)
5. Example Output
Here's a summary of the latest developments in quantum computing: 1. **IBM's Quantum Computing Milestone** - IBM announced their new 1,000+ qubit quantum processor, demonstrating significant progress in quantum hardware scaling. - The system includes advanced error correction techniques that improve computational stability. 2. **Google's Quantum Supremacy Update** - Researchers at Google AI Quantum published results showing their quantum computer performed a calculation in minutes that would take traditional supercomputers thousands of years. - The team has made substantial improvements to their error mitigation techniques, bringing practical quantum advantage closer to reality. 3. **Quantum Machine Learning Breakthroughs** - Recent research has demonstrated quantum algorithms that can potentially offer exponential speedups for specific machine learning tasks. - These advancements could revolutionize areas like drug discovery, materials science, and complex systems modeling. These developments suggest we're approaching a critical threshold where quantum computing may begin delivering practical advantages for specific computational problems, though general-purpose quantum computing still faces significant challenges.
6. Complete Code Example

Here's a comprehensive example you can copy into a Python script or Jupyter notebook to test the Desearch wrapper:

PYTHON
from openai import OpenAI
from desearch_py import Desearch
from desearch_py.protocol import ToolEnum, ModelEnum

# Initialize clients
openai = OpenAI(api_key='YOUR_OPENAI_API_KEY')
desearch = Desearch(api_key='YOUR_DESEARCH_API_KEY')

# Enhance the OpenAI client
desearch_openai = desearch.wrap(openai)

# Create a completion with RAG capabilities
completion = desearch_openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What are the latest breakthroughs in nuclear fusion?"}]
)

# Display the enhanced response
print(completion.choices[0].message.content)
7. Handling Multiple Questions

Here's how to process multiple questions efficiently with the Desearch wrapper:

PYTHON
# Define a list of questions
questions = [
    "What progress has been made in CRISPR gene editing recently?",
    "How are autonomous vehicles handling extreme weather conditions?",
]

# Process each question with enhanced context
for question in questions:
    completion = desearch_openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )

    print(f"Question: {question}")
    print(f"Answer: {completion.choices[0].message.content}")
    print("-" * 50)

## Information Source Selection

Specify which information sources to include using the tools parameter:

PYTHON
from desearch_py import ToolEnum

completion = desearch_openai.chat.completions.create(
    model="gpt-4",
    messages=messages,
    desearch_tools=[DesearchTool.web, DesearchTool.twitter, DesearchTool.hacker_news]
)
Time Relevance

Filter results by date using the date_filter parameter:

PYTHON
from desearch_py import DateFilterEnum

completion = desearch_openai.chat.completions.create(
    model="gpt-4",
    messages=messages,
    date_filter=DateFilterEnum.PAST_WEEK
)
Response Format

Customize how results are returned with the result_type parameter:

PYTHON
from desearch_py import ResultTypeEnum

completion = desearch_openai.chat.completions.create(
    model="gpt-4",
    messages=messages,
    result_type=ResultTypeEnum.LINKS_WITH_FINAL_SUMMARY
)
Model Selection

Choose which Desearch model to use for processing:

PYTHON
from desearch_py import ModelEnum

completion = desearch_openai.chat.completions.create(
    model="gpt-4",
    messages=messages,
    desearch_model=ModelEnum.HORIZON
)
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
