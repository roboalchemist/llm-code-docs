Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/DndTeamInfoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DndTeamInfoArguments

# Interface: DndTeamInfoArguments

Defined in: [packages/web-api/src/types/request/dnd.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/dnd.ts#L22)

## Extends {#extends}

* `TokenOverridable`.`OptionalTeamAssignable`

## Properties {#properties}

### team_id? {#team_id}

```text
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from}

```text
OptionalTeamAssignable.team_id
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

* * *

### users {#users}

```text
users: string;
```

Defined in: [packages/web-api/src/types/request/dnd.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/dnd.ts#L24)

#### Description {#description-2}

Comma-separated list of users to fetch Do Not Disturb status for.
