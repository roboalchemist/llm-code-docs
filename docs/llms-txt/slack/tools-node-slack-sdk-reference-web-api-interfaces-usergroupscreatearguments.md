Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsergroupsCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsergroupsCreateArguments

# Interface: UsergroupsCreateArguments

Defined in: [packages/web-api/src/types/request/usergroups.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L10)

## Extends {#extends}

* `TokenOverridable`.`OptionalTeamAssignable`.`UsergroupsIncludeCount`

## Properties {#properties}

### channels? {#channels}

```text
optional channels: string;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L14)

#### Description {#description}

A comma separated string of encoded channel IDs for which the User Group uses as a default.

* * *

### description? {#description-1}

```text
optional description: string;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L16)

#### Description {#description-2}

A short description of the User Group.

* * *

### handle? {#handle}

```text
optional handle: string;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L18)

#### Description {#description-3}

A mention handle. Must be unique among channels, users and User Groups.

* * *

### include_count? {#include_count}

```text
optional include_count: boolean;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L6)

#### Description {#description-4}

Include the number of users in each User Group.

#### Inherited from {#inherited-from}

```text
UsergroupsIncludeCount.include_count
```text

* * *

### name {#name}

```text
name: string;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L12)

#### Description {#description-5}

A name for the User Group. Must be unique among User Groups.

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-6}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-1}

```text
OptionalTeamAssignable.team_id
```text

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-7}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```text
