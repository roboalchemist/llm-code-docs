Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminWorkflowsCollaboratorsRemoveArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminWorkflowsCollaboratorsRemoveArguments

# Interface: AdminWorkflowsCollaboratorsRemoveArguments

Defined in: [packages/web-api/src/types/request/admin/workflows.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/workflows.ts#L19)

## Extends {#extends}

* `CollaboratorIDs`.`WorkflowIDs`.`TokenOverridable`

## Properties {#properties}

### collaborator_ids {#collaborator_ids}

```text
collaborator_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/admin/workflows.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/workflows.ts#L7)

#### Description {#description}

Array of collaborators (encoded user IDs) - maximum of 50 items.

#### Inherited from {#inherited-from}

```text
CollaboratorIDs.collaborator_ids
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

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

#### Inherited from {#inherited-from-2}

```text
WorkflowIDs.workflow_ids
```
