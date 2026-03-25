# Source: https://docs.port.io/workflows/build-workflows/action-nodes/upsert-entity.md

# Upsert entity

The upsert entity action node creates or updates entities in your Port software catalog. If an entity with the specified identifier exists, it will be updated; otherwise, a new entity will be created.

## Configuration[â](#configuration "Direct link to Configuration")

| Field                 | Type                          | Description                                                                 |
| --------------------- | ----------------------------- | --------------------------------------------------------------------------- |
| `type`                | `"UPSERT_ENTITY"`             | **Required.** Must be `"UPSERT_ENTITY"`                                     |
| `blueprintIdentifier` | `string`                      | **Required.** The blueprint to create/update the entity in                  |
| `mapping`             | `object`                      | **Required.** Entity field mappings                                         |
| `onFailure`           | `'continue'` \| `'terminate'` | Whether to continue the workflow if this node fails. Default: `'terminate'` |

### Mapping fields[â](#mapping-fields "Direct link to Mapping fields")

| Field        | Type                   | Description                                                    |
| ------------ | ---------------------- | -------------------------------------------------------------- |
| `identifier` | `string`               | The entity identifier. If omitted, Port will auto-generate one |
| `title`      | `string`               | The entity title                                               |
| `team`       | `string` \| `string[]` | Team(s) owning the entity                                      |
| `icon`       | `string`               | Icon for the entity                                            |
| `properties` | `object`               | Entity property values                                         |
| `relations`  | `object`               | Entity relation values                                         |

## Basic example[â](#basic-example "Direct link to Basic example")

Create a deployment entity with properties from the trigger inputs and a timestamp:

```
{
  "identifier": "create-deployment",
  "title": "Create Deployment Entity",
  "config": {
    "type": "UPSERT_ENTITY",
    "blueprintIdentifier": "deployment",
    "mapping": {
      "identifier": "{{ .outputs.trigger.service }}-{{ .outputs.trigger.environment }}-{{ .outputs.trigger.version }}",
      "title": "{{ .outputs.trigger.service }} v{{ .outputs.trigger.version }}",
      "properties": {
        "version": "{{ .outputs.trigger.version }}",
        "environment": "{{ .outputs.trigger.environment }}",
        "deployedAt": "{{ now | todateiso8601 }}"
      },
      "relations": {
        "service": "{{ .outputs.trigger.service }}"
      }
    }
  }
}
```

## Update existing entity[â](#update-existing-entity "Direct link to Update existing entity")

When the identifier matches an existing entity, only the specified fields are updated. This example updates a service's status and deployment timestamp:

```
{
  "identifier": "update-service-status",
  "title": "Update Service Status",
  "config": {
    "type": "UPSERT_ENTITY",
    "blueprintIdentifier": "service",
    "mapping": {
      "identifier": "{{ .outputs.trigger.service }}",
      "properties": {
        "status": "deployed",
        "lastDeployedAt": "{{ now | todateiso8601 }}",
      }
    }
  }
}
```

## Using with event triggers[â](#using-with-event-triggers "Direct link to Using with event triggers")

Update the triggering entity based on workflow logic. This example marks an entity as reviewed when an event trigger fires:

```
{
  "identifier": "mark-reviewed",
  "title": "Mark as Reviewed",
  "config": {
    "type": "UPSERT_ENTITY",
    "blueprintIdentifier": "{{ .outputs.trigger.diff.after.blueprint }}",
    "mapping": {
      "identifier": "{{ .outputs.trigger.diff.after.identifier }}",
      "properties": {
        "reviewStatus": "reviewed",
        "reviewedAt": "{{ now | todateiso8601 }}"
      }
    }
  }
}
```

## Setting relations[â](#setting-relations "Direct link to Setting relations")

Use the `relations` field to link entities together. Relations can be single (one-to-one) or multi (one-to-many).

* Single relation
* Multi-relation (array)
* Dynamic multi-relation

```
{
  "mapping": {
    "identifier": "my-deployment",
    "relations": {
      "service": "{{ .outputs.trigger.service }}",
      "environment": "{{ .outputs.trigger.environment }}"
    }
  }
}
```

```
{
  "mapping": {
    "identifier": "my-service",
    "relations": {
      "dependencies": ["service-a", "service-b", "service-c"]
    }
  }
}
```

```
{
  "mapping": {
    "identifier": "my-service",
    "relations": {
      "dependencies": "{{ .outputs.trigger.dependencies | fromjson }}"
    }
  }
}
```

## Setting team ownership[â](#setting-team-ownership "Direct link to Setting team ownership")

Use the `team` field to assign ownership to one or more teams.

* Single team
* Multiple teams

```
{
  "mapping": {
    "identifier": "my-service",
    "team": "{{ .outputs.trigger.owningTeam }}"
  }
}
```

```
{
  "mapping": {
    "identifier": "my-service",
    "team": ["team-a", "team-b"]
  }
}
```

## Examples[â](#examples "Direct link to Examples")

### Create environment on request[â](#create-environment-on-request "Direct link to Create environment on request")

A complete workflow that creates a new environment entity when a user submits a self-service request with environment details and TTL:

**Workflow example (click to expand)**

```
{
  "identifier": "create-env-workflow",
  "title": "Create Environment",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "Request Environment",
      "config": {
        "type": "SELF_SERVE_TRIGGER",
        "userInputs": {
          "properties": {
            "name": {
              "type": "string",
              "title": "Environment Name"
            },
            "type": {
              "type": "string",
              "title": "Type",
              "enum": ["development", "staging", "production"]
            },
            "ttlDays": {
              "type": "number",
              "title": "TTL (Days)",
              "default": 7
            }
          },
          "required": ["name", "type"]
        }
      }
    },
    {
      "identifier": "create-entity",
      "title": "Create Environment Entity",
      "config": {
        "type": "UPSERT_ENTITY",
        "blueprintIdentifier": "environment",
        "mapping": {
          "identifier": "{{ .outputs.trigger.name | lower | replace \" \" \"-\" }}",
          "title": "{{ .outputs.trigger.name }}",
          "team": "{{ .outputs.trigger.team }}",
          "properties": {
            "type": "{{ .outputs.trigger.type }}",
            "status": "provisioning",
            "createdAt": "{{ now | todateiso8601 }}",
            "expiresAt": "{{ now + (.outputs[\"trigger\"].ttlDays * 24 * 3600) | todateiso8601 }}"
          }
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "trigger",
      "targetIdentifier": "create-entity"
    }
  ]
}
```

### Update status after external action[â](#update-status-after-external-action "Direct link to Update status after external action")

Chain a webhook call with an entity update to record external API results in Port:

**Workflow example (click to expand)**

```
{
  "nodes": [
    {
      "identifier": "call_api",
      "title": "Call External API",
      "config": {
        "type": "WEBHOOK",
        "url": "https://api.example.com/provision",
        "method": "POST",
        "body": {
          "resourceName": "{{ .outputs.trigger.name }}"
        }
      }
    },
    {
      "identifier": "update-entity",
      "title": "Update Entity Status",
      "config": {
        "type": "UPSERT_ENTITY",
        "blueprintIdentifier": "resource",
        "mapping": {
          "identifier": "{{ .outputs.trigger.name }}",
          "properties": {
            "status": "provisioned",
            "externalId": "{{ .outputs.call_api.response.data.resourceId }}"
          }
        }
      }
    }
  ],
  "connections": [
    {
      "sourceIdentifier": "call_api",
      "targetIdentifier": "update-entity"
    }
  ]
}
```
