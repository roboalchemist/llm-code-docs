Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MigrationExchangeArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MigrationExchangeArguments

# Interface: MigrationExchangeArguments

Defined in: [packages/web-api/src/types/request/migration.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/migration.ts#L4)

## Extends {#extends}

* `TokenOverridable`.`OptionalTeamAssignable`

## Properties {#properties}

### team_id? {#team_id}

```text
optional team_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from}

```text
OptionalTeamAssignable.team_id
```text

* * *

### to_old? {#to_old}

```text
optional to_old: boolean;
```text

Defined in: [packages/web-api/src/types/request/migration.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/migration.ts#L8)

#### Description {#description-1}

Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```text

* * *

### users {#users}

```text
users: string;
```text

Defined in: [packages/web-api/src/types/request/migration.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/migration.ts#L6)

#### Description {#description-3}

A comma-separated list of user IDs, up to 400 per request.
