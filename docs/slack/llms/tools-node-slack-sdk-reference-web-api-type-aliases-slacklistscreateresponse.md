Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/SlackListsCreateResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsCreateResponse

# Type Alias: SlackListsCreateResponse

```typescript
type SlackListsCreateResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/SlackListsCreateResponse.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/SlackListsCreateResponse.ts#L4)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### list_id? {#list_id}

```typescript
optional list_id: string;
```

### list_metadata? {#list_metadata}

```typescript
optional list_metadata: object;
```

#### list_metadata.schema? {#list_metadataschema}

```typescript
optional schema: SlackListsSchemaColumnResponse[];
```

#### list_metadata.subtask_schema? {#list_metadatasubtask_schema}

```typescript
optional subtask_schema: SlackListsSchemaColumnResponse[];
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
