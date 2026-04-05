<!--
source: https://desearch.ai/docs/guide/integrations/mcp
title: MCP - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# MCP - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/mcp

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
MCP

A Model Context Protocol (MCP) server lets clients like Claude or Cursor use the Desearch AI for real-time AI X search and web search.

Tools

The Desearch MCP server includes the following tools:

AI Search: Performs real-time AI Twitter and web searches with relevant links and summary.
X Search: Real-time tweet search on X.
Prerequisites 📋
An Desearch API Key
Node.js (v18 or higher)
Claude Desktop installed
Cursor IDE
Installation 🛠️
NPM Installation
BASH
npm install -g desearch-mcp-server

## Using Smithery

To install the Desearch MCP server for Claude Desktop automatically via Smithery:

BASH
npx -y @smithery/cli install @Desearch-ai/desearch --client claude

Or for Cursor IDE:

BASH
npx -y @smithery/cli install @Desearch-ai/desearch --client cursor

## Configuration

### Configure Cursor IDE to run the Desearch MCP server

Open Cursor IDE, access command palette Cmd+Shift+P or Ctrl+Shift+P, and search for Open MCP Settings. Click on Add new global MCP server to open the mcp.json file.

### Add the Desearch server configuration
JSON
{
    "mcpServers": {
        "desearch": {
            "command": "desearch-mcp-server",
            "env": {
                "DESEARCH_API_KEY": "your-api-key"
            }
        }
    }
}

Replace your-api-key with your actual Desearch API key from console.desearch.ai/api-keys.

### Restart Cursor IDE

For the changes to take effect:

- Completely quit Cursor IDE
- Start Cursor IDE again

### Configure Claude Desktop to run the Desearch MCP server

Open the Claude Desktop app and enable Developer Mode from the top-left menu bar.

Once enabled, open Settings (also from the top-left menu bar) and navigate to the Developer Option, where you'll find the Edit Config button. Clicking it will open the claude_desktop_config.json file, allowing you to make the necessary edits.

OR (if you want to open claude_desktop_config.json from terminal)

**For macOS:**

Open your Claude Desktop config:

BASH
code ~/Library/Application\ Support/Claude/claude_desktop_config.json

**For Windows:**

Open your Claude Desktop configuration:

POWERSHELL
code %APPDATA%\Claude\claude_desktop_config.json

### Add the Desearch server configuration
JSON
{
    "mcpServers": {
        "desearch": {
            "command": "desearch-mcp-server",
            "env": {
                "DESEARCH_API_KEY": "your-api-key"
            }
        }
    }
}

Replace your-api-key with your actual Desearch API key from console.desearch.ai/api-keys.

### Restart Claude Desktop

For the changes to take effect:

- Completely quit Claude Desktop
- Start Claude Desktop again

You can verify the server by checking status in Settings > Developer > desearch

## Troubleshooting

### Common Issues

### Server Not Found

- Check Claude or Cursor Desktop configuration syntax
- Ensure Node.js is installed

### API Key Issues

- Confirm your DESEARCH_API_KEY is valid
- Check the DESEARCH_API_KEY is correctly set in the Cursor or Claude Desktop config
- Verify that there are no spaces around the API key

### Connection Issues

- Restart Claude Desktop or Cursor IDE completely
- Check Claude Desktop logs:

BASH
# macOS
tail -n 50 -f ~/Library/Logs/Claude/mcp*.log

# Windows
type "%APPDATA%\Claude\logs\mcp*.log"
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
