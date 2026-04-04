Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsOpenArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsOpenArguments

# Type Alias: ConversationsOpenArguments

```typescript
type ConversationsOpenArguments = Channel | Users & TokenOverridable & object;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:169](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L169)

## Type Declaration {#type-declaration}

### prevent_creation? {#prevent_creation}

```typescript
optional prevent_creation: boolean;
```

#### Description {#description}

Do not create a direct message or multi-person direct message. This is used to see if there is an existing dm or mpdm.

### return_im? {#return_im}

```typescript
optional return_im: boolean;
```

#### Description {#description-1}

Indicates you want the full IM channel definition in the response.
