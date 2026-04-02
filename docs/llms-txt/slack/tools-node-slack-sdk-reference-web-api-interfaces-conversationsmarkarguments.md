Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsMarkArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsMarkArguments

# Interface: ConversationsMarkArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:163](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L163)

## Extends {#extends}

* `MessageSpecifier`.`TokenOverridable`

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
MessageSpecifier.channel
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

### ts {#ts}

```text
ts: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L36)

#### Description {#description-2}

Unique identifier of message.

#### Inherited from {#inherited-from-2}

```text
MessageSpecifier.ts
```
