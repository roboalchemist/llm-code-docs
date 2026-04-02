Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ReactionsAddArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ReactionsAddArguments

# Interface: ReactionsAddArguments

Defined in: [packages/web-api/src/types/request/reactions.ts:21](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reactions.ts#L21)

## Extends {#extends}

* `MessageArgument`.`TokenOverridable`.`ReactionName`

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:111](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L111)

#### Description {#description}

Channel where the message was posted.

#### Inherited from {#inherited-from}

```text
MessageArgument.channel
```text

* * *

### name {#name}

```text
name: string;
```text

Defined in: [packages/web-api/src/types/request/reactions.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reactions.ts#L18)

#### Description {#description-1}

Reaction (emoji) name.

#### Inherited from {#inherited-from-1}

```text
ReactionName.name
```text

* * *

### timestamp {#timestamp}

```text
timestamp: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:113](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L113)

#### Description {#description-2}

Timestamp of the message.

#### Inherited from {#inherited-from-2}

```text
MessageArgument.timestamp
```text

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```text
TokenOverridable.token
```text
