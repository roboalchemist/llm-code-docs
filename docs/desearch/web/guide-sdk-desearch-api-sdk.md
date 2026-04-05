<!--
source: https://desearch.ai/docs/guide/sdk/desearch-api-sdk
title: Desearch API SDK - SDK Documentation | Desearch
captured: 2026-04-04
-->
# Desearch API SDK - SDK Documentation | Desearch

Source: https://desearch.ai/docs/guide/sdk/desearch-api-sdk

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
Desearch API SDK
Introduction

The Desearch API provides powerful AI-powered search capabilities that can be easily integrated into your applications. To simplify integration and reduce boilerplate code, we offer official SDK implementations for the most popular programming languages.

Our SDKs provide:

Type safety: Full TypeScript/Python type definitions for all API responses
Error handling: Consistent error handling across all endpoints
Authentication: Simplified API key management
Convenience methods: Helper functions for common use cases
Documentation: Inline documentation and examples
Supported Languages

We currently offer official SDK implementations for the following languages:

Python SDK

Our Python SDK is ideal for:

Data science and machine learning applications
Backend services and APIs
Automation scripts and bots
Jupyter notebook integrations
AI agent frameworks (LangChain, LlamaIndex, CrewAI)

Key features:

Async client support with asyncio
Pydantic models for type validation
Compatible with Python 3.8+
Easy integration with popular frameworks

View Python SDK Documentation →

JavaScript/TypeScript SDK

Our JavaScript SDK is perfect for:

Node.js backend applications
React, Vue, or Angular frontends
Serverless functions (AWS Lambda, Vercel, Cloudflare Workers)
Browser-based applications
Full-stack TypeScript projects

Key features:

Full TypeScript support with type definitions
Works in both Node.js and browser environments
Promise-based async API
Tree-shakeable for optimal bundle size

View JavaScript SDK Documentation →

Quick Comparison

| Feature | Python SDK | JavaScript SDK |
|---------|-----------|----------------|
| Async Support | ✅ asyncio | ✅ Promises |
| Type Safety | ✅ Pydantic | ✅ TypeScript |
| Browser Support | ❌ | ✅ |
| Node.js Support | ❌ | ✅ |
| Framework Integrations | LangChain, LlamaIndex | React, Vue, Next.js |
Common Features

Both SDKs support all Desearch API endpoints:

Search Endpoints
AI Contextual Search: Multi-source semantic search with optional AI-generated summaries
AI Web Links Search: Raw link search across web sources without AI summaries
AI X Posts Links Search: AI-powered X (Twitter) post link search
X Search: Advanced X (Twitter) search with extensive filtering options
SERP Web Search: Paginated web search replicating a typical search engine
X (Twitter) Data Endpoints
Fetch Posts by URLs: Retrieve full post data for a list of X post URLs
Retrieve Post by ID: Fetch a single X post by its unique ID
Search X Posts by User: Search posts from a specific user with optional keyword filtering
Get Retweeters of a Post: List users who retweeted a specific post
Get X Posts by Username: Retrieve a user's timeline posts
Fetch User's Tweets and Replies: Fetch tweets and replies from a specific user
Retrieve Replies for a Post: Fetch replies to a specific X post
Web Crawling
Crawl a URL: Fetch page content as plain text or HTML
Getting Started
Step 1: Get Your API Key

Before using any SDK, you'll need a Desearch API key:

Visit console.desearch.ai
Create an account or sign in
Navigate to API Keys section
Generate a new API key
Copy and securely store your key
Step 2: Choose Your SDK

Select the SDK that matches your development environment:

Python developers: Python SDK Guide
JavaScript/TypeScript developers: JavaScript SDK Guide
Step 3: Install and Configure

Follow the installation instructions in your chosen SDK's documentation. Both SDKs can be installed via their respective package managers:

Python:

BASH
pip install desearch-py

JavaScript:

```bash
npm install desearch-js
# or
yarn add desearch-js
```

## Step 4: Make Your First Request

Python:

PYTHON
import asyncio
from desearch_py import Desearch

async def main():
    async with Desearch(api_key="your_api_key") as desearch:
        result = await desearch.ai_search(
            prompt="Latest developments in AI",
            tools=["web", "twitter", "reddit"],
        )
        print(result)

asyncio.run(main())

JavaScript:

TYPESCRIPT
import Desearch from "desearch-js";

const desearch = new Desearch("your-api-key");

desearch
  .aiSearch({
    prompt: "Latest developments in AI",
    tools: ["web", "twitter", "reddit"],
  })
  .then((response) => {
    console.log(response);
  });
Support and Resources
API Reference: docs.desearch.ai/api-reference
GitHub Issues: Report bugs or request features
Discord Community: Get help from other developers
Email Support: support@desearch.ai
Choosing the Right SDK
Use Python SDK if:
You're building ML/AI applications
You need integration with pandas, numpy, or scikit-learn
You're using LangChain or LlamaIndex
You're running automation scripts
You prefer async Python code patterns
Use JavaScript SDK if:
You're building web applications
You need browser compatibility
You're using Node.js for backend
You want TypeScript type safety
You're building serverless functions

Both SDKs are maintained and updated regularly to support new API features and improvements. Check the respective documentation pages for version history and changelog information.

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
