Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersProfileSetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersProfileSetArguments

# Interface: UsersProfileSetArguments

Defined in: [packages/web-api/src/types/request/users.ts:76](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L76)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### name? {#name}

```text
optional name: string;
```text

Defined in: [packages/web-api/src/types/request/users.ts:90](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L90)

#### Description {#description}

Name of a single profile field to set. If both `name` and `profile` are set, `name` takes precedence.

#### See {#see}

[\`users.profile.set\` Profile fields usage info](https://docs.slack.dev/reference/methods/users.profile.set#profile-fields).

* * *

### profile? {#profile}

```text
optional profile: Record<string, unknown>;
```text

Defined in: [packages/web-api/src/types/request/users.ts:83](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L83)

#### Description {#description-1}

Sets profile fields using a single argument. Collection of key:value pairs presented. At most 50 fields may be set. Each field name is limited to 255 characters.

#### See {#see-1}

[\`users.profile.set\` Profile fields usage info](https://docs.slack.dev/reference/methods/users.profile.set#profile-fields).

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text

* * *

### user? {#user}

```text
optional user: string;
```text

Defined in: [packages/web-api/src/types/request/users.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L85)

#### Description {#description-3}

ID of user to change. This argument may only be specified by admins on paid teams.

* * *

### value? {#value}

```text
optional value: string;
```text

Defined in: [packages/web-api/src/types/request/users.ts:95](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L95)

#### Description {#description-4}

Value to set for the profile field specified by `name`. Usable only if profile is not passed.

#### See {#see-2}

[\`users.profile.set\` Profile fields usage info](https://docs.slack.dev/reference/methods/users.profile.set#profile-fields).
