Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CallsEndArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CallsEndArguments

# Interface: CallsEndArguments

Defined in: [packages/web-api/src/types/request/calls.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L48)

## Extends {#extends}

* `ID`.`TokenOverridable`

## Properties {#properties}

### duration? {#duration}

```text
optional duration: number;
```

Defined in: [packages/web-api/src/types/request/calls.ts:50](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L50)

#### Description {#description}

Call duration in seconds.

* * *

### id {#id}

```text
id: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L6)

#### Description {#description-1}

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

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
