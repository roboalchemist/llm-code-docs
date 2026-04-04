Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatPostEphemeralArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatPostEphemeralArguments

# Type Alias: ChatPostEphemeralArguments

```typescript
type ChatPostEphemeralArguments = TokenOverridable & MessageContents & object & Authorship & Parse & LinkNames & Partial<ThreadTS>;
```

Defined in: [packages/web-api/src/types/request/chat.ts:196](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L196)

## Type Declaration {#type-declaration}

### user {#user}

```typescript
user: string;
```

#### Description {#description}

`id` of the user who will receive the ephemeral message. The user should be in the channel specified by the `channel` argument.
