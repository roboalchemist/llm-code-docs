Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsRequestSharedInviteApproveArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsRequestSharedInviteApproveArguments

# Interface: ConversationsRequestSharedInviteApproveArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:195](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L195)

## Extends {#extends}

* `InviteID`.`Partial`<`ChannelID`\>.`TokenOverridable`

## Properties {#properties}

### channel_id? {#channel_id}

```text
optional channel_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L85)

#### Description {#description}

Encoded channel ID.

#### Inherited from {#inherited-from}

[`AdminConversationsArchiveArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsArchiveArguments).[`channel_id`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsArchiveArguments#channel_id)

* * *

### invite_id {#invite_id}

```text
invite_id: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L28)

#### Description {#description-1}

ID of the invite.

#### Inherited from {#inherited-from-1}

```text
InviteID.invite_id
```

* * *

### is_external_limited? {#is_external_limited}

```text
optional is_external_limited: boolean;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:203](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L203)

#### Description {#description-2}

Whether the invited team will have post-only permissions in the channel. Will override the value on the requested invite.

* * *

### message? {#message}

```text
optional message: object;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:205](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L205)

#### is_override {#is_override}

```text
is_override: boolean;
```

##### Description {#description-3}

When `true`, will override the user specified message. Otherwise, `text` will be appended to the user specified message on the invite request.

#### text {#text}

```text
text: string;
```

##### Description {#description-4}

Text to include along with the email invite.

#### Description {#description-5}

Optional additional messaging to attach to the invite approval message.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-6}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```
