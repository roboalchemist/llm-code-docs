Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersAssignArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersAssignArguments

# Interface: AdminUsersAssignArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L54)

## Extends {#extends}

* `TeamID`.`UserID`.`Partial`<`ChannelIDs`\>.`IsRestricted`.`IsUltraRestricted`.`TokenOverridable`

## Properties {#properties}

### channel_ids? {#channel_ids}

```text
optional channel_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L81)

#### Description {#description}

An array of channel IDs (must include at least one ID).

#### Inherited from {#inherited-from}

[`AdminConversationsBulkArchiveArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkArchiveArguments).[`channel_ids`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkArchiveArguments#channel_ids)

* * *

### is_restricted? {#is_restricted}

```text
optional is_restricted: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L15)

#### Description {#description-1}

Set to `true` if user should be added to the workspace as a guest.

#### Inherited from {#inherited-from-1}

```text
IsRestricted.is_restricted
```

* * *

### is_ultra_restricted? {#is_ultra_restricted}

```text
optional is_ultra_restricted: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L20)

#### Description {#description-2}

Set to `true` if user should be added to the workspace as a guest.

#### Inherited from {#inherited-from-2}

```text
IsUltraRestricted.is_ultra_restricted
```

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L61)

#### Description {#description-3}

The encoded team ID.

#### Inherited from {#inherited-from-3}

```text
TeamID.team_id
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-4}

```text
TokenOverridable.token
```

* * *

### user_id {#user_id}

```text
user_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:96](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L96)

#### Description {#description-5}

Encoded user ID.

#### Inherited from {#inherited-from-5}

```text
UserID.user_id
```
