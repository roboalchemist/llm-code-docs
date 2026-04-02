Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminWorkflowsPermissionsLookupArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminWorkflowsPermissionsLookupArguments

# Interface: AdminWorkflowsPermissionsLookupArguments

Defined in: [packages/web-api/src/types/request/admin/workflows.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/workflows.ts#L22)

## Extends {#extends}

* `WorkflowIDs`.`TokenOverridable`

## Properties {#properties}

### max_workflow_triggers? {#max_workflow_triggers}

```text
optional max_workflow_triggers: number;
```

Defined in: [packages/web-api/src/types/request/admin/workflows.ts:27](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/workflows.ts#L27)

#### Description {#description}

Maximum number of triggers to fetch for each workflow when determining overall run permissions. Defaults to `100`. Maximum of `1000`.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

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

#### Description {#description-2}

Array of workflow IDs - maximum of 50 items.

#### Inherited from {#inherited-from-1}

```text
WorkflowIDs.workflow_ids
```
