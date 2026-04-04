Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/EntityPresentDetailsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / EntityPresentDetailsArguments

# Type Alias: EntityPresentDetailsArguments

```typescript
type EntityPresentDetailsArguments = TokenOverridable & object;
```

Defined in: [packages/web-api/src/types/request/entity.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/entity.ts#L5)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: object;
```

#### Description {#description}

Error response preventing flexpane data from being returned.

#### error.actions? {#erroractions}

```typescript
optional actions: EntityActionButton[];
```

##### Description {#description-1}

Set of action buttons to be shown in case of a specific error.

#### error.custom_message? {#errorcustom_message}

```typescript
optional custom_message: string;
```

##### Description {#description-2}

If status is 'custom', you can use this field to provide a message to the client.

#### error.custom_title? {#errorcustom_title}

```typescript
optional custom_title: string;
```

##### Description {#description-3}

If status is 'custom', you can use this field to provide a title to the client.

#### error.message_format? {#errormessage_format}

```typescript
optional message_format: string;
```

##### Description {#description-4}

String format, eg. 'markdown'.

#### error.status {#errorstatus}

```typescript
status: string;
```

##### Description {#description-5}

Error status indicating why the entity could not be presented.

### metadata? {#metadata}

```typescript
optional metadata: EntityMetadata;
```

#### Description {#description-6}

Entity metadata to be presented in the flexpane.

### trigger_id {#trigger_id}

```typescript
trigger_id: string;
```

#### Description {#description-7}

A reference to the original user action that initated the request.

### user_auth_required? {#user_auth_required}

```typescript
optional user_auth_required: boolean;
```

#### Description {#description-8}

Set user\_auth\_required to true to indicate that the user must authenticate to view the full flexpane data. Defaults to false.

### user_auth_url? {#user_auth_url}

```typescript
optional user_auth_url: string;
```

#### Description {#description-9}

A custom URL to which users are directed for authentication if required. Example: "[https://example.com/onboarding?user\_id=xxx](https://example.com/onboarding?user_id=xxx)"
