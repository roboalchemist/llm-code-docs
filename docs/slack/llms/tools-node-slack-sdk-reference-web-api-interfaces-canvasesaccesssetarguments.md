Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CanvasesAccessSetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CanvasesAccessSetArguments

# Interface: CanvasesAccessSetArguments

Defined in: [packages/web-api/src/types/request/canvas.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L61)

## Extends {#extends}

* `CanvasID`.`Partial`<`ChannelIDs`\>.`TokenOverridable`.`Partial`<`UserIDs`\>

## Properties {#properties}

### access_level {#access_level}

```text
access_level: "read" | "write";
```

Defined in: [packages/web-api/src/types/request/canvas.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L63)

#### Description {#description}

Desired level of access.

* * *

### canvas_id {#canvas_id}

```text
canvas_id: string;
```

Defined in: [packages/web-api/src/types/request/canvas.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L6)

#### Description {#description-1}

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

#### Description {#description-2}

An array of channel IDs (must include at least one ID).

#### Inherited from {#inherited-from-1}

[`AdminConversationsBulkArchiveArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkArchiveArguments).[`channel_ids`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkArchiveArguments#channel_ids)

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

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

#### Description {#description-4}

List of encoded user IDs.

#### Inherited from {#inherited-from-3}

[`AdminConversationsInviteArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsInviteArguments).[`user_ids`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsInviteArguments#user_ids)
