# Source: https://docs.statsig.com/integrations/mcp/chatgpt-connector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Statsig ChatGPT App

> Learn how to talk directly to Statsig from within OpenAI's ChatGPT.

## Overview

You can set up a ChatGPT App (built on top of the Statsig MCP server), allowing you to query experiments, manage feature flags, explore analytics -- all directly within OpenAI's ChatGPT conversational interface.

## Installation

1. Navigate to the Statsig App in the ChatGPT Apps Directory [here](https://chatgpt.com/apps/statsig/asdk_app_6967f065ac9481918969c660ff7686e9).
2. Click "Connect" and "Continue" to complete OAuth for your Statsig project.
   <Note>
     ChatGPT App OAuth only supports Personal Console API Keys. Ensure your
     Statsig org owner has enabled Personal Console API Keys creation for your
     role [here](https://console.statsig.com/settings?tab=organization){" "}
   </Note>
   <img src="https://mintcdn.com/statsig-4b2ff144/0Bw8hThvo5QsdxM6/images/integrations/mcp/statsig-chatgpt-app-listing.png?fit=max&auto=format&n=0Bw8hThvo5QsdxM6&q=85&s=d083bbed220d44a4649cbb73a5f708c7" alt="Statsig listing in the ChatGPT Apps Directory" className="w-full rounded-lg border border-gray-200 dark:border-gray-800" width="1684" height="1250" data-path="images/integrations/mcp/statsig-chatgpt-app-listing.png" />

## Using Statsig MCP within ChatGPT

With Statsig MCP configured in ChatGPT, you can:

* **Explore Experiments**: "List all my active experiments"
* **Manage Gates**: "What gates are currently stale?"
* **Configure Dynamic Configs**: "Show me the configuration for the dynamic config 'dynamic-config'"
* **Get Insights**: "Show me details about the experiment called 'new-checkout-flow'"

## Next Steps

After installation, you can:

* List experiments, gates, and dynamic configs
* Create and update experiments, gates, and configs
* Access your Statsig data directly from Codex

For more information about available MCP capabilities, see the [MCP capabilities](/integrations/mcp#current-mcp-capabilities) section.


Built with [Mintlify](https://mintlify.com).