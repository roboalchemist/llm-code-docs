Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminTeamsSettingsSetDiscoverabilityArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminTeamsSettingsSetDiscoverabilityArguments

# Interface: AdminTeamsSettingsSetDiscoverabilityArguments

Defined in: [packages/web-api/src/types/request/admin/teams.ts:41](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L41)

## Extends {#extends}

* `TeamID`.`TokenOverridable`

## Properties {#properties}

### discoverability {#discoverability}

```text
discoverability: TeamDiscoverability;
```

Defined in: [packages/web-api/src/types/request/admin/teams.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L43)

#### Description {#description}

This workspace's discovery setting.

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L61)

#### Description {#description-1}

The encoded team ID.

#### Inherited from {#inherited-from}

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

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
