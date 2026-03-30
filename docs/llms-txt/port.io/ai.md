# Source: https://docs.port.io/workflows/build-workflows/action-nodes/ai.md

# AI

The AI action node invokes [Port AI](/ai-interfaces/port-ai/overview.md) directly from your workflow. It supports two modes of operation: invoking an [AI agent](/ai-interfaces/ai-agents/overview.md) by identifier, or invoking Port AI with custom configuration.

The workflow pauses execution after sending the AI request and automatically resumes once the AI invocation completes (or fails).

## Modes[â](#modes "Direct link to Modes")

* Invoke AI Agent
* Invoke AI

Use the `AI_AGENT` type to invoke a pre-configured [AI agent](/ai-interfaces/ai-agents/overview.md) by its identifier. The agent's tools, system prompt, and domain configuration are defined on the agent itself â you only need to provide the prompt.

### Configuration[â](#configuration "Direct link to Configuration")

| Field             | Type         | Description                                            |
| ----------------- | ------------ | ------------------------------------------------------ |
| `type`            | `"AI_AGENT"` | **Required.** Must be `"AI_AGENT"`                     |
| `agentIdentifier` | `string`     | **Required.** The identifier of the AI agent to invoke |
| `userPrompt`      | `string`     | **Required.** The prompt or query to send to the agent |

### Example[â](#example "Direct link to Example")

Invoke an incident response agent to analyze a service's health:

```
{
  "identifier": "analyze-health",
  "title": "Analyze Service Health",
  "config": {
    "type": "AI_AGENT",
    "agentIdentifier": "incident-response-agent",
    "userPrompt": "Analyze the health of service {{ .outputs.trigger.service }} and provide a summary of any issues"
  }
}
```

Use the `AI` type for general-purpose AI invocations where you configure the tools, system prompt, and other parameters directly in the node.

### Configuration[â](#configuration-1 "Direct link to Configuration")

| Field          | Type       | Description                                                                                                                                                                  |
| -------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`         | `"AI"`     | **Required.** Must be `"AI"`                                                                                                                                                 |
| `userPrompt`   | `string`   | **Required.** The prompt or query to send to Port AI                                                                                                                         |
| `systemPrompt` | `string`   | Instructions that guide the AI's behavior, role, and operational rules                                                                                                       |
| `tools`        | `string[]` | **Required.** List of regex patterns to match against available tool names. See [available tools](/ai-interfaces/port-ai/overview.md?execution-modes=manual#available-tools) |
| `provider`     | `string`   | The AI provider to use. If not specified, the default provider is used                                                                                                       |
| `model`        | `string`   | The AI model to use. Must be specified together with `provider`                                                                                                              |

Provider and model

The `provider` and `model` fields must both be specified together, or both omitted. When omitted, the organization's default AI provider and model are used. For more information, see [LLM providers management](/ai-interfaces/port-ai/llm-providers-management/overview.md).

### Example[â](#example-1 "Direct link to Example")

Invoke Port AI with a custom system prompt and specific tools to generate a deployment summary:

```
{
  "identifier": "generate-summary",
  "title": "Generate Deployment Summary",
  "config": {
    "type": "AI",
    "userPrompt": "Generate a deployment summary for service {{ .outputs.trigger.service }} in the {{ .outputs.trigger.environment }} environment",
    "systemPrompt": "You are a deployment analyst. Provide concise, actionable summaries of deployment status and any risks.",
    "tools": ["search_entities", "get_entity"]
  }
}
```

## Outputs[â](#outputs "Direct link to Outputs")

When the AI invocation completes, the node produces the following outputs:

| Field                  | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| `response`             | The AI response text                                  |
| `invocationIdentifier` | The identifier of the AI invocation entity            |
| `error`                | Error message (only present if the invocation failed) |

Reference these outputs in subsequent nodes:

```
{{ .outputs.analyze_health.response }}
{{ .outputs.analyze_health.invocationIdentifier }}
```

## Examples[â](#examples "Direct link to Examples")

### Invoke an AI agent and notify Slack with the result[â](#invoke-an-ai-agent-and-notify-slack-with-the-result "Direct link to Invoke an AI agent and notify Slack with the result")

This workflow invokes an AI agent to analyze a service and sends the AI response to Slack:

**Workflow example (click to expand)**

```
{
  "identifier": "ai-analyze-and-notify",
  "title": "AI Analysis with Notification",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "Select Service",
      "config": {
        "type": "SELF_SERVE_TRIGGER",
        "userInputs": {
          "properties": {
            "service": {
              "type": "string",
              "format": "entity",
              "blueprint": "service",
              "title": "Service"
            }
          },
          "required": ["service"]
        }
      }
    },
    {
      "identifier": "ai-analyze",
      "title": "Analyze with AI Agent",
      "config": {
        "type": "AI_AGENT",
        "agentIdentifier": "service-analyzer",
        "userPrompt": "Analyze the health and status of service {{ .outputs.trigger.service }}. Include any recent incidents and scorecard results."
      }
    },
    {
      "identifier": "notify-slack",
      "title": "Send Analysis to Slack",
      "config": {
        "type": "WEBHOOK",
        "url": "https://hooks.slack.com/services/xxx",
        "method": "POST",
        "body": {
          "text": "AI Analysis for {{ .outputs.trigger.service }}:\n{{ .outputs[\"ai-analyze\"].response }}"
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "ai-analyze"
    },
    {
      "sourceIdentifier": "ai-analyze",
      "targetIdentifier": "notify-slack"
    }
  ]
}
```

### Generate an incident summary on service degradation[â](#generate-an-incident-summary-on-service-degradation "Direct link to Generate an incident summary on service degradation")

This event-driven workflow detects service degradation and uses AI to generate an incident summary:

**Workflow example (click to expand)**

```
{
  "identifier": "ai-incident-summary",
  "title": "Generate Incident Summary on Degradation",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "On Service Degraded",
      "config": {
        "type": "EVENT_TRIGGER",
        "event": {
          "type": "ENTITY_UPDATED",
          "blueprintIdentifier": "service"
        },
        "condition": {
          "type": "JQ",
          "expressions": [
            ".diff.before.properties.healthStatus == \"healthy\"",
            ".diff.after.properties.healthStatus != \"healthy\""
          ],
          "combinator": "and"
        }
      }
    },
    {
      "identifier": "ai-summarize",
      "title": "Generate Incident Summary",
      "config": {
        "type": "AI",
        "userPrompt": "Service {{ .outputs.trigger.diff.after.title }} has degraded from {{ .outputs.trigger.diff.before.properties.healthStatus }} to {{ .outputs.trigger.diff.after.properties.healthStatus }}. Analyze the service and its dependencies to generate a concise incident summary with potential root causes.",
        "systemPrompt": "You are an incident response analyst. Provide structured incident summaries with severity assessment, affected components, and recommended next steps.",
        "tools": ["search_entities", "get_entity"]
      }
    },
    {
      "identifier": "create-incident-entity",
      "title": "Create Incident Record",
      "config": {
        "type": "UPSERT_ENTITY",
        "blueprintIdentifier": "incident",
        "mapping": {
          "identifier": "incident-{{ .outputs.trigger.diff.after.identifier }}-{{ now | todateiso8601 }}",
          "title": "Degradation: {{ .outputs.trigger.diff.after.title }}",
          "properties": {
            "summary": "{{ .outputs[\"ai-summarize\"].response }}",
            "status": "open",
            "detectedAt": "{{ now | todateiso8601 }}"
          },
          "relations": {
            "service": "{{ .outputs.trigger.diff.after.identifier }}"
          }
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "ai-summarize"
    },
    {
      "sourceIdentifier": "ai-summarize",
      "targetIdentifier": "create-incident-entity"
    }
  ]
}
```
