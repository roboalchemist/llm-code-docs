Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsergroupsUsersListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsergroupsUsersListArguments

# Interface: UsergroupsUsersListArguments

Defined in: [packages/web-api/src/types/request/usergroups.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L51)

## Extends {#extends}

* `TokenOverridable`.`OptionalTeamAssignable`

## Properties {#properties}

### include_disabled? {#include_disabled}

```text
optional include_disabled: boolean;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:55](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L55)

#### Description {#description}

Allow results that involve disabled User Groups.

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

* * *

### usergroup {#usergroup}

```text
usergroup: string;
```text

Defined in: [packages/web-api/src/types/request/usergroups.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/usergroups.ts#L53)

#### Description {#description-3}

The encoded ID of the User Group to list users for.
