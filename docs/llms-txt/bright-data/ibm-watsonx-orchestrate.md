# Source: https://docs.brightdata.com/integrations/ibm-watsonx-orchestrate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IBM Watsonx Orchestrate

> Integrate Bright Data's powerful web scraping and data extraction capabilities into IBM watsonx Orchestrate using the MCP Server method.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

## Overview

This integration provides your agents with enterprise-grade capabilities for web scraping, and multi-engine search operations with bot protection bypass.

## Prerequisites

Before you begin, ensure you have:

* Access to IBM watsonx Orchestrate
* A Bright Data account with an active subscription
* Your Bright Data API token

## Steps to Get Started

<Steps>
  <Step title="Obtain Your Bright Data API Token">
    * Log in to your [Bright Data dashboard](https://brightdata.com/cp)
    * Navigate to [Account Settings](https://brightdata.com/cp/setting/users)
    * [Generate an API token](https://docs.brightdata.com/api-reference/authentication#how-do-i-authenticate-with-api-key%3F) if you haven't already
    * Copy and securely store your API token for the next steps
  </Step>

  <Step title="Open the Agent Toolset">
    * Navigate to **Manage Agents** in IBM watsonx Orchestrate
    * Select your agent
    * In the left menu, click **Toolset**
    * Click **Add Tool**

      <img src="https://mintcdn.com/brightdata/vHUxe1fKDakReg5j/images/Screenshot2025-10-20at10.12.52.png?fit=max&auto=format&n=vHUxe1fKDakReg5j&q=85&s=108d33b728f853c33b6230f1e3576f14" alt="Screenshot 2025-10-20 at 10.12.52.png" width="872" height="373" data-path="images/Screenshot2025-10-20at10.12.52.png" />
  </Step>

  <Step title="Add MCP Server Connection">
    In the "Add tool" dialog:

        <img src="https://mintcdn.com/brightdata/vHUxe1fKDakReg5j/images/Screenshot2025-10-20at10.14.58.png?fit=max&auto=format&n=vHUxe1fKDakReg5j&q=85&s=7fe409d207643a88b6c017d6a2769609" alt="Screenshot 2025-10-20 at 10.14.58.png" width="686" height="482" data-path="images/Screenshot2025-10-20at10.14.58.png" />

    * Select **Add from file or MCP server**
    * Choose **Import from MCP Server**
    * Fill in the configuration fields:
      * **Name**: Enter a descriptive name (e.g., `Bright Data MCP`)
      * **Connection**: Select `None`
      * **Install Command**: Enter the following, replacing `<your_api_token>` with your actual token:

    ```bash  theme={null}
    npx mcp-remote https://mcp.brightdata.com/sse?token=<your_api_token>
    ```

    * Click **Install** to initiate the connection
  </Step>

  <Step title="Enable Available Capabilities">
    Once installation completes, multiple capabilities will appear in your agent's toolset. Enable the following:

    `search_engine`

    `scrape_as_markdown`
  </Step>

  <Step title="Test Your Connection">
    Verify the integration is working:

    * Open your agent's chat interface
    * Ask the agent to perform a simple task (e.g., "Search for recent AI trends")
    * Confirm the agent successfully retrieves and processes data from Bright Data
  </Step>
</Steps>

## What's Next

Your agent is now connected to Bright Data and ready to:

* Extract structured data from major platforms
* Perform geo-targeted web searches
* Scrape website content while bypassing bot protection
* Process large-scale data extraction tasks

## Support

Need help? Contact Bright Data support or refer to the [Bright Data documentation](https://docs.brightdata.com) for detailed API references and troubleshooting guides.
