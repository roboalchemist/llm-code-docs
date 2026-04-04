Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/DndSetSnoozeArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DndSetSnoozeArguments

# Interface: DndSetSnoozeArguments

Defined in: [packages/web-api/src/types/request/dnd.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/dnd.ts#L17)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### num_minutes {#num_minutes}

```text
num_minutes: number;
```

Defined in: [packages/web-api/src/types/request/dnd.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/dnd.ts#L19)

#### Description {#description}

Number of minutes, from now, to snooze until.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```
