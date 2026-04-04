Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsCreateArguments

# Interface: ConversationsCreateArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:75](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L75)

## Extends {#extends}

* `IsPrivate`.`TokenOverridable`.`OptionalTeamAssignable`

## Properties {#properties}

### is_private? {#is_private}

```text
optional is_private: boolean;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L32)

#### Description {#description}

Whether the channel should be private.

#### Inherited from {#inherited-from}

```text
IsPrivate.is_private
```

* * *

### name {#name}

```text
name: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:77](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L77)

#### Description {#description-1}

Name of the public or private channel to create.

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-2}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-1}

```text
OptionalTeamAssignable.team_id
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```
