Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminTeamsCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminTeamsCreateArguments

# Interface: AdminTeamsCreateArguments

Defined in: [packages/web-api/src/types/request/admin/teams.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L11)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### team_description? {#team_description}

```text
optional team_description: string;
```

Defined in: [packages/web-api/src/types/request/admin/teams.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L17)

#### Description {#description}

Description for the team.

* * *

### team_discoverability? {#team_discoverability}

```text
optional team_discoverability: TeamDiscoverability;
```

Defined in: [packages/web-api/src/types/request/admin/teams.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L19)

#### Description {#description-1}

Who can join the team.

* * *

### team_domain {#team_domain}

```text
team_domain: string;
```

Defined in: [packages/web-api/src/types/request/admin/teams.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L13)

#### Description {#description-2}

Team domain (for example, slacksoftballteam). Domains are limited to 21 characters.

* * *

### team_name {#team_name}

```text
team_name: string;
```

Defined in: [packages/web-api/src/types/request/admin/teams.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/teams.ts#L15)

#### Description {#description-3}

Team name (for example, Slack Softball Team).

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```
