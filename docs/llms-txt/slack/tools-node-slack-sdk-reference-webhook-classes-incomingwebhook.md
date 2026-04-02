Source: https://docs.slack.dev/tools/node-slack-sdk/reference/webhook/classes/IncomingWebhook

[@slack/webhook](/tools/node-slack-sdk/reference/webhook/) / IncomingWebhook

# Class: IncomingWebhook

Defined in: [packages/webhook/src/IncomingWebhook.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L12)

A client for Slack's Incoming Webhooks

## Constructors {#constructors}

### Constructor {#constructor}

```text
new IncomingWebhook(url, defaults?): IncomingWebhook;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L28)

#### Parameters {#parameters}

##### url {#url}

`string`

##### defaults? {#defaults}

[`IncomingWebhookDefaultArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookDefaultArguments) = `...`

#### Returns {#returns}

`IncomingWebhook`

## Methods {#methods}

### send() {#send}

```text
send(message): Promise<IncomingWebhookResult>;
```

Defined in: [packages/webhook/src/IncomingWebhook.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/webhook/src/IncomingWebhook.ts#L60)

Send a notification to a conversation

#### Parameters {#parameters-1}

##### message {#message}

the message (a simple string, or an object describing the message)

`string` | [`IncomingWebhookSendArguments`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookSendArguments)

#### Returns {#returns-1}

`Promise`<[`IncomingWebhookResult`](/tools/node-slack-sdk/reference/webhook/interfaces/IncomingWebhookResult)\>
