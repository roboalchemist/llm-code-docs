Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AssistantThreadsSetTitleArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AssistantThreadsSetTitleArguments

# Interface: AssistantThreadsSetTitleArguments

Defined in: [packages/web-api/src/types/request/assistant.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L35)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L37)

#### Description {#description}

Channel ID containing the assistant thread.

* * *

### thread_ts {#thread_ts}

```text
thread_ts: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L39)

#### Description {#description-1}

Message timestamp of the thread.

* * *

### title {#title}

```text
title: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:41](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L41)

#### Description {#description-2}

Title of the thread.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```
