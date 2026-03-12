# Source: https://docs.port.io/workflows/build-workflows/data-flow.md

# Data flow

Workflows pass data between nodes using **outputs** and **variables**. Understanding how data flows through your workflow is essential for building effective automations.

## Outputs[â](#outputs "Direct link to Outputs")

Every node in a workflow produces outputs that can be referenced by subsequent nodes. Outputs are accessed using bracket notation:

```
{{ .outputs["<node-identifier>"].<field> }}
```

Safe identifier access

Always use bracket notation (`.outputs["node-id"]`) when referencing node outputs. This ensures your expressions work correctly even when node identifiers contain hyphens or special characters.

### Trigger node outputs[â](#trigger-node-outputs "Direct link to Trigger node outputs")

The `<node-identifier>` used to access trigger outputs is the `identifier` field you define for your trigger node, not a fixed keyword. For example, if your trigger node has `"identifier": "my-trigger"`, you would access its outputs via `.outputs["my-trigger"].<field>`.

For **self-service triggers**, user inputs are stored directly as outputs:

```
{
  "identifier": "trigger",
  "config": {
    "type": "SELF_SERVE_TRIGGER",
    "userInputs": {
      "properties": {
        "serviceName": { "type": "string" }
      }
    }
  }
}
```

Since the trigger node above has `"identifier": "trigger"`, access the input in subsequent nodes using:

```
{{ .outputs["trigger"].serviceName }}
```

For **event triggers**, the full event object is stored as output:

```
{{ .outputs["trigger"].diff.after.identifier }}
{{ .outputs["trigger"].diff.after.properties.status }}
{{ .outputs["trigger"].diff.before.properties.status }}
{{ .outputs["trigger"].action }}
```

### Action node outputs[â](#action-node-outputs "Direct link to Action node outputs")

Webhook nodes store their response in the output:

```
{{ .outputs.my_webhook.response.status }}
{{ .outputs.my_webhook.response.data }}
```

## Variables[â](#variables "Direct link to Variables")

Variables allow you to transform and reshape node outputs before they're stored. This is useful for:

* Extracting specific fields from a response
* Simplifying complex data structures
* Removing sensitive data from outputs

Variables are defined on a node and evaluated **after** the node executes.

**Variables replace default outputs**

When you define `variables` on a node, the entire outputs object is replaced by your variables. The default outputs (such as `response.status` and `response.data` for webhook nodes) are **not** included unless you explicitly define them.

### JQ context in variables[â](#jq-context-in-variables "Direct link to JQ context in variables")

Inside a node's `variables` JQ expressions, you have access to:

| Context              | Description                   | Example                               |
| -------------------- | ----------------------------- | ------------------------------------- |
| `.result`            | The current node's raw output | `{{ .result.response.data.field }}`   |
| `.outputs["<node>"]` | Outputs from previous nodes   | `{{ .outputs["fetch_data"].entity }}` |

### Syntax[â](#syntax "Direct link to Syntax")

```
{
  "identifier": "my_node",
  "config": { ... },
  "variables": {
    "myField": "{{ .result.response.data.someValue }}",
    "simplified": "{{ .result.response.data.items[0] }}",
    "previousData": "{{ .outputs[\"trigger\"].serviceName }}"
  }
}
```

The variables are then accessible as:

```
{{ .outputs.my_node.myField }}
{{ .outputs.my_node.simplified }}
{{ .outputs.my_node.previousData }}
```

### Example[â](#example "Direct link to Example")

**Extracting entity data**

When fetching entities from Port's API, you might want to extract just the entity:

**Node example (click to expand)**

```
{
  "identifier": "fetch_entity",
  "config": {
    "type": "WEBHOOK",
    "url": "https://api.port.io/v1/blueprints/service/entities/search",
    "method": "POST",
    "body": {
      "query": {
        "rules": [
          {
            "property": "$identifier",
            "operator": "=",
            "value": "{{ .outputs.trigger.serviceId }}"
          }
        ],
        "combinator": "and"
      }
    }
  },
  "variables": {
    "entity": "{{ .result.response.data.entities[0] }}"
  }
}
```

Now you can access the entity directly:

```
{{ .outputs.fetch_entity.entity.title }}
{{ .outputs.fetch_entity.entity.properties.status }}
```

Since `variables` replaces the default outputs, only the extracted `entity` will be available in subsequent nodes.

**Combining current output with previous node data**

You can use `.outputs` inside variables to combine the current node's result with data from previous nodes:

```
{
  "identifier": "enrich_data",
  "config": {
    "type": "WEBHOOK",
    "url": "https://api.example.com/data",
    "method": "GET"
  },
  "variables": {
    "data": "{{ .result.response.data }}",
    "serviceName": "{{ .outputs[\"trigger\"].serviceName }}",
    "enrichedTitle": "{{ .outputs[\"trigger\"].serviceName + \" - \" + .result.response.data.status }}"
  }
}
```

In this example, the node's variables combine the current webhook response (`.result.response.data`) with data from the trigger node (`.outputs["trigger"].serviceName`).

## Fetching data from the catalog[â](#fetching-data-from-the-catalog "Direct link to Fetching data from the catalog")

Workflows can fetch entities from Port's catalog using webhook nodes. This is useful for:

* Getting related entities based on relations
* Looking up additional data not available in the trigger
* Building notifications with rich context

Automatic authentication

When calling Port's API, you don't need to include an access token. Port automatically authenticates the request using your organization's credentials.

### Port's entity search API[â](#ports-entity-search-api "Direct link to Port's entity search API")

Use the entity search endpoint to query entities:

```
POST https://api.port.io/v1/blueprints/<blueprint>/entities/search
```

### Examples[â](#examples "Direct link to Examples")

**Fetching a related entity**

This workflow fetches a service entity when a deployment changes:

**Workflow example (click to expand)**

```
{
  "identifier": "notify-on-deployment",
  "title": "Notify on Deployment",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "On Deployment Change",
      "config": {
        "type": "EVENT_TRIGGER",
        "event": {
          "type": "ANY_ENTITY_CHANGE",
          "blueprintIdentifier": "deployment"
        }
      }
    },
    {
      "identifier": "fetch_service",
      "title": "Fetch Service",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.port.io/v1/blueprints/service/entities/search",
        "method": "POST",
        "headers": {
          "Content-Type": "application/json"
        },
        "body": {
          "query": {
            "rules": [
              {
                "property": "$identifier",
                "operator": "=",
                "value": "{{ .outputs.trigger.diff.after.relations.service }}"
              }
            ],
            "combinator": "and"
          }
        }
      },
      "variables": {
        "entity": "{{ .result.response.data.entities[0] }}"
      }
    },
    {
      "identifier": "send_notification",
      "title": "Send Notification",
      "config": {
        "type": "WEBHOOK",
        "url": "https://hooks.slack.com/services/xxx",
        "method": "POST",
        "body": {
          "text": "Deployment updated for {{ .outputs.fetch_service.entity.title }}",
          "blocks": [
            {
              "type": "section",
              "fields": [
                {
                  "type": "mrkdwn",
                  "text": "*Service:*\n{{ .outputs.fetch_service.entity.title }}"
                },
                {
                  "type": "mrkdwn",
                  "text": "*Status:*\n{{ .outputs.trigger.diff.after.properties.status }}"
                }
              ]
            }
          ]
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "fetch_service"
    },
    {
      "sourceIdentifier": "fetch_service",
      "targetIdentifier": "send_notification"
    }
  ]
}
```

**Chaining multiple fetches**

You can chain multiple fetch operations to traverse entity relations:

**Workflow example (click to expand)**

```
{
  "nodes": [
    {
      "identifier": "trigger",
      "config": {
        "type": "EVENT_TRIGGER",
        "event": {
          "type": "ENTITY_UPDATED",
          "blueprintIdentifier": "deployment"
        }
      }
    },
    {
      "identifier": "fetch_environment",
      "title": "Fetch Environment",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.port.io/v1/blueprints/environment/entities/search",
        "method": "POST",
        "body": {
          "query": {
            "rules": [
              {
                "property": "$identifier",
                "operator": "=",
                "value": "{{ .outputs.trigger.diff.after.relations.environment }}"
              }
            ],
            "combinator": "and"
          }
        }
      },
      "variables": {
        "entity": "{{ .result.response.data.entities[0] }}"
      }
    },
    {
      "identifier": "fetch_cluster",
      "title": "Fetch Cluster",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.port.io/v1/blueprints/cluster/entities/search",
        "method": "POST",
        "body": {
          "query": {
            "rules": [
              {
                "property": "$identifier",
                "operator": "=",
                "value": "{{ .outputs.fetch_environment.entity.relations.cluster }}"
              }
            ],
            "combinator": "and"
          }
        }
      },
      "variables": {
        "entity": "{{ .result.response.data.entities[0] }}"
      }
    },
    {
      "identifier": "notify",
      "title": "Send Alert",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.example.com/alert",
        "method": "POST",
        "body": {
          "deployment": "{{ .outputs.trigger.diff.after.identifier }}",
          "environment": "{{ .outputs.fetch_environment.entity.title }}",
          "cluster": "{{ .outputs.fetch_cluster.entity.title }}",
          "region": "{{ .outputs.fetch_cluster.entity.properties.region }}"
        }
      }
    }
  ],
  "connections": [
    { "sourceIdentifier": "trigger", "targetIdentifier": "fetch_environment" },
    { "sourceIdentifier": "fetch_environment", "targetIdentifier": "fetch_cluster" },
    { "sourceIdentifier": "fetch_cluster", "targetIdentifier": "notify" }
  ]
}
```

## Secrets[â](#secrets "Direct link to Secrets")

Access organization secrets using the `.secrets` context:

```
{{ .secrets["my-api-key"] }}
```

Example with authorization header:

```
{
  "config": {
    "type": "WEBHOOK",
    "url": "https://api.example.com/endpoint",
    "headers": {
      "Authorization": "Bearer {{ .secrets[\"api-token\"] }}"
    }
  }
}
```

## Summary[â](#summary "Direct link to Summary")

### In node config (evaluated before execution)[â](#in-node-config-evaluated-before-execution "Direct link to In node config (evaluated before execution)")

| Context                      | Description                 | Example                                 |
| ---------------------------- | --------------------------- | --------------------------------------- |
| `.outputs["<node>"].<field>` | Output from a previous node | `{{ .outputs["trigger"].serviceName }}` |
| `.secrets["<name>"]`         | Organization secret         | `{{ .secrets["api-key"] }}`             |

### In node variables (evaluated after execution)[â](#in-node-variables-evaluated-after-execution "Direct link to In node variables (evaluated after execution)")

| Context                      | Description                 | Example                                 |
| ---------------------------- | --------------------------- | --------------------------------------- |
| `.result.<field>`            | Current node's raw output   | `{{ .result.response.data.items[0] }}`  |
| `.outputs["<node>"].<field>` | Output from a previous node | `{{ .outputs["trigger"].serviceName }}` |
