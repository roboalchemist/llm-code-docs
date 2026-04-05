<!--
source: https://desearch.ai/docs/guide/integrations/elizaos-agents
title: ElizaOs Agents with Desearch - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# ElizaOs Agents with Desearch - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/elizaos-agents

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
ElizaOs Agents with Desearch

plugin-desearch is a plugin for ElizaOS that adds powerful AI and web search capabilities powered by the Desearch API.

In this guide, you'll learn how to:

Install and configure the Desearch plugin
Use Desearch-powered actions in your agents
Trigger AI search tasks for Twitter and the web
🚀 ElizaOS + Desearch Plugin Example: Research Assistant

This example sets up an ElizaOS agent that gathers Twitter and web insights on any topic.

1. Install the Plugin

Use your preferred package manager:

BASH
pnpm install plugin-desearch
# or
npm install plugin-desearch

## Set Your API Key

Add your Desearch API key in your .env file:

ENV
DESEARCH_API_KEY=your_desearch_api_key

Make sure your ElizaOS runtime loads environment variables correctly.

1. Register the Plugin

Import and register the plugin inside your ElizaOS config:

TS
import desearchPlugin from "plugin-desearch";

export default {
    plugins: [desearchPlugin],
    // ... other configuration
};

1. Available Actions

Once the plugin is registered, your agent can access these actions:

| Action Name | Description |
|---|---|
| AI_SEARCH | AI-powered multi-platform search |
| TWITTER_LINKS_SEARCH | AI-assisted search for Twitter links |
| WEB_LINKS_SEARCH | AI-assisted search for web links |
| TWITTER_SEARCH | Keyword search on X (Twitter) |
| TWEET_BY_ID | Get tweet details by ID |
| TWEET_BY_USER | Search a user's tweets by query |
| LATEST_TWEET | Fetch latest tweets from a user |
| WEB_SEARCH | Standard web search |

1. Example Prompts
AI Search
User: Can you perform a search for the latest AI advancements? Agent: Sure, let me perform an AI-powered search for the latest AI advancements. User: Find recent research papers on machine learning. Agent: I'll search for recent research papers on machine learning.
Twitter Link Search
User: Can you find Twitter links related to AI advancements? Agent: Sure, let me find some Twitter links related to AI advancements. User: Search for Twitter discussions on machine learning. Agent:I'll search for Twitter discussions on machine learning.
Web Link Search
User: Can you find web links related to AI advancements? Agent: Sure, let me find some web links related to AI advancements. User: Search for web articles on machine learning. Agent: I'll search for web articles on machine learning.
Twitter Search
User: Search for tweets on machine learning. Agent: I'll search for tweets on machine learning.
Twitter URL Search
User: https://twitter.com/user/status/1234567890 Agent: Sure, let me fetch tweets from the provided URLs.
Twitter By Id Search
User: Search by tweet id? 5544332211 Agent: Let me fetch tweet by id.
Tweet By User Search
User: Search tweets for Elonmusk Agent: Sure, let me search for tweets related to 'Elonmusk'.
Web Search
User: Can you find web contents related to AI advancements? Agent: Sure, let me search for web content related to AI advancements.

1. Troubleshooting
Missing API Key: Ensure DESEARCH_API_KEY is set in your environment.
Rate Limits: Slow down your requests or upgrade your Desearch plan.
API Errors: Review logs; the plugin handles and reports Desearch errors cleanly.
🔧 Action Interface

All actions implement ElizaOS’s Action interface:

TS
interface Action {
    name: string;
    description: string;
    validate: (runtime: IAgentRuntime) => Promise<boolean>;
    handler: (
        runtime: IAgentRuntime,
        message: Memory,
        state: State,
        options: any,
        callback: HandlerCallback
    ) => Promise<boolean>;
    examples: ActionExample[][];
}

This makes the plugin fully extensible and override-friendly.

🔐 Security Best Practices
Store DESEARCH_API_KEY securely using .env or secrets manager
Never hard-code or commit secrets
Validate all input passed to Desearch actions
Handle API limits and errors gracefully in your flows
✅ Summary

The plugin-desearch plugin lets ElizaOS agents perform real-time, AI-powered searches across the web and social media.

It’s perfect for agents that:

Research live trends
Extract tweet info
Search the web for articles, tools, or docs
Build live digests and alerts
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
