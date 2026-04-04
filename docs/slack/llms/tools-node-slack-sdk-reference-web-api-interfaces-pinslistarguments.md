Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/PinsListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PinsListArguments

# Interface: PinsListArguments

Defined in: [packages/web-api/src/types/request/pins.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/pins.ts#L6)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```text

Defined in: [packages/web-api/src/types/request/pins.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/pins.ts#L8)

#### Description {#description}

Channel to get pinned items for.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text
