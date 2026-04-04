Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/SlackListsItemsInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsInfoResponse

# Type Alias: SlackListsItemsInfoResponse

```typescript
type SlackListsItemsInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/SlackListsItemsInfoResponse.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/SlackListsItemsInfoResponse.ts#L4)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### list? {#list}

```typescript
optional list: SlackList;
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

### record? {#record}

```typescript
optional record: SlackListsItemWithSubscription;
```

### subtasks? {#subtasks}

```typescript
optional subtasks: SlackListsItem[];
```
