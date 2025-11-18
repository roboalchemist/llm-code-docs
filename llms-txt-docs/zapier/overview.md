# Source: https://docs.zapier.com/platform/build-cli/overview.md

# Source: https://docs.zapier.com/mcp/usage/overview.md

# Usage & Billing Overview

> Understand how Zapier MCP usage works, rate limits, and pricing during beta

Zapier MCP provides access to thousands of apps and actions through the Model Context Protocol. This guide explains how usage is tracked, what limits apply, and how billing works.

<Note>
  **Beta Status**: Zapier MCP is currently in beta and part of your existing
  [Zapier Plan](https://zapier.com/pricing).
</Note>

## Key Concepts

### What counts as a tool call?

A **tool call** in Zapier MCP is any operation that interacts with an external app:

* ✅ Sending a Slack message
* ✅ Creating a Google Sheets row
* ✅ Searching for emails in Gmail
* ✅ Creating a task in Asana
* ❌ Asking what tools are available
* ❌ Getting help or documentation
* ❌ Failed tool calls due to configuration errors

## Tool Call Quota

MCP tool calls use tasks from an end-users' Zapier account. One MCP tool call uses 2 tasks. [Contact us](https://zapier.com/developer-platform#form) about sponsoring tasks for your users to reduce friction.

Interested in piloting developer tools for deeper integration? [Contact our team](https://mcpp.zapier.app/waitlist).

<Warning>
  **Enterprise Users**: Zapier MCP is not enabled by default on Enterprise
  accounts. If you'd still like to beta test Zapier MCP, reach out
  [here](https://mcpp.zapier.app/enterprise-access).
</Warning>

## How Usage is Calculated

### How is Zapier MCP priced?

Zapier MCP is available to all accounts. One Zapier MCP tool call uses **two tasks** from your Zapier plan’s quota. If you would like more tasks, explore [Zapier plans here.](https://zapier.com/pricing)

### What uses a tool call?

Each successful API call to an external service counts as one tool call:

```text  theme={null}
Examples that use 1 tool call each:
- "Send a message to Slack"
- "Create a row in Google Sheets"
- "Find contacts in HubSpot"
- "Update a Notion page"
```

### What doesn't use a tool call?

These operations are free and don't count against your limit:

* Listing available tools
* Authentication and setup
* Viewing action history
* Failed tool calls due to:
  * Invalid authentication
  * Missing required fields
  * Configuration errors

### Batch Operations

Some operations may use multiple tool calls:

```text  theme={null}
"Add 5 rows to a spreadsheet" = 5 tool calls
"Send emails to 3 people" = 3 tool calls
"Search and update 10 records" = 11 tool calls (1 search + 10 updates)
```

## Monitoring Your Usage

### Check Current Usage

Visit [mcp.zapier.com](https://mcp.zapier.com) to see usage across all servers.
<img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/mcp/usage.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=7de5553096e4d9e4ba8fb117d22d8b35" alt="Usage" data-og-width="502" width="502" data-og-height="318" height="318" data-path="images/mcp/usage.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/mcp/usage.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=fb143d1ce159d30752ec521623b5a5d4 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/mcp/usage.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ede549ad6c1d4130fe8b389993529aa6 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/mcp/usage.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=99e6bfc5481839d1cc61409bc33cf8e2 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/mcp/usage.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=893054f8a485ab25a48f487547dfe35d 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/mcp/usage.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=91ad1d42b2b9cde8a5bba4f67f1099ea 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/mcp/usage.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=18e20e9baccba9eca706a19a588bb5b2 2500w" />

### Usage Notifications

Zapier will notify you when you run out of Zapier Tasks. An error message will be returned to attempted tool calls.

## What Happens at the Limit?

When you reach any rate limit:

1. **Immediate Effect**: New tool call requests will be declined
2. **Error Message**: Your AI client will receive an error about the limit exceeded

### Options When You Hit the Limit

<Tabs>
  <Tab title="Wait for Reset">
    Tasks reset on a monthly basis and you can see your next reset date when
    logged in to your Zapier account on [zapier.com](https://zapier.com)
  </Tab>

  <Tab title="Upgrade your Zapier Account">
    You can add more tasks to your Zapier account at any time [from
    here.](https://zapier.com/pricing)
  </Tab>
</Tabs>

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Can our Enterprise use Zapier MCP?">
    Yes. If you're on an Enterprise plan and would like to use Zapier MCP, please have your Zapier admin reach out to us to enable it for your organization. [Contact us](https://mcpp.zapier.app/enterprise-access).
  </Accordion>

  <Accordion title="How much does Zapier MCP cost?">
    Zapier MCP is available to all accounts. One Zapier MCP tool call uses **two
    tasks** from your Zapier plan’s quota. If you would like more tasks, explore
    [Zapier plans here.](https://zapier.com/pricing)
  </Accordion>

  <Accordion title="Do test actions count against my limit?">
    Yes, all successful tool calls count, including tests.
  </Accordion>

  <Accordion title="When will Zapier MCP exit Beta?">
    Beta period end date TBD.
  </Accordion>

  <Accordion title="As a developer, can I pay for Zapier MCP for my customers?">
    Yes. To explore options to cover the costs of Zapier MCP for your users [get in touch here.](https://zapier.com/developer-platform#form)
  </Accordion>
</AccordionGroup>

## Next Steps

* [Monitor your usage](https://mcp.zapier.com)
* [Try Zapier Agents](https://zapier.com/agents) to build always on AI Agents with access to thousands of Trigger events.
