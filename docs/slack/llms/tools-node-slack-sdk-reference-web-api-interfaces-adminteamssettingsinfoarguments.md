Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminTeamsSettingsInfoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminTeamsSettingsInfoArguments

# Interface: AdminTeamsSettingsInfoArguments

Defined in: [packages/web-api/src/types/request/admin/teams.ts:29](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L29)

## Extends {#extends}

* `TeamID`.`TokenOverridable`

## Properties {#properties}

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L61)

#### Description {#description}

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

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
