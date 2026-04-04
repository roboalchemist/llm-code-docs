Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/EmojiChangedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / EmojiChangedEvent

# Interface: EmojiChangedEvent

Defined in: packages/types/dist/events/emoji.d.ts:1

## Properties {#properties}

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: packages/types/dist/events/emoji.d.ts:9

* * *

### name? {#name}

```text
optional name: string;
```

Defined in: packages/types/dist/events/emoji.d.ts:5

* * *

### names? {#names}

```text
optional names: string[];
```

Defined in: packages/types/dist/events/emoji.d.ts:4

* * *

### new_name? {#new_name}

```text
optional new_name: string;
```

Defined in: packages/types/dist/events/emoji.d.ts:8

* * *

### old_name? {#old_name}

```text
optional old_name: string;
```

Defined in: packages/types/dist/events/emoji.d.ts:7

* * *

### subtype {#subtype}

```text
subtype: "add" | "remove" | "rename";
```

Defined in: packages/types/dist/events/emoji.d.ts:3

* * *

### type {#type}

```text
type: "emoji_changed";
```

Defined in: packages/types/dist/events/emoji.d.ts:2

* * *

### value? {#value}

```text
optional value: string;
```

Defined in: packages/types/dist/events/emoji.d.ts:6
