Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CallsInfoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CallsInfoArguments

# Interface: CallsInfoArguments

Defined in: [packages/web-api/src/types/request/calls.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L54)

## Extends {#extends}

* `ID`.`TokenOverridable`

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
