# Source: https://docs.agent.ai/knowledge-agents/tools-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools & Integration

> Give your knowledge agent the power to take action with workflow agents, MCP servers, and app integrations

## Overview

This is where knowledge agents become **truly powerful**. While knowledge lets your agent understand and answer questions, tools let it **actually do things**.

Knowledge agents can orchestrate three types of tools:

| Tool Type                 | What It Does                                    | Best For                        |
| ------------------------- | ----------------------------------------------- | ------------------------------- |
| **Workflow Agents**       | Call your existing Agent.AI workflow agents     | Custom automations you've built |
| **MCP Servers**           | Connect custom tools via Model Context Protocol | Advanced/developer capabilities |
| **Composio Integrations** | Take actions in 100+ external apps              | Slack, Gmail, HubSpot, etc.     |

**The key concept:** Your knowledge agent intelligently decides when to use each tool based on the conversation context. You just enable the tools and write good system prompts that guide when to use them.

## How Function Calling Works

When you enable tools for your knowledge agent, here's what happens:

```
User: "Research Acme Corp and add them to HubSpot"
        ↓
Knowledge Agent analyzes the request
        ↓
Recognizes it needs two tools: research + CRM
        ↓
Calls "Company Research" workflow agent
        ↓
Gets company data back
        ↓
Calls HubSpot integration to create contact
        ↓
Responds: "Done! I found Acme Corp, researched them,
and created a contact in HubSpot with [details]."
```

**Important:** The AI decides which tools to call and in what order. You guide this through:

* System instructions that explain when to use each tool
* Clear tool names and descriptions
* Good conversation design

## Workflow Agents as Tools

This is the most common and powerful integration. Your knowledge agent can call any of your workflow agents to accomplish tasks.

### How It Works

**Workflow agents** are your deterministic automations (step-by-step processes). **Knowledge agents** are conversational and decide when to invoke those automations.

Think of it like:

* **Workflow agents** = Specialized workers (do one thing really well)
* **Knowledge agents** = Manager (decides who to call for what task)

### Adding Workflow Agents

1. Navigate to your knowledge agent builder
2. Click the **"Action Agents"** tab
3. You'll see a list of all your workflow agents
4. Check the box next to each workflow you want to enable
5. Click **"Save Action Agents Selection"**

That's it! Your knowledge agent can now call those workflows.

<Tip>
  **Start with 2-3 workflows maximum** when testing. Add more once you've verified each one works individually.
</Tip>

### Making Your Knowledge Agent Use Workflows

Just enabling a workflow doesn't mean your knowledge agent will use it. You need to guide the AI through **system instructions**.

#### Good System Instructions for Workflow Tools

```
You are a marketing assistant with access to several workflows:

- Use the "Competitor Research" workflow when users ask about competitors
- Use the "Content Generator" workflow to create marketing content
- Use the "Social Media Poster" workflow to schedule or publish posts

When a user asks you to research competitors:
1. Call the Competitor Research workflow with the company names
2. Analyze the results
3. Present findings in bullet points
4. Ask if they want you to create content based on the research

When creating content:
1. Ask clarifying questions about audience and goals
2. Use the Content Generator workflow
3. Show the user the draft
4. Get approval before using Social Media Poster workflow

Never post publicly without explicit user approval.
```

<Warning>
  **Bad example:** "You have workflows available to help users."

  This is too vague. The AI won't know when to use what.
</Warning>

#### Naming Your Workflow Agents

Make sure your workflow agents have clear, descriptive names:

**Good names:**

* "Company Research Tool"
* "Email Sender"
* "Data Analyzer"
* "LinkedIn Profile Enricher"

**Bad names:**

* "Agent 1"
* "My Workflow"
* "Test"
* "Automation"

The name is part of the AI's decision-making process!

### Passing Data Between Expert and Workflow Agents

When your knowledge agent calls a workflow, it can:

**Send data to the workflow:**

* User input from the conversation
* Data retrieved from knowledge base
* Results from previous tool calls

**Receive data from the workflow:**

* Workflow outputs
* Structured data
* Generated content
* Status/error messages

The knowledge agent then uses this data to continue the conversation naturally.

### Example: Research Assistant with Multiple Workflows

**Enabled workflows:**

* "Web Search" - Searches the internet
* "Company Enrichment" - Gets company details
* "Create Google Doc" - Saves to Google Docs

**System instructions:**

```
You are a research assistant that helps users conduct thorough research.

When users ask you to research companies:
1. Use the "Web Search" workflow to find recent news and information
2. Use the "Company Enrichment" workflow to get detailed company data
3. Synthesize findings from both sources
4. If the user wants to save the research, use "Create Google Doc" workflow

Always cite your sources and ask before saving documents.
```

**Sample conversation:**

```
User: "Research TechCorp and competitors"

Agent: "I'll research TechCorp and their competitive landscape.
[Calls Web Search workflow with query: "TechCorp news competitors"]
[Calls Company Enrichment workflow with company: "TechCorp"]

Based on my research:

TechCorp:
- Revenue: $50M, 200 employees
- Recent news: Just raised Series B
- Main product: Enterprise SaaS

Top 3 Competitors:
- CompanyA: Similar product, larger scale
- CompanyB: Newer, focused on SMB
- CompanyC: Premium positioning

Would you like me to save this to a Google Doc?"

User: "Yes please"

Agent: [Calls Create Google Doc workflow]
Done! Research saved to 'TechCorp Analysis' in your Google Drive.
```

## MCP (Model Context Protocol) Servers

MCP is an advanced feature for developers who want to build custom tools for their knowledge agents.

### What is MCP?

**Model Context Protocol** is an open standard for connecting AI agents to external tools and data sources. It allows you to:

* Build custom tools in any programming language
* Connect to proprietary systems
* Extend agent capabilities beyond built-in features
* Share tools across different agents

### When to Use MCP

Use MCP servers when:

* You need custom functionality not available in workflow agents or integrations
* You're connecting to proprietary internal systems
* You want fine-grained control over tool behavior
* You're comfortable with development/technical setup

### Setting Up MCP Servers

<Note>
  **Technical knowledge required:** Setting up MCP servers requires development experience. Most users should start with workflow agents and Composio integrations.
</Note>

**High-level process:**

1. **Build your MCP server** following the [MCP specification](https://docs.agent.ai/mcp-server)
2. **Deploy it** somewhere your knowledge agent can access
3. **Register it** with your knowledge agent:
   * Go to knowledge agent settings
   * Navigate to MCP configuration
   * Add your server URL and authentication
4. **Reference it in system instructions** so the agent knows when to use it

**Example MCP server use case:**

```
You built an internal company database search tool as an MCP server.
Your knowledge agent can now search your proprietary data by calling this MCP tool.
```

### MCP vs Workflow Agents

| Aspect           | Workflow Agents         | MCP Servers                |
| ---------------- | ----------------------- | -------------------------- |
| Setup difficulty | Easy (no-code)          | Advanced (coding required) |
| Best for         | Business automations    | Custom technical tools     |
| Visibility       | Visual workflow builder | Code-based                 |
| Sharing          | Clone in platform       | Deploy infrastructure      |

**Recommendation:** Start with workflow agents. Only use MCP if you have specific technical requirements.

## Composio Integrations

Composio provides 100+ pre-built integrations with popular apps and services. This lets your knowledge agent take actions in external systems.

### Available Integrations

**Communication:**

* Slack - Send messages, create channels
* Gmail - Send emails, read inbox
* Discord - Post messages, manage servers

**CRM & Sales:**

* HubSpot - Create contacts, deals, notes
* Salesforce - Update records, search data
* Pipedrive - Manage pipeline

**Productivity:**

* Google Drive - Create/read documents
* Notion - Update databases, create pages
* Asana - Create/update tasks

**And 90+ more integrations** across categories like marketing, development, data, and analytics.

### Setting Up Composio Integrations

1. **Navigate to your knowledge agent builder**
2. Click the **"Integrations"** tab (or "Composio" tab)
3. **Browse available integrations**
4. Click on an integration you want to enable
5. **Authenticate** - Connect your account (OAuth flow)
6. **Configure permissions** - Choose what the agent can access
7. **Save the integration**

Now your knowledge agent can call that service!

### Guiding Your Agent to Use Integrations

Like with workflow agents, you need to tell your knowledge agent when to use integrations via system instructions.

#### Example: Slack Integration

**System instructions:**

```
You are a team communication assistant with access to Slack.

When users ask you to notify the team or send a message:
1. Ask which channel (if they didn't specify)
2. Confirm the message content
3. Use the Slack integration to send the message
4. Confirm it was sent

Always get approval before sending messages to public channels.
```

**Conversation:**

```
User: "Let the engineering team know the API is ready"

Agent: "I'll send a message to the engineering team on Slack.
Should I post in #engineering-general or a different channel?"

User: "#engineering-general"

Agent: "I'll send this message to #engineering-general:
'The API is ready for testing and integration.'

Should I send it?"

User: "Yes"

Agent: [Calls Slack integration]
Message sent to #engineering-general ✓
```

### Security Best Practices

<Warning>
  **Important:** Integrations have real access to your accounts. Be careful with public knowledge agents.

  * Don't share agents that have sensitive integrations
  * Review what permissions each integration needs
  * Add confirmation steps for destructive actions
  * Consider separate accounts for agent integrations
</Warning>

**Safe system instruction pattern:**

```
Before taking any action that:
- Sends messages/emails to others
- Creates/modifies records
- Posts publicly
- Deletes anything

Always ask the user to confirm explicitly.
```

## Combining Multiple Tools

The real power comes from knowledge agents orchestrating multiple tools together.

### Example: End-to-End Sales Research Agent

**Enabled tools:**

* "Company Research" workflow agent
* "LinkedIn Profile Enrichment" workflow agent
* HubSpot integration (Composio)
* Gmail integration (Composio)

**System instructions:**

```
You are a sales research assistant that helps research prospects
and add them to our CRM.

Your workflow:
1. When given a company name, use Company Research workflow
2. Identify key decision-makers
3. Use LinkedIn Profile Enrichment workflow for each person
4. Create contacts in HubSpot with all enriched data
5. Ask if user wants you to draft outreach emails
6. If yes, draft personalized emails using research insights
7. Send via Gmail integration (only after approval)

Always research thoroughly before taking CRM or email actions.
```

**Sample interaction:**

```
User: "Research Acme Corp and add decision-makers to HubSpot"

Agent: "I'll research Acme Corp for you.
[Calls Company Research workflow]

Found Acme Corp:
- Industry: Enterprise SaaS
- Size: 500 employees
- Key decision-makers identified: CEO, CTO, VP Sales

Let me enrich their LinkedIn profiles...
[Calls LinkedIn enrichment for each person]

Great! I have complete profiles for:
1. Jane Doe - CEO
2. John Smith - CTO
3. Sarah Johnson - VP Sales

Should I create these contacts in HubSpot?"

User: "Yes, and draft outreach emails"

Agent: [Calls HubSpot integration to create 3 contacts]
✓ Created 3 contacts in HubSpot

Now drafting personalized outreach emails based on their backgrounds...

[Shows 3 email drafts using research insights]

Ready to send via Gmail. Should I send all three?"

User: "Send only the CEO email for now"

Agent: [Calls Gmail integration]
✓ Email sent to Jane Doe (CEO of Acme Corp)

I've also added notes to her HubSpot record that we sent initial outreach.
```

### Multi-Tool Orchestration Best Practices

**Do:**

* Let the agent decide the order of tool calls
* Build confirmation steps for sensitive actions
* Chain related tools logically (research → enrich → save)
* Use results from one tool to inform the next

**Don't:**

* Try to hard-code exact sequences (let AI adapt)
* Enable too many tools at once (start with 3-5)
* Skip confirmation on actions like sending emails
* Forget to handle errors gracefully

## Troubleshooting Tools

<AccordionGroup>
  <Accordion title="Knowledge agent isn't calling my workflow">
    **Symptoms:** Agent responds conversationally but doesn't invoke the workflow

    **Possible causes:**

    1. Workflow not enabled in Action Agents tab
    2. System instructions don't mention when to use it
    3. Workflow name is unclear
    4. Agent doesn't think it's relevant to the request

    **Solutions:**

    * Verify workflow is checked in Action Agents tab
    * Add explicit instructions: "Use \[workflow name] when users ask to \[task]"
    * Rename workflow to be more descriptive
    * Ask more directly: "Use the \[workflow name] to research..."
    * Test workflow independently to ensure it works
  </Accordion>

  <Accordion title="Workflow keeps failing or returning errors">
    **Symptoms:** Agent calls the workflow but gets errors

    **Possible causes:**

    1. Workflow itself has a bug
    2. Knowledge agent passing wrong data format
    3. Workflow expecting different inputs

    **Solutions:**

    * Test the workflow agent independently (run it directly)
    * Check workflow input requirements
    * Review what data the knowledge agent is passing
    * Update system instructions to format data correctly
    * Add error handling to the workflow
  </Accordion>

  <Accordion title="Agent calls the wrong tool">
    **Symptoms:** Agent uses Tool A when Tool B would be better

    **Possible causes:**

    1. Tool names/descriptions are ambiguous
    2. System instructions unclear about when to use what
    3. User request was vague

    **Solutions:**

    * Make tool names more specific and distinct
    * Add clear boundaries in system instructions:
      "Use Tool A for \[specific case]. Use Tool B for \[different case]."
    * Test with specific requests that clearly need one tool
    * Reduce number of similar tools enabled
  </Accordion>

  <Accordion title="Composio integration authentication failed">
    **Symptoms:** Can't connect or authenticate with external service

    **Possible causes:**

    1. OAuth flow expired or interrupted
    2. Wrong permissions requested
    3. Service credentials changed
    4. Rate limits exceeded

    **Solutions:**

    * Re-authenticate the integration (disconnect and reconnect)
    * Check service status (is the external service down?)
    * Review required permissions for the integration
    * Wait if rate limited, then try again
    * Contact support if integration consistently fails
  </Accordion>

  <Accordion title="Agent calls too many tools for simple requests">
    **Symptoms:** Agent over-engineers simple tasks by calling multiple tools

    **Possible causes:**

    1. System instructions encourage thoroughness without boundaries
    2. Agent trying to be helpful but overdoing it

    **Solutions:**

    * Add efficiency guidelines to system instructions:
      "Use the minimum number of tools needed to complete the task"
    * Specify when NOT to use certain tools
    * Test with simple requests and iterate on prompts
    * Consider if you enabled too many overlapping tools
  </Accordion>

  <Accordion title="How do I know which tool was called?">
    **Answer:** As the builder testing your agent:

    * Look for "\[Calling workflow name...]" messages
    * Watch for integration loading states
    * Check agent response for explicit mentions

    For end users, the visibility depends on your UX preferences. You can:

    * Configure system instructions to announce tool usage
    * Have agent explain what it's doing
    * Keep tool calls invisible for seamless experience

    Example system instruction:
    "When you call a tool, tell the user: 'Let me use \[tool name] to \[accomplish task]...'"
  </Accordion>
</AccordionGroup>

## Advanced: Tool Call Patterns

### The Research-Execute Pattern

```
System instructions:
"Always research before executing actions.
1. Gather information using research tools
2. Present findings to user
3. Get approval
4. Execute action using integration tools
5. Confirm completion"
```

**Good for:** Sales outreach, content creation, CRM management

### The Pipeline Pattern

```
System instructions:
"Process requests through a pipeline:
1. Input validation
2. Data enrichment
3. Transformation
4. Storage/output
5. Notification

Use [Tool A] for step 2, [Tool B] for step 3, [Tool C] for step 4."
```

**Good for:** Data processing, lead enrichment, report generation

### The Approval-Gate Pattern

```
System instructions:
"For sensitive operations:
1. Explain what you're about to do
2. Show exactly what data will be used
3. Wait for explicit user approval
4. Execute only after confirmation
5. Confirm completion with details

Sensitive operations include: sending emails, posting publicly,
creating CRM records, making purchases."
```

**Good for:** Public-facing agents, agents with write permissions

### The Fallback Pattern

```
System instructions:
"Try tools in order of preference:
1. First, try [Primary Tool]
2. If that fails or isn't available, try [Secondary Tool]
3. If all tools fail, explain to user and suggest manual approach

Always try your tools before saying you can't do something."
```

**Good for:** Resilient agents, agents with redundant capabilities

## Testing Your Tools

After enabling tools, thoroughly test:

### 1. Individual Tool Testing

Test each tool separately:

* "Use \[workflow name] to research Microsoft"
* "Send a test message to #test-channel on Slack"
* "Create a test contact in HubSpot"

**Verify:**

* Tool is called correctly
* Data is passed properly
* Results come back as expected
* Errors are handled gracefully

### 2. Multi-Tool Sequences

Test tool combinations:

* "Research Company X and add them to HubSpot"
* "Analyze this data and save results to Google Sheets"
* "Find recent news and post summary to Slack"

**Verify:**

* Tools are called in logical order
* Data flows between tools correctly
* User gets progress updates
* Final result is complete

### 3. Edge Cases

Test failure scenarios:

* What happens if a workflow fails?
* What if an integration is disconnected?
* What if the user provides incomplete information?

**Verify:**

* Graceful error messages
* Agent asks clarifying questions
* Doesn't get stuck in loops
* Offers alternatives

### 4. Approval Workflows

Test confirmation flows:

* Does agent ask before sensitive actions?
* Can user say "no" and agent respects it?
* Does agent re-confirm if request changes?

## Best Practices Summary

<Card title="Tool Integration Best Practices" icon="star">
  **DO:**

  * Start with 2-3 tools and add more gradually
  * Write explicit system instructions for each tool
  * Use clear, descriptive tool names
  * Test each tool individually before combining
  * Add confirmation steps for sensitive actions
  * Let the AI decide when to use tools (don't hard-code)

  **DON'T:**

  * Enable every tool at once
  * Assume the AI knows when to use tools without guidance
  * Skip testing multi-tool scenarios
  * Give public agents access to sensitive integrations
  * Forget to handle errors and edge cases
</Card>

## Next Steps

Now that you understand how to give your knowledge agent powerful action-taking capabilities:

<CardGroup cols={2}>
  <Card title="Manage Conversations" icon="messages" href="/knowledge-agents/conversations">
    Learn about conversation management, sharing, and user experience
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Advanced techniques for building exceptional knowledge agents
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve common issues and optimize performance
  </Card>

  <Card title="Build Workflow Agents" icon="diagram-project" href="/builder/overview">
    Create the workflow agents your knowledge agent will call
  </Card>
</CardGroup>

<Note>
  **Remember:** Tools transform your knowledge agent from a conversational assistant into a powerful automation orchestrator. Start simple, test thoroughly, and gradually build up to complex multi-tool workflows.
</Note>
