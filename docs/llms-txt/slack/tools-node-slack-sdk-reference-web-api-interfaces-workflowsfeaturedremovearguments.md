Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowsFeaturedRemoveArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowsFeaturedRemoveArguments

# Interface: WorkflowsFeaturedRemoveArguments

Defined in: [packages/web-api/src/types/request/workflows.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L26)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:30](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L30)

#### Description {#description}

Channel to remove featured workflow from.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text

* * *

### trigger_ids {#trigger_ids}

```text
trigger_ids: string[];
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L35)

#### Description {#description-2}

Comma-separated array of trigger IDs to remove; max 15

#### Example {#example}

```text
["Ft012345", "Ft012346"]
```text
