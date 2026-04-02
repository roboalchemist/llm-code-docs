Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/DndEndSnoozeResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DndEndSnoozeResponse

# Type Alias: DndEndSnoozeResponse

```typescript
type DndEndSnoozeResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/DndEndSnoozeResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/DndEndSnoozeResponse.ts#L11)

## Type Declaration {#type-declaration}

### dnd_enabled? {#dnd_enabled}

```typescript
optional dnd_enabled: boolean;
```

### error? {#error}

```typescript
optional error: string;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### next_dnd_end_ts? {#next_dnd_end_ts}

```typescript
optional next_dnd_end_ts: number;
```

### next_dnd_start_ts? {#next_dnd_start_ts}

```typescript
optional next_dnd_start_ts: number;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### provided? {#provided}

```typescript
optional provided: string;
```

### snooze_enabled? {#snooze_enabled}

```typescript
optional snooze_enabled: boolean;
```
