# Source: https://docs.port.io/workflows/build-workflows/event-trigger.md

# Event trigger

Event triggers allow workflows to run automatically in response to changes in your software catalog. When an entity is created, updated, or deleted, the workflow can be triggered to perform automated actions.

## Trigger types[â](#trigger-types "Direct link to Trigger types")

You can configure the following event types:

| Event type          | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| `ENTITY_CREATED`    | Triggered when a new entity is created in the specified blueprint |
| `ENTITY_UPDATED`    | Triggered when an existing entity is updated                      |
| `ENTITY_DELETED`    | Triggered when an entity is deleted                               |
| `ANY_ENTITY_CHANGE` | Triggered on any change (create, update, or delete)               |
| `TIMER_EXPIRED`     | Triggered when a timer property expires                           |

## Configuration[â](#configuration "Direct link to Configuration")

Here's how to configure each event trigger type:

* Entity created
* Entity updated
* Entity deleted
* Any entity change
* Timer expired

```
{
  "identifier": "trigger",
  "title": "On Service Created",
  "config": {
    "type": "EVENT_TRIGGER",
    "event": {
      "type": "ENTITY_CREATED",
      "blueprintIdentifier": "service"
    }
  }
}
```

```
{
  "identifier": "trigger",
  "title": "On Service Updated",
  "config": {
    "type": "EVENT_TRIGGER",
    "event": {
      "type": "ENTITY_UPDATED",
      "blueprintIdentifier": "service"
    }
  }
}
```

```
{
  "identifier": "trigger",
  "title": "On Service Deleted",
  "config": {
    "type": "EVENT_TRIGGER",
    "event": {
      "type": "ENTITY_DELETED",
      "blueprintIdentifier": "service"
    }
  }
}
```

```
{
  "identifier": "trigger",
  "title": "On Any Service Change",
  "config": {
    "type": "EVENT_TRIGGER",
    "event": {
      "type": "ANY_ENTITY_CHANGE",
      "blueprintIdentifier": "service"
    }
  }
}
```

Triggered when a timer property on an entity expires:

```
{
  "identifier": "trigger",
  "title": "On TTL Expired",
  "config": {
    "type": "EVENT_TRIGGER",
    "event": {
      "type": "TIMER_EXPIRED",
      "blueprintIdentifier": "environment",
      "propertyIdentifier": "ttl"
    }
  }
}
```

## Published[â](#published "Direct link to Published")

The `published` field controls whether the trigger is active and listening for events. When set to `false`, the trigger will not respond to any events.

| Property    | Type      | Default | Description                                                                                               |
| ----------- | --------- | ------- | --------------------------------------------------------------------------------------------------------- |
| `published` | `boolean` | `true`  | When \`true\`, the trigger is active and will respond to events. When \`false\`, the trigger is disabled. |

This is useful for temporarily disabling a workflow without deleting it, or for creating workflows that are not yet ready for production use.

## Conditions[â](#conditions "Direct link to Conditions")

Add conditions to filter which events trigger the workflow using JQ expressions:

```
{
  "identifier": "trigger",
  "title": "On Production Service Updated",
  "config": {
    "type": "EVENT_TRIGGER",
    "event": {
      "type": "ENTITY_UPDATED",
      "blueprintIdentifier": "service"
    },
    "condition": {
      "type": "JQ",
      "expressions": [
        ".diff.after.properties.environment == \"production\""
      ],
      "combinator": "and"
    }
  }
}
```

### Condition properties[â](#condition-properties "Direct link to Condition properties")

| Property      | Description                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| `type`        | Must be `"JQ"`                                                                  |
| `expressions` | Array of JQ expressions that must evaluate to true                              |
| `combinator`  | How to combine expressions: `"and"` (all must match) or `"or"` (any must match) |

### Common condition patterns[â](#common-condition-patterns "Direct link to Common condition patterns")

* Property changed
* Property equals value
* Property changed to value
* Has relation

Check if a property value has changed:

```
{
  "expressions": [
    ".diff.before.properties.status != .diff.after.properties.status"
  ]
}
```

Filter for entities with a specific property value:

```
{
  "expressions": [
    ".diff.after.properties.tier == \"critical\""
  ]
}
```

Check if a property changed from any value to a specific value:

```
{
  "expressions": [
    ".diff.before.properties.status != \"deployed\"",
    ".diff.after.properties.status == \"deployed\""
  ],
  "combinator": "and"
}
```

Check if an entity has a specific relation set:

```
{
  "expressions": [
    ".diff.after.relations.team != null"
  ]
}
```

## Outputs[â](#outputs "Direct link to Outputs")

Event triggers store the full event object as outputs that can be referenced in subsequent nodes. Outputs are accessed using bracket notation `.outputs["<trigger-node-identifier>"].<field>`.

| Output                                                        | Description                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------ |
| `.outputs["<trigger-node-identifier>"].diff.before`           | The entity state before the change (null for created events) |
| `.outputs["<trigger-node-identifier>"].diff.after`            | The entity state after the change (null for deleted events)  |
| `.outputs["<trigger-node-identifier>"].action`                | The action type: `"CREATE"`, `"UPDATE"`, or `"DELETE"`       |
| `.outputs["<trigger-node-identifier>"].diff.after.blueprint`  | The blueprint identifier of the entity                       |
| `.outputs["<trigger-node-identifier>"].diff.after.identifier` | The identifier of the entity                                 |

### Entity structure[â](#entity-structure "Direct link to Entity structure")

The `diff.before` and `diff.after` objects have the following structure:

```
{
  "identifier": "my-service",
  "title": "My Service",
  "blueprint": "service",
  "properties": {
    "language": "python",
    "status": "running"
  },
  "relations": {
    "team": "backend-team"
  },
  "team": ["backend-team"],
  "icon": "Service"
}
```

### Using outputs in action nodes[â](#using-outputs-in-action-nodes "Direct link to Using outputs in action nodes")

This example shows how to reference event trigger outputs in an action node. Since the trigger node's identifier is `trigger`, outputs are accessed via `.outputs["trigger"]`:

```
{
  "config": {
    "type": "WEBHOOK",
    "url": "https://api.example.com/notify",
    "body": {
      "entityIdentifier": "{{ .outputs.trigger.diff.after.identifier }}",
      "entityTitle": "{{ .outputs.trigger.diff.after.title }}",
      "newStatus": "{{ .outputs.trigger.diff.after.properties.status }}",
      "previousStatus": "{{ .outputs.trigger.diff.before.properties.status }}",
      "action": "{{ .outputs.trigger.action }}"
    }
  }
}
```

## Examples[â](#examples "Direct link to Examples")

### Notify on critical service status change[â](#notify-on-critical-service-status-change "Direct link to Notify on critical service status change")

This workflow monitors critical services and sends a Slack notification when their status changes. It uses conditions to trigger only for services with `tier` set to critical.

**Workflow example (click to expand)**

```
{
  "identifier": "notify-critical-status",
  "title": "Notify on Critical Service Status Change",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "On Status Change",
      "config": {
        "type": "EVENT_TRIGGER",
        "event": {
          "type": "ENTITY_UPDATED",
          "blueprintIdentifier": "service"
        },
        "condition": {
          "type": "JQ",
          "expressions": [
            ".diff.after.properties.tier == \"critical\"",
            ".diff.before.properties.status != .diff.after.properties.status"
          ],
          "combinator": "and"
        }
      }
    },
    {
      "identifier": "send-notification",
      "title": "Send Slack Notification",
      "config": {
        "type": "WEBHOOK",
        "url": "https://hooks.slack.com/services/xxx",
        "method": "POST",
        "body": {
          "text": "Critical service {{ .outputs.trigger.diff.after.title }} status changed from {{ .outputs.trigger.diff.before.properties.status }} to {{ .outputs.trigger.diff.after.properties.status }}"
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "send-notification"
    }
  ]
}
```

### Clean up resources on environment deletion[â](#clean-up-resources-on-environment-deletion "Direct link to Clean up resources on environment deletion")

This workflow triggers when an environment entity is deleted and calls an external API to clean up the associated cloud resources.

**Workflow example (click to expand)**

```
{
  "identifier": "cleanup-environment",
  "title": "Cleanup on Environment Deletion",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "On Environment Deleted",
      "config": {
        "type": "EVENT_TRIGGER",
        "event": {
          "type": "ENTITY_DELETED",
          "blueprintIdentifier": "environment"
        }
      }
    },
    {
      "identifier": "cleanup",
      "title": "Trigger Cleanup",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.example.com/cleanup",
        "method": "POST",
        "body": {
          "environmentId": "{{ .outputs.trigger.diff.before.identifier }}",
          "environmentName": "{{ .outputs.trigger.diff.before.title }}",
          "cloudProvider": "{{ .outputs.trigger.diff.before.properties.cloudProvider }}"
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "cleanup"
    }
  ]
}
```

### Auto-expire TTL environments[â](#auto-expire-ttl-environments "Direct link to Auto-expire TTL environments")

This workflow uses a timer trigger to automatically mark environments as expired when their TTL property expires, then notifies the owner.

**Workflow example (click to expand)**

```
{
  "identifier": "expire-environment",
  "title": "Expire Environment on TTL",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "On TTL Expired",
      "config": {
        "type": "EVENT_TRIGGER",
        "event": {
          "type": "TIMER_EXPIRED",
          "blueprintIdentifier": "environment",
          "propertyIdentifier": "ttl"
        }
      }
    },
    {
      "identifier": "update-status",
      "title": "Mark as Expired",
      "config": {
        "type": "UPSERT_ENTITY",
        "blueprintIdentifier": "environment",
        "mapping": {
          "identifier": "{{ .outputs.trigger.diff.after.identifier }}",
          "properties": {
            "status": "expired"
          }
        }
      }
    },
    {
      "identifier": "notify",
      "title": "Notify Owner",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.example.com/notify",
        "body": {
          "message": "Environment {{ .outputs.trigger.diff.after.title }} has expired",
          "owner": "{{ .outputs.trigger.diff.after.relations.owner }}"
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "update-status"
    },
    {
      "sourceIdentifier": "update-status",
      "targetIdentifier": "notify"
    }
  ]
}
```
