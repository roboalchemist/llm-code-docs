Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CanvasesDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CanvasesDeleteArguments

# Interface: CanvasesDeleteArguments

Defined in: [packages/web-api/src/types/request/canvas.ts:84](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L84)

## Extends {#extends}

* `CanvasID`.`TokenOverridable`

## Properties {#properties}

### canvas_id {#canvas_id}

```text
canvas_id: string;
```

Defined in: [packages/web-api/src/types/request/canvas.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L6)

#### Description {#description}

Encoded ID of the canvas.

#### Inherited from {#inherited-from}

```text
CanvasID.canvas_id
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
