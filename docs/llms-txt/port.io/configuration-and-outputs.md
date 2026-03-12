# Source: https://docs.port.io/workflows/build-workflows/action-nodes/configuration-and-outputs.md

# Configuration and outputs

Action nodes perform operations in your workflow. They execute after trigger nodes and can be chained together to create complex automation flows.

## Common configuration[â](#common-configuration "Direct link to Common configuration")

All action nodes share these common fields:

| Field         | Description                                        |
| ------------- | -------------------------------------------------- |
| `identifier`  | Unique identifier for the node within the workflow |
| `title`       | Display name for the node                          |
| `icon`        | Optional icon for the node                         |
| `description` | Optional description of what the node does         |
| `config`      | The action configuration (type-specific)           |
| `variables`   | Optional key-value pairs for reusable expressions  |

### On failure[â](#on-failure "Direct link to On failure")

Action nodes that execute operations (WEBHOOK, KAFKA, UPSERT\_ENTITY, INTEGRATION\_ACTION) support an `onFailure` configuration option:

| Field       | Type                          | Default       | Description                                                                                                                                                                                       |
| ----------- | ----------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onFailure` | `'continue'` \| `'terminate'` | `'terminate'` | When set to `'continue'`, the workflow continues to the next nodes even if this node fails. When set to `'terminate'`, the workflow run is marked as failed and no subsequent nodes are executed. |

By default, when an action node fails, the entire workflow run is marked as failed and no subsequent nodes are executed. Setting `onFailure: 'continue'` allows the workflow to proceed despite the failure.

FAILED status persists

The failed node is still marked with a `FAILED` result. The `onFailure` option only affects whether subsequent nodes are executed.

**Example:**

```
{
  "identifier": "optional-notification",
  "title": "Send Optional Notification",
  "config": {
    "type": "WEBHOOK",
    "url": "https://hooks.slack.com/services/xxx",
    "method": "POST",
    "onFailure": "continue",
    "body": {
      "text": "Deployment started for {{ .outputs.trigger.service }}"
    }
  }
}
```

In this example, even if the Slack notification fails, the workflow will continue to execute subsequent nodes.

When a node fails, its output includes an `error` object with a `message` field describing the failure. Downstream nodes can reference it (for example when using `onFailure: 'continue'`) to handle or log the error:

| Field                  | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| `output.error.message` | Human-readable error message describing why the node failed |

Example output from a failed node:

```
{
  "error": {
    "message": "Request failed: connection refused"
  }
}
```

## Referencing outputs[â](#referencing-outputs "Direct link to Referencing outputs")

Action nodes can reference outputs from previous nodes using bracket notation `.outputs["<node_identifier>"].<field>`:

| Context                                 | Description                                       |
| --------------------------------------- | ------------------------------------------------- |
| `.outputs["<node_identifier>"].<field>` | Output from any previous node (including trigger) |
| `.secrets["<name>"]`                    | Organization secrets                              |

For self-service triggers, the user inputs are stored directly at `.outputs["<trigger-node-identifier>"].<input_key>`.

For event triggers, the event data is stored at `.outputs["<trigger-node-identifier>"].diff.after`, `.outputs["<trigger-node-identifier>"].action`, etc.

### Example[â](#example "Direct link to Example")

**Chaining node outputs**

This example demonstrates how to pass data between nodes. A self-service trigger collects a resource name from the user, passes it to a webhook that creates the resource, and then sends a Slack notification with the newly created resource ID.

**Chaining node outputs (click to expand)**

```
{
  "nodes": [
    {
      "identifier": "trigger",
      "title": "Start",
      "config": {
        "type": "SELF_SERVE_TRIGGER",
        "userInputs": {
          "properties": {
            "resourceName": { "type": "string" }
          }
        }
      }
    },
    {
      "identifier": "create_resource",
      "title": "Create Resource",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.example.com/resources",
        "method": "POST",
        "body": {
          "name": "{{ .outputs.trigger.resourceName }}"
        }
      }
    },
    {
      "identifier": "notify",
      "title": "Send Notification",
      "config": {
        "type": "WEBHOOK",
        "url": "https://hooks.slack.com/xxx",
        "method": "POST",
        "body": {
          "text": "Created resource with ID: {{ .outputs.create_resource.response.data.resourceId }}"
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "create_resource"
    },
    {
      "sourceIdentifier": "create_resource",
      "targetIdentifier": "notify"
    }
  ]
}
```

## Condition nodes[â](#condition-nodes "Direct link to Condition nodes")

In addition to action nodes, workflows support **condition nodes** for branching logic:

```
{
  "identifier": "check-environment",
  "title": "Check Environment",
  "config": {
    "type": "CONDITION",
    "options": [
      {
        "identifier": "production",
        "title": "Production",
        "expression": ".outputs.trigger.environment == \"production\""
      },
      {
        "identifier": "staging",
        "title": "Staging",
        "expression": ".outputs.trigger.environment == \"staging\""
      }
    ]
  }
}
```

Connections from condition nodes must specify which option they're connected to:

```
{
  "connections": [
    {
      "sourceIdentifier": "check-environment",
      "targetIdentifier": "production-deploy",
      "sourceOptionIdentifier": "production"
    },
    {
      "sourceIdentifier": "check-environment",
      "targetIdentifier": "staging-deploy",
      "sourceOptionIdentifier": "staging"
    },
    {
      "sourceIdentifier": "check-environment",
      "targetIdentifier": "default-deploy",
      "fallback": true
    }
  ]
}
```
