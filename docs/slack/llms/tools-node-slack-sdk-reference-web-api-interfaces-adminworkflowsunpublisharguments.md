Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminWorkflowsUnpublishArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminWorkflowsUnpublishArguments

# Interface: AdminWorkflowsUnpublishArguments

Defined in: [packages/web-api/src/types/request/admin/workflows.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/workflows.ts#L51)

## Extends {#extends}

* `WorkflowIDs`.`TokenOverridable`

## Properties {#properties}

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```

* * *

### workflow_ids {#workflow_ids}

```text
workflow_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/admin/workflows.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/workflows.ts#L12)

#### Description {#description-1}

Array of workflow IDs - maximum of 50 items.

#### Inherited from {#inherited-from-1}

```text
WorkflowIDs.workflow_ids
```
