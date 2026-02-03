# Source: https://docs.datadoghq.com/actions/agents.md

---
title: Agents
description: Build custom AI agents that can access the Action Catalog.
breadcrumbs: Docs > Agents
---

# Agents

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Agents are in Preview. Click Request Access and fill in the Datadog Product Preview Program form.

[Request Access](https://www.datadoghq.com/product-preview/agent-builder/)
{% /callout %}

## Overview{% #overview %}

You can build custom AI agents to act on your observability data and third-party integrations. Agents can use any action from the [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/) to investigate problems, start remediation, or manage resources.

When building an agent, choose a blueprint to get started. Blueprints come with pre-filled instructions and relevant tools. They're named after their main role, like Security Analyst, Log Analyzer, Incident Responder, or DevOps Assistant.

{% image
   source="https://datadog-docs.imgix.net/images/actions/agents/blank-new-agent.c3cd29119a15caa7600174812a687a91.png?auto=format"
   alt="The Agents page, filtered to show only 'My agents'" /%}

## Agents page{% #agents-page %}

You can create a new agent from the [Agents](https://app.datadoghq.com/actions/agents) page. The page lists information about existing agents, including the following:

- Agent Name
- Description
- Author
- Creation date

Hover over an agent for options to clone or delete it. You can also enable the **My agents** toggle to see only agents that you've created:

{% image
   source="https://datadog-docs.imgix.net/images/actions/agents/agent-dashboard.92640af22d9c7162e59ca5b8a2fe368a.png?auto=format"
   alt="The Agents page, filtered to show only 'My agents'" /%}

## Create an agent{% #create-an-agent %}

### Build an agent from a blueprint{% #build-an-agent-from-a-blueprint %}

Blueprints are starter agents that cover common use cases. They come loaded with instructions for the agent's behavior and related tools from the Action Catalog. Blueprints also showcase best practices for setting up agent functionality.

To build an agent from a blueprint:

1. Navigate to the [Agents](https://app.datadoghq.com/actions/agents) page.
1. In **Agent Blueprints**, click the blueprint you want to use. Alternatively, you can click **New Agent** and browse the full list of blueprints.
1. Click **Create From Blueprint**.
1. Your new agent has pre-populated settings and tools. You can immediately start chatting with the agent or further customize it.

### Create a custom agent{% #create-a-custom-agent %}

To build an agent from scratch:

1. Navigate to the [Agents](https://app.datadoghq.com/actions/agents) page.
1. Click **New Agent**.
1. Customize your agent. Changes are saved automatically.
1. Start chatting with your agent.

## Customize your agent{% #customize-your-agent %}

When configuring your agent, you have the following options for customization.

### Instructions{% #instructions %}

Enter the instructions for your agent to follow when performing tasks. You can describe the agent as if it were a person, including its role, specialties, and steps to follow. Click **Suggest With AI** to get help with writing and refining your instructions.

Below is a sample set of instructions for an agent acting as an incident responder.

```
You are an Incident Responder AI assistant specialized in managing and coordinating incident response activities.

Your role involves:
- Guiding incident response procedures and best practices
- Helping assess incident severity and impact
- Coordinating communication between teams and stakeholders
- Managing incident lifecycle from detection to resolution
- Facilitating post-incident reviews and improvements

During incident response:
1. Help classify incident severity (P0/P1/P2/etc.)
2. Guide through incident response runbooks and procedures
3. Assist with stakeholder communication and updates
4. Track action items and follow-up tasks
5. Support post-mortem analysis and lessons learned

Focus on clear communication, structured processes, and continuous improvement of incident response capabilities.
```

### Model{% #model %}

By default, new custom agents run on the latest GPT model.

To change your agent's model, click **Auto** in the chatbox to open a dropdown menu and choose another model. You can compare these models using [OpenAI's comparison tool](https://platform.openai.com/docs/models) and [Anthropic's models comparison](https://docs.claude.com/en/docs/about-claude/models/overview#latest-models-comparison).

### Self Improve{% #self-improve %}

By default, the **Self Improve** feature is not enabled. Self improvement allows the agent to read its own configuration and update it when requested or when it determines its configuration can be changed to improve.

To enable this feature, click the settings **{% icon name="icon-sliders" /%}** icon, then the toggle button next to **Self Improve**.

### Actions{% #actions %}

Click the plus **{% icon name="icon-plus-circled-wui" /%}** icon to add actions from the [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/) for the agent to use. The agent is restricted to only its added tools. For example, if you encounter an error when the agent attempts to perform a task you've requested, it might be missing a necessary action.

### MCP Server{% #mcp-server %}

Click the toggle button to enable the [Datadog MCP Server](https://docs.datadoghq.com/bits_ai/mcp_server). MCP servers use the Model Context Protocol to provide additional tools and capabilities that the agent can use to interact with external systems.

## Add an agent action{% #add-an-agent-action %}

After you create an agent, you can add it to a workflow or app.

### Add to a workflow{% #add-to-a-workflow %}

To invoke an agent in a workflow step:

1. In [Workflow Automation](https://app.datadoghq.com/workflow), navigate to a workflow and click **Edit**.
1. Click the plus **{% icon name="icon-plus-circled-wui" /%}** icon.
1. Select the **Execute Custom Agent** action.
1. Configure the action:
   1. Enter a **Step name**.
   1. Selection a **Connection**.
   1. Select a **Custom Agent ID**.
   1. Enter a **User Prompt**.
   1. Optionally, add a [**Wait until condition**](https://docs.datadoghq.com/actions/workflows/build/#wait-until-condition).
   1. Optionally, add [**Retries**](https://docs.datadoghq.com/actions/workflows/build/#retries).
1. Click **Save**.

### Add to an app{% #add-to-an-app %}

To invoke an agent in an app:

1. In [App Builder](https://app.datadoghq.com/app-builder/apps/list), navigate to an app and click **Edit**.
1. Click the plus **{% icon name="icon-plus-2" /%}** icon, then click **Actions**.
1. Select the **Execute Custom Agent** action.
1. Configure the action:
   1. Select the **Run Settings**.
   1. Selection a **Connection**.
   1. Select a **Custom Agent ID**.
   1. Enter a **User Prompt**.
1. Click **Save**.

## Further Reading{% #further-reading %}

- [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/)
- [What are AI agents and how do they work?](https://www.datadoghq.com/knowledge-center/aiops/ai-agents/)
