# Source: https://docs.port.io/ai-interfaces/ai-agents/interact-with-ai-agents.md

# Interact with AI agents

<!-- -->

Open Beta

This feature is currently in open beta and available to all organizations. Should you encounter any bugs or functionality issues, please let us know so we can rectify them as soon as possible. Your feedback is greatly appreciated! â­

To get access, please fill out [this form](https://forms.gle/XtTR9R9pzo8tMYDT8) with your organization details.

Built on Port AI

AI Agents are specialized implementations built on top of [Port AI](/ai-interfaces/port-ai/overview.md), designed for machine-to-machine communication and autonomous operations within defined domains.

## Getting started[â](#getting-started "Direct link to Getting started")

Once you've built your AI agents, you can integrate them into your workflows and systems. AI agents are designed for machine-to-machine communication and can be triggered programmatically through Port's API or automatically through workflow automations.

## How AI Agents Work[â](#how-ai-agents-work "Direct link to How AI Agents Work")

AI Agents are domain-specific entities built on [Port AI](/ai-interfaces/port-ai/overview.md) with configured tools and prompts. For details on agent architecture and configuration, see [AI agents overview](/ai-interfaces/ai-agents/overview.md) and [Build an AI agent](/ai-interfaces/ai-agents/build-an-ai-agent.md).

## Interaction approaches[â](#interaction-approaches "Direct link to Interaction approaches")

AI agents are designed for specific domains and use cases. When interacting with agents, you target the specific agent that has the expertise and tools needed for your task. This approach works best for structured scenarios like automation triggers and API integrations where you know which domain-specific capabilities you need.

## Interaction methods[â](#interaction-methods "Direct link to Interaction methods")

* AI Chat Widget
* API integration
* Actions and automations

You can add AI agents directly to your dashboards as interactive widgets, providing easy access to their capabilities right where you need them.

Follow these steps to add an AI agent widget:

1. Go to a dashboard.

2. Click on `+ Widget`.

3. Select the `AI Chat` widget.

4. Configure your widget settings:

   <!-- -->

   * **Agent**: Select the specific AI agent to use
   * **Title**: Set a descriptive name for the widget
   * **Description**: Add a description for the widget

5. Save your dashboard configuration.

6. Start asking questions through the chat interface.

![](/img/ai-agents/AIAgentWidgetMenu.png)![](/img/ai-agents/AIAgentsTaskManagerWidget.png)

The widget provides a chat interface where you can ask questions and receive responses from the **selected agent** without leaving your dashboard.

The widget will inherit all the agent's configuration including the prompts, conversation starters, tool access, etc.

**Context Awareness**: The widget automatically understands the context of the page and entity where it's located. For example, when placed on a team entity page, you can ask questions like "What is this team's lead time for change?" or "How many open bugs does the team have?" without needing to specify the team name.

Conversation starters appear in the initial state, helping users understand what they can ask the agent. Users can either click a starter to begin a new chat or type their own question.

![](/img/ai-agents/AIAgentsWidgetConversationStarters.png)

AI agents can be integrated into your applications and workflows through Port's API. Agents use the same streaming API patterns as Port AI.

**Agent-specific endpoint:**

```
curl 'https://api.port.io/v1/agent/<AGENT_IDENTIFIER>/invoke?stream=true' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"prompt":"Analyze the health of our production services"}'
```

For comprehensive details on API interaction, streaming responses, event types, quota management, and integration patterns, see [Port AI API Interaction](/ai-interfaces/port-ai/api-interaction.md).

You can trigger AI agents through Port's actions and automations, enabling integration of AI capabilities into your existing workflows. This is the primary method for creating autonomous, machine-to-machine AI systems.

### Automation Workflows[â](#automation-workflows "Direct link to Automation Workflows")

Automations allow you to automatically trigger AI agents based on events in your Port catalog. This enables reactive AI systems that respond to changes in your infrastructure or applications.

**Example: Automatic Incident Response (Click to expand)**

When a new incident is created, automatically trigger an agent that:

* Analyzes the incident context
* Gathers relevant information from related services
* Creates initial response documentation
* Notifies appropriate teams

Create in Port

```
{
  "identifier": "incident_response_automation",
  "title": "Automatic Incident Response",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "ENTITY_CREATED",
      "blueprintIdentifier": "incident"
    }
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://api.port.io/v1/agent/incident_response_agent/invoke",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "prompt": "New incident created: {{ .entity.title }}. Severity: {{ .entity.properties.severity }}. Please analyze and provide initial response recommendations.",
      "labels": {
        "source": "automation",
        "incident_id": "{{ .entity.identifier }}",
        "trigger_type": "incident_created"
      }
    }
  }
}
```

**Example: Infrastructure Healing (Click to expand)**

Monitor infrastructure health and automatically trigger healing agents when issues are detected:

Create in Port

```
{
  "identifier": "k8s_healing_automation",
  "title": "Kubernetes Workload Healing",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "ENTITY_UPDATED",
      "blueprintIdentifier": "k8s_workload"
    },
    "condition": {
      "type": "JQ",
      "expressions": [
        ".diff.before.properties.isHealthy == \"Healthy\"",
        ".diff.after.properties.isHealthy == \"Unhealthy\""
      ],
      "combinator": "and"
    }
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://api.port.io/v1/agent/k8s_healing_agent/invoke",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "prompt": "Workload {{ .event.diff.after.title }} is unhealthy. Current state: {{ .event.diff.after.properties.replicas }} replicas, {{ .event.diff.after.properties.readyReplicas }} ready. Please analyze and fix.",
      "labels": {
        "source": "automation",
        "workload_name": "{{ .event.diff.after.identifier }}",
        "namespace": "{{ .event.diff.after.properties.namespace }}"
      }
    }
  }
}
```

### Self-Service Actions[â](#self-service-actions "Direct link to Self-Service Actions")

You can create self-service actions that invoke AI agents, allowing users to trigger intelligent workflows on-demand.

**Example: Service Analysis Action (Click to expand)**

Create in Port

```
{
  "identifier": "analyze_service_health",
  "title": "Analyze Service Health",
  "description": "Get AI-powered analysis of service health and recommendations",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "blueprintIdentifier": "service"
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://api.port.io/v1/agent/service_health_agent/invoke",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "prompt": "Analyze the health of service {{ .entity.title }}. Check metrics, recent deployments, and incidents.",
      "labels": {
        "source": "self_service",
        "service_name": "{{ .entity.identifier }}",
        "requested_by": "{{ .trigger.by.user.email }}"
      }
    }
  }
}
```

For comprehensive examples, see our [AI guides](/guides/.md?tags=AI).

## Discovering Available Agents[â](#discovering-available-agents "Direct link to Discovering Available Agents")

You can discover available AI agents through the AI Agents catalog page or programmatically via the API using the `_ai_agent` blueprint.

cURL Example

```
curl -L 'https://api.port.io/v1/blueprints/_ai_agent/entities' \
    -H 'Accept: application/json' \
    -H 'Authorization: Bearer <YOUR_API_TOKEN>'
```

## AI interaction details[â](#ai-interaction-details "Direct link to AI interaction details")

Every AI agent interaction creates an entity in Port, providing tracking and analysis capabilities. For comprehensive details on AI invocations, execution plans, and tools used, see [Port AI Overview](/ai-interfaces/port-ai/overview.md#ai-invocations).

### Data & security considerations[â](#data--security-considerations "Direct link to Data & security considerations")

For information on data handling and security, see [AI Security and Data Controls](/ai-interfaces/port-ai/security-and-data-controls.md).

## Limits[â](#limits "Direct link to Limits")

AI agents use the same rate limits and quotas as Port AI.

*Note: These limits apply when using Port's managed AI infrastructure. [Bring your own LLM provider](/ai-interfaces/port-ai/llm-providers-management/overview.md) to use your provider's limits instead.*

For detailed information on limits, monitoring, and quota management, see [Port AI API Interaction](/ai-interfaces/port-ai/api-interaction.md#rate-limits-and-quotas).

## Troubleshooting & FAQ[â](#troubleshooting--faq "Direct link to Troubleshooting & FAQ")

**How can I integrate agents into my workflows? (Click to expand)**

AI agents are designed for machine-to-machine communication and can be integrated through:

* **API integration**: Direct HTTP calls to agent endpoints
* **Workflow automations**: Automatic triggering based on Port catalog events
* **Self-service actions**: User-initiated agent workflows

For examples, see our [automation guides](/guides/.md?tags=AI).

**What happens if an agent can't answer my question? (Click to expand)**

If the agent doesn't have the knowledge or capabilities to answer your question, you'll receive a response mentioning that it can't assist you with your specific query. Consider using a different agent that's specialized for your domain or task.

**How do I improve agent performance? (Click to expand)**

For comprehensive guidance on improving AI performance, debugging issues, and analyzing invocation details, see [Port AI Overview](/ai-interfaces/port-ai/overview.md). The troubleshooting approaches for Port AI apply to AI agents as well.

For agent-specific improvements, see [Build an AI agent](/ai-interfaces/ai-agents/build-an-ai-agent.md) for prompt engineering and tool configuration guidance.
