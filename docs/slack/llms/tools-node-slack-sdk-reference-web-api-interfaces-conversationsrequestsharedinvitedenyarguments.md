Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsRequestSharedInviteDenyArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsRequestSharedInviteDenyArguments

# Interface: ConversationsRequestSharedInviteDenyArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:217](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L217)

## Extends {#extends}

* `InviteID`.`Message`.`TokenOverridable`

## Properties {#properties}

### invite_id {#invite_id}

```text
invite_id: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L28)

#### Description {#description}

ID of the invite.

#### Inherited from {#inherited-from}

```text
InviteID.invite_id
```

* * *

### message? {#message}

```text
optional message: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:40](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L40)

#### Description {#description-1}

A message to send to the user who requested the invite.

#### Inherited from {#inherited-from-1}

```text
Message.message
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
