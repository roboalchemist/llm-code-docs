# Source: https://www.courier.com/docs/sdk-libraries/java.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Java SDK

> Send notifications from your Java backend using the Courier SDK. Wraps the full REST API with builder-pattern requests, automatic retries, and error handling.

The Courier Java SDK provides typed access to the [Courier REST API](/reference/get-started) from applications written in Java 8+. It uses builder-pattern request construction, OkHttp for transport, and returns strongly typed response objects.

Available on
<Link href="https://github.com/trycourier/courier-java"><Icon icon="github" iconType="solid" /> GitHub</Link>
and <Link href="https://central.sonatype.com/artifact/com.courier/courier-java"><Icon icon="java" iconType="solid" /> Maven Central</Link>.

## Installation

<CodeGroup>
  ```kotlin Gradle theme={null}
  implementation("com.courier:courier-java:4.9.1")
  ```

  ```xml Maven theme={null}
  <dependency>
    <groupId>com.courier</groupId>
    <artifactId>courier-java</artifactId>
    <version>4.9.1</version>
  </dependency>
  ```
</CodeGroup>

Requires Java 8+.

## Quick Start

```java  theme={null}
import com.courier.client.CourierClient;
import com.courier.client.okhttp.CourierOkHttpClient;
import com.courier.core.JsonValue;
import com.courier.models.UserRecipient;
import com.courier.models.send.SendMessageParams;

CourierClient client = CourierOkHttpClient.fromEnv();

SendMessageParams params = SendMessageParams.builder()
    .message(SendMessageParams.Message.builder()
        .to(UserRecipient.builder().userId("your_user_id").build())
        .template("your_template_id")
        .data(SendMessageParams.Message.Data.builder()
            .putAdditionalProperty("foo", JsonValue.from("bar"))
            .build())
        .build())
    .build();

var response = client.send().message(params);
System.out.println(response.requestId());
```

<Tip>
  `CourierOkHttpClient.fromEnv()` reads `COURIER_API_KEY` from your environment (or the `courier.apiKey` system property). You can also configure it with the builder: `.apiKey("your-key")`.
</Tip>

## Authentication

Get your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in the Courier dashboard. Set it as an environment variable:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

Or pass it via the builder:

```java  theme={null}
CourierClient client = CourierOkHttpClient.builder()
    .apiKey("your-api-key")
    .build();
```

| Setter    | System property   | Environment variable | Default                   |
| --------- | ----------------- | -------------------- | ------------------------- |
| `apiKey`  | `courier.apiKey`  | `COURIER_API_KEY`    | --                        |
| `baseUrl` | `courier.baseUrl` | `COURIER_BASE_URL`   | `https://api.courier.com` |

## Sending Notifications

### With a template

```java  theme={null}
var params = SendMessageParams.builder()
    .message(SendMessageParams.Message.builder()
        .to(UserRecipient.builder().userId("user_123").build())
        .template("my-template-id")
        .data(SendMessageParams.Message.Data.builder()
            .putAdditionalProperty("orderNumber", JsonValue.from("10042"))
            .build())
        .build())
    .build();

var response = client.send().message(params);
```

### With inline content

```java  theme={null}
var params = SendMessageParams.builder()
    .message(SendMessageParams.Message.builder()
        .to(UserRecipient.builder().email("jane@example.com").build())
        .content(SendMessageParams.Message.Content.builder()
            .title("Order shipped")
            .body("Your order {{orderNumber}} has shipped!")
            .build())
        .data(SendMessageParams.Message.Data.builder()
            .putAdditionalProperty("orderNumber", JsonValue.from("10042"))
            .build())
        .build())
    .build();

var response = client.send().message(params);
```

## Available Resources

The SDK covers the full Courier API. Every method returns strongly typed response objects.

| Resource      | Namespace                | Description                                            |
| ------------- | ------------------------ | ------------------------------------------------------ |
| Send          | `client.send()`          | Send messages to one or more recipients                |
| Messages      | `client.messages()`      | Retrieve status, history, and content of sent messages |
| Profiles      | `client.profiles()`      | Create, update, and retrieve user profiles             |
| Users         | `client.users()`         | Manage preferences, tenants, and push tokens per user  |
| Auth          | `client.auth()`          | Issue JWT tokens for client-side SDK authentication    |
| Bulk          | `client.bulk()`          | Send messages to large recipient lists via jobs        |
| Lists         | `client.lists()`         | Manage subscription lists and their subscribers        |
| Audiences     | `client.audiences()`     | Define and query audience segments                     |
| Tenants       | `client.tenants()`       | Manage tenants for multi-tenant setups                 |
| Automations   | `client.automations()`   | Invoke multi-step automation workflows                 |
| Brands        | `client.brands()`        | Manage brand settings (logos, colors, templates)       |
| Notifications | `client.notifications()` | List and inspect notification templates                |
| Translations  | `client.translations()`  | Manage localized content                               |

## Common Operations

### Checking Message Status

```java  theme={null}
var message = client.messages().retrieve("your-message-id");
System.out.println(message.status());
System.out.println(message.delivered());
```

### Managing User Profiles

```java  theme={null}
client.profiles().create("user_123", ProfileCreateParams.builder()
    .profile(Map.of(
        "email", "jane@example.com",
        "name", "Jane Doe"
    ))
    .build());

var profile = client.profiles().retrieve("user_123");
```

### Issuing JWT Tokens

```java  theme={null}
var result = client.auth().issueToken(AuthIssueTokenParams.builder()
    .scope("user_id:user_123 inbox:read:messages inbox:write:events")
    .expiresIn("2 days")
    .build());

System.out.println(result.token());
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

When the API returns a non-success status code, the SDK throws a `CourierServiceException`:

```java  theme={null}
try {
    client.send().message(params);
} catch (CourierServiceException e) {
    System.out.println(e.statusCode());
    System.out.println(e.message());
}
```

### Retries

The SDK automatically retries failed requests up to 2 times with exponential backoff. Configure globally:

```java  theme={null}
CourierClient client = CourierOkHttpClient.builder()
    .maxRetries(0)
    .build();
```

### Timeouts

Requests time out after 60 seconds by default. Configure globally:

```java  theme={null}
CourierClient client = CourierOkHttpClient.builder()
    .timeout(Duration.ofSeconds(20))
    .build();
```

Or override per-request using `withOptions`:

```java  theme={null}
client.withOptions(options -> options.timeout(Duration.ofSeconds(5)))
    .send().message(params);
```

## More Operations

The SDK covers the full [Courier REST API](/reference/get-started). Here are a few more resources beyond what's documented above:

| Resource         | Method                                              | Use case                                                                                                                                      |
| ---------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User preferences | `client.users().preferences().retrieve(userId)`     | Fetch a user's notification preferences for your [preference center](/platform/preferences/preferences-overview)                              |
| Cancel a message | `client.messages().cancel(messageId)`               | Cancel a delayed or queued message before delivery                                                                                            |
| Push tokens      | `client.users().tokens().addSingle(token, params)`  | Register a device push token for [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), or [React Native](/sdk-libraries/react-native) |
| Automations      | `client.automations().invoke().invokeAdHoc(params)` | Run a multi-step workflow via [Automations](/platform/automations/automations-overview)                                                       |

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

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-java">
    Source code, issues, and changelog.
  </Card>
</CardGroup>
