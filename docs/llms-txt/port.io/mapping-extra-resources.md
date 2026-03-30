# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cicd/octopus-deploy/mapping-extra-resources.md

# Ingest additional resources

In addition to the supported resources listed in the [integration page](/build-your-software-catalog/sync-data-to-catalog/cicd/octopus-deploy/.md), other resources can be ingested, as described on this page.

This page will help you understand what kind of Octopus Deploy resources are supported by the integration and how to map them into Port.

## Check if a resource is supported[â](#check-if-a-resource-is-supported "Direct link to Check if a resource is supported")

The Octopus Deploy integration relies on Octopus' API-first architecture, which maintains a consistent pattern for most resources. This means that you can bring virtually any resource into Port, as long as it follows the standard API structure. Hereâs how to determine if a resource is supported:

1. Visit the [Octopus Deploy API Swagger documentation](https://demo.octopus.com/swaggerui/index.html) to see the available resources and their API structure.

2. **Check the resource path**: Determine if the API of the resource you want to integrate follows the standard pattern **`GET /{spaceId}/{resources}`**

   * **If the resource follows this pattern**: Great! It can be integrated.
   * **If not**: Please contact us or contribute by [adding support](https://ocean.getport.io/develop-an-integration/) to [the integration](https://github.com/port-labs/ocean/tree/main/integrations/octopus) yourself.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party API into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform, and perform other operations on existing fields and values from the integration API. ged

### Mapping the Resource to Port[â](#mapping-the-resource-to-port "Direct link to Mapping the Resource to Port")

After determining that the resource is supported by the API, you can map it to Port by following these steps:

* **Define the resource kind**: The value of `kind` should be the value of the resource in the api pattern **`GET /{spaceId}/{resources}`** without the trailing `s`. For example, if API path is **`GET /{spaceId}/runbooks`**, the value of `kind` should be `runbook`.
* **Define the selector**: The selector is a JQ query that filters the resources you want to ingest. If the query evaluates to `false`, the resource will be skipped.
* **Define the properties**: The properties are the fields of the Port entity. You can map the resource fields to the entity properties using JQ queries.
* **Define the blueprint**: The blueprint is the name of the Port entity blueprint that you want to use for the resource.
* **Define the relations**: You can define `relations` between the resource and other resources in Port by mapping the related fields.

## Example configurations[â](#example-configurations "Direct link to Example configurations")

Here are some examples of how to expand the integration to include additional resources

### Runbook[â](#runbook "Direct link to Runbook")

Runbook Blueprint

Create in Port

```
{
  "identifier": "octopusRunbook",
  "title": "Octopus Runbook",
  "icon": "Octopus",
  "description": "A runbook in Octopus Deploy",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The description of the runbook"
      },
      "lastModifiedOn": {
        "type": "string",
        "title": "Last Modified On",
        "format": "date-time",
        "description": "The date and time when the runbook was last modified"
      },
      "environmentScope": {
        "type": "string",
        "title": "Environment Scope",
        "description": "The scope of environments for the runbook"
      },
      "environments": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Environments",
        "description": "The environments associated with the runbook"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
},
```

Mapping configuration for Runbook

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: runbook
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusRunbook"'
          properties:
            description: .Description
            lastModifiedOn: .LastModifiedOn
            environmentScope: .EnvironmentScope
            environments: .Environments
          relations:
            space: .SpaceId
```

### Task[â](#task "Direct link to Task")

Task Blueprint

Create in Port

```
{
  "identifier": "octopusTask",
  "title": "Octopus Task",
  "icon": "Octopus",
  "description": "A task in Octopus Deploy",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The description of the task"
      },
      "state": {
        "type": "string",
        "title": "State",
        "description": "The current state of the task"
      },
      "isCompleted": {
        "type": "boolean",
        "title": "Is Completed",
        "description": "Indicates if the task is completed"
      },
      "completedTime": {
        "type": "string",
        "title": "Completed Time",
        "format": "date-time",
        "description": "The time when the task was completed"
      },
      "hasWarningsOrErrors": {
        "type": "boolean",
        "title": "Has Warnings or Errors",
        "description": "Indicates if the task encountered warnings or errors"
      },
      "finishedSuccessfully": {
        "type": "boolean",
        "title": "Finished Successfully",
        "description": "Indicates if the task finished successfully"
      },
      "duration": {
        "type": "string",
        "title": "Duration",
        "description": "The duration of the task"
      },
      "queueTime": {
        "type": "string",
        "title": "Queue Time",
        "format": "date-time",
        "description": "The time when the task was queued"
      },
      "startTime": {
        "type": "string",
        "title": "Start Time",
        "format": "date-time",
        "description": "The time when the task started"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Task

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: task
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusTask"'
          properties:
            description: .Description
            state: .State
            isCompleted: .IsCompleted
            completedTime: .CompletedTime
            hasWarningsOrErrors: .HasWarningsOrErrors
            finishedSuccessfully: .FinishedSuccessfully
            duration: .Duration
            queueTime: .QueueTime
            startTime: .StartTime
          relations:
            space: .SpaceId
```

### Team[â](#team "Direct link to Team")

Team Blueprint

Create in Port

```
{
  "identifier": "octopusTeam",
  "title": "Octopus Team",
  "icon": "Octopus",
  "description": "A team in Octopus Deploy",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The description of the team"
      },
      "canBeDeleted": {
        "type": "boolean",
        "title": "Can Be Deleted",
        "description": "Indicates if the team can be deleted"
      },
      "canBeRenamed": {
        "type": "boolean",
        "title": "Can Be Renamed",
        "description": "Indicates if the team can be renamed"
      },
      "canChangeMembers": {
        "type": "boolean",
        "title": "Can Change Members",
        "description": "Indicates if the team members can be changed"
      },
      "canChangeRoles": {
        "type": "boolean",
        "title": "Can Change Roles",
        "description": "Indicates if the team roles can be changed"
      },
      "memberUserIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Member User IDs",
        "description": "The IDs of the users who are members of the team"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Team

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: team
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusTeam"'
          properties:
            description: .Description
            canBeDeleted: .CanBeDeleted
            canBeRenamed: .CanBeRenamed
            canChangeMembers: .CanChangeMembers
            canChangeRoles: .CanChangeRoles
            memberUserIds: .MemberUserIds
          relations:
            space: .SpaceId
```

### WorkerPool[â](#workerpool "Direct link to WorkerPool")

WorkerPool Blueprint

Create in Port

```
{
  "identifier": "octopusWorkerPool",
  "title": "Octopus Worker Pool",
  "icon": "Octopus",
  "description": "A worker pool in Octopus Deploy",
  "schema": {
    "properties": {
      "workerPoolType": {
        "type": "string",
        "title": "Worker Pool Type",
        "description": "The type of the worker pool (e.g., StaticWorkerPool)"
      },
      "isDefault": {
        "type": "boolean",
        "title": "Is Default",
        "description": "Indicates if the worker pool is the default"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for WorkerPool

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: workerpool
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusWorkerPool"'
          properties:
            workerPoolType: .WorkerPoolType
            isDefault: .IsDefault
          relations:
            space: .SpaceId
```

### Worker[â](#worker "Direct link to Worker")

Worker Blueprint

Create in Port

```
{
  "identifier": "octopusWorker",
  "title": "Octopus Worker",
  "icon": "Octopus",
  "description": "A worker in Octopus Deploy",
  "schema": {
    "properties": {
      "operatingSystem": {
        "type": "string",
        "title": "Operating System",
        "description": "The operating system of the worker"
      },
      "healthStatus": {
        "type": "string",
        "title": "Health Status",
        "description": "The health status of the worker"
      },
      "isDisabled": {
        "type": "boolean",
        "title": "Is Disabled",
        "description": "Indicates if the worker is disabled"
      },
      "architecture": {
        "type": "string",
        "title": "Architecture",
        "description": "The architecture of the worker"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Team

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: worker
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusWorker"'
          properties:
            operatingSystem: .OperatingSystem
            healthStatus: .HealthStatus
            isDisabled: .IsDisabled
            architecture: .Architecture
          relations:
            space: .SpaceId
```

### Environment[â](#environment "Direct link to Environment")

Environment Blueprint

Create in Port

```
{
  "identifier": "octopusEnvironment",
  "title": "Octopus Environment",
  "icon": "Octopus",
  "description": "An environment in Octopus Deploy",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The description of the environment"
      },
      "allowDynamicInfrastructure": {
        "type": "boolean",
        "title": "Allow Dynamic Infrastructure",
        "description": "Indicates if dynamic infrastructure is allowed in this environment"
      },
      "useGuidedFailure": {
        "type": "boolean",
        "title": "Use Guided Failure",
        "description": "Indicates if guided failure mode is enabled for this environment"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Environment

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: environment
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusEnvironment"'
          properties:
            description: .Description
            allowDynamicInfrastructure: .AllowDynamicInfrastructure
            useGuidedFailure: .UseGuidedFailure
          relations:
            space: .SpaceId
```

### Proxy[â](#proxy "Direct link to Proxy")

Proxy Blueprint

Create in Port

```
{
  "identifier": "octopusProxy",
  "title": "Octopus Proxy",
  "icon": "Octopus",
  "description": "A proxy configuration in Octopus Deploy",
  "schema": {
    "properties": {
      "host": {
        "type": "string",
        "title": "Host",
        "description": "The hostname of the proxy"
      },
      "port": {
        "type": "integer",
        "title": "Port",
        "description": "The port used by the proxy"
      },
      "username": {
        "type": "string",
        "title": "Username",
        "description": "The username for authentication with the proxy"
      },
      "proxyType": {
        "type": "string",
        "title": "Proxy Type",
        "description": "The type of the proxy"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Proxy

Kind value

The value of `kind` should be `proxie` for Proxy resources. This is because of the pattern of the API endpoints discussed in the [mapping the resource to port](#mapping-the-resource-to-port) section.

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: proxie
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusProxy"'
          properties:
            host: .Host
            port: .Port
            username: .Username
            proxyType: .ProxyType
          relations:
            space: .SpaceId
```

### Account[â](#account "Direct link to Account")

Account Blueprint

Create in Port

```
{
  "identifier": "octopusAccount",
  "title": "Octopus Account",
  "icon": "Octopus",
  "description": "An account configuration in Octopus Deploy",
  "schema": {
    "properties": {
      "accountType": {
        "type": "string",
        "title": "Account Type",
        "description": "The type of the account, e.g., AmazonWebServicesAccount"
      },
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The description of the account"
      },
      "environmentIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Environment IDs",
        "description": "IDs of the environments associated with the account"
      },
      "tenantedDeploymentParticipation": {
        "type": "string",
        "title": "Tenanted Deployment Participation",
        "description": "Indicates the participation of the account in tenanted deployments"
      },
      "tenantIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Tenant IDs",
        "description": "IDs of the tenants associated with the account"
      },
      "tenantTags": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Tenant Tags",
        "description": "Tags of tenants associated with the account"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Account

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: account
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusAccount"'
          properties:
            accountType: .AccountType
            description: .Description
            environmentIds: .EnvironmentIds
            tenantedDeploymentParticipation: .TenantedDeploymentParticipation
            tenantIds: .TenantIds
            tenantTags: .TenantTags
          relations:
            space: .SpaceId
```

### Package[â](#package "Direct link to Package")

Package Blueprint

Create in Port

```
{
  "identifier": "octopusPackage",
  "title": "Octopus Package",
  "icon": "Octopus",
  "description": "A package stored in Octopus Deploy",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The description of the package"
      },
      "feedId": {
        "type": "string",
        "title": "Feed ID",
        "description": "ID of the feed associated with the package"
      },
      "fileExtension": {
        "type": "string",
        "title": "File Extension",
        "description": "The file extension of the package"
      },
      "version": {
        "type": "string",
        "title": "Version",
        "description": "The version of the package"
      },
      "hash": {
        "type": "string",
        "title": "Hash",
        "description": "The hash of the package for verification"
      },
      "packageSizeBytes": {
        "type": "integer",
        "title": "Package Size (Bytes)",
        "description": "The size of the package in bytes"
      },
      "published": {
        "type": "string",
        "title": "Published Date",
        "format": "date-time",
        "description": "The date the package was published"
      },
      "releaseNotes": {
        "type": "string",
        "title": "Release Notes",
        "description": "Notes provided for the release of the package"
      },
      "summary": {
        "type": "string",
        "title": "Summary",
        "description": "A summary of the package"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Package

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: package
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Title
          blueprint: '"octopusPackage"'
          properties:
            description: .Description
            feedId: .FeedId
            fileExtension: .FileExtension
            version: .Version
            hash: .Hash
            packageSizeBytes: .PackageSizeBytes
            published: .Published
            releaseNotes: .ReleaseNotes
            summary: .Summary
          relations:
            space: .SpaceId
```

### Subscription[â](#subscription "Direct link to Subscription")

Subscription Blueprint

Create in Port

```
{
  "identifier": "octopusSubscription",
  "title": "Octopus Subscription",
  "icon": "Octopus",
  "description": "An event notification subscription in Octopus Deploy",
  "schema": {
    "properties": {
      "name": {
        "type": "string",
        "title": "Name",
        "description": "The name of the subscription"
      },
      "type": {
        "type": "string",
        "title": "Type",
        "description": "The type of the subscription"
      },
      "isDisabled": {
        "type": "boolean",
        "title": "Is Disabled",
        "description": "Indicates if the subscription is disabled"
      },
      "emailFrequencyPeriod": {
        "type": "string",
        "title": "Email Frequency Period",
        "description": "The frequency at which email notifications are sent"
      },
      "emailPriority": {
        "type": "string",
        "title": "Email Priority",
        "description": "The priority of email notifications"
      },
      "webhookURI": {
        "type": "string",
        "title": "Webhook URI",
        "description": "The URI for the webhook"
      },
      "webhookTimeout": {
        "type": "string",
        "title": "Webhook Timeout",
        "description": "The timeout setting for the webhook"
      },
      "lastModifiedBy": {
        "type": "string",
        "title": "Last Modified By",
        "description": "The user who last modified the subscription"
      },
      "lastModifiedOn": {
        "type": "string",
        "title": "Last Modified On",
        "format": "date-time",
        "description": "The date and time when the subscription was last modified"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "space": {
      "title": "Space",
      "description": "The space to which this project belongs",
      "target": "octopusSpace",
      "required": false,
      "many": false
    }
  }
}
```

Mapping configuration for Subscription

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: subscription
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusSubscription"'
          properties:
            type: .Type
            isDisabled: .IsDisabled
            emailFrequencyPeriod: .EventNotificationSubscription.EmailFrequencyPeriod
            emailPriority: .EventNotificationSubscription.EmailPriority
            webhookURI: .EventNotificationSubscription.WebhookURI
            webhookTimeout: .EventNotificationSubscription.WebhookTimeout
            lastModifiedBy: .LastModifiedBy
            lastModifiedOn: .LastModifiedOn
          relations:
            space: .SpaceId
```
