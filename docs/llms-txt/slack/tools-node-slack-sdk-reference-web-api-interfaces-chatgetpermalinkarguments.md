Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChatGetPermalinkArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatGetPermalinkArguments

# Interface: ChatGetPermalinkArguments

Defined in: [packages/web-api/src/types/request/chat.ts:190](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L190)

## Extends {#extends}

* `ChannelAndMessageTS`.`TokenOverridable`

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L22)

#### Description {#description}

Channel ID for the message.

#### Inherited from {#inherited-from}

```text
ChannelAndMessageTS.channel
```

* * *

### message_ts {#message_ts}

```text
message_ts: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:30](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L30)

#### Description {#description-1}

Timestamp of the message.

#### Inherited from {#inherited-from-1}

```text
ChannelAndMessageTS.message_ts
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```
