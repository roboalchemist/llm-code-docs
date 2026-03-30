# Source: https://www.courier.com/docs/platform/inbox/sending-a-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send an Inbox Message

> Send Inbox messages with the Courier Send API

Send an Inbox message using the [Send API](/api-reference/send/send-a-message), including `inbox` as a routing channel.
Routing channels control the delivery method for a message. Other channels include `email`, `SMS` and `push`.

<Tip>
  Sending to the Inbox channel requires the Courier Inbox provider to be added to your workspace. In [your workspace](https://app.courier.com/) navigate to **Integrations > Add Integration > Inbox > Courier** to add the provider.
</Tip>

In the example below, we call the Send API to send a message to a user's Inbox with variable interpolation.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "user_id": "example_user"
        },
        "content": {
          "title": "How does {{ villain }} like his toast?",
          "body": "On the dark side."
        },
        "data": {
          "villain": "Darth Vader"
        },
        "routing": {
          "method": "single",
          "channels": ["inbox"]
        }
      }
    }'
  ```

  ```javascript Node.js theme={null}
  const { requestId } = await courier.send({
    message: {
      to: { user_id: "example_user" },
      content: {
        title: "How does {{ villain }} like his toast?",
        body: "On the dark side."
      },
      data: {
        villain: "Darth Vader"
      },
      routing: {
        method: "single",
        channels: ["inbox"]
      }
    }
  });
  ```

  ```python Python theme={null}
  response = client.send(
    message=courier.ContentMessage(
      to=courier.UserRecipient(user_id="example_user"),
      content=courier.ElementalContentSugar(
        title="How does {{ villain }} like his toast?",
        body="On the dark side."
      ),
      data={"villain": "Darth Vader"},
      routing=courier.Routing(method="single", channels=["inbox"])
    )
  )
  ```

  ```ruby Ruby theme={null}
  res = client.send({
    message: {
      to: { user_id: "example_user" },
      content: {
        title: "How does {{ villain }} like his toast?",
        body: "On the dark side."
      },
      data: {
        villain: "Darth Vader"
      },
      routing: {
        method: "single",
        channels: ["inbox"]
      }
    }
  })
  ```

  ```php PHP theme={null}
  $result = $courier->send(
    (object) [
      'to' => [
        'user_id' => "example_user"
      ],
      'content' => [
        'title' => "How does {{ villain }} like his toast?",
        'body' => "On the dark side."
      ],
      'data' => [
        'villain' => "Darth Vader"
      ],
      'routing' => [
        'method' => "single",
        'channels' => ["inbox"]
      ]
    ]
  );
  ```

  ```java Java theme={null}
  courier.send(SendMessageRequest.builder()
    .message(Message.of(TemplateMessage.builder()
      .to(MessageRecipient.of(Recipient.of(UserRecipient.builder()
        .userId("example_user")
        .build())))
      .content(ContentMessage.builder()
        .title("How does {{ villain }} like his toast?")
        .body("On the dark side.")
        .build())
      .data(Map.of("villain", "Darth Vader"))
      .routing(Routing.builder()
        .method("single")
        .channels(List.of("inbox"))
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
          "user_id": "example_user",
        },
        "content": map[string]string{
          "title": "How does {{ villain }} like his toast?",
          "body": "On the dark side.",
        },
        "data": map[string]string{
          "villain": "Darth Vader",
        },
        "routing": map[string]interface{}{
          "method": "single",
          "channels": []string{"inbox"},
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
            UserId = "example_user"
          },
          Content = new MessageContent 
          {
            Title = "How does {{ villain }} like his toast?",
            Body = "On the dark side."
          },
          Data = new Dictionary<string, object> 
          {
            { "villain", "Darth Vader" }
          },
          Routing = new MessageRouting 
          {
            Method = "single",
            Channels = new[] { "inbox" }
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
</CodeGroup>

## Passing `data` with an Inbox message

If you provide information in the `data` field, it will be passed with the inbox or push message to the SDK.

Data that is referenced in your `content` payload or in a template (like `{{ villain }}` in the example above),
will be interpolated.

Data that is not referenced will still be passed through with the message. This can be
particularly useful for *deep linking*, opening a particular view in your app from a link or push notification.

## Using Courier Elemental Syntax

Inbox SDKs support a subset of [Elemental syntax](/platform/content/elemental/elemental-overview).
Elemental is a JSON-based templating format for composing cross-platform notifications.

| Element | Web                                           | iOS                                           | Android                                       |
| :------ | :-------------------------------------------- | :-------------------------------------------- | :-------------------------------------------- |
| Title   | <Icon icon="square-check" iconType="solid" /> | <Icon icon="square-check" iconType="solid" /> | <Icon icon="square-check" iconType="solid" /> |
| Body    | <Icon icon="square-check" iconType="solid" /> | <Icon icon="square-check" iconType="solid" /> | <Icon icon="square-check" iconType="solid" /> |
| Text    | <Icon icon="square-check" iconType="solid" /> |                                               |                                               |
| Action  | <Icon icon="square-check" iconType="solid" /> | <Icon icon="square-check" iconType="solid" /> | <Icon icon="square-check" iconType="solid" /> |

Check out the [full list of elements](/platform/content/elemental/elements/index) for syntax and examples.

## Send Using A Template

You can create a notification template using the [Notification Designer](https://app.courier.com/assets/templates). After you create a template (or edit an existing one), add a new channel and select "Inbox". This will provide you with a blank template that you can use to customize the content that will delivered with that notification.

When calling the API, replace the `content` field with a `template` field that defines either a Template ID or an Event ID.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "user_id": "example_user"
        },
        "template": "TEMPLATE_OR_EVENT_ID",
        "data": {
          "villain": "Darth Vader"
        },
        "routing": {
          "method": "single",
          "channels": ["inbox"]
        }
      }
    }'
  ```

  ```javascript Node.js theme={null}
  const { requestId } = await courier.send({
    message: {
      to: { user_id: "example_user" },
      template: "TEMPLATE_OR_EVENT_ID",
      data: {
        villain: "Darth Vader"
      },
      routing: {
        method: "single",
        channels: ["inbox"]
      }
    }
  });
  ```

  ```python Python theme={null}
  response = client.send(
    message=courier.TemplateMessage(
      to=courier.UserRecipient(user_id="example_user"),
      template="TEMPLATE_OR_EVENT_ID",
      data={"villain": "Darth Vader"},
      routing=courier.Routing(method="single", channels=["inbox"])
    )
  )
  ```

  ```ruby Ruby theme={null}
  res = client.send({
    message: {
      to: { user_id: "example_user" },
      template: "TEMPLATE_OR_EVENT_ID",
      data: {
        villain: "Darth Vader"
      },
      routing: {
        method: "single",
        channels: ["inbox"]
      }
    }
  })
  ```

  ```php PHP theme={null}
  $result = $courier->send(
    (object) [
      'to' => [
        'user_id' => "example_user"
      ],
      'template' => "TEMPLATE_OR_EVENT_ID",
      'data' => [
        'villain' => "Darth Vader"
      ],
      'routing' => [
        'method' => "single",
        'channels' => ["inbox"]
      ]
    ]
  );
  ```

  ```java Java theme={null}
  courier.send(SendMessageRequest.builder()
    .message(Message.of(TemplateMessage.builder()
      .to(MessageRecipient.of(Recipient.of(UserRecipient.builder()
        .userId("example_user")
        .build())))
      .template("TEMPLATE_OR_EVENT_ID")
      .data(Map.of("villain", "Darth Vader"))
      .routing(Routing.builder()
        .method("single")
        .channels(List.of("inbox"))
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
          "user_id": "example_user",
        },
        "template": "TEMPLATE_OR_EVENT_ID",
        "data": map[string]string{
          "villain": "Darth Vader",
        },
        "routing": map[string]interface{}{
          "method": "single",
          "channels": []string{"inbox"},
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
            UserId = "example_user"
          },
          Template = "TEMPLATE_OR_EVENT_ID",
          Data = new Dictionary<string, object> 
          {
            { "villain", "Darth Vader" }
          },
          Routing = new MessageRouting 
          {
            Method = "single",
            Channels = new[] { "inbox" }
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
</CodeGroup>
