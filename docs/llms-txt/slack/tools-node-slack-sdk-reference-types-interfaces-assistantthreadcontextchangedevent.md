Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/AssistantThreadContextChangedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / AssistantThreadContextChangedEvent

# Interface: AssistantThreadContextChangedEvent

Defined in: [events/assistant.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/assistant.ts#L16)

## Properties {#properties}

### assistant_thread {#assistant_thread}

```text
assistant_thread: object;
```

Defined in: [events/assistant.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/assistant.ts#L18)

#### channel_id {#channel_id}

```text
channel_id: string;
```

#### context {#context}

```text
context: object;
```

##### context.channel_id? {#contextchannel_id}

```text
optional channel_id: string;
```

##### context.enterprise_id? {#contextenterprise_id}

```text
optional enterprise_id: string | null;
```

##### context.team_id? {#contextteam_id}

```text
optional team_id: string;
```

#### thread_ts {#thread_ts}

```text
thread_ts: string;
```

#### user_id {#user_id}

```text
user_id: string;
```

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: [events/assistant.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/assistant.ts#L28)

* * *

### type {#type}

```text
type: "assistant_thread_context_changed";
```

Defined in: [events/assistant.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/assistant.ts#L17)
