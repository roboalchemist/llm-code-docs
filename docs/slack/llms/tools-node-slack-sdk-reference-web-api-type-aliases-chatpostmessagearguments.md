Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatPostMessageArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatPostMessageArguments

# Type Alias: ChatPostMessageArguments

```typescript
type ChatPostMessageArguments = TokenOverridable & MessageContents & ReplyInThread & Authorship & Parse & LinkNames & ChatPostMessageMetadata & Unfurls & object;
```

Defined in: [packages/web-api/src/types/request/chat.ts:209](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L209)

## Type Declaration {#type-declaration}

### mrkdwn? {#mrkdwn}

```typescript
optional mrkdwn: boolean;
```

#### Description {#description}

Disable Slack markup parsing by setting to `false`. Enabled by default.
