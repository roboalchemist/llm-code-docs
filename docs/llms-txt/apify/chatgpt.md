# Source: https://docs.apify.com/platform/integrations/chatgpt.md

# ChatGPT integration

**Learn how to integrate Apify Actors with ChatGPT to provide web context in real-time.**

***

The *ChatGPT* integration enables you to connect ChatGPT to Apify's extensive library of https://apify.com/store through the https://modelcontextprotocol.io/docs/getting-started/intro. This allows ChatGPT to access real-time web data and automation capabilities by using Apify tools directly in conversations. By default, the Apify MCP server exposes a set of tools that let you search and run any Actor you have access to, including all public Actors and rental Actors you have rented.

*Example query*: "Find and run an Actor that scrapes Instagram profiles and gets the profile of @natgeo"

In this tutorial, you'll learn how to connect *ChatGPT* to the *Apify MCP server* using a custom connector.

## Prerequisites

Before connecting ChatGPT to Apify, you'll need:

* *An Apify account* - If you don't have an Apify account already, you can https://console.apify.com/sign-up
* *Apify API token* - Get your API token from the **Integrations** section in https://console.apify.com/account#/integrations. This token authorizes the MCP server to run Actors on your behalf. Make sure to keep it secure.
* *An OpenAI account with access to ChatGPT* - You need an OpenAI account to use ChatGPT.
* *ChatGPT with Developer mode enabled* - You must enable https://platform.openai.com/docs/guides/developer-mode to add custom connectors (when the Developer mode is active, the message input box is outlined in orange).

## Create an MCP connector

1. In ChatGPT, go to **Settings > Apps & Connectors > Create**. If you don't see the **Create** button, enable Developer mode or reload the page.

2. Fill in the following fields:

   * **Name** – a user-facing title, e.g., `apify-mcp`

   * **Description** – a short description of what the connector does

   * **MCP Server URL** – choose one of the following:

     <!-- -->

     * `https://mcp.apify.com` - use the default set of Apify tools
     * `https://mcp.apify.com?tools=actors,docs,mtrunkat/url-list-download-html` - use specific tools
     * Refer to https://mcp.apify.com for details

   * **Authentication** – OAuth, you don’t need to provide a client ID or secret.

3. Select **Create** to proceed to the authentication page. You’ll be redirected to the Apify website to authorize ChatGPT to access your Apify account.

![ChatGPT Create connection](/assets/images/chatgpt-connector-34503d19858fd26769e1118c0420e35b.png)

Once authorized, you'll return to ChatGPT and see a success message with a list of tools available from the Apify MCP server.

Cannot modify tools after creation

ChatGPT does not allow modifying the selected tools after the connector is created. If you need to add or remove tools later, you'll need to create a new connector.

## Try the MCP connector in ChatGPT

Once your connector is ready:

1. Open a **new chat** in ChatGPT.

2. Click the **+** button near the message composer and select **More**.

3. Choose your **Apify MCP connector** to add it to the conversation.

4. Ask ChatGPT to use Apify tools, for example:

   > “Search the web and summarize recent trends in AI agents”

You’ll need to grant permission for each Apify tool when it’s used for the first time. You should see ChatGPT calling Apify tools — such as the https://apify.com/apify/rag-web-browser — to gather information.

![ChatGPT Apify tools](/assets/images/chatgpt-with-rag-web-browser-27398b335899c31c3ee69f9fac9982c3.png)

## Limitations

* MCP integration in ChatGPT is still in *beta* and may have some limitations or bugs.
* Tool selection and execution can be *slow*, especially with the latest GPT models.
* *Custom connectors* are only available in ChatGPT *Developer mode*.
* When creating connectors that include social media scrapers (Instagram, TikTok), OpenAI may display a *Safety Scan* warning indicating that some tools might fetch sensitive data.

## Related integrations

* https://docs.apify.com/platform/integrations/openai-assistants.md - Use Apify Actors with OpenAI Assistants API via function calling
* https://docs.apify.com/platform/integrations/openai-agents.md - Integrate Apify MCP server with OpenAI Agents SDK

## Resources

* https://platform.openai.com/docs/guides/developer-mode - Learn how to enable Developer Mode in ChatGPT
* https://platform.openai.com/docs/guides/tools-connectors-mcp - Official OpenAI documentation on using MCP servers with ChatGPT
* https://mcp.apify.com - Interactive configuration tool for the Apify MCP server
* https://docs.apify.com/platform/integrations/mcp.md - Complete guide to using the Apify MCP server
