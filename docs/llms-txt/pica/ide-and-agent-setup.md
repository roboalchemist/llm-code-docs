# Source: https://docs.picaos.com/get-started/ide-and-agent-setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IDE and Agent Setup

> Configure your AI-powered IDE to build faster with Pica's MCP server and documentation indexing

Optimize your development environment to build with integrations faster. This guide shows you how to configure AI-powered IDEs to leverage Pica's MCP server and documentation.

<Tabs>
  <Tab title="Cursor" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/cursor.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=15834048a0a2eec7556d98df5fe97a10" width="66" height="66" data-path="images/cursor.svg">
    Cursor is an AI-powered code editor that can significantly accelerate your development with Pica. Follow these steps to set it up optimally.

    ### Install the Pica MCP Server

    The Model Context Protocol (MCP) server gives Cursor direct access to Pica's integration knowledge and request-building capabilities. With the MCP server installed, you can prompt Cursor to construct integration requests based on your specific needs.

    <Steps>
      <Step title="Open MCP Settings">
        In Cursor, open the MCP Settings panel from the settings menu.
      </Step>

      <Step title="Add the Pica MCP Server">
        Add the following configuration to your MCP settings:

        ```json  theme={null}
        {
          "mcpServers": {
            "pica": {
              "command": "npx",
              "args": [
                "@picahq/mcp"
              ],
              "env": {
                "PICA_SECRET": "your-api-key"
              }
            }
          }
        }
        ```

        Replace `your-api-key` with your actual [Pica API key](https://app.picaos.com/settings/api-keys).
      </Step>

      <Step title="Verify setup">
        Once configured, Cursor can now construct Pica integration requests for you. Just describe what you want to build in natural language.

        <Frame caption="MCP Settings in Cursor">
          <img src="https://mintcdn.com/pica-236d4a1e/gaxAkxyaf6yTtwaj/images/ide-setup/mcp-settings.png?fit=max&auto=format&n=gaxAkxyaf6yTtwaj&q=85&s=db15f3b0c43f105dd71c8adfc391283b" alt="MCP Settings in Cursor" width="2670" height="1694" data-path="images/ide-setup/mcp-settings.png" />
        </Frame>
      </Step>

      <Step title="Example Prompts">
        Here are some examples of what you can ask Cursor to build with Pica:

        **Check your connections**

        * What connections do I have in my Pica account?
        * Do I have a connection to Google Calendar?

        **Fetch data from integrations**

        * Add an endpoint that uses Pica to fetch the list of contacts from Salesforce
        * Using Pica, add an endpoint that fetches the list of invoices from QuickBooks and displays them in a table
        * Build a paginatable table component that fetches and displays QuickBooks invoices with search and sort using Pica

        **Send data to integrations**

        * When my form is submitted, use Pica to send an email using Gmail
        * Using Pica, create a new lead in HubSpot when a user signs up
        * Create a page with a form that can post messages to multiple Slack channels with message scheduling using Pica

        **Query Pica knowledge**

        * What fields are available when to create a QuickBooks invoice?
        * What's the response schema for listing my HubSpot contacts?
        * What are the filter options for fetching Gmail emails?

        <Tip>
          The MCP server has access to all integration schemas, authentication patterns, and edge cases. The more specific your prompt, the better the generated code.
        </Tip>
      </Step>
    </Steps>

    ### Index Pica Documentation

    Cursor can index external documentation, making it easy to ask questions about Pica and get contextual answers while you code.

    <Steps>
      <Step title="Open Codebase Indexing Settings">
        1. Open Cursor Settings (`Cmd/Ctrl + ,`)
        2. Navigate to **Features** → **Codebase indexing**
      </Step>

      <Step title="Add Pica Documentation">
        Add the Pica documentation URL to your indexed sources:

        ```
        https://docs.picaos.com
        ```

        <Frame>
          <img src="https://mintcdn.com/pica-236d4a1e/gaxAkxyaf6yTtwaj/images/ide-setup/cursor-indexing.png?fit=max&auto=format&n=gaxAkxyaf6yTtwaj&q=85&s=0cbead3feceba9ede8a5a4a2fe13e5ba" alt="Documentation indexing in Cursor" width="2670" height="1696" data-path="images/ide-setup/cursor-indexing.png" />
        </Frame>
      </Step>

      <Step title="Verify setup">
        Once indexed, Cursor will have access to the documentation. You can now ask questions about Pica directly in the chat.
      </Step>

      <Step title="Example Questions">
        Here are some examples of questions you can ask:

        * What can Pica help me do?
        * How can I add AuthKit to my app?
        * What API can I use to list the available connections I have in my Pica account?
        * What is the Passthrough API?

        <Info>
          Documentation indexing works alongside the MCP server. Use the MCP server to build integration features, and use documentation indexing to learn about Pica's products and APIs.
        </Info>
      </Step>
    </Steps>
  </Tab>
</Tabs>

## What's next?

<CardGroup cols={2}>
  <Card title="Connect your first integration" icon="plug" href="/get-started/quickstart">
    Follow the quickstart to connect Gmail and make your first request
  </Card>

  <Card title="Browse integration examples" icon="book" href="/use-cases/overview">
    See real-world examples of what you can build with Pica
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).