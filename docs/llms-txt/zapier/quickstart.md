# Source: https://docs.zapier.com/mcp/quickstart.md

# Quickstart

> Get up and running with Zapier MCP in 5 minutes

This guide will help you connect your AI assistant to Zapier MCP and run your first tool call. We'll use Claude as an example, but the process is similar for other MCP clients.

<Note>
  **Beta Status**: Zapier MCP is currently in beta and part of your existing
  [Zapier Plan](https://zapier.com/pricing).
</Note>

<Warning>
  **Enterprise Users**: Zapier MCP is not enabled by default on Enterprise
  accounts. If you'd still like to beta test Zapier MCP, reach out
  [here](https://mcpp.zapier.app/enterprise-access).
</Warning>

## Prerequisites

* A Zapier account ([sign up free](https://zapier.com/sign-up))
* An MCP-compatible AI client (Claude, Cursor, Windsurf, etc.)
* At least one app connected to your Zapier account

## Step 1: Create an MCP Server

First, let's create your MCP server in Zapier:

1. Go to [mcp.zapier.com](https://mcp.zapier.com)
2. Click **"+ New MCP Server"**
3. Select your AI client from the dropdown (e.g., "Claude")
4. Give your server a name (e.g., "My MCP Assistant")
5. Click **"Create MCP Server"**

You'll be taken to the configuration page for your new server.

## Step 2: Configure Your Tools

Now add the Zapier actions your AI can use:

1. Click **"+ Add tool"** to add your first tool
2. Type the name of an app (e.g., "Slack", "Google Sheets")
3. From the list of available actions, pick the action you want (e.g., "Send Channel Message", "Create Spreadsheet Row")
4. Connect your app account if prompted
5. Fill out any mandatory or optional fields for the action
   * You can let AI suggest values for certain fields
6. Click **"Save"**

Repeat this process for any other tools you want your AI to access.

## Step 3: Connect Your AI Client

Click on the **Connect** which will give you step by step instructions on how to configure your selected client. Each client has its own connection process and requirements. You can also select the "Other" Client in step 1 as a generic option and connect it with any MCP Client.

## Step 4: Test Your Connection

Once connected, test that everything is working:

1. Ask your AI: "What tools do I have available?"
2. Your AI should list the Zapier actions you configured
3. Try a simple command like: "Send a test message to #general in Slack" (If you have enabled the "Send Channel Message" in Slack)

## Step 5: Start Automating

Now you can use natural language to interact with your connected apps:

* "Add a row to my sales spreadsheet with today's numbers"
* "Create a task in Asana for the marketing team"
* "Search for recent emails from John"
* "Post a message to Discord announcing the meeting"

### Tips for Better Results

1. **Be Clear and Specific**
   * Include all necessary details in your request
   * Specify recipients, dates, and other important information

2. **Provide Context**
   * The clients can maintain context throughout a conversation
   * Reference previous messages: "Send that report to Sarah in Slack"

3. **Review Before Confirming**
   * The clients will often show you what it plans to do
   * You can ask for changes before execution

## Common Use Cases

### Personal Productivity

```text  theme={null}
"Check my unread emails from today and summarize the important ones"
"Create a reminder in Todoist to prepare for tomorrow's presentation"
"Add this week's expenses to my tracking spreadsheet"
```

### Team Collaboration

```text  theme={null}
"Post a message in #general about the server maintenance tonight"
"Create a meeting invite for the team sync next Monday at 2 PM"
"Update the project status in Notion to 'In Review'"
```

### Content Creation

```text  theme={null}
"Draft a blog post about AI productivity tips and save it to Google Docs"
"Schedule a tweet for tomorrow morning about our new feature"
"Create a new page in Confluence for the API documentation"
```

## Privacy & Security

### Data Handling

* Each client has their own Data and Usage Policies
* For Zapier, the Actions are logged in your MCP server's History tab
* No data is stored by Zapier unless required for the action

## Advanced Features

### Action Chaining

Have the LLM perform multiple actions in sequence:

```text  theme={null}
"Find all emails from clients today, summarize them, and create tasks for any that need follow-up"
```

### Conditional Logic

Have the LLM make decisions based on results:

```text  theme={null}
"Check if I have any meetings this afternoon. If not, schedule time for deep work"
```

### Data Transformation

Have the LLM process data between actions:

```text  theme={null}
"Get my recent expenses from the spreadsheet and create a summary report in Notion"
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="My AI can't see any Zapier tools">
    * Ensure you've completed the integration setup
    * Verify the Integration URL was entered correctly
    * Check that you've added at least one tool in your MCP server configuration
    * Make sure you're enabling the Zapier MCP connection in whatever client you are using
  </Accordion>

  <Accordion title="Actions fail with permission errors">
    * Verify you've authenticated the specific app in Zapier - Some apps require
      re-authentication periodically - Check the app's permissions in your Zapier
      account
  </Accordion>

  <Accordion title="My AI says it can't perform an action">
    * Make sure the specific action is configured in your MCP server
    * Some actions may have required fields - provide all necessary information
    * Check your [usage](/mcp/usage) limits
  </Accordion>
</AccordionGroup>

## Next Steps

* [Explore available clients](/mcp/clients) - Set up MCP with other AI assistants
* [Understand rate limits](/mcp/usage/overview) - Learn about beta limitations
* [Browse integrations](https://zapier.com/apps) - Discover what apps you can connect
* [Compare with Zapier Agents](https://zapier.com/agents) - Explore our no-code/no-setup alternative
