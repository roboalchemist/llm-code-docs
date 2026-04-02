Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsListConnectInvitesResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsListConnectInvitesResponse

# Type Alias: ConversationsListConnectInvitesResponse

```typescript
type ConversationsListConnectInvitesResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ConversationsListConnectInvitesResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ConversationsListConnectInvitesResponse.ts#L11)

## Type Declaration {#type-declaration}

### arg? {#arg}

```typescript
optional arg: string;
```

### error? {#error}

```typescript
optional error: string;
```

### invites? {#invites}

```typescript
optional invites: InviteElement[];
```

### needed? {#needed}

```typescript
optional needed: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```
