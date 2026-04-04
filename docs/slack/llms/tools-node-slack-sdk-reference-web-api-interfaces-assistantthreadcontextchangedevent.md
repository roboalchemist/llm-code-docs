Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AssistantThreadContextChangedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AssistantThreadContextChangedEvent

# Interface: AssistantThreadContextChangedEvent

Defined in: packages/types/dist/events/assistant.d.ts:15

## Properties {#properties}

### assistant_thread {#assistant_thread}

```text
assistant_thread: object;
```

Defined in: packages/types/dist/events/assistant.d.ts:17

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

Defined in: packages/types/dist/events/assistant.d.ts:27

* * *

### type {#type}

```text
type: "assistant_thread_context_changed";
```

Defined in: packages/types/dist/events/assistant.d.ts:16
