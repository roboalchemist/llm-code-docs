Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/RtmStartResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RtmStartResponse

# Type Alias: RtmStartResponse

```typescript
type RtmStartResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/RtmStartResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/RtmStartResponse.ts#L11)

## Type Declaration {#type-declaration}

### accept_tos_url? {#accept_tos_url}

```typescript
optional accept_tos_url: string;
```

### bots? {#bots}

```typescript
optional bots: Bot[];
```

### cache_ts? {#cache_ts}

```typescript
optional cache_ts: number;
```

### cache_ts_version? {#cache_ts_version}

```typescript
optional cache_ts_version: string;
```

### cache_version? {#cache_version}

```typescript
optional cache_version: string;
```

### can_manage_shared_channels? {#can_manage_shared_channels}

```typescript
optional can_manage_shared_channels: boolean;
```

### channels? {#channels}

```typescript
optional channels: Channel[];
```

### dnd? {#dnd}

```typescript
optional dnd: Dnd;
```

### error? {#error}

```typescript
optional error: string;
```

### groups? {#groups}

```typescript
optional groups: Group[];
```

### ims? {#ims}

```typescript
optional ims: Im[];
```

### is_europe? {#is_europe}

```typescript
optional is_europe: boolean;
```

### latest_event_ts? {#latest_event_ts}

```typescript
optional latest_event_ts: string;
```

### links? {#links}

```typescript
optional links: Links;
```

### mobile_app_requires_upgrade? {#mobile_app_requires_upgrade}

```typescript
optional mobile_app_requires_upgrade: boolean;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### non_threadable_channels? {#non_threadable_channels}

```typescript
optional non_threadable_channels: string[];
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### provided? {#provided}

```typescript
optional provided: string;
```

### read_only_channels? {#read_only_channels}

```typescript
optional read_only_channels: string[];
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### self? {#self}

```typescript
optional self: Self;
```

### subteams? {#subteams}

```typescript
optional subteams: Subteams;
```

### team? {#team}

```typescript
optional team: Team;
```

### thread_only_channels? {#thread_only_channels}

```typescript
optional thread_only_channels: string[];
```

### url? {#url}

```typescript
optional url: string;
```

### users? {#users}

```typescript
optional users: User[];
```
