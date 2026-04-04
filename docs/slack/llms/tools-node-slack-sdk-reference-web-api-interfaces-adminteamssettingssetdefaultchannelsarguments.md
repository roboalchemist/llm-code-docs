Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminTeamsSettingsSetDefaultChannelsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminTeamsSettingsSetDefaultChannelsArguments

# Interface: AdminTeamsSettingsSetDefaultChannelsArguments

Defined in: [packages/web-api/src/types/request/admin/teams.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L32)

## Extends {#extends}

* `ChannelIDs`.`TeamID`.`TokenOverridable`

## Properties {#properties}

### channel_ids {#channel_ids}

```text
channel_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L81)

#### Description {#description}

An array of channel IDs (must include at least one ID).

#### Inherited from {#inherited-from}

```text
ChannelIDs.channel_ids
```

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L61)

#### Description {#description-1}

The encoded team ID.

#### Inherited from {#inherited-from-1}

```text
TeamID.team_id
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
