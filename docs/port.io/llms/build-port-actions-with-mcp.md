# Source: https://docs.port.io/guides/all/build-port-actions-with-mcp.md

# Build actions and automations with AI

Use Port's MCP (Model Context Protocol) server to create self-service actions and automations through natural language conversations with AI. This guide demonstrates how to design workflows, configure action inputs, and set up automationsâall by describing what you need in plain English.

Instead of manually writing JSON schemas or navigating complex forms, you can have conversations with your AI assistant to build actions iteratively, getting instant feedback and making adjustments on the fly.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Create deployment workflows**: Describe deployment processes and let AI create the actions.
* **Set up incident management**: Ask AI to create PagerDuty or Opsgenie integration actions.
* **Build approval workflows**: Explain approval requirements and have AI configure the action.
* **Configure automations**: Describe event-driven workflows and let AI set them up.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes you have:

* Basic understanding of [self-service actions](/actions-and-automations/create-self-service-experiences/.md) and [automations](/actions-and-automations/define-automations/.md).
* Port MCP server configured in your [IDE](/ai-interfaces/port-mcp-server/overview-and-installation.md?mcp-setup=cursor).

## Create actions with AI[â](#create-actions-with-ai "Direct link to Create actions with AI")

The Port MCP server provides tools like `list_actions` and `upsert_action` that enable AI agents to build your actions through natural language conversations. You can describe what you need, and the AI will generate the appropriate configuration and create it in Port.

### Start with a simple description

Describe the action you want to create in natural language. The AI will interpret your requirements and generate the appropriate schema.

**Example conversation:**

*"Create a self-service action called 'Deploy to Staging' for the service blueprint. It should trigger a GitHub workflow that accepts an optional version parameter and deployment environment."*

The AI will use the MCP `upsert_action` tool to generate and create the action:

* MCP server input
* Port output

![](/img/guides/MCPCreateAction.png)

![](/img/guides/MCPCreateActionPort.png)

Iterative refinement

After creating an action, you can refine it by asking follow-up questions like "Add a required approval step" or "Change the backend to use a webhook instead of GitHub".

### Add complex user inputs

Describe dynamic forms and the AI will configure them:

**Example conversation:**

*"Add a multi-select input for deployment regions with options for us-east-1, us-west-2, and eu-west-1"*

The AI will update the action's `userInputs` schema with the appropriate configuration.

### Configure different backends

Port actions support multiple backend types. Describe your preferred backend and AI will configure it:

**Example conversations:**

* *"Create a restart service action that triggers a GitHub workflow in the ops-automation repo"*
* *"Create an action that calls our internal API at <https://api.internal.com/deploy>"*
* *"Create an action that triggers a GitLab pipeline in the infrastructure project"*

The AI will configure the appropriate `invocationMethod` (GitHub, GitLab, Webhook, etc.).

### Real webhook backend examples

When you have web search access enabled, AI can research API documentation to build complete actions. Here are examples:

* Create Jira ticket
* Update PR status
* Trigger incident

*"Create a self-service action called 'Open Jira Issue' for the service blueprint. It should use a webhook to call the Jira REST API to create an issue. Include inputs for project key, issue type, summary, and description."*

* MCP server input
* Port output

![](/img/guides/MCPCreateActionJira.png)

![](/img/guides/MCPCreateActionJiraPort.png)

*"Create an action called 'Update PR Status' that calls the GitHub API via webhook to add a status check to a pull request. Accept repository, PR number, and status as inputs."*

* MCP server input
* Port output

![](/img/guides/MCPCreateActionPR.png)

![](/img/guides/MCPCreateActionPRPort.png)

*"Create a 'Trigger PagerDuty Incident' action using a webhook to call the PagerDuty Events API. Include inputs for summary, severity, and routing key."*

* MCP server input
* Port output

![](/img/guides/MCPCreateActionPagerDuty.png)

![](/img/guides/MCPCreateActionPagerDutyPort.png)

Running and reusing actions

Once you've created an action, you can immediately run it through your AI assistant. Simply ask: *"Run the 'Open Jira Issue' action for the checkout-service"*. The AI will discover the action, understand its inputs, and execute it.

To ensure AI can effectively run your actions later, include detailed descriptions and tooltips when creating them. These provide context when developers run actions from their IDE.

## Set up automation triggers[â](#set-up-automation-triggers "Direct link to Set up automation triggers")

Automations respond to events in your software catalog. AI can help you create event-driven workflows that react to changes automatically.

### Describe the trigger condition

Explain what event should trigger the automation:

**Example conversation:**

*"Create an automation that triggers a Slack notification when a service's health score drops below 50"*

* MCP server input
* Port output

![](/img/guides/MCPCreateAutomation.png)

![](/img/guides/MCPCreateAutomationPort.png)

### Common automation patterns

Here are patterns you can describe to AI:

**Entity lifecycle events:**

* *"When a new service is created, send a welcome message to the owning team's Slack channel"*
* *"When a service is deleted, create a cleanup task in Jira"*

**Property change events:**

* *"When a service's status changes to deprecated, notify the platform team"*
* *"When an incident severity is upgraded to critical, page the on-call engineer"*

**Timer-based events:**

* *"When a service's compliance certificate expires, create a renewal ticket"*

## Chain actions for complex workflows[â](#chain-actions-for-complex-workflows "Direct link to Chain actions for complex workflows")

Port can chain multiple actions together. Design your workflows by asking AI to create a holistic chain of actions to achieve your goal.

**Example conversation:**

*"Create an automation: when a PagerDuty incident is created with critical severity, automatically create a Jira ticket for tracking, post to the #incidents Slack channel, and trigger a 'Scale Up Resources' action for the affected service."*

This creates actions that trigger one another:

1. Critical incident detected â Create Jira ticket â Post to Slack â Scale up resources

* MCP server input
* Port output

![](/img/guides/MCPCreateChainedActions.png)

![](/img/guides/MCPCreateChainedActionsPort.png)

## Let's test it[â](#lets-test-it "Direct link to Let's test it")

After creating your actions, test them with an MCP-enabled AI assistant. In this example, we'll create a PagerDuty incident using the action we built.

### Prompt

Ask your AI assistant:

> *"Create a high urgency PagerDuty incident for the PORT-2 service with title 'High latency detected in checkout flow'"*

### What happens

The agent will:

1. **Discover the action** - Find `create_incident_webhook` via `list_actions`.
2. **Understand the inputs** - Use the action schema to determine required fields.
3. **Execute the action** - Call `run_create_incident_webhook` with the entity identifier and input parameters.
4. **Return the result** - Report whether the incident was created successfully.

* MCP server input
* Port output

![](/img/guides/MCPActionsCreateIncidentCursor.png)

![](/img/guides/MCPActionsCreateIncidentPort.png)

## Best practices for AI-driven action creation[â](#best-practices-for-ai-driven-action-creation "Direct link to Best practices for AI-driven action creation")

When using AI to create actions, follow these practices to get the best results:

### Be specific about inputs

The more detail you provide about inputs, the better the action schema:

* **Good**: *"Create a deploy action with inputs for environment (enum: production, staging, dev), version (string, required), and notify\_slack (boolean, default true)"*
* **Less effective**: *"Create a deploy action"*

### Specify the backend type

Tell AI what backend to use:

* *"...that triggers a GitHub workflow in the deployments repo"*
* *"...that calls a webhook at <https://api.example.com/deploy>"*
* *"...that triggers a GitLab pipeline"*

### Describe approval requirements

If your action needs approval:

*"Create a production deploy action that requires approval from the platform-admins team"*

### Use clear action names

Use verb-noun patterns that AI can understand:

* Good: `deploy_to_production`, `restart_service`, `trigger_incident`
* Less clear: `prod_dep`, `svc_rst`, `inc`

## Related documentation[â](#related-documentation "Direct link to Related documentation")

* [Self-service actions](/actions-and-automations/create-self-service-experiences/.md) - Complete guide to creating actions.
* [Define automations](/actions-and-automations/define-automations/.md) - Event-driven workflow configuration.
* [Available MCP tools](/ai-interfaces/port-mcp-server/available-tools.md) - Complete reference for all MCP tools.
* [Action backends](/actions-and-automations/create-self-service-experiences/setup-the-backend/.md) - Configure webhooks, GitHub, GitLab, and more.
