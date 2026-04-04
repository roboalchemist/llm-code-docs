Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RemindersAddArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RemindersAddArguments

# Interface: RemindersAddArguments

Defined in: [packages/web-api/src/types/request/reminders.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reminders.ts#L17)

## Extends {#extends}

* `TokenOverridable`.`OptionalTeamAssignable`

## Properties {#properties}

### recurrence? {#recurrence}

```text
optional recurrence: ReminderRecurrence;
```text

Defined in: [packages/web-api/src/types/request/reminders.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reminders.ts#L37)

#### Description {#description}

Specify the repeating behavior of a reminder. If you set the sub-property `frequency` to `weekly`, you must also set the `weekdays` array to specify which days of the week to recur on.

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

### text {#text}

```text
text: string;
```text

Defined in: [packages/web-api/src/types/request/reminders.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reminders.ts#L19)

#### Description {#description-2}

The content of the reminder.

* * *

### time {#time}

```text
time: string | number;
```text

Defined in: [packages/web-api/src/types/request/reminders.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reminders.ts#L26)

#### Description {#description-3}

When this reminder should happen, one of:

* the Unix timestamp (up to five years from now),
* the number of seconds until the reminder (if within 24 hours), or
* a natural language description (Ex. "in 15 minutes," or "every Thursday").

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```text

* * *

### user? {#user}

```text
optional user: string;
```text

Defined in: [packages/web-api/src/types/request/reminders.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/reminders.ts#L32)

#### Description {#description-5}

No longer supported - reminders cannot be set for other users.

#### Deprecated {#deprecated}

#### See {#see}

[Changes to \`reminders.\*\` APIs announcement](https://docs.slack.dev/changelog/2023-07-its-later-already-for-stars-and-reminders).
