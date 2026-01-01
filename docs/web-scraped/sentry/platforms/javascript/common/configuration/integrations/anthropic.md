---
---
title: Anthropic
description: "Adds instrumentation for Anthropic API."
---

This integration works in the Node.js, Cloudflare Workers, Vercel Edge Functions, and browser runtimes. It requires SDK version `10.12.0` or higher.

_Import name: `Sentry.anthropicAIIntegration`_

The `anthropicAIIntegration` adds instrumentation for the `@anthropic-ai/sdk` to capture spans by automatically wrapping Anthropic client calls and recording LLM interactions with configurable input/output recording.

It is enabled by default and will automatically capture spans for Anthropic API method calls. You can opt-in to capture inputs and outputs by setting `recordInputs` and `recordOutputs` in the integration config:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.anthropicAIIntegration({
      recordInputs: true,
      recordOutputs: true,
    }),
  ],
});
```

For Cloudflare Workers, you need to manually instrument the Anthropic client using the `instrumentAnthropicAiClient` helper:

```javascript
const anthropic = new Anthropic();
const client = Sentry.instrumentAnthropicAiClient(anthropic, {
  recordInputs: true,
  recordOutputs: true,
});

// Use the wrapped client instead of the original anthropic instance
const response = await client.messages.create({
  model: "claude-3-5-sonnet-20241022",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

For browser applications, you need to manually instrument the Anthropic client using the `instrumentAnthropicAiClient` helper:

```javascript
const anthropic = new Anthropic();
const client = Sentry.instrumentAnthropicAiClient(anthropic, {
  recordInputs: true,
  recordOutputs: true,
});

// Use the wrapped client instead of the original anthropic instance
const response = await client.messages.create({
  model: "claude-3-5-sonnet-20241022",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Options

### `recordInputs`

_Type: `boolean`_

Records inputs to Anthropic API method calls (such as prompts and messages).

Defaults to `true` if `sendDefaultPii` is `true`.

```javascript
Sentry.init({
  integrations: [Sentry.anthropicAIIntegration({ recordInputs: true })],
});
```

### `recordOutputs`

_Type: `boolean`_

Records outputs from Anthropic API method calls (such as generated text and responses).

Defaults to `true` if `sendDefaultPii` is `true`.

```javascript
Sentry.init({
  integrations: [Sentry.anthropicAIIntegration({ recordOutputs: true })],
});
```

## Configuration

By default this integration adds tracing support to Anthropic API method calls including:

- `messages.create()` - Create messages with Claude models
- `messages.stream()` - Stream messages with Claude models
- `messages.countTokens()` - Count tokens for messages
- `models.get()` - Get model information
- `completions.create()` - Create completions (legacy)
- `models.retrieve()` - Retrieve model details
- `beta.messages.create()` - Beta messages API

The integration will automatically detect streaming vs non-streaming requests and handle them appropriately.

## Edge runtime

This integration is automatically instrumented in the Node.js runtime. For Next.js applications using the Edge runtime, you need to manually instrument the Anthropic client:

```javascript
const anthropic = new Anthropic();
const client = Sentry.instrumentAnthropicAiClient(anthropic, {
  recordInputs: true,
  recordOutputs: true,
});

// Use the wrapped client instead of the original anthropic instance
const response = await client.messages.create({
  model: "claude-3-5-sonnet-20241022",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Supported Versions

- `@anthropic-ai/sdk`: `>=0.19.2 <1.0.0`
