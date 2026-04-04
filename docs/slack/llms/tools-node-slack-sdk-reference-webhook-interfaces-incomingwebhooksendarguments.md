Source: https://docs.slack.dev/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookSendArguments

[@slack/webhook](/tools/node-slack-sdk/reference/webhook/) / IncomingWebhookSendArguments

# Interface: IncomingWebhookSendArguments

Defined in: [packages/webhook/src/IncomingWebhook.ts:111](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L111)

## Extends {#extends}

* [`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments)

## Properties {#properties}

### agent? {#agent}

```typescript
optional agent: Agent;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:107](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L107)

#### Inherited from {#inherited-from}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`agent`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#agent)

* * *

### attachments? {#attachments}

```typescript
optional attachments: MessageAttachment[];
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:112](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L112)

* * *

### blocks? {#blocks}

```typescript
optional blocks: (Block | KnownBlock)[];
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:113](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L113)

* * *

### channel? {#channel}

```typescript
optional channel: string;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:104](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L104)

#### Inherited from {#inherited-from-1}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`channel`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#channel)

* * *

### icon_emoji? {#icon_emoji}

```typescript
optional icon_emoji: string;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:102](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L102)

#### Inherited from {#inherited-from-2}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`icon_emoji`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#icon_emoji)

* * *

### icon_url? {#icon_url}

```typescript
optional icon_url: string;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:103](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L103)

#### Inherited from {#inherited-from-3}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`icon_url`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#icon_url)

* * *

### link_names? {#link_names}

```typescript
optional link_names: boolean;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:106](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L106)

#### Inherited from {#inherited-from-4}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`link_names`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#link_names)

* * *

### metadata? {#metadata}

```typescript
optional metadata: object;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:116](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L116)

#### event_payload {#event_payload}

```typescript
event_payload: Record<string, any>;
```

#### event_type {#event_type}

```typescript
event_type: string;
```

* * *

### text? {#text}

```typescript
optional text: string;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:105](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L105)

#### Inherited from {#inherited-from-5}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`text`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#text)

* * *

### timeout? {#timeout}

```typescript
optional timeout: number;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:108](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L108)

#### Inherited from {#inherited-from-6}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`timeout`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#timeout)

* * *

### unfurl_links? {#unfurl_links}

```typescript
optional unfurl_links: boolean;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:114](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L114)

* * *

### unfurl_media? {#unfurl_media}

```typescript
optional unfurl_media: boolean;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:115](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L115)

* * *

### username? {#username}

```typescript
optional username: string;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L101)

#### Inherited from {#inherited-from-7}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments).[`username`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments#username)
