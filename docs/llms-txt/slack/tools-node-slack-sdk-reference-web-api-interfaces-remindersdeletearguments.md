Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RemindersDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RemindersDeleteArguments

# Interface: RemindersDeleteArguments

Defined in: [packages/web-api/src/types/request/reminders.ts:45](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reminders.ts#L45)

## Extends {#extends}

* `TokenOverridable`.`OptionalTeamAssignable`

## Properties {#properties}

### reminder {#reminder}

```text
reminder: string;
```text

Defined in: [packages/web-api/src/types/request/reminders.ts:47](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reminders.ts#L47)

#### Description {#description}

The ID of the reminder to delete.

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-1}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from}

```text
OptionalTeamAssignable.team_id
```text

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
