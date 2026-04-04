Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminTeamsSettingsSetDescriptionArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminTeamsSettingsSetDescriptionArguments

# Interface: AdminTeamsSettingsSetDescriptionArguments

Defined in: [packages/web-api/src/types/request/admin/teams.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L35)

## Extends {#extends}

* `TeamID`.`TokenOverridable`

## Properties {#properties}

### description {#description}

```text
description: string;
```

Defined in: [packages/web-api/src/types/request/admin/teams.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L37)

#### Description {#description-1}

The new description for the workspace.

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L61)

#### Description {#description-2}

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

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
