# Source: https://docs.port.io/actions-and-automations/define-automations/setup-action.md

# Set up backend

The automation's backend is the logic that you want to execute when a trigger event occurs. It will run on all entities tied to the blueprint specified in the automation's definition, whenever the trigger event occurs.

Port uses the same backend types for automations and for [self-service actions](/actions-and-automations/create-self-service-experiences/.md).

## Define the backend[â](#define-the-backend "Direct link to Define the backend")

The automation's backend is defined under the `Backend` tab of the automation creation form in Port's UI.<br /><!-- -->Let's break the definition down to two parts:

### Define your backend's type and metadata[â](#define-your-backends-type-and-metadata "Direct link to Define your backend's type and metadata")

In this section we provide information about the backend logic and its location, so that Port can access and run it.

Port uses the same backend types for both automations and [self-service actions](https://docs.port.io/actions-and-automations/create-self-service-experiences/).<br /><!-- -->For more information and examples for the available backend types, check out the [backend types](/actions-and-automations/setup-backend/.md) page.

Depending on the backend type you choose, you will need to provide different configuration parameters.

### Define the payload[â](#define-the-payload "Direct link to Define the payload")

When creating an automation, you can construct a JSON payload that will be sent to your backend upon every execution. You can use this to send data about the automation that you want your backend to have.

Still in the `Backend` tab, scroll down to the `Configure the invocation payload` section. This is where we define the automation's payload.

The payload is defined using JSON, and accessing your data is done using `jq`, wrapping each expression with `{{ }}`.

Here is an example for an automation payload:

```
{
  "port_context": {
    "runId": "{{ .run.id }}"
  }
}
```

`.run` available values

When the automation is triggered, the `.run` object includes only the run `id`.

You may have noticed that the example above also sends `{{ .run.id }}`. This is a unique identifier for each execution of the automation, and can be used to interact with the automation run in Port from your backend.

Now you might be thinking - *how do I know what data is available to me when constructing the payload?*<br /><!-- -->Enter `trigger data`.

#### Trigger data[â](#trigger-data "Direct link to Trigger data")

When a self-service action or automation is executed, Port creates an object that contains data about the execution.

This entire object is accessible to you when constructing the payload.<br /><!-- -->Depending on the [trigger type](/actions-and-automations/define-automations/setup-trigger.md), the object's structure will differ:

* Entity trigger
* Action run trigger

Below is an example of trigger data for an automation that triggers whenever a `service` entity is **updated**:

```
{
  "inputs": null,
  "trigger": {
    "by": {
      "orgId": "org_BneDtWovPqXaA2VZ",
      "userId": "auth0|62ceaea697ca00f09d7c4f45",
      "user": {
        "email": "example-user@test.com",
        "firstName": "SomeFirstName",
        "lastName": "SomeLastName",
        "phoneNumber": "",
        "picture": "",
        "providers": [],
        "status": "ACTIVE",
        "id": "auth0|62ceaea697ca00f09d7c4f45",
        "createdAt": "2024-06-09T09:57:50.444Z",
        "updatedAt": "2024-06-09T09:57:50.444Z"
      }
    },
    "origin": "AUTOMATION",
    "at": "2024-06-09T12:28:18.663Z"
  },
  "event": {
    "action": "UPDATE",
    "resourceType": "entity",
    "trigger": {
      "by": {
        "orgId": "org_BneDtWovPqXaA2VZ",
        "userId": "auth0|62ceaea697ca00f09d7c4f45"
      },
      "origin": "UI",
      "at": "2024-06-09T12:28:18.477Z"
    },
    "context": {
      "blueprintIdentifier": "service",
      "entityIdentifier": "example-service-identifier",
      "propertyIdentifier": null
    },
    "diff": {
      "before": {
        "identifier": "example-service-identifier",
        "title": "Example service",
        "icon": null,
        "blueprint": "service",
        "team": [
          "Rocket"
        ],
        "properties": {
          "latestVersion": "12.8.2",
          "language": "TypeScript",
          "one_hop_service_language": "Ruby",
          "two_hops_service_language": "Ruby",
          "repo": "https://github.com/some-org/example-service"
        },
        "relations": {
          "using": "rogue-service"
        },
        "createdAt": "2024-06-09T09:57:52.931Z",
        "createdBy": "60EsooJtOqimlekxrNh7nfr2iOgTcyLZ",
        "updatedAt": "2024-06-09T09:57:52.931Z",
        "updatedBy": "60EsooJtOqimlekxrNh7nfr2iOgTcyLZ"
      },
      "after": {
        "identifier": "example-service-identifier",
        "title": "Example service renamed",
        "icon": "Microservice",
        "blueprint": "service",
        "team": [
          "Rocket"
        ],
        "properties": {
          "latestVersion": "12.8.22",
          "language": "Python",
          "one_hop_service_language": "Ruby",
          "two_hops_service_language": "Ruby",
          "repo": "https://github.com/some-org/example-service"
        },
        "relations": {
          "using": "rogue-service"
        },
        "createdAt": "2024-06-09T09:57:52.931Z",
        "createdBy": "60EsooJtOqimlekxrNh7nfr2iOgTcyLZ",
        "updatedAt": "2024-06-09T12:28:18.628Z",
        "updatedBy": "auth0|62ceaea697ca00f09d7c4f45"
      }
    }
  },
  "entity": null,
  "action": {
    "identifier": "automation"
  },
  "run": {
    "id": "r_k86OUzq80jRlxFV0"
  }
}
```

The example above is for an automation that uses the `ENTITY_UPDATED` trigger event. The `event.diff` object contains data from `before` and `after` the update.

The other trigger events have the same structure, with the following differences:

* `ENTITY_CREATED` - In the `diff` object, `before` will be `null`, and `after` will contain the new entity data.

* `ENTITY_DELETED` - In the `diff` object, `before` will contain the entity data before deletion, and `after` will be `null`.

* `ANY_ENTITY_CHANGE` - The `diff` object will contain `before` and/or `after` data according to the entity change.

* `TIMER_PROPERTY_EXPIRED` - In the `diff` object, there will be an `after` object containing the entity data.

Below is an example of trigger data for an automation that triggers whenever an action run is **updated**:

Create in Port

```
{
  "inputs": null,
  "trigger": {
    "by": {
      "orgId": "org_BneDtWovPqXaA2VZ",
      "userId": "auth0|62ceaaa497ea00f09d7c4f41",
      "user": {
        "email": "test-admin-user@test.com",
        "firstName": "James",
        "lastName": "Hetfield",
        "status": "ACTIVE",
        "id": "auth0|82zea497e300f09d7c1f41",
        "createdAt": "2024-08-15T11:17:02.699Z",
        "updatedAt": "2024-08-15T11:17:02.699Z"
      }
    },
    "origin": "AUTOMATION",
    "at": "2024-08-15T12:30:05.569Z"
  },
  "event": {
    "id": "event_GH2680QIOEzwwNZB",
    "resourceType": "run",
    "action": "UPDATE",
    "trigger": {
      "by": {
        "orgId": "org_BneVtWovPbXaA6V6Z",
        "userId": "auth0|82zea497e300f09d7c1f41"
      },
      "origin": "UI",
      "at": "2024-08-15T12:30:05.505Z"
    },
    "context": {
      "action": {
        "identifier": "myActionId",
        "title": "Some action title",
        "trigger": {
          "type": "self-service",
          "operation": "CREATE",
          "userInputs": {
            "properties": {},
            "required": [],
            "order": []
          }
        },
        "invocationMethod": {
          "type": "WEBHOOK",
          "url": "https://example.com",
          "agent": false,
          "synchronized": false,
          "method": "POST",
          "headers": {
            "RUN_ID": "{{ .run.id }}"
          },
          "body": {
            "{{ spreadValue() }}": "{{ .inputs }}",
            "port_context": {
              "runId": "{{ .run.id }}"
            }
          }
        },
        "requiredApproval": false,
        "createdBy": "auth0|82zea497e300f09d7c1f41",
        "updatedBy": "auth0|82zea497e300f09d7c1f41",
        "createdAt": "2024-08-15T12:29:45.817Z",
        "updatedAt": "2024-08-15T12:29:45.817Z"
      }
    },
    "diff": {
      "before": {
        "id": "r_Q0YotCZMKxDLdlaU",
        "status": "IN_PROGRESS",
        // "blueprint" and "entity" will be available if the action is tied to a blueprint
        // (meaning that the action run is tied to an entity)
        "blueprint": {
          "identifier": "blueprintIdentifier",
          "title": "blueprintTitle",
          "icon": "blueprintIcon"
        },
        "entity": {
          "identifier": "entityIdentifier",
          "title": "entityTitle",
          "icon": "entityIcon",
        },
        "action": {
          "identifier": "myActionId",
          "title": null,
          "icon": null,
          "deleted": true
        },
        "source": "UI",
        "link": [],
        "requiredApproval": false,
        "properties": {},
        "createdAt": "2024-08-15T12:29:57.379Z",
        "updatedAt": "2024-08-15T12:29:57.379Z",
        "createdBy": "auth0|82zea497e300f09d7c1f41",
        "updatedBy": "auth0|82zea497e300f09d7c1f41",
        "payload": {
          "type": "WEBHOOK",
          "url": "https://example.com",
          "agent": false,
          "synchronized": false,
          "method": "POST",
          "headers": {
            "RUN_ID": "r_Q0YotCZMKxDLdlaU"
          },
          "body": {
            "port_context": {
              "runId": "r_Q0YotCZMKxDLdlaU"
            }
          }
        }
      },
      "after": {
        "id": "r_Q0YotCZMKxDLdlaU",
        "status": "IN_PROGRESS",
        // "blueprint" and "entity" will be available if the action is tied to a blueprint
        // (meaning that the action run is tied to an entity)
        "blueprint": {
          "identifier": "blueprintIdentifier",
          "title": "blueprintTitle",
          "icon": "blueprintIcon"
        },
        "entity": {
          "identifier": "entityIdentifier",
          "title": "entityTitle",
          "icon": "entityIcon",
        },
        "action": {
          "identifier": "myActionId",
          "title": null,
          "icon": null,
          "deleted": true
        },
        "source": "UI",
        "link": [],
        "requiredApproval": false,
        "properties": {},
        "createdAt": "2024-08-15T12:29:57.379Z",
        "updatedAt": "2024-08-15T12:30:05.481Z",
        "createdBy": "auth0|82zea497e300f09d7c1f41",
        "updatedBy": "auth0|82zea497e300f09d7c1f41",
        "payload": {
          "type": "WEBHOOK",
          "url": "https://example.com",
          "agent": false,
          "synchronized": false,
          "method": "POST",
          "headers": {
            "RUN_ID": "r_Q0YotCZMKxDLdlaU"
          },
          "body": {
            "port_context": {
              "runId": "r_Q0YotCZMKxDLdlaU"
            }
          }
        }
      }
    }
  },
  "entity": null,
  "action": {
    "identifier": "automation"
  },
  "run": {
    "id": "r_au3aJdlOHUO3d99n"
  }
}
```

The example above is for an automation that uses the `RUN_UPDATED` trigger event. The `event.diff` object contains data from `before` and `after` the update.

The other trigger events have the same structure, with the following differences:

* `RUN_CREATED` - In the `diff` object, `before` will be `null`, and `after` will contain the new action run data.

* `ANY_RUN_CHANGE` - The `diff` object will contain `before` and/or `after` data according to the entity change.

#### Pass user context to the backend[â](#pass-user-context-to-the-backend "Direct link to Pass user context to the backend")

You can access any value in the trigger data structure and add it to the payload. This is particularly useful for passing **user context** to your backend.

Port automatically captures the executing user's information (email, name, ID, etc.) in the trigger data. You can easily pass this information to your backend to implement features like audit trails, personalized workflows, or user-specific logic.

For example, to add the executing user's email to the payload, you can use the following expression:

```
{
  "executing_user_email": "{{.trigger.by.user.email}}"
}
```

You can also access other user properties like `{{.trigger.by.user.firstName}}`, `{{.trigger.by.user.lastName}}`, etc. To see all available user properties, you can use the testing method explained below.

Use the `Test JQ` button in the bottom-left corner to test your expressions against your automation and ensure you are sending the correct data.

Inspect the Full Object in `jq`

You can use the `jq` expression `{{ . }}` when testing to see the entire available object, and then drill down to the specific data you need.

#### Using secrets in the payload[â](#using-secrets-in-the-payload "Direct link to Using secrets in the payload")

Sensitive data such as tokens and passwords can be stored using [Port secrets](/sso-rbac/port-secrets/.md).

To use a secret in the payload, you can reference it using `{{ .secrets.<secret_name> }}`.

For example:

```
"token": "{{ .secrets.token_name }}"
```

Note that if your secret name contains hyphens or special characters, you should use bracket notation, for example:

```
"Authorization": "Bearer {{ .secrets["my-api-token"] }}"
```

#### spreadValue() function[â](#spreadvalue-function "Direct link to spreadValue() function")

You can use the `spreadValue()` function to add multiple keys to the root of the payload at once. This function will spread all of the keys under a given object.<br /><!-- -->A common use case for this function is to add all of the user inputs to the payload:

```
{
  "{{ spreadValue() }}": "{{ .inputs }}"
}
```

This will add all of the action's/automation's user inputs to the root of the payload, so that they can be accessed directly by your backend.

#### Using `jq` expressions in keys[â](#using-jq-expressions-in-keys "Direct link to using-jq-expressions-in-keys")

The keys in the payload can also be `jq` expressions.<br /><!-- -->For example, the following expression will add the `ref` key to the payload only if a `ref` input was provided when executing the action/automation:

```
{
  "{{if (.inputs | has(\"ref\")) then \"ref\" else null end}}": "{{.inputs.ref}}"
}
```

Using jq in keys

Note that if a **key** in the payload evaluates to `null` for any reason, the entire expression (key + value) will be omitted from the payload.

## Backend JSON structure[â](#backend-json-structure "Direct link to Backend JSON structure")

In some cases, you may prefer to define the backend configuration using a JSON object.<br /><!-- -->The backend is defined under the `invocationMethod` object in the automation's JSON structure.

Create in Port

```
{
  "identifier": "unique_id",
  "title": "Title",
  "icon": "icon_identifier",
  "description": "automation description",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "event_type",
      "blueprintIdentifier": "blueprint_id"
    },
    "condition": {
      "type": "JQ",
      "expressions": ["expression1", "expression2"],
      "combinator": "and"
    }
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://example.com",
    "headers": {
      "RUN_ID": "{{ .run.id }}"
    },
    "body": {
      "payload_key": "{{ some-jq-value }}"
    }
  },
  "publish": false
}
```

## Supported backends[â](#supported-backends "Direct link to Supported backends")

The **`type`** field defines the action's backend type, and can have one of the following values: `WEBHOOK`, `GITHUB`, `INTEGRATION_ACTION`, `GITLAB`, `KAFKA`, `UPSERT_ENTITY`.

Depending on the backend type you choose, the available fields will be different:

* Webhook
* Github app
* GitHub Ocean
* Gitlab
* Azure DevOps
* Kafka
* Create/update entity

`invocationMethod.type` should be set to `WEBHOOK`.

| Field          | Type      | Description                                                                                                                                                | Example values                   |
| -------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| `agent`        | `boolean` | Defines whether to use [Port Agent](/actions-and-automations/setup-backend/webhook/port-execution-agent/.md) for execution or not.                         | `true` or `false`                |
| `url`          | `string`  | Defines the webhook URL to which Port will send the action via an HTTP POST request.                                                                       | <https://example.com>            |
| `method`       | `string`  | Defines the HTTP method to be used for the request.                                                                                                        | `POST`, `PUT`, `DELETE`, `PATCH` |
| `synchronized` | `boolean` | If true, the action will be executed [synchronously](https://docs.port.io/create-self-service-experiences/setup-backend/webhook/#sync-vs-async-execution). | `true` or `false`                |
| `headers`      | `object`  | An object containing the payload headers to be sent to the webhook in each execution, in `"key":"value"` pairs.                                            |                                  |
| `body`         | `object`  | Defines the **payload** that will be sent to the backend upon execution of the action.<br />An object containing `"key":"value"` pairs.                    |                                  |

To learn more about this backend type, refer to the [webhook backend](/actions-and-automations/setup-backend/webhook/.md) documentation.

`invocationMethod.type` should be set to `GITHUB`.

| Field                  | Type      | Description                                                                                                                                    | Example values    |
| ---------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `org`                  | `string`  | The GitHub *organization* name.                                                                                                                | `port-labs`       |
| `repo`                 | `string`  | The GitHub *repository* name.                                                                                                                  | `port-docs`       |
| `workflow`             | `string`  | Defines the GitHub *workflow ID* to run (You can also pass the workflow file name as a string).                                                | `workflow.yml`    |
| `reportWorkflowStatus` | `boolean` | A flag to control whether to automatically update the Port `run` object status (SUCCESS/FAILURE) at the end of the workflow (default: `true`). | `true` or `false` |
| `workflowInputs`       | `object`  | Defines the **payload** that will be sent to the backend upon execution of the action.<br />An object containing `"key":"value"` pairs.        |                   |

To learn more about this backend type, refer to the [GitHub workflow backend](/actions-and-automations/setup-backend/github-workflow/.md) documentation.

The `invocationMethod.type` should be set to `INTEGRATION_ACTION`.

You can specify which integration to use using the `invocationMethod.installationId` field.

The `integrationActionType` is `dispatch_workflow`.

| Field                  | Type      | Description                                                                                                                                                        | Example values    |
| ---------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| `org`                  | `string`  | The GitHub *organization* name. Behavior depends on installation type: **hosted by Port** (hidden/prefilled in UI), **self-hosted** and **API** (always required). | `port-labs`       |
| `repo`                 | `string`  | The GitHub *repository* name.                                                                                                                                      | `port-docs`       |
| `workflow`             | `string`  | Defines the GitHub *workflow ID* to run (You can also pass the workflow file name as a string).                                                                    | `workflow.yml`    |
| `reportWorkflowStatus` | `boolean` | A flag to control whether to automatically update the Port `run` object status (SUCCESS/FAILURE) at the end of the workflow (default: `true`).                     | `true` or `false` |
| `workflowInputs`       | `object`  | Defines the **payload** that will be sent to the backend upon execution of the action.<br />An object containing `"key":"value"` pairs.                            |                   |

Token requirements

This invocation method works only with integrations that use Port machine tokens (organization-level tokens).<br /><!-- -->Personal tokens or service account tokens are not supported at the moment.

Secrets not supported

Secrets are not supported with this invocation method. This includes both encrypted user inputs and organization secrets (`.secrets.*`) in JQ templates.

To learn more about this backend type, refer to the [GitHub Ocean backend](/actions-and-automations/setup-backend/github-ocean/.md) documentation.

`invocationMethod.type` should be set to `GITLAB`.

| Field               | Type     | Description                                                                                                                                                                                      | Example values |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| `defaultRef`        | `string` | The default ref (branch/tag name) we want the action to use.<br />`defaultRef` can be overridden dynamically, by adding `ref` as user input.<br />Can only be used if `type` is set to `GITLAB`. |                |
| `projectName`       | `string` | The GitLab *project* name.<br />Can only be used if `type` is set to `GITLAB`.                                                                                                                   | `port`         |
| `groupName`         | `string` | The GitLab *group* name.<br />Can only be used if `type` is set to `GITLAB`.                                                                                                                     | `port-labs`    |
| `pipelineVariables` | `object` | Defines the **payload** that will be sent to the backend upon execution of the action.<br />An object containing `"key":"value"` pairs.                                                          |                |

To learn more about this backend type, refer to the [GitLab pipeline backend](/actions-and-automations/setup-backend/gitlab-pipeline/.md) documentation.

`invocationMethod.type` should be set to `AZURE_DEVOPS`.

| Field     | Type     | Description                                                                                                                             | Example values |
| --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `webhook` | `string` | The name of the webhook resource in the Azure YAML pipeline file.                                                                       |                |
| `org`     | `string` | The Azure DevOps organization in which the pipeline is located.                                                                         | `port-labs`    |
| `payload` | `object` | Defines the **payload** that will be sent to the backend upon execution of the action.<br />An object containing `"key":"value"` pairs. |                |

To learn more about this backend type, refer to the [Azure pipeline backend](/actions-and-automations/setup-backend/azure-pipeline/.md) documentation.

`invocationMethod.type` should be set to `KAFKA`.

| Field     | Type     | Description                                                                                                                             | Example values |
| --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `payload` | `object` | Defines the **payload** that will be sent to the backend upon execution of the action.<br />An object containing `"key":"value"` pairs. |                |

To learn more about this backend type, refer to the [Kafka backend](/actions-and-automations/setup-backend/kafka/.md) documentation.

`invocationMethod.type` should be set to `UPSERT_ENTITY`.

| Field                 | Type     | Description                                                                    | Example values             |
| --------------------- | -------- | ------------------------------------------------------------------------------ | -------------------------- |
| `blueprintIdentifier` | `string` | The identifier of the blueprint from which the entity will be created/updated. | `service`                  |
| `mapping`             | `object` | Defines the properties of the entity that will be created/updated.             | `{"name":"newEntityName"}` |

To learn more about this backend type, refer to the [create/update entity backend](/actions-and-automations/setup-backend/create-update-entity/.md) documentation.

To read more about each backend type, see the [backend types](/actions-and-automations/setup-backend/.md) page.
