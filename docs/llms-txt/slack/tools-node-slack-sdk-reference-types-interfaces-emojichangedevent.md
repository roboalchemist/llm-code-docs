Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/EmojiChangedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / EmojiChangedEvent

# Interface: EmojiChangedEvent

Defined in: [events/emoji.ts:2](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L2)

## Properties {#properties}

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: [events/emoji.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L10)

* * *

### name? {#name}

```text
optional name: string;
```

Defined in: [events/emoji.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L6)

* * *

### names? {#names}

```text
optional names: string[];
```

Defined in: [events/emoji.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L5)

* * *

### new_name? {#new_name}

```text
optional new_name: string;
```

Defined in: [events/emoji.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L9)

* * *

### old_name? {#old_name}

```text
optional old_name: string;
```

Defined in: [events/emoji.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L8)

* * *

### subtype {#subtype}

```text
subtype: "add" | "remove" | "rename";
```

Defined in: [events/emoji.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L4)

* * *

### type {#type}

```text
type: "emoji_changed";
```

Defined in: [events/emoji.ts:3](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L3)

* * *

### value? {#value}

```text
optional value: string;
```

Defined in: [events/emoji.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/emoji.ts#L7)
