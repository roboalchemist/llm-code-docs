Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminInviteRequestsApproveArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminInviteRequestsApproveArguments

# Interface: AdminInviteRequestsApproveArguments

Defined in: [packages/web-api/src/types/request/admin/inviteRequests.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/inviteRequests.ts#L9)

## Extends {#extends}

* `InviteRequestID`.`Required`<`OptionalTeamAssignable`\>.`TokenOverridable`

## Properties {#properties}

### invite_request_id {#invite_request_id}

```text
invite_request_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/inviteRequests.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/inviteRequests.ts#L5)

#### Description {#description}

ID of the request to invite.

#### Inherited from {#inherited-from}

```text
InviteRequestID.invite_request_id
```

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-1}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-1}

[`AdminUsergroupsAddChannelsArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsergroupsAddChannelsArguments).[`team_id`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsergroupsAddChannelsArguments#team_id)

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
