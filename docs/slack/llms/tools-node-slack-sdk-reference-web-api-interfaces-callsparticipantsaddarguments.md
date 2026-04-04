Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CallsParticipantsAddArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CallsParticipantsAddArguments

# Interface: CallsParticipantsAddArguments

Defined in: [packages/web-api/src/types/request/calls.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L60)

## Extends {#extends}

* `ID`.`Users`.`TokenOverridable`

## Properties {#properties}

### id {#id}

```text
id: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L6)

#### Description {#description}

`id` returned when registering the call using the `calls.add` method.

#### Inherited from {#inherited-from}

```text
ID.id
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
users: CallUser[];
```

Defined in: [packages/web-api/src/types/request/calls.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L13)

#### Description {#description-2}

The list of users to add/remove to/from the Call.

#### See {#see}

[Using the Calls API: a note on Users](https://docs.slack.dev/apis/web-api/using-the-calls-api).

#### Inherited from {#inherited-from-2}

```text
Users.users
```
