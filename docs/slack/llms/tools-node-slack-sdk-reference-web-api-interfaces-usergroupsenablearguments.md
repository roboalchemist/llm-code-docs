Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsergroupsEnableArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsergroupsEnableArguments

# Interface: UsergroupsEnableArguments

Defined in: [packages/web-api/src/types/request/usergroups.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L26)

## Extends {#extends}

* `TokenOverridable`.`OptionalTeamAssignable`.`UsergroupsIncludeCount`

## Properties {#properties}

### include_count? {#include_count}

```text
optional include_count: boolean;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L6)

#### Description {#description}

Include the number of users in each User Group.

#### Inherited from {#inherited-from}

```text
UsergroupsIncludeCount.include_count
```text

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-1}

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

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```text

* * *

### usergroup {#usergroup}

```text
usergroup: string;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L28)

#### Description {#description-3}

The encoded ID of the User Group to enable.
