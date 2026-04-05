<!--
source: https://desearch.ai/docs/guide/apis/authorization
title: Authorization - APIs Documentation | Desearch
captured: 2026-04-04
-->
# Authorization - APIs Documentation | Desearch

Source: https://desearch.ai/docs/guide/apis/authorization

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
Authorization

To access the Desearch API, you must include your API key in the request header for authentication. All API endpoints are authenticated using tokens.

Use the following format to add the authorization header to your API Requests.

JSON
'Authorization': '<your token>'

To access the Desearch API, you must authenticate your requests using an API key that was generated as defined here. This key grants secure access and ensures proper authorization for each API call. All API endpoints require authentication via tokens.

Authentication Method

Include your API key in the request header using the Authorization header. The correct format is as below.

CURL
curl --location 'https://api.desearch.ai/desearch/ai/search' \
    --header 'Authorization: dt_$UZA25rX0jLD654y7AGswWvqABCeJHFiCLqqBWPF6abc' \
    --header 'Content-Type: application/json' \
    --data '{
    "date_filter": "PAST_24_HOURS",
    "model": "NOVA",
    "prompt": "Latest TAO trends",
    "streaming": true,
    "tools": [
        "Twitter Search"
    ]
    }'
PYTHON
import requests
    url = "https://apis.datura.ai/desearch/ai/search"
    headers = {
        "Authorization": "dt_$YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "date_filter": "PAST_24_HOURS",
        "model": "NOVA",
        "prompt": "Washington Crash",
        "response_order": "SUMMARY_FIRST",
        "streaming": True,
        "tools": ["Twitter Search"]
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.json())

    const fetch = require('node-fetch');

    const url = "https://apis.datura.ai/desearch/ai/search";
    const headers = {
        "Authorization": "dt_$YOUR_API_KEY",
        "Content-Type": "application/json"
    };
    const data = JSON.stringify({
        "date_filter": "PAST_24_HOURS",
        "model": "NOVA",
        "prompt": "Washington Crash",
        "response_order": "SUMMARY_FIRST",
        "streaming": true,
        "tools": ["Twitter Search"]
    });

    fetch(url, {
        method: "POST",
        headers: headers,
        body: data
    })
    .then(response => response.json())
    .then(result => console.log(result))
    .catch(error => console.error("Error:", error));

❗️ Securing API Key

Keep your API key confidential and do not expose it in client-side code.

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
