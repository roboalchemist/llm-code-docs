Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatUpdateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatUpdateArguments

# Type Alias: ChatUpdateArguments

```typescript
type ChatUpdateArguments = MessageContents & object & TokenOverridable & AsUser & LinkNames & Metadata & Parse & object;
```

Defined in: [packages/web-api/src/types/request/chat.ts:343](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L343)

## Type Declaration {#type-declaration}

### ts {#ts}

```typescript
ts: string;
```

#### Description {#description}

Timestamp of the message to be updated.

## Type Declaration {#type-declaration-1}

### file_ids? {#file_ids}

```typescript
optional file_ids: string[];
```

#### Description {#description-1}

Array of new file ids that will be sent with this message.

### reply_broadcast? {#reply_broadcast}

```typescript
optional reply_broadcast: boolean;
```

#### Description {#description-2}

Broadcast an existing thread reply to make it visible to everyone in the channel or conversation.
