# Source: https://www.courier.com/docs/sdk-libraries/php.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier PHP SDK

> Send notifications from your PHP backend using the Courier SDK. Wraps the full REST API with typed responses, automatic retries, and error handling.

The Courier PHP SDK provides typed access to the [Courier REST API](/reference/get-started) from any PHP 8.1+ application. It uses named parameters for optional arguments and returns strongly typed response objects.

Available on
<Link href="https://github.com/trycourier/courier-php"><Icon icon="github" iconType="solid" /> GitHub</Link>.

<Note>
  The PHP SDK is currently in beta. APIs may change between releases. [Share feedback or report issues on GitHub.](https://github.com/trycourier/courier-php/issues/new)
</Note>

## Installation

Add to your `composer.json`:

```json  theme={null}
{
  "repositories": [
    {
      "type": "vcs",
      "url": "git@github.com:trycourier/courier-php.git"
    }
  ],
  "require": {
    "trycourier/courier": "dev-main"
  }
}
```

Then run `composer install`. Requires PHP 8.1+.

## Quick Start

```php  theme={null}
<?php

use Courier\Client;

$client = new Client(apiKey: getenv('COURIER_API_KEY'));

$response = $client->send->message(
  message: [
    'to' => ['email' => 'you@example.com'],
    'content' => [
      'title' => 'Hello from Courier!',
      'body' => 'Your first notification, sent with the PHP SDK.',
    ],
  ],
);

var_dump($response->requestId);
```

<Tip>
  Pass your API key via the `COURIER_API_KEY` environment variable or directly to the constructor: `new Client(apiKey: 'your-key')`.
</Tip>

## Authentication

Get your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in the Courier dashboard. Set it as an environment variable:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

Or pass it to the client constructor:

```php  theme={null}
$client = new Client(apiKey: 'your-api-key');
```

## Sending Notifications

### With a template

```php  theme={null}
$response = $client->send->message(
  message: [
    'to' => ['user_id' => 'user_123'],
    'template' => 'my-template-id',
    'data' => ['orderNumber' => '10042', 'itemName' => 'Courier Hoodie'],
  ],
);
```

### With inline content

```php  theme={null}
$response = $client->send->message(
  message: [
    'to' => ['email' => 'jane@example.com'],
    'content' => [
      'title' => 'Order shipped',
      'body' => 'Your order {{orderNumber}} has shipped!',
    ],
    'data' => ['orderNumber' => '10042'],
    'routing' => ['method' => 'single', 'channels' => ['email']],
  ],
);
```

## Available Resources

The SDK covers the full Courier API.

| Resource      | Namespace                | Description                                            |
| ------------- | ------------------------ | ------------------------------------------------------ |
| Send          | `$client->send`          | Send messages to one or more recipients                |
| Messages      | `$client->messages`      | Retrieve status, history, and content of sent messages |
| Profiles      | `$client->profiles`      | Create, update, and retrieve user profiles             |
| Users         | `$client->users`         | Manage preferences, tenants, and push tokens per user  |
| Auth          | `$client->auth`          | Issue JWT tokens for client-side SDK authentication    |
| Bulk          | `$client->bulk`          | Send messages to large recipient lists via jobs        |
| Lists         | `$client->lists`         | Manage subscription lists and their subscribers        |
| Audiences     | `$client->audiences`     | Define and query audience segments                     |
| Tenants       | `$client->tenants`       | Manage tenants for multi-tenant setups                 |
| Automations   | `$client->automations`   | Invoke multi-step automation workflows                 |
| Brands        | `$client->brands`        | Manage brand settings (logos, colors, templates)       |
| Notifications | `$client->notifications` | List and inspect notification templates                |
| Translations  | `$client->translations`  | Manage localized content                               |

## Common Operations

### Checking Message Status

```php  theme={null}
$message = $client->messages->retrieve('your-message-id');
echo $message->status;
echo $message->delivered;
```

### Managing User Profiles

```php  theme={null}
$client->profiles->create('user_123', profile: [
    'email' => 'jane@example.com',
    'phone_number' => '+15551234567',
    'name' => 'Jane Doe',
]);

$profile = $client->profiles->retrieve('user_123');
```

### Issuing JWT Tokens

```php  theme={null}
$result = $client->auth->issueToken(
  scope: 'user_id:user_123 inbox:read:messages inbox:write:events',
  expiresIn: '2 days',
);

echo $result->token;
```

| Scope                 | Permission                             |
| --------------------- | -------------------------------------- |
| `user_id:<id>`        | Which user the token is for (required) |
| `inbox:read:messages` | Read inbox messages                    |
| `inbox:write:events`  | Mark messages as read/archived         |
| `read:preferences`    | Read notification preferences          |
| `write:preferences`   | Update notification preferences        |
| `write:user-tokens`   | Register push notification tokens      |

## Configuration

### Error Handling

The SDK throws typed exceptions for API failures. All extend `Courier\Core\Exceptions\APIException`:

```php  theme={null}
use Courier\Core\Exceptions\APIConnectionException;
use Courier\Core\Exceptions\RateLimitException;
use Courier\Core\Exceptions\APIStatusException;

try {
  $client->send->message(message: [
    'to' => ['user_id' => 'user_123'],
    'template' => 'my-template',
  ]);
} catch (APIConnectionException $e) {
  echo "The server could not be reached\n";
} catch (RateLimitException $e) {
  echo "Rate limited; back off a bit.\n";
} catch (APIStatusException $e) {
  echo "API error: " . $e->getMessage() . "\n";
}
```

### Retries

The SDK automatically retries failed requests up to 2 times with exponential backoff.

```php  theme={null}
// Disable retries
$client = new Client(requestOptions: ['maxRetries' => 0]);

// Or per-request
$client->send->message(
  message: ['to' => ['user_id' => 'user_123'], 'template' => 'my-template'],
  requestOptions: ['maxRetries' => 5],
);
```

## More Operations

The SDK covers the full [Courier REST API](/reference/get-started). Here are a few more resources beyond what's documented above:

| Resource         | Method                                                       | Use case                                                                                                                                      |
| ---------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User preferences | `$client->users->preferences->retrieve($userId)`             | Fetch a user's notification preferences for your [preference center](/platform/preferences/preferences-overview)                              |
| Cancel a message | `$client->messages->cancel($messageId)`                      | Cancel a delayed or queued message before delivery                                                                                            |
| Push tokens      | `$client->users->tokens->addSingle($token, userId: $userId)` | Register a device push token for [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), or [React Native](/sdk-libraries/react-native) |
| Automations      | `$client->automations->invoke->invokeAdHoc(automation: ...)` | Run a multi-step workflow via [Automations](/platform/automations/automations-overview)                                                       |

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

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-php">
    Source code, issues, and changelog.
  </Card>
</CardGroup>
