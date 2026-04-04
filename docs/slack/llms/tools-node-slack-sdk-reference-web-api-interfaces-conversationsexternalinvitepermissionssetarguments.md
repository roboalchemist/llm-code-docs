Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsExternalInvitePermissionsSetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsExternalInvitePermissionsSetArguments

# Interface: ConversationsExternalInvitePermissionsSetArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:84](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L84)

## Extends {#extends}

* `Channel`.`Required`<`TargetTeam`\>.`TokenOverridable`

## Properties {#properties}

### action {#action}

```text
action: "downgrade" | "upgrade";
```

Defined in: [packages/web-api/src/types/request/conversations.ts:89](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L89)

#### Description {#description}

The type of action be taken: `upgrade` or `downgrade`.

* * *

### channel {#channel}

```text
channel: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L15)

#### Description {#description-1}

ID of conversation.

#### Inherited from {#inherited-from}

```text
Channel.channel
```

* * *

### target_team {#target_team}

```text
target_team: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:74](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L74)

#### Description {#description-2}

The team or enterprise id of the other party.

#### Inherited from {#inherited-from-1}

[`ConversationsApproveSharedInviteArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsApproveSharedInviteArguments).[`target_team`](/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsApproveSharedInviteArguments#target_team)

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
