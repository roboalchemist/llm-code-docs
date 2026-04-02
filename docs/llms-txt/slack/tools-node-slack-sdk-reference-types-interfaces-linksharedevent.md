Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/LinkSharedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / LinkSharedEvent

# Interface: LinkSharedEvent

Defined in: [events/link-shared.ts:1](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L1)

## Properties {#properties}

### channel {#channel}

```
channel: string;
```

Defined in: [events/link-shared.ts:3](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L3)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/link-shared.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L14)

* * *

### is_bot_user_member {#is_bot_user_member}

```
is_bot_user_member: boolean;
```

Defined in: [events/link-shared.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L4)

* * *

### links {#links}

```
links: object[];
```

Defined in: [events/link-shared.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L8)

#### domain {#domain}

```
domain: string;
```

#### url {#url}

```
url: string;
```

* * *

### message_ts {#message_ts}

```
message_ts: string;
```

Defined in: [events/link-shared.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L6)

* * *

### source? {#source}

```
optional source: string;
```

Defined in: [events/link-shared.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L13)

* * *

### thread_ts? {#thread_ts}

```
optional thread_ts: string;
```

Defined in: [events/link-shared.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L7)

* * *

### type {#type}

```
type: "link_shared";
```

Defined in: [events/link-shared.ts:2](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L2)

* * *

### unfurl_id? {#unfurl_id}

```
optional unfurl_id: string;
```

Defined in: [events/link-shared.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L12)

* * *

### user {#user}

```
user: string;
```

Defined in: [events/link-shared.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/link-shared.ts#L5)
