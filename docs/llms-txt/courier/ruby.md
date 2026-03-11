# Source: https://www.courier.com/docs/sdk-libraries/ruby.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Ruby SDK

> Send notifications from your Ruby backend using the Courier SDK. Wraps the full REST API with typed responses, Sorbet support, and automatic retries.

The Courier Ruby SDK provides typed access to the [Courier REST API](/reference/get-started) from any Ruby 3.2+ application. It ships with Yard docstrings, RBS and RBI type definitions for Sorbet, and uses `net/http` with connection pooling.

Available on
<Link href="https://github.com/trycourier/courier-ruby"><Icon icon="github" iconType="solid" /> GitHub</Link>
and <Link href="https://rubygems.org/gems/trycourier"><Icon icon="gem" iconType="solid" /> RubyGems</Link>.

## Installation

Add to your `Gemfile`:

```ruby  theme={null}
gem "trycourier", "~> 4.7"
```

Then run `bundle install`. Requires Ruby 3.2+.

## Quick Start

```ruby  theme={null}
require "bundler/setup"
require "courier"

client = Courier::Client.new

response = client.send_.message(
  message: {
    to: { email: "you@example.com" },
    content: {
      title: "Hello from Courier!",
      body: "Your first notification, sent with the Ruby SDK."
    }
  }
)

puts response.request_id
```

<Tip>
  The client reads `COURIER_API_KEY` from your environment automatically. You can also pass it explicitly: `Courier::Client.new(api_key: "your-key")`.
</Tip>

<Note>
  The method is `send_` (with a trailing underscore) because `send` is a reserved method in Ruby.
</Note>

## Authentication

Get your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in the Courier dashboard. Set it as an environment variable:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

The SDK picks this up by default. To pass it explicitly:

```ruby  theme={null}
client = Courier::Client.new(api_key: "your-api-key")
```

## Sending Notifications

### With a template

```ruby  theme={null}
response = client.send_.message(
  message: {
    to: { user_id: "user_123" },
    template: "my-template-id",
    data: { orderNumber: "10042", itemName: "Courier Hoodie" }
  }
)
```

### With inline content

```ruby  theme={null}
response = client.send_.message(
  message: {
    to: { email: "jane@example.com" },
    content: {
      title: "Order shipped",
      body: "Your order {{orderNumber}} has shipped!"
    },
    data: { orderNumber: "10042" },
    routing: { method: "single", channels: ["email"] }
  }
)
```

## Available Resources

The SDK covers the full Courier API. Every method is documented with Yard docstrings.

| Resource      | Namespace              | Description                                            |
| ------------- | ---------------------- | ------------------------------------------------------ |
| Send          | `client.send_`         | Send messages to one or more recipients                |
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

```ruby  theme={null}
message = client.messages.retrieve("your-message-id")
puts message.status
puts message.delivered

history = client.messages.history("your-message-id")
```

### Managing User Profiles

```ruby  theme={null}
client.profiles.create("user_123", profile: {
  email: "jane@example.com",
  phone_number: "+15551234567",
  name: "Jane Doe"
})

profile = client.profiles.retrieve("user_123")
```

### Issuing JWT Tokens

```ruby  theme={null}
result = client.auth.issue_token(
  scope: "user_id:user_123 inbox:read:messages inbox:write:events",
  expires_in: "2 days"
)

puts result.token
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

The SDK throws typed errors for API failures. All errors extend `Courier::Errors::APIError`:

```ruby  theme={null}
begin
  client.send_.message(message: { to: { user_id: "user_123" }, template: "my-template" })
rescue Courier::Errors::APIConnectionError => e
  puts "The server could not be reached"
rescue Courier::Errors::RateLimitError => e
  puts "Rate limited; back off a bit."
rescue Courier::Errors::APIStatusError => e
  puts "API error: #{e.status}"
end
```

### Retries

The SDK automatically retries failed requests up to 2 times with exponential backoff.

```ruby  theme={null}
client = Courier::Client.new(max_retries: 0)

# Or per-request
client.send_.message(
  message: { to: { user_id: "user_123" }, template: "my-template" },
  request_options: { max_retries: 5 }
)
```

### Timeouts

Requests time out after 60 seconds by default. Configure globally or per-request:

```ruby  theme={null}
client = Courier::Client.new(timeout: 20)

client.send_.message(
  message: { to: { user_id: "user_123" }, template: "my-template" },
  request_options: { timeout: 5 }
)
```

## More Operations

The SDK covers the full [Courier REST API](/reference/get-started). Here are a few more resources beyond what's documented above:

| Resource         | Method                                                 | Use case                                                                                                                                      |
| ---------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User preferences | `client.users.preferences.retrieve(user_id)`           | Fetch a user's notification preferences for your [preference center](/platform/preferences/preferences-overview)                              |
| Cancel a message | `client.messages.cancel(message_id)`                   | Cancel a delayed or queued message before delivery                                                                                            |
| Push tokens      | `client.users.tokens.add_single(token, user_id:)`      | Register a device push token for [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), or [React Native](/sdk-libraries/react-native) |
| Automations      | `client.automations.invoke.invoke_ad_hoc(automation:)` | Run a multi-step workflow via [Automations](/platform/automations/automations-overview)                                                       |

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

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-ruby">
    Source code, issues, and changelog.
  </Card>
</CardGroup>
