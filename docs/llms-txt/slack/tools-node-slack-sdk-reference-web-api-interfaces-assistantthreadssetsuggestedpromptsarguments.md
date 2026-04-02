Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AssistantThreadsSetSuggestedPromptsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AssistantThreadsSetSuggestedPromptsArguments

# Interface: AssistantThreadsSetSuggestedPromptsArguments

Defined in: [packages/web-api/src/types/request/assistant.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L16)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L18)

#### Description {#description}

Channel ID containing the assistant thread.

* * *

### prompts {#prompts}

```text
prompts: AssistantPrompt[];
```

Defined in: [packages/web-api/src/types/request/assistant.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L20)

#### Description {#description-1}

Prompt suggestions that appear when opening assistant thread.

* * *

### thread_ts {#thread_ts}

```text
thread_ts: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L22)

#### Description {#description-2}

Message timestamp of the thread.

* * *

### title? {#title}

```text
optional title: string;
```

Defined in: [packages/web-api/src/types/request/assistant.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/assistant.ts#L24)

#### Description {#description-3}

Title for the prompts.

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
