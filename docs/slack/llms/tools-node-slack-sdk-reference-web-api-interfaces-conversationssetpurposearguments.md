Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsSetPurposeArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsSetPurposeArguments

# Interface: ConversationsSetPurposeArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:237](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L237)

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

### purpose {#purpose}

```text
purpose: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:239](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L239)

#### Description {#description-1}

A new, specialer purpose.

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
