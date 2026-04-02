Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowsFeaturedListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowsFeaturedListArguments

# Interface: WorkflowsFeaturedListArguments

Defined in: [packages/web-api/src/types/request/workflows.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L17)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel_ids {#channel_ids}

```text
channel_ids: string[];
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L22)

#### Description {#description}

Comma-separated array of channel IDs to list featured workflows for.

#### Example {#example}

```text
["C012345678", "C987654321"]
```text

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
