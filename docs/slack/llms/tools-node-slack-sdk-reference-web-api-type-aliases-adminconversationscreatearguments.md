Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminConversationsCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsCreateArguments

# Type Alias: AdminConversationsCreateArguments

```typescript
type AdminConversationsCreateArguments = TokenOverridable & WorkspaceAccess & object;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L85)

## Type Declaration {#type-declaration}

### description? {#description}

```typescript
optional description: string;
```

#### Description {#description-1}

Description of the public or private channel to create.

### is_private {#is_private}

```typescript
is_private: boolean;
```

#### Description {#description-2}

When `true`, creates a private channel instead of a public channel.

### name {#name}

```typescript
name: string;
```

#### Description {#description-3}

Name of the public or private channel to create.
