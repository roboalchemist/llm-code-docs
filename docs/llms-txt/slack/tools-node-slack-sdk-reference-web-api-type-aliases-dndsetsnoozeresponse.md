Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/DndSetSnoozeResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DndSetSnoozeResponse

# Type Alias: DndSetSnoozeResponse

```typescript
type DndSetSnoozeResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/DndSetSnoozeResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/DndSetSnoozeResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
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

### snooze_enabled? {#snooze_enabled}

```typescript
optional snooze_enabled: boolean;
```

### snooze_endtime? {#snooze_endtime}

```typescript
optional snooze_endtime: number;
```

### snooze_is_indefinite? {#snooze_is_indefinite}

```typescript
optional snooze_is_indefinite: boolean;
```

### snooze_remaining? {#snooze_remaining}

```typescript
optional snooze_remaining: number;
```
