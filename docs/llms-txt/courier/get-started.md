# Source: https://www.courier.com/docs/reference/get-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Reference

> Authenticate, explore endpoints, and start integrating with the Courier API.

This section documents every Courier REST API endpoint with request/response schemas, code examples, and authentication details.

## API Keys

To call the Courier API, you need an API key. Grab one from the [Courier dashboard](https://app.courier.com/settings/api-keys), then pass it as a Bearer token:

```bash  theme={null}
Authorization: Bearer <YOUR_API_KEY>
```

***

## SDKs

Courier's server SDKs wrap the REST API with typed methods for sending notifications, managing users, configuring channels, and more. Install the SDK for your language to get started.

<CodeGroup>
  ```bash Node.js theme={null}
  npm install @trycourier/courier
  ```

  ```bash Python theme={null}
  pip install trycourier
  ```

  ```bash Go theme={null}
  go get github.com/trycourier/courier-go/v4
  ```

  ```bash Ruby theme={null}
  gem install trycourier
  ```

  ```bash Java theme={null}
  # Gradle
  implementation("com.courier:courier-java:4.9.1")
  ```

  ```bash PHP theme={null}
  composer require trycourier/courier
  ```

  ```bash C# theme={null}
  dotnet add package Courier
  ```
</CodeGroup>

<Tip>
  Courier also offers mobile SDKs (iOS, Android, Flutter, React Native) and client-side browser SDKs. See the [SDKs overview](/sdk-libraries/sdks-overview) for the full list.
</Tip>

***

## Rate Limiting

| Endpoint   | Operation               | Limit               |
| ---------- | ----------------------- | ------------------- |
| Lists API  | `POST` to subscriptions | 20 requests/minute  |
|            | `PUT` to lists          | 20 requests/minute  |
| Events API | `PUT` to events         | 20 requests/minute  |
| Brands API | `PUT` to brands         | 200 requests/minute |

***

## Payload Limits

The maximum request body size for all Courier API endpoints is **6 MB**. Requests that exceed this limit are rejected with a `413 Payload Too Large` response.

Base64-encoded content (common for email attachments) inflates size by roughly 33%; a 4.5 MB raw file will approach the limit after encoding. For large files, host them externally (S3, GCS, or your own CDN) and pass download URLs to your notification via `data` variables.

<Note>
  Payload limits cap the size of a single API request. For limits on how many messages you can send to a user or workspace, see [Send Limits](/platform/sending/send-limits).
</Note>

***

## Idempotency

Add an `Idempotency-Key` header to any `POST` request to ensure it runs only once, even if retried.

```bash cURL theme={null}
curl --request POST \
  --url https://api.courier.com/send \
  --header 'Authorization: Bearer <YOUR_API_KEY>' \
  --header 'Content-Type: application/json' \
  --header 'Idempotency-Key: <YOUR_UNIQUE_KEY>' \
  --data '{
    "message": {
      "to": { "user_id": "user-123" },
      "template": "WELCOME_TEMPLATE",
      "data": { "name": "Alice" }
    }
  }'
```

* Use a unique value (like a UUID) for each logical request.
* Replaying the same key returns the original response, even if it was an error.
* Keys expire after 24 hours.

## Next Steps

<CardGroup cols={2}>
  <Card title="Send a message" href="/api-reference/send/send-a-message" icon="paper-plane" />

  <Card title="Create a user profile" href="/api-reference/user-profiles/create-a-profile" icon="user" />

  <Card title="Create a JWT" href="/api-reference/authentication/create-a-jwt" icon="key" />

  <Card title="Update a list" href="/api-reference/lists/update-a-list" icon="list" />
</CardGroup>
