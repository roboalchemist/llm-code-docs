Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatScheduleMessageArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatScheduleMessageArguments

# Type Alias: ChatScheduleMessageArguments

```typescript
type ChatScheduleMessageArguments = TokenOverridable & MessageContents & object & ReplyInThread & Parse & LinkNames & AsUser & Metadata & Unfurls;
```

Defined in: [packages/web-api/src/types/request/chat.ts:222](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L222)

## Type Declaration {#type-declaration}

### post_at {#post_at}

```typescript
post_at: string | number;
```

#### Description {#description}

Unix EPOCH timestamp of time in future to send the message.
