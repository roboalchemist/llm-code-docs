# Source: https://docs.xano.com/xanoscript/triggers.md

# Source: https://docs.xano.com/building/logic/triggers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Triggers

> Triggers are workflows that can run based on other events that happen in your workspace.

<Tip>
  Before continuing, make sure you're familiar with:

  * [Core Components](/building/logic/core-components)
  * [Working with Data](/building/logic/working-with-data)

  You'll also want to make sure you've already built something to apply triggers to.
</Tip>

Triggers in Xano are workflows that will run only when triggered by another event. You can build triggers for the following events:

* Database Operations
  * Adding records
  * Editing records
  * Deleting records
  * Truncating records (clearing the table)

* Realtime Events
  * When a user attempts to join a channel
  * When a user sends a message to a channel

* Workspace Events
  * When a branch is merged
  * When a branch is changed to live
  * When a new branch is created

* MCP Server Connections
  * When a connection is made to an MCP server

For more information on each type of trigger and how to build them, see the following pages:

<Columns col={2}>
  <Card title="Database Triggers" icon="database" href="/building/logic/triggers/database" />

  <Card title="Realtime Triggers" icon="messages" href="/building/logic/triggers/realtime" />

  <Card title="Workspace Triggers" icon="objects-column" href="/building/logic/triggers/workspace" />

  <Card title="MCP Server Triggers" icon="server" href="/building/logic/triggers/mcp-servers" />

  <Card title="AI Agent Triggers" icon="robot" href="/building/logic/triggers/ai-agent" />
</Columns>


Built with [Mintlify](https://mintlify.com).