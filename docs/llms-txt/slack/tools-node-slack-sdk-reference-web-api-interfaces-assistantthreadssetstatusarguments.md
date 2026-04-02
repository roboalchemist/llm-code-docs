Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AssistantThreadsSetStatusArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AssistantThreadsSetStatusArguments

# Interface: AssistantThreadsSetStatusArguments

Defined in: [packages/web-api/src/types/request/assistant.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L4)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L6)

#### Description {#description}

Channel ID containing the assistant thread.

* * *

### loading_messages? {#loading_messages}

```text
optional loading_messages: string[];
```

Defined in: [packages/web-api/src/types/request/assistant.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L12)

#### Description {#description-1}

The list of messages to rotate through as a loading indicator.

* * *

### status {#status}

```text
status: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L8)

#### Description {#description-2}

Status of the assistant (e.g. 'is thinking...')

* * *

### thread_ts {#thread_ts}

```text
thread_ts: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L10)

#### Description {#description-3}

Message timestamp of the thread.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```
