Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsInviteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsInviteArguments

# Interface: ConversationsInviteArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:109](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L109)

## Extends {#extends}

* `Channel`.`Users`.`TokenOverridable`

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

### force? {#force}

```text
optional force: boolean;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:114](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L114)

#### Description {#description-1}

When set to `true` and multiple user IDs are provided, continue inviting the valid ones while disregarding invalid IDs. Defaults to `false`.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```

* * *

### users {#users}

```text
users: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L49)

#### Description {#description-3}

A comma separated list of user IDs. Up to 1000 users may be listed.

#### Inherited from {#inherited-from-2}

```text
Users.users
```
