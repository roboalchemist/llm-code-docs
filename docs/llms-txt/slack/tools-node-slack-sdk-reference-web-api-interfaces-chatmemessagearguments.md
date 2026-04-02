Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChatMeMessageArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatMeMessageArguments

# Interface: ChatMeMessageArguments

Defined in: [packages/web-api/src/types/request/chat.ts:193](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L193)

## Extends {#extends}

* `ChannelAndText`.`TokenOverridable`

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
ChannelAndText.channel
```

* * *

### text {#text}

```text
text: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:56](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L56)

#### Description {#description-1}

Text of the message. If used in conjunction with `blocks` or `attachments`, `text` will be used as fallback text for notifications only.

#### Inherited from {#inherited-from-1}

```text
ChannelAndText.text
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
