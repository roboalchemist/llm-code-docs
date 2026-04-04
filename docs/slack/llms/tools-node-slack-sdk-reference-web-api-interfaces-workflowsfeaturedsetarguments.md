Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowsFeaturedSetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowsFeaturedSetArguments

# Interface: WorkflowsFeaturedSetArguments

Defined in: [packages/web-api/src/types/request/workflows.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L39)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L43)

#### Description {#description}

Channel to set featured workflow in.

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

Defined in: [packages/web-api/src/types/request/workflows.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L48)

#### Description {#description-2}

Comma-separated array of trigger IDs that will replace any existing featured workflows in the channel; max 15

#### Example {#example}

```text
["Ft012345", "Ft012346"]
```text
