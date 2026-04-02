Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsDeclineSharedInviteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsDeclineSharedInviteArguments

# Interface: ConversationsDeclineSharedInviteArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L81)

## Extends {#extends}

* `InviteID`.`TargetTeam`.`TokenOverridable`

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

### target_team? {#target_team}

```text
optional target_team: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:74](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L74)

#### Description {#description-1}

The team or enterprise id of the other party.

#### Inherited from {#inherited-from-1}

```text
TargetTeam.target_team
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
