<!--
source: https://desearch.ai/docs/guide/apis/api-keys
title: API Keys - APIs Documentation | Desearch
captured: 2026-04-04
-->
# API Keys - APIs Documentation | Desearch

Source: https://desearch.ai/docs/guide/apis/api-keys

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
API Keys

Learn how to create and manage API keys for authenticating your requests in the section below. To create an API key, you must have an account on the Desearch console.

Create an API Key

1. Sign Up / Log In

   Visit the Desearch Console [https://console.desearch.ai/](https://console.desearch.ai/) and log in to your account. If you don’t have an account, create one first.

2. Navigate to API Keys

   After logging in to the Desearch Console, go to the API Keys page.

3. Generate New Key

   - Click on the “Generate API Key” button.
   - Give your key a name for easy identification.
   - Click on the “Generate” button to create the key.
   - Copy the key immediately and store it securely. You will not be able to see it again.

❗️ Securing your API Key

Keep your API key confidential. Do not share it publicly or expose it in client-side code. If compromised, it could result in unauthorized access to your account

API keys are essential for authenticating requests to Desearch’s API. They ensure secure access and help manage usage limits. Follow this guide to create and use your API key effectively.

Using Your API Key

To authenticate requests, include your API key in the Authorization header.

CURL
curl --location 'https://api.desearch.ai/desearch/ai/search' \
  
\--header 'Authorization: dt_$UZA25rX0jLD654y7AGswWvqABCeJHFiCLqqBWPF6abc' \
\--header 'Content-Type: application/json' \
\--data '{
  "date_filter": "PAST_24_HOURS",
  "model": "NOVA",
  "prompt": "Latest TAO trends",
  "streaming": true,
  "tools": [
    "Twitter Search"
  ]
}'
Managing Your API Key

Regenerate Key: If your key is compromised, revoke it and generate a new one.

Delete Key: Remove unused keys to enhance security.

📘 Important API Key Security Practices

✅ Keep your API key secret.

✅ Use environment variables to store keys securely.

✅ Implement rate limiting and monitoring for API usage.

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
