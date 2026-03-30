# Source: https://www.courier.com/docs/sdk-libraries/node.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Node.js SDK

> Send notifications from your Node.js or TypeScript backend using the Courier SDK. Wraps the full REST API with typed requests, automatic retries, and error handling.

The Courier Node.js SDK provides typed access to the [Courier REST API](/reference/get-started) from server-side TypeScript or JavaScript. Use it to send notifications, manage users and profiles, work with templates, and more.

Available on
<Link href="https://github.com/trycourier/courier-node"><Icon icon="github" iconType="solid" /> GitHub</Link>
and <Link href="https://www.npmjs.com/package/@trycourier/courier"><Icon icon="npm" iconType="solid" /> npm</Link>.

## Installation

<CodeGroup>
  ```bash npm theme={null}
  npm install @trycourier/courier
  ```

  ```bash yarn theme={null}
  yarn add @trycourier/courier
  ```

  ```bash pnpm theme={null}
  pnpm add @trycourier/courier
  ```
</CodeGroup>

Requires Node.js 20+ (LTS), TypeScript 4.9+. Also works in Deno 1.28+, Bun 1.0+, Cloudflare Workers, and Vercel Edge Runtime.

## Quick Start

```ts  theme={null}
import Courier from '@trycourier/courier';

const client = new Courier();

const response = await client.send.message({
  message: {
    to: { email: 'you@example.com' },
    content: {
      title: 'Hello from Courier!',
      body: 'Your first notification, sent with the Node.js SDK.',
    },
  },
});

console.log(response.requestId);
```

<Tip>
  The client reads `COURIER_API_KEY` from your environment automatically. You can also pass it explicitly: `new Courier({ apiKey: 'your-key' })`.
</Tip>

## Authentication

Get your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in the Courier dashboard. Set it as an environment variable:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

The SDK picks this up by default. To pass it explicitly:

```ts  theme={null}
const client = new Courier({
  apiKey: 'your-api-key',
});
```

## Sending Notifications

### With a template

Design your notification in the [template designer](/platform/content/template-designer/template-designer-overview), then reference it by ID:

```ts  theme={null}
const response = await client.send.message({
  message: {
    to: { user_id: 'user_123' },
    template: 'my-template-id',
    data: { orderNumber: '10042', itemName: 'Courier Hoodie' },
  },
});
```

### With inline content

Skip templates and define content directly in code:

```ts  theme={null}
const response = await client.send.message({
  message: {
    to: { email: 'jane@example.com' },
    content: {
      title: 'Order shipped',
      body: 'Your order {{orderNumber}} has shipped!',
    },
    data: { orderNumber: '10042' },
    routing: {
      method: 'single',
      channels: ['email'],
    },
  },
});
```

### To multiple recipients

Send to a list of users in a single call:

```ts  theme={null}
const response = await client.send.message({
  message: {
    to: [
      { user_id: 'user_1' },
      { user_id: 'user_2' },
      { email: 'guest@example.com' },
    ],
    template: 'welcome-template',
  },
});
```

## Available Resources

The SDK covers the full Courier API. Every method is typed and documented in your editor on hover.

| Resource      | Namespace              | Description                                            |
| ------------- | ---------------------- | ------------------------------------------------------ |
| Send          | `client.send`          | Send messages to one or more recipients                |
| Messages      | `client.messages`      | Retrieve status, history, and content of sent messages |
| Profiles      | `client.profiles`      | Create, update, and retrieve user profiles             |
| Users         | `client.users`         | Manage preferences, tenants, and push tokens per user  |
| Auth          | `client.auth`          | Issue JWT tokens for client-side SDK authentication    |
| Bulk          | `client.bulk`          | Send messages to large recipient lists via jobs        |
| Lists         | `client.lists`         | Manage subscription lists and their subscribers        |
| Audiences     | `client.audiences`     | Define and query audience segments                     |
| Tenants       | `client.tenants`       | Manage tenants for multi-tenant setups                 |
| Automations   | `client.automations`   | Invoke multi-step automation workflows                 |
| Brands        | `client.brands`        | Manage brand settings (logos, colors, templates)       |
| Notifications | `client.notifications` | List and inspect notification templates                |
| Translations  | `client.translations`  | Manage localized content                               |

## Common Operations

### Checking Message Status

After sending, use the `requestId` to check delivery status or get the full event timeline:

```ts  theme={null}
const message = await client.messages.retrieve('your-message-id');
console.log(message.status);    // e.g. 'DELIVERED'
console.log(message.delivered);  // timestamp
console.log(message.channels);  // which channels were used

const history = await client.messages.history('your-message-id');
for (const event of history.results) {
  console.log(event.type, event.event);
}
```

You can also list recent messages with optional filters:

```ts  theme={null}
const recent = await client.messages.list({ status: 'DELIVERED' });
```

### Managing User Profiles

Profiles store recipient data (email, phone, custom fields) that Courier uses for delivery. You need a profile before you can send to a `user_id`.

```ts  theme={null}
// Create or merge into a profile
await client.profiles.create('user_123', {
  profile: {
    email: 'jane@example.com',
    phone_number: '+15551234567',
    name: 'Jane Doe',
  },
});

// Retrieve a profile
const profile = await client.profiles.retrieve('user_123');
console.log(profile.profile.email);

// Partial update (merge)
await client.profiles.update('user_123', {
  profile: { name: 'Jane Smith' },
});
```

<Note>
  `create` merges with any existing profile. Use `replace` for a full overwrite (any fields not included will be removed).
</Note>

### Issuing JWT Tokens

If you use Courier's [client-side SDKs](/sdk-libraries/sdks-overview) (React, JavaScript, mobile), your backend needs to issue JWT tokens for user authentication. The `auth.issueToken` method handles this:

```ts  theme={null}
const { token } = await client.auth.issueToken({
  scope: 'user_id:user_123 inbox:read:messages inbox:write:events read:preferences write:preferences',
  expires_in: '2 days',
});

// Return this token to your frontend
```

The `scope` string controls what the token can access. Common scopes:

| Scope                 | Permission                             |
| --------------------- | -------------------------------------- |
| `user_id:<id>`        | Which user the token is for (required) |
| `inbox:read:messages` | Read inbox messages                    |
| `inbox:write:events`  | Mark messages as read/archived         |
| `read:preferences`    | Read notification preferences          |
| `write:preferences`   | Update notification preferences        |
| `write:user-tokens`   | Register push notification tokens      |

### Bulk Sending

For large recipient lists, use the bulk API. It works in three steps: create a job, add users, then run it.

```ts  theme={null}
// 1. Create a bulk job
const job = await client.bulk.createJob({
  message: { event: 'welcome-notification' },
});

// 2. Add recipients
await client.bulk.addUsers(job.jobId, {
  users: [
    { profile: { email: 'alice@example.com' }, data: { name: 'Alice' } },
    { profile: { email: 'bob@example.com' }, data: { name: 'Bob' } },
  ],
});

// 3. Run the job
await client.bulk.runJob(job.jobId);

// Check status
const status = await client.bulk.retrieveJob(job.jobId);
console.log(status.status);
```

<Warning>
  For email-based bulk jobs, include `profile.email` on each user. The `to.email` field alone is not sufficient for email provider routing.
</Warning>

## TypeScript Types

The SDK ships with full TypeScript definitions for every request and response. Import them directly:

```ts  theme={null}
import Courier from '@trycourier/courier';

const params: Courier.SendMessageParams = {
  message: {
    to: { user_id: 'user_123' },
    template: 'my-template-id',
    data: { foo: 'bar' },
  },
};

const response: Courier.SendMessageResponse = await client.send.message(params);
```

All methods, parameters, and response fields have docstrings that appear on hover in VS Code and other editors.

## Configuration

### Error Handling

The SDK throws typed errors for API failures. All errors extend `Courier.APIError`:

```ts  theme={null}
try {
  await client.send.message({ message: { to: { user_id: 'user_123' }, template: 'my-template' } });
} catch (err) {
  if (err instanceof Courier.APIError) {
    console.log(err.status);  // e.g. 400
    console.log(err.name);    // e.g. 'BadRequestError'
    console.log(err.message);
  }
}
```

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

The SDK automatically retries failed requests up to 2 times with exponential backoff. Retried errors include connection failures, 408, 409, 429, and 5xx responses.

```ts  theme={null}
// Disable retries
const client = new Courier({ maxRetries: 0 });

// Or override per-request
await client.send.message(
  { message: { to: { user_id: 'user_123' }, template: 'my-template' } },
  { maxRetries: 5 },
);
```

### Timeouts

Requests time out after 60 seconds by default. Configure globally or per-request:

```ts  theme={null}
const client = new Courier({
  timeout: 20 * 1000, // 20 seconds
});

// Override per-request
await client.send.message(
  { message: { to: { user_id: 'user_123' }, template: 'my-template' } },
  { timeout: 5 * 1000 },
);
```

On timeout, an `APIConnectionTimeoutError` is thrown. Timed-out requests are retried by default.

### Logging

Enable debug logging with the `COURIER_LOG` environment variable or the `logLevel` client option:

```ts  theme={null}
const client = new Courier({
  logLevel: 'debug', // 'debug' | 'info' | 'warn' | 'error' | 'off'
});
```

At `debug` level, all HTTP requests and responses are logged including headers and bodies. You can also pass a custom logger (pino, winston, etc.):

```ts  theme={null}
import pino from 'pino';

const client = new Courier({
  logger: pino().child({ name: 'Courier' }),
  logLevel: 'debug',
});
```

### Raw Response Access

Access HTTP headers or the underlying `Response` object:

```ts  theme={null}
// Headers only (does not consume body)
const raw = await client.send.message({
  message: { to: { user_id: 'user_123' }, template: 'my-template' },
}).asResponse();
console.log(raw.headers.get('x-request-id'));

// Parsed data + raw response
const { data, response } = await client.send.message({
  message: { to: { user_id: 'user_123' }, template: 'my-template' },
}).withResponse();
console.log(data.requestId);
```

## More Operations

The SDK covers the full [Courier REST API](/reference/get-started). Here are a few more resources beyond what's documented above:

| Resource         | Method                                                  | Use case                                                                                                                                      |
| ---------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User preferences | `client.users.preferences.retrieve(userId)`             | Fetch a user's notification preferences for your [preference center](/platform/preferences/preferences-overview)                              |
| Cancel a message | `client.messages.cancel(messageId)`                     | Cancel a delayed or queued message before delivery (returns 409 if already delivered)                                                         |
| Push tokens      | `client.users.tokens.addSingle(token, { user_id })`     | Register a device push token for [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), or [React Native](/sdk-libraries/react-native) |
| Automations      | `client.automations.invoke.invokeAdHoc({ automation })` | Run a multi-step workflow (delay, send, update profile) via [Automations](/platform/automations/automations-overview)                         |

<CardGroup cols={2}>
  <Card title="API Reference" icon="code" href="/reference/get-started">
    Full REST API docs with request/response examples.
  </Card>

  <Card title="Send API" icon="paper-plane" href="/platform/sending/send-message">
    Learn about the Send endpoint, routing, and message options.
  </Card>

  <Card title="Quickstart" icon="bolt" href="/getting-started/quickstart">
    Send your first notification in under two minutes.
  </Card>

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-node">
    Source code, issues, and changelog.
  </Card>
</CardGroup>
