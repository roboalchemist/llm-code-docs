# Source: https://docs.apify.com/platform/integrations/skyfire.md

# Agentic payments with Skyfire

Agentic payments enable AI agents to autonomously run Apify Actors using third-party payment providers, without requiring traditional Apify user accounts. This allows agents to discover, execute, and pay for web scraping and automation tasks independently.

Apify supports agentic payments through *Skyfire*, a payment network specifically designed for AI agents.

Experimental feature

Keep in mind that agentic payments are an experimental feature and may undergo significant changes considering the rapid evolution of payment protocols and AI technologies.

## What is Skyfire?

https://skyfire.xyz/ is a payment network built specifically for AI agents, enabling autonomous transactions with digital wallets and spending controls. It provides the infrastructure necessary for agents to make payments on behalf of users, allowing autonomous AI-driven workflows.

With Skyfire integration, agents can discover available Apify Actors, execute scraping and automation tasks, and pay for services using pre-funded Skyfire tokens, all without human intervention.

## Using Skyfire with Apify MCP Server

The https://docs.apify.com/platform/integrations/mcp provides the simplest way for agents to access Apify's Actor library using Skyfire payments.

### Prerequisites

Before using agentic payments through MCP, you need:

1. *A Skyfire account* with a funded wallet - https://app.skyfire.xyz/
2. *An MCP client* that supports multiple server connections, such as https://opencode.ai/, https://claude.com/download with MCP support, or other compatible clients
3. *Both MCP servers configured*: Skyfire's MCP server and Apify's MCP server

### Configuration

Configure your MCP client to connect to both the Skyfire and Apify MCP servers. When connecting to the Apify MCP server for agentic payments, you must include the `?payment=skyfire` query parameter in the server URL. This enables the agentic payment flow and informs the agent about payment requirements.


```
https://mcp.apify.com?payment=skyfire
```


* OpenCode
* Claude Desktop

If you're using https://opencode.ai/, add this configuration to your `opencode.json` file (refer to https://opencode.ai/docs/config/ for file location on your system):


```
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "skyfire": {
      "enabled": true,
      "type": "remote",
      "url": "https://mcp.skyfire.xyz/mcp",
      "headers": {
        "skyfire-api-key": "YOUR_SKYFIRE_API_KEY"
      }
    },
    "apify": {
      "enabled": true,
      "type": "remote",
      "url": "https://mcp.apify.com?payment=skyfire"
    }
  }
}
```


If you're using https://claude.com/download, add this configuration to your `claude_desktop_config.json` file (refer to https://modelcontextprotocol.io/docs/develop/connect-local-servers for file location on your system) and restart the application:


```
{
  "mcpServers": {
    "skyfire": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.skyfire.xyz/mcp",
        "--header",
        "skyfire-api-key: YOUR_SKYFIRE_API_KEY"
      ]
    },
    "apify": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.apify.com?payment=skyfire"
      ]
    }
  },
  "isUsingBuiltInNodeForMcp": true
}
```


Replace `YOUR_SKYFIRE_API_KEY` with Skyfire buyer API key, which you can obtain from your https://app.skyfire.xyz/.

### How it works

When an agent uses the Apify MCP server with Skyfire payments, the workflow proceeds as follows:

1. The agent searches for suitable Actors using the search tools or works with pre-loaded Actors.
2. When attempting to run an Actor, the agent recognizes the need for a Skyfire PAY token with a minimum of $5 and calls the Skyfire MCP server to create it.
3. The agent calls the Actor tool with the payment token.
4. The Apify platform validates the token and starts the Actor run.
5. The Actor does the work and delivers results.
6. When the run completes, the agent receives the Actor results and can retrieve additional data if needed.
7. Finally, Apify's billing system charges the Skyfire PAY token for the actual usage cost.

Any unused funds remain available in the token for future runs or are returned to your Skyfire wallet when the token expires. This means you will not lose money if the actual usage is less than the $5 minimum.

![The flow](/assets/images/skyfire-apify-agentic-flow-8e2a4fdfa231b55b0dfc103ceaad0f88.png)

### Pre-loading Actors

For more predictable workflows, you can pre-load specific Actors when connecting to the MCP server by adding them to the URL:


```
https://mcp.apify.com?payment=skyfire&tools=actor1,actor2,actor3
```


Replace `actor1,actor2,actor3` with the actual Actor IDs you want to make available, such as `junglee/free-amazon-product-scraper,streamers/youtube-scraper`. See which Actors .

### Actor discovery

When not pre-loading Actors, agents can discover suitable Actors dynamically using the search tools. The search automatically filters results to show only Actors that support agentic payments.

## Using Skyfire with Apify API

For direct API integration, you can use Skyfire PAY tokens to authenticate and pay for Actor runs.

Handled by MCP

The MCP client handles these operations automatically when using Skyfire PAY tokens.

### Authentication

Instead of using a traditional Apify API token, pass your Skyfire PAY token in the request header:


```
skyfire-pay-id: YOUR_SKYFIRE_PAY_TOKEN
```


### Running an Actor

Make a standard Actor run request to the https://docs.apify.com/api/v2#/reference/actors/run-collection/run-actor, but include the Skyfire PAY token in the header.

Example of using the synchronous run endpoint


```
curl -X POST \
  'https://api.apify.com/v2/acts/ACTOR_ID/run-sync' \
  -H 'skyfire-pay-id: YOUR_SKYFIRE_PAY_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "input": {
      "your": "input"
    }
  }'
```


You can also use the asynchronous https://docs.apify.com/api/v2#/reference/actors/run-collection/run-actor if you don't need to wait for results immediately.

### Retrieving results

After your Actor run completes, you can retrieve results using the https://docs.apify.com/api/v2#/reference/datasets or https://docs.apify.com/api/v2#/reference/key-value-stores. Include the same `skyfire-pay-id` header to authenticate these requests.

### Supported Actors

Not all Actors in the Apify Store can be run using agentic payments.

Apify maintains a curated list of Actors approved for agentic payments. To check if an Actor supports agentic payments, use the `allowsAgenticUsers=true` query parameter when https://docs.apify.com/api/v2#/reference/store/store-actors-collection/get-list-of-actors-in-store.


```
https://api.apify.com/v2/store?allowsAgenticUsers=true
```


### Payment requirements

Your Skyfire PAY token must have at least *$5* available to run Actors. However, you will only be charged for actual usage. If an Actor run costs less than 5$, the unused funds remain available in your token for future runs or return to your Skyfire wallet when the token expires.

### Unsupported features

The following operations are not supported with agentic payments:

* Schedule creation or management
* Standby run initiation
* Integration setup such as webhooks to external services
* Actor resurrection after the payment token has been settled

## Resources

* **https://docs.apify.com/platform/integrations/mcp** - Complete guide to using the Apify MCP server
* **https://skyfire.xyz/** - Official Skyfire guides and API reference
* **https://docs.apify.com/api/v2** - Complete API documentation for direct integration
* **https://docs.apify.com/platform/actors/development/permissions** - Understanding Actor permission levels
