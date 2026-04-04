Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatUnfurlArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatUnfurlArguments

# Type Alias: ChatUnfurlArguments

```typescript
type ChatUnfurlArguments = ChatUnfurlUnfurls | ChatUnfurlMetadata & UnfurlTarget & TokenOverridable & object;
```

Defined in: [packages/web-api/src/types/request/chat.ts:294](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L294)

## Type Declaration {#type-declaration}

### user_auth_blocks? {#user_auth_blocks}

```typescript
optional user_auth_blocks: (KnownBlock | Block)[];
```

#### Description {#description}

Provide a JSON based array of structured blocks presented as URL-encoded string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior.

### user_auth_message? {#user_auth_message}

```typescript
optional user_auth_message: string;
```

#### Description {#description-1}

Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior. Provides two buttons, Not now or Never ask me again.

### user_auth_required? {#user_auth_required}

```typescript
optional user_auth_required: boolean;
```

#### Description {#description-2}

Set to `true` to indicate the user must install your Slack app to trigger unfurls for this domain. Defaults to `false`.

### user_auth_url? {#user_auth_url}

```typescript
optional user_auth_url: string;
```

#### Description {#description-3}

Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.
