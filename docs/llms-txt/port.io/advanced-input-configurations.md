# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/advanced-input-configurations.md

# Advanced input configurations

This page covers advanced configuration options for workflow user inputs, including dependencies, visibility controls, and dynamic defaults.

## Input dependencies[â](#input-dependencies "Direct link to Input dependencies")

Use the `dependsOn` property to create dependencies between inputs. When an input depends on another, it will be re-evaluated when the dependency changes.

```
{
  "properties": {
    "environment": {
      "type": "string",
      "title": "Environment",
      "enum": ["development", "staging", "production"]
    },
    "cluster": {
      "type": "string",
      "format": "entity",
      "blueprint": "cluster",
      "title": "Cluster",
      "dependsOn": ["environment"],
      "dataset": {
        "combinator": "and",
        "rules": [
          {
            "property": "environment",
            "operator": "=",
            "value": {
              "jqQuery": ".form.environment"
            }
          }
        ]
      }
    }
  }
}
```

In this example, the `cluster` input filters its available entities based on the selected `environment`.

## Visibility controls[â](#visibility-controls "Direct link to Visibility controls")

Control when inputs are visible using the `visible` property.

* Static
* Dynamic with JQ

```
{
  "hiddenInput": {
    "type": "string",
    "title": "Hidden Input",
    "visible": false
  }
}
```

```
{
  "properties": {
    "deploymentType": {
      "type": "string",
      "title": "Deployment Type",
      "enum": ["standard", "canary", "blue-green"]
    },
    "canaryPercentage": {
      "type": "number",
      "title": "Canary Percentage",
      "minimum": 1,
      "maximum": 100,
      "visible": {
        "jqQuery": ".form.deploymentType == \"canary\""
      },
      "dependsOn": ["deploymentType"]
    }
  }
}
```

The `canaryPercentage` input only appears when `deploymentType` is set to "canary".

## Dynamic defaults[â](#dynamic-defaults "Direct link to Dynamic defaults")

Set default values dynamically using JQ expressions.

* Based on other inputs
* Based on context
* Conditional defaults

```
{
  "properties": {
    "serviceName": {
      "type": "string",
      "title": "Service Name"
    },
    "repositoryName": {
      "type": "string",
      "title": "Repository Name",
      "default": {
        "jqQuery": ".form.serviceName + \"-repo\""
      },
      "dependsOn": ["serviceName"]
    }
  }
}
```

```
{
  "requestedBy": {
    "type": "string",
    "format": "user",
    "title": "Requested By",
    "default": {
      "jqQuery": ".trigger.by.user.email"
    },
    "readOnly": true
  }
}
```

```
{
  "properties": {
    "environment": {
      "type": "string",
      "title": "Environment",
      "enum": ["development", "production"]
    },
    "replicas": {
      "type": "number",
      "title": "Replicas",
      "default": {
        "jqQuery": "if .form.environment == \"production\" then 3 else 1 end"
      },
      "dependsOn": ["environment"]
    }
  }
}
```

## Read-only inputs[â](#read-only-inputs "Direct link to Read-only inputs")

Mark inputs as read-only to display values that users cannot modify:

```
{
  "workflowRunId": {
    "type": "string",
    "title": "Workflow Run ID",
    "default": {
      "jqQuery": ".run.id"
    },
    "readOnly": true
  }
}
```

## Input ordering[â](#input-ordering "Direct link to Input ordering")

Control the display order of inputs using the `order` property:

```
{
  "properties": {
    "name": { "type": "string", "title": "Name" },
    "environment": { "type": "string", "title": "Environment" },
    "description": { "type": "string", "title": "Description" }
  },
  "order": ["environment", "name", "description"]
}
```

## Example[â](#example "Direct link to Example")

This example shows a userInputs configuration that combines input dependencies, conditional defaults, and visibility controls for a deployment form.

**Deployment form configuration (click to expand)**

```
{
  "userInputs": {
    "properties": {
      "environment": {
        "type": "string",
        "title": "Environment",
        "enum": ["development", "staging", "production"],
        "enumColors": {
          "development": "blue",
          "staging": "orange",
          "production": "green"
        }
      },
      "service": {
        "type": "string",
        "format": "entity",
        "blueprint": "service",
        "title": "Service",
        "dependsOn": ["environment"],
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "property": "environment",
              "operator": "=",
              "value": { "jqQuery": ".form.environment" }
            }
          ]
        }
      },
      "version": {
        "type": "string",
        "title": "Version",
        "description": "Version tag to deploy"
      },
      "replicas": {
        "type": "number",
        "title": "Replicas",
        "default": {
          "jqQuery": "if .form.environment == \"production\" then 3 else 1 end"
        },
        "dependsOn": ["environment"],
        "minimum": 1,
        "maximum": 10
      },
      "enableMonitoring": {
        "type": "boolean",
        "title": "Enable Monitoring",
        "default": {
          "jqQuery": ".form.environment == \"production\""
        },
        "dependsOn": ["environment"]
      },
      "monitoringEndpoint": {
        "type": "string",
        "format": "url",
        "title": "Monitoring Endpoint",
        "visible": {
          "jqQuery": ".form.enableMonitoring == true"
        },
        "dependsOn": ["enableMonitoring"]
      }
    },
    "required": ["environment", "service", "version"],
    "order": [
      "environment",
      "service",
      "version",
      "replicas",
      "enableMonitoring",
      "monitoringEndpoint"
    ]
  }
}
```
