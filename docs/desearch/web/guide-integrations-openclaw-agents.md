<!--
source: https://desearch.ai/docs/guide/integrations/openclaw-agents
title: OpenClaw Agent with Desearch - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# OpenClaw Agent with Desearch - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/openclaw-agents

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
OpenClaw Agent with Desearch
OpenClaw Agent with Desearch

Desearch provides real-time search and web crawling capabilities for OpenClaw agents.

You can directly use our published skills on ClawHub and connect your agent to live external data using a single API key.

GitHub Repository (source of all skills):
https://github.com/Desearch-ai/desearch-openclaw-skills

Available Skills on ClawHub
🔎 AI Search

https://clawhub.ai/okradze/desearch-ai-search

AI-powered multi-source search aggregating results from:

Web
X
Reddit
Hacker News
YouTube
ArXiv
Wikipedia

Returns summarized answers or curated links for agent workflows.

𝕏 X Search

https://clawhub.ai/okradze/desearch-x-search

Real-time X search supporting:

Keyword search
User timelines
Replies
Retweeters
Date filters
Engagement filters
Sorting options

Built for monitoring and live social intelligence agents.

🌐 Web Search

https://clawhub.ai/okradze/desearch-web-search

Real-time SERP-style web search returning:

Titles
URLs
Snippets

Designed for fast discovery before deeper analysis.

🕷️ Web Crawl

https://clawhub.ai/okradze/desearch-crawl

Crawl any webpage and extract:

Clean text
Raw HTML

Useful for deep content extraction and structured processing.

Requirements

To use these skills inside OpenClaw, you need a Desearch API key.

Generate your key at:
https://console.desearch.ai

Set the environment variable in your OpenClaw environment:

BASH
export DESEARCH_API_KEY='your-key-here'

Once defined, your agent can immediately start using any of the above skills.

Typical Agent Use Cases
Research agents requiring live context
Social monitoring agents using X data
RAG systems that need fresh external knowledge
Fact validation pipelines
Autonomous knowledge extraction workflows
How It Works
OpenClaw Agent → Desearch Skill (ClawHub) → Desearch API → Real-time external data sources

Desearch acts as a decentralized search layer designed specifically for AI agents.

Resources

For full technical details, parameters, and examples, refer to:

Individual skill pages on ClawHub
GitHub repository: https://github.com/Desearch-ai/desearch-openclaw-skills
API documentation at https://desearch.ai
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
