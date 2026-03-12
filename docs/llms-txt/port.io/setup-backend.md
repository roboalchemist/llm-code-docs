# Source: https://docs.port.io/actions-and-automations/setup-backend.md

# Backend types

Port's self-service actions and automations support a variety of backends that can be used when triggered.

The process contains the following steps:

1. **The action is triggered in Port** - the trigger can either be a user executing a self-service action via the UI, or an automation triggering an action.
2. **The payload is sent to your backend** - the payload, as defined by the action's creator, is sent to your backend. The backend can be a URL, a dedicated Kafka topic or one of your CI/CD workflows/pipelines.
3. **Your backend receives the payload and handles the request** - depending on the action, your backend might open a PR, create a cloud resource, provision a new environment, or perform any other logic you would like.
4. **Your backend updates Port on the status of the execution** - You can [enrich the action run object](/actions-and-automations/reflect-action-progress/.md) in Port by adding logs, attaching links to other workflows or pipelines that help fulfill the request and add a final success/fail status once the action is complete.

## Supported backends[â](#supported-backends "Direct link to Supported backends")

Port supports the backends listed below.<br /><!-- -->Examples can be found under each type, under the `Self-service examples` section in the sidebar.

## [ðï¸<!-- --> <!-- -->Webhook](/actions-and-automations/setup-backend/webhook/.md)

[7 items](/actions-and-automations/setup-backend/webhook/.md)

## [ðï¸<!-- --> <!-- -->GitHub workflow via Ocean](/actions-and-automations/setup-backend/github-ocean/.md)

[The GitHub Ocean backend allows you to trigger GitHub workflows for your self-service actions and automations, using the GitHub Ocean integration.](/actions-and-automations/setup-backend/github-ocean/.md)

## [ðï¸<!-- --> <!-- -->Kafka topic](/actions-and-automations/setup-backend/kafka/.md)

[Port manages a Kafka topic per customer that publishes the execution run requests.](/actions-and-automations/setup-backend/kafka/.md)

## [ðï¸<!-- --> <!-- -->GitHub workflow](/actions-and-automations/setup-backend/github-workflow/.md)

[1 item](/actions-and-automations/setup-backend/github-workflow/.md)

## [ðï¸<!-- --> <!-- -->Jenkins pipeline](/actions-and-automations/setup-backend/jenkins-pipeline/.md)

[The Jenkins backend allows you to trigger Jenkins pipelines for your self-service actions and automations, using webhooks.](/actions-and-automations/setup-backend/jenkins-pipeline/.md)

## [ðï¸<!-- --> <!-- -->GitLab pipeline](/actions-and-automations/setup-backend/gitlab-pipeline/.md)

[2 items](/actions-and-automations/setup-backend/gitlab-pipeline/.md)

## [ðï¸<!-- --> <!-- -->Azure Pipeline](/actions-and-automations/setup-backend/azure-pipeline/.md)

[2 items](/actions-and-automations/setup-backend/azure-pipeline/.md)

## [ðï¸<!-- --> <!-- -->Create/update entity](/actions-and-automations/setup-backend/create-update-entity/.md)

[In some cases, we don't want to run complex logic via a workflow or pipeline, but rather want our backend to simply create or update an entity in our software catalog.](/actions-and-automations/setup-backend/create-update-entity/.md)

## [ðï¸<!-- --> <!-- -->Send Slack message](/actions-and-automations/setup-backend/send-slack-message/.md)

[The Send Slack message backend type allows you to send a message to a Slack channel, using a webhook URL.](/actions-and-automations/setup-backend/send-slack-message/.md)

## JSON structure[â](#json-structure "Direct link to JSON structure")

For both self-service actions and automations, the backend is defined under the `invocationMethod` object.<br /><!-- -->The following example shows a backend definition that uses a GitHub workflow:

```
{
  "invocationMethod": {
    "type": "GITHUB",
    "org": "Port-samples",
    "repo": "Port-actions",
    "workflow": "reportBug.yaml",
    "workflowInputs": {
      "port_context": {
        "user_first_name": "{{ .trigger.by.user.firstName }}",
        "user_last_name": "{{ .trigger.by.user.lastName }}",
        "runId": "{{.run.id}}"
      },
      "short_title": "{{ .inputs.short_title }}",
      "description": "{{ .inputs.description }}"
    },
    "reportWorkflowStatus": true
  },
}
```

### Invocation method structure fields[â](#invocation-method-structure-fields "Direct link to Invocation method structure fields")

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
