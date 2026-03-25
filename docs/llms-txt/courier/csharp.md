# Source: https://www.courier.com/docs/sdk-libraries/csharp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier C# SDK

> Send notifications from your .NET backend using the Courier SDK. Wraps the full REST API with strongly typed models, async methods, and automatic retries.

The Courier C# SDK provides typed access to the [Courier REST API](/reference/get-started) from applications written in C#. It targets .NET Standard 2.0, uses async/await throughout, and returns strongly typed response objects.

Available on
<Link href="https://github.com/trycourier/courier-csharp"><Icon icon="github" iconType="solid" /> GitHub</Link>.

## Installation

```bash  theme={null}
dotnet add package Courier
```

Requires .NET Standard 2.0 or later.

## Quick Start

```csharp  theme={null}
using Courier;
using Courier.Models;
using Courier.Models.Send;

CourierClient client = new();

var response = await client.Send.Message(new SendMessageParams
{
    Message = new()
    {
        To = new UserRecipient { Email = "you@example.com" },
        Content = new()
        {
            Title = "Hello from Courier!",
            Body = "Your first notification, sent with the C# SDK.",
        },
    },
});

Console.WriteLine(response.RequestId);
```

<Tip>
  The client reads `COURIER_API_KEY` from your environment automatically. You can also set it explicitly: `new CourierClient { ApiKey = "your-key" }`.
</Tip>

## Authentication

Get your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in the Courier dashboard. Set it as an environment variable:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

Or pass it to the client:

```csharp  theme={null}
CourierClient client = new() { ApiKey = "your-api-key" };
```

| Property  | Environment variable | Default                   |
| --------- | -------------------- | ------------------------- |
| `ApiKey`  | `COURIER_API_KEY`    | --                        |
| `BaseUrl` | `COURIER_BASE_URL`   | `https://api.courier.com` |

## Sending Notifications

### With a template

```csharp  theme={null}
var response = await client.Send.Message(new SendMessageParams
{
    Message = new()
    {
        To = new UserRecipient { UserId = "user_123" },
        Template = "my-template-id",
        Data = new Dictionary<string, JsonElement>
        {
            { "orderNumber", JsonSerializer.SerializeToElement("10042") },
        },
    },
});
```

### With inline content

```csharp  theme={null}
var response = await client.Send.Message(new SendMessageParams
{
    Message = new()
    {
        To = new UserRecipient { Email = "jane@example.com" },
        Content = new()
        {
            Title = "Order shipped",
            Body = "Your order {{orderNumber}} has shipped!",
        },
        Data = new Dictionary<string, JsonElement>
        {
            { "orderNumber", JsonSerializer.SerializeToElement("10042") },
        },
    },
});
```

## Available Resources

The SDK covers the full Courier API. Every method is async and returns strongly typed models.

| Resource      | Namespace              | Description                                            |
| ------------- | ---------------------- | ------------------------------------------------------ |
| Send          | `client.Send`          | Send messages to one or more recipients                |
| Messages      | `client.Messages`      | Retrieve status, history, and content of sent messages |
| Profiles      | `client.Profiles`      | Create, update, and retrieve user profiles             |
| Users         | `client.Users`         | Manage preferences, tenants, and push tokens per user  |
| Auth          | `client.Auth`          | Issue JWT tokens for client-side SDK authentication    |
| Bulk          | `client.Bulk`          | Send messages to large recipient lists via jobs        |
| Lists         | `client.Lists`         | Manage subscription lists and their subscribers        |
| Audiences     | `client.Audiences`     | Define and query audience segments                     |
| Tenants       | `client.Tenants`       | Manage tenants for multi-tenant setups                 |
| Automations   | `client.Automations`   | Invoke multi-step automation workflows                 |
| Brands        | `client.Brands`        | Manage brand settings (logos, colors, templates)       |
| Notifications | `client.Notifications` | List and inspect notification templates                |
| Translations  | `client.Translations`  | Manage localized content                               |

## Common Operations

### Checking Message Status

```csharp  theme={null}
var message = await client.Messages.Retrieve("your-message-id");
Console.WriteLine(message.Status);
Console.WriteLine(message.Delivered);
```

### Managing User Profiles

```csharp  theme={null}
await client.Profiles.Create("user_123", new ProfileCreateParams
{
    Profile = new Dictionary<string, object>
    {
        { "email", "jane@example.com" },
        { "name", "Jane Doe" },
    },
});

var profile = await client.Profiles.Retrieve("user_123");
```

### Issuing JWT Tokens

```csharp  theme={null}
var result = await client.Auth.IssueToken(new AuthIssueTokenParams
{
    Scope = "user_id:user_123 inbox:read:messages inbox:write:events",
    ExpiresIn = "2 days",
});

Console.WriteLine(result.Token);
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

When the API returns a non-success status code, the SDK throws a `CourierException`:

```csharp  theme={null}
try
{
    await client.Send.Message(parameters);
}
catch (CourierException e)
{
    Console.WriteLine(e.StatusCode);
    Console.WriteLine(e.Message);
}
```

### Retries and Timeouts

The SDK automatically retries failed requests up to 2 times with exponential backoff. Use `WithOptions` to configure per-request:

```csharp  theme={null}
var response = await client
    .WithOptions(options => options with
    {
        Timeout = TimeSpan.FromSeconds(20),
        MaxRetries = 0,
    })
    .Send.Message(parameters);
```

`WithOptions` returns a new client instance; the original is unchanged.

## More Operations

The SDK covers the full [Courier REST API](/reference/get-started). Here are a few more resources beyond what's documented above:

| Resource         | Method                                          | Use case                                                                                                                                      |
| ---------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User preferences | `client.Users.Preferences.Retrieve(userId)`     | Fetch a user's notification preferences for your [preference center](/platform/preferences/preferences-overview)                              |
| Cancel a message | `client.Messages.Cancel(messageId)`             | Cancel a delayed or queued message before delivery                                                                                            |
| Push tokens      | `client.Users.Tokens.AddSingle(token, params)`  | Register a device push token for [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), or [React Native](/sdk-libraries/react-native) |
| Automations      | `client.Automations.Invoke.InvokeAdHoc(params)` | Run a multi-step workflow via [Automations](/platform/automations/automations-overview)                                                       |

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

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-csharp">
    Source code, issues, and changelog.
  </Card>
</CardGroup>
