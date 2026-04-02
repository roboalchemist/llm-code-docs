Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CanvasesAccessDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CanvasesAccessDeleteArguments

# Interface: CanvasesAccessDeleteArguments

Defined in: [packages/web-api/src/types/request/canvas.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L54)

## Extends {#extends}

* `CanvasID`.`Partial`<`ChannelIDs`\>.`TokenOverridable`.`Partial`<`UserIDs`\>

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

### channel_ids? {#channel_ids}

```text
optional channel_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L81)

#### Description {#description-1}

An array of channel IDs (must include at least one ID).

#### Inherited from {#inherited-from-1}

[`AdminConversationsBulkArchiveArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkArchiveArguments).[`channel_ids`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkArchiveArguments#channel_ids)

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```

* * *

### user_ids? {#user_ids}

```text
optional user_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L92)

#### Description {#description-3}

List of encoded user IDs.

#### Inherited from {#inherited-from-3}

[`AdminConversationsInviteArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsInviteArguments).[`user_ids`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsInviteArguments#user_ids)
