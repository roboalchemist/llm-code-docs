Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsCanvasesCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsCanvasesCreateArguments

# Interface: ConversationsCanvasesCreateArguments

Defined in: [packages/web-api/src/types/request/canvas.ts:93](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L93)

## Extends {#extends}

* `ChannelID`.`TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L85)

#### Description {#description}

Encoded channel ID.

#### Inherited from {#inherited-from}

```text
ChannelID.channel_id
```

* * *

### document_content? {#document_content}

```text
optional document_content: DocumentContent;
```

Defined in: [packages/web-api/src/types/request/canvas.ts:95](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L95)

#### Description {#description-1}

Structure describing the type and contents of the Canvas being created.

* * *

### title? {#title}

```text
optional title: string;
```

Defined in: [packages/web-api/src/types/request/canvas.ts:97](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/canvas.ts#L97)

#### Description {#description-2}

Title of the newly created canvas.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
