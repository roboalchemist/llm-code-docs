Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsKickArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsKickArguments

# Interface: ConversationsKickArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:129](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L129)

## Extends {#extends}

* `Channel`.`TokenOverridable`

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L15)

#### Description {#description}

ID of conversation.

#### Inherited from {#inherited-from}

```text
Channel.channel
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```

* * *

### user {#user}

```text
user: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:130](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L130)
