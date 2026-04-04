# Source: https://www.courier.com/docs/platform/sending/send-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send a Message

Use the Courier API to send notifications from your app when important events happen, like a new sign-up, order update, or password reset. Each send request specifies the recipient, content, and delivery channels.

Let's start with a simple example. The example below sends a welcome email using inline content without a template to show how the Send API works over a single channel.

<CodeGroup>
  ```javascript Node.js theme={null}
  const { requestId } = await courier.send({
    message: {
      to: { email: "user@example.com" },
      content: {
        title: "Welcome!",
        body: "Thanks for signing up, {{name}}"
      },
      data: { name: "John Doe" },
      routing: {
        method: "single",
        channels: ["email"]
      }
    }
  });
  ```

  ```python Python theme={null}
  response = client.send(
    message=courier.ContentMessage(
      to=courier.UserRecipient(email="user@example.com"),
      content=courier.ElementalContentSugar(
        title="Welcome!",
        body="Thanks for signing up, {{name}}"
      ),
      data={"name": "John Doe"},
      routing=courier.Routing(method="single", channels=["email"])
    )
  )
  ```

  ```ruby Ruby theme={null}
  res = client.send({
    message: {
      to: { email: "user@example.com" },
      content: {
        title: "Welcome!",
        body: "Thanks for signing up, {{name}}"
      },
      data: { name: "John Doe" },
      routing: {
        method: "single",
        channels: ["email"]
      }
    }
  })
  ```

  ```php PHP theme={null}
  $result = $courier->send(
    (object) [
      'to' => [
        'email' => "user@example.com"
      ],
      'content' => [
        'title' => "Welcome!",
        'body' => "Thanks for signing up, {{name}}"
      ],
      'data' => [
        'name' => "John Doe"
      ],
      'routing' => [
        'method' => "single",
        'channels' => ["email"]
      ]
    ]
  );
  ```

  ```java Java theme={null}
  courier.send(SendMessageRequest.builder()
    .message(Message.of(TemplateMessage.builder()
      .to(MessageRecipient.of(Recipient.of(UserRecipient.builder()
        .email("user@example.com")
        .build())))
      .content(ContentMessage.builder()
        .title("Welcome!")
        .body("Thanks for signing up, {{name}}")
        .build())
      .data(Map.of("name", "John Doe"))
      .routing(Routing.builder()
        .method("single")
        .channels(List.of("email"))
        .build())
      .build()))
    .build());
  ```

  ```go Go theme={null}
  requestID, err := client.SendMessage(
    context.Background(),
    courier.SendMessageRequestBody{
      Message: map[string]interface{}{
        "to": map[string]string{
          "email": "user@example.com",
        },
        "content": map[string]string{
          "title": "Welcome!",
          "body": "Thanks for signing up, {{name}}",
        },
        "data": map[string]string{
          "name": "John Doe",
        },
        "routing": map[string]interface{}{
          "method": "single",
          "channels": []string{"email"},
        },
      },
    },
  )

  if err != nil {
    log.Fatal(err)
  }
  log.Printf("Message sent! Request ID: %s", requestID)
  ```

  ```csharp C# theme={null}
  try 
  {
    var response = await courier.SendAsync(
      new SendMessageRequest 
      {
        Message = new Message 
        {
          To = new Recipient 
          {
            Email = "user@example.com"
          },
          Content = new MessageContent 
          {
            Title = "Welcome!",
            Body = "Thanks for signing up, {{name}}"
          },
          Data = new Dictionary<string, object> 
          {
            { "name", "John Doe" }
          },
          Routing = new MessageRouting 
          {
            Method = "single",
            Channels = new[] { "email" }
          }
        }
      });

    Console.WriteLine($"Message sent! Request ID: {response.RequestId}");
  }
  catch (CourierException e)
  {
    Console.WriteLine($"Error: {e.Message}");
    Console.WriteLine($"Status Code: {e.StatusCode}");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {"email": "user@example.com"},
        "content": {
          "title": "Welcome!",
          "body": "Thanks for signing up, {{name}}"
        },
        "data": {"name": "John Doe"},
        "routing": {
          "method": "single",
          "channels": ["email"]
        }
      }
    }'
  ```
</CodeGroup>

<Tip>
  Courier also supports SDKs to send with popular languages and frameworks. Check out the <a href="https://github.com/trycourier/courier-samples" target="_blank">courier-samples</a> repository for ready-to-run Courier send examples.
</Tip>

Every send request contains a `message` object with four core fields: `to` (recipient), `content` or `template` (what to send), `routing` (which channels), and `data` (personalization variables). For a conceptual overview of how these work together, see [How Sending Works](/platform/sending/sending-overview).

### Sending Messages with Templates

[Templates](/platform/content/template-designer/template-designer-overview) are an easy way to create, update, and manage notification content in Courier without changing your code.

The `template` parameter accepts either a **template ID** or a **template alias**. Template IDs are permanent unique identifiers, while aliases are human-readable names you can give a template (eg welcome-email).

```json  theme={null}
{
  "message": {
    "template": "JN96DHQ99CMNZ5KVQ2RXJ1XYJRHT",
    "to": { "user_id": "user_123" },
    "data": {
      "name": "John Doe",
      "company": "Acme Corp"
    }
  }
}
```

### Sending to Users

Send to a [Courier User](/platform/users/users-overview) by specifying their `user_id` in the `to` field. Courier automatically looks up the user’s stored identifiers (email, phone, push tokens, chat handles) and applies your routing rules to deliver the message through the best available channels.

Use `profile` variables from the user object in your templates or channel conditions to personalize message content and control which channels are used.

```json  theme={null}
{
  "user_id": "user_123",
  "profile": {
    "email": "user@example.com",
    "phone_number": "+1234567890",
    "custom": {
      "name": "John Doe",
      "subscription_tier": "premium",
      "company": "Acme Corp",
      "role": "admin"
    }
  }
}
```

### Sending to Multiple Channels

You can send a single message across multiple channels using routing rules. In this example, Courier will try each channel in order until the message is successfully delivered.

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user_123" },
    "template": "order-confirmation", // Template alias
    "routing": {
      "method": "single",
      "channels": ["email", "sms", "push"]
    },
    "data": {
      "order_id": "ORD-12345",
      "total": "$99.99"
    }
  }
}
```

Courier supports two routing methods that define how messages flow across channels:

* **`single`** — Try channels in the listed order until one succeeds. This is the default and provides priority-based fallback delivery (for example, try push first, then email, then SMS).
* **`all`** — Send through every listed channel at once so users receive the message everywhere they’re active.

With `single`, the order of channels in the array determines priority. Courier attempts the first channel, and if delivery fails or the user lacks contact info for that channel, it moves to the next one.

### What Channels does Courier Support?

Courier supports sending through multiple channel types. Each channel can connect to one or more providers that you configure in your workspace.

* **`email`** — [SendGrid](/external-integrations/email/sendgrid), [Mailgun](/external-integrations/email/mailgun), [AWS SES](/external-integrations/email/aws-ses), and [more](/external-integrations/email/intro-to-email)
* **`sms`** — [Twilio](/external-integrations/sms/twilio), [MessageBird](/external-integrations/sms/messagebird), [Plivo](/external-integrations/sms/plivo), and [more](/external-integrations/sms/intro-to-sms)
* **`push`** — [Firebase FCM](/external-integrations/push/firebase-fcm), [Apple Push](/external-integrations/push/apple-push-notification), and [more](/external-integrations/push/intro-to-push)
* **`chat`** — [Slack](/external-integrations/direct-message/slack), [Microsoft Teams](/external-integrations/direct-message/microsoft-teams), and [more](/external-integrations/direct-message/intro-to-direct-message)
* **`inbox`** — [Courier Inbox](/platform/inbox/inbox-overview) for in-app notifications for web and mobile

Each channel is configured independently. You can include any combination of channels in a single send request and control delivery order or fallback behavior using routing rules.

### Sending to Multiple Users

Send the same message to multiple recipients in a single API call by using an array in the `to` field:

```json  theme={null}
{
  "message": {
    "to": [
      { "email": "user1@example.com" },
      { "email": "user2@example.com" },
      { "email": "user3@example.com" }
    ],
    "template": "FRH3QXM9E34W4RKP7MRC8NZ1T8V8",
    "data": {
      "payload": "Example payload"
    }
  }
}
```

When sending to multiple users, Courier processes each recipient individually. Each user receives their own personalized message based on their profile data and the template variables you provide.

The `data` object applies to all recipients. For user-specific personalization, ensure your template uses profile-based variables (`{{profile.variable}}`).

## Related Resources

<CardGroup cols={2}>
  <Card title="Send API Reference" href="/api-reference/send/send-a-message" icon="book">
    Complete API documentation and parameters
  </Card>

  <Card title="Message Logs" href="/platform/analytics/message-logs" icon="chart-line">
    Track delivery status and troubleshoot issues
  </Card>
</CardGroup>
