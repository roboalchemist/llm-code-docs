# Source: https://www.courier.com/docs/sdk-libraries/go.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Go SDK

> Send notifications from your Go backend using the Courier SDK. Wraps the full REST API with strongly typed params, automatic retries, and error handling.

The Courier Go SDK provides typed access to the [Courier REST API](/reference/get-started) from applications written in Go. It uses strongly typed request structs with `omitzero` semantics and returns parsed response types.

Available on
<Link href="https://github.com/trycourier/courier-go"><Icon icon="github" iconType="solid" /> GitHub</Link>
and <Link href="https://pkg.go.dev/github.com/trycourier/courier-go/v4"><Icon icon="golang" iconType="solid" /> pkg.go.dev</Link>.

## Installation

```go  theme={null}
import (
	"github.com/trycourier/courier-go/v4" // imported as courier
)
```

Or pin a specific version:

```bash  theme={null}
go get -u 'github.com/trycourier/courier-go/v4'
```

Requires Go 1.22+.

## Quick Start

```go  theme={null}
package main

import (
	"context"
	"fmt"

	"github.com/trycourier/courier-go/v4"
	"github.com/trycourier/courier-go/v4/option"
	"github.com/trycourier/courier-go/v4/shared"
)

func main() {
	client := courier.NewClient(
		option.WithAPIKey("My API Key"), // defaults to os.LookupEnv("COURIER_API_KEY")
	)
	response, err := client.Send.Message(context.TODO(), courier.SendMessageParams{
		Message: courier.SendMessageParamsMessage{
			To: courier.SendMessageParamsMessageToUnion{
				OfUserRecipient: &shared.UserRecipientParam{
					UserID: courier.String("your_user_id"),
				},
			},
			Template: courier.String("your_template_id"),
			Data: map[string]any{
				"foo": "bar",
			},
		},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.RequestID)
}
```

<Tip>
  The client reads `COURIER_API_KEY` from your environment automatically. You can also pass it explicitly with `option.WithAPIKey("your-key")`.
</Tip>

## Authentication

Get your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in the Courier dashboard. Set it as an environment variable:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

The SDK picks this up by default. To pass it explicitly:

```go  theme={null}
client := courier.NewClient(
	option.WithAPIKey("your-api-key"),
)
```

## Sending Notifications

### With a template

```go  theme={null}
response, err := client.Send.Message(context.TODO(), courier.SendMessageParams{
	Message: courier.SendMessageParamsMessage{
		To: courier.SendMessageParamsMessageToUnion{
			OfUserRecipient: &shared.UserRecipientParam{
				UserID: courier.String("user_123"),
			},
		},
		Template: courier.String("my-template-id"),
		Data: map[string]any{
			"orderNumber": "10042",
		},
	},
})
```

### With inline content

```go  theme={null}
response, err := client.Send.Message(context.TODO(), courier.SendMessageParams{
	Message: courier.SendMessageParamsMessage{
		To: courier.SendMessageParamsMessageToUnion{
			OfUserRecipient: &shared.UserRecipientParam{
				Email: courier.String("jane@example.com"),
			},
		},
		Content: &courier.SendMessageParamsMessageContent{
			Title: courier.String("Order shipped"),
			Body:  courier.String("Your order {{orderNumber}} has shipped!"),
		},
		Data: map[string]any{
			"orderNumber": "10042",
		},
	},
})
```

## Available Resources

The SDK covers the full Courier API. Every method is typed and documented with Go docstrings.

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

```go  theme={null}
message, err := client.Messages.Retrieve(context.TODO(), "your-message-id")
fmt.Println(message.Status)
fmt.Println(message.Delivered)
```

### Managing User Profiles

```go  theme={null}
_, err := client.Profiles.Create(context.TODO(), "user_123", courier.ProfileCreateParams{
	Profile: map[string]any{
		"email": "jane@example.com",
		"name":  "Jane Doe",
	},
})

profile, err := client.Profiles.Retrieve(context.TODO(), "user_123")
```

### Issuing JWT Tokens

```go  theme={null}
result, err := client.Auth.IssueToken(context.TODO(), courier.AuthIssueTokenParams{
	Scope:     "user_id:user_123 inbox:read:messages inbox:write:events",
	ExpiresIn: "2 days",
})
fmt.Println(result.Token)
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

When the API returns a non-success status code, the SDK returns an error that can be unwrapped to access status and details:

```go  theme={null}
response, err := client.Send.Message(context.TODO(), params)
if err != nil {
	var apiErr *courier.Error
	if errors.As(err, &apiErr) {
		fmt.Println(apiErr.StatusCode)
		fmt.Println(apiErr.Message)
	}
}
```

### Retries

The SDK automatically retries failed requests up to 2 times with exponential backoff. Configure globally or per-request:

```go  theme={null}
client := courier.NewClient(
	option.WithMaxRetries(0), // disable retries
)
```

### Timeouts

Requests time out after 60 seconds by default. Configure with a custom context or client option:

```go  theme={null}
ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
defer cancel()

response, err := client.Send.Message(ctx, params)
```

## More Operations

The SDK covers the full [Courier REST API](/reference/get-started). Here are a few more resources beyond what's documented above:

| Resource         | Method                                               | Use case                                                                                                                                      |
| ---------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User preferences | `client.Users.Preferences.Retrieve(ctx, userId)`     | Fetch a user's notification preferences for your [preference center](/platform/preferences/preferences-overview)                              |
| Cancel a message | `client.Messages.Cancel(ctx, messageId)`             | Cancel a delayed or queued message before delivery                                                                                            |
| Push tokens      | `client.Users.Tokens.AddSingle(ctx, token, params)`  | Register a device push token for [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), or [React Native](/sdk-libraries/react-native) |
| Automations      | `client.Automations.Invoke.InvokeAdHoc(ctx, params)` | Run a multi-step workflow via [Automations](/platform/automations/automations-overview)                                                       |

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

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-go">
    Source code, issues, and changelog.
  </Card>
</CardGroup>
