Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChatDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatDeleteArguments

# Interface: ChatDeleteArguments

Defined in: [packages/web-api/src/types/request/chat.ts:181](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L181)

## Extends {#extends}

* `ChannelAndTS`.`AsUser`.`TokenOverridable`

## Properties {#properties}

### as_user? {#as_user}

```text
optional as_user: boolean;
```

Defined in: [packages/web-api/src/types/request/chat.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L38)

#### Description {#description}

Pass `true` to act as the authed user with [\`chat:write:user\` scope](https://docs.slack.dev/reference/scopes/chat.write). Bot users in this context are considered authed users. If unused or `false`, the message will be acted upon with [\`chat:write:bot\` scope](https://docs.slack.dev/reference/scopes/chat.write).

#### Inherited from {#inherited-from}

```text
AsUser.as_user
```

* * *

### channel {#channel}

```text
channel: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L22)

#### Description {#description-1}

Channel ID for the message.

#### Inherited from {#inherited-from-1}

```text
ChannelAndTS.channel
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

* * *

### ts {#ts}

```text
ts: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L26)

#### Description {#description-3}

Timestamp of the message.

#### Inherited from {#inherited-from-3}

```text
ChannelAndTS.ts
```
