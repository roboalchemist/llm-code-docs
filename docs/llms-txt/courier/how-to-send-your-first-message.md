# Source: https://www.courier.com/docs/tutorials/sending/how-to-send-your-first-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Send Your First Message

> Welcome to Courier! In this guide we'll walk you through the basics for sending your first notification.

## Creating a Notification Template

To create your first notification, head to the [Templates page](https://app.courier.com/assets/templates) and create a notification from the `New` button. Select `Message Template`, and follow the prompt to name your notification.

<Steps>
  <Step title="Add a Delivery Channel">
    After creating your message template, select a delivery channel and choose a provider, or you can directly select a standalone provider. In this example, we've added an `Email` channel and selected [SendGrid](/external-integrations/email/sendgrid) as the provider.

    <Frame caption="Select your channel provider">
      <img src="https://mintcdn.com/courier-4f1f25dc/QbP8b2qHqZl-zVnL/assets/tutorials/sending/channel-selection.png?fit=max&auto=format&n=QbP8b2qHqZl-zVnL&q=85&s=2f2eb920dd40131a8cffcb304a9c01d8" width="2606" height="1296" data-path="assets/tutorials/sending/channel-selection.png" />
    </Frame>
  </Step>

  <Step title="Go Back to your Channel">
    After selecting your delivery channel, you can begin editing your template by selecting the newly added channel on the left side of the page.
  </Step>

  <Step title="Create Your Notification Content">
    Now that you have selected a channel and provider, you can begin creating content for your notification. Courier offers an intuitive UI for building notifications using [content blocks](/platform/content/content-blocks/content-block-basics) and [dynamic variables](/platform/content/variables/inserting-variables).

    <Tip>
      To learn more about designing notifications effectively, see our [Template Designer tutorial](/tutorials/content/how-to-design-your-first-notification).
    </Tip>
  </Step>

  <Step title="Design for Multiple Channels (Optional)">
    Once you're satisfied with your email channel content, you can add additional channels and easily reuse content blocks from the Content Library. Courier automatically adapts your content blocks for each channel's unique technical requirements.
  </Step>

  <Step title="Understand Delivery Routing Strategy">
    By default, message templates in the Courier designer will be configured to use the `best of` [routing strategy](/platform/sending/channel-priority). This means that if your message template has multiple delivery channels, Courier will send to the first channel in the list and try the following channels in order if we encounter an error.

    Below you can find a brief breakdown of the different routing strategies:

    | Strategy           | Routing Description                                                                                                                                                                                                                                   | API Definition |
    | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
    | **Best of**        | Courier will attempt to send to the first channel configured in the message template. Any subsequent channels will be used if the request encounters an `INCOMPLETE_PROFILE` error, and continue down the list until all options have been exhausted. | `single`       |
    | **Always send to** | Courier will send to **all** configured channels in the message template.                                                                                                                                                                             | `all`          |
  </Step>
</Steps>

## Previewing and Publishing your Template

Now that you have a complete notification template, you can easily test it right within the template UI before sending it to real users.

<Steps>
  <Step title="Preview Your Notification">
    Start by opening the `Preview` tab in your notification, then hit `Create Test Event` to see how it will render in a simulated email client. Here you can see how [dynamic variables](/platform/content/variables/inserting-variables) will render from the data in your test events.

    <Tip>
      For a more in-depth walkthrough, check out our Template Designer preview [tutorial](/platform/content/template-designer/how-to-preview-notification).
    </Tip>
  </Step>

  <Step title="Understand Data and Profile Objects">
    Courier uses JSON-formatted payloads to pass relevant data (e.g. names, dates, email addresses, phone numbers) into your message templates. There are of two key elements in a Courier send request that help you personalize your notifications:

    | JSON Object | Description                                                                                                                                                                                                                                                        | API Definition |
    | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
    | Data        | The data object in the send request contains key-value pairs for dynamic fields in your template, such as `name`, `date`, or `flight time`. If your template includes `{name}`, Courier fills it using the value from the data object, e.g., `"name": "John Doe"`. | `data`         |
    | Profile     | The [profile object](/platform/users/users) contains all your recipient information, like `email` and `phone_number`. If you want to reference values from the profile in your message template, you must format the path like `{profile.name}`.                   | `to`           |
  </Step>

  <Step title="Publish Your Changes">
    After confirming that your preview displays all variables and content blocks correctly, click `Publish` in the top right corner to apply your changes. Your notification is now live and ready to send.
  </Step>
</Steps>

## Sending a Test Notification

Now that you're happy with your message template, how it looks, and you've published it, it's time to send. We'll cover 2 ways you can send your notification:

### 1. Sending from the Designer

Once your template is published, the fastest way to test it is via the Designer UI `Send` tab. Here you can edit your test event data or specify a non-default [brand](/tutorials/content/how-to-create-and-use-brands) if you want to customize your message.

<Frame caption="Send test notification from the Designer">
  <img src="https://mintcdn.com/courier-4f1f25dc/fzDzb8rXw-5hGi1q/assets/tutorials/sending/send-notification-code.jpeg?fit=max&auto=format&n=fzDzb8rXw-5hGi1q&q=85&s=bf7e40dcc0c600a4dbce4cf9d6f663ce" width="3456" height="1804" data-path="assets/tutorials/sending/send-notification-code.jpeg" />
</Frame>

When you're ready, click the green `Send Test` button, and Courier will deliver the notification to the profile specified in your test event. You'll see a toast notification confirming your test message has been sent. Afterward, you can [view the logs](/platform/analytics/message-logs) to verify its delivery status.

<Check>
  **Congratulations!** You've successfully created and sent your first notification with Courier. For a more configurable and powerful way to send your templated messages, check out the next section on sending from an API platform.
</Check>

### 2. Sending from an API Platform

Now, let's explore how to send your notification using an API platform such as Postman or Insomnia. This approach gives you a foundation for programmatically integrating Courier notifications into your application. To make a successful send, you'll need the following:

1. **Notification template ID:** Locate this in your [template settings](/platform/content/template-settings/general-settings) by selecting the gear icon at the top right, or by finding it in the template's URL just before `/design`
2. **API Key:** Navigate to [workspace settings](https://app.courier.com/settings/api-keys) to find your [Courier API key](/platform/workspaces/environments-api-keys) from the appropriate environment (usually `Production` or `Test`)

The send API uses the `https://api.courier.com/send` [endpoint](/api-reference/send/send-a-message) to send messages. Use the following complete request in your API platform editor, replacing the `template`, `email`, and `YOUR_AUTH_TOKEN` fields with your own:

```bash cURL theme={null}
curl -X POST https://api.courier.com/send \
  -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "template": "YOUR_TEMPLATE_ID",
      "to": {
        "email": "YOUR_EMAIL"
      },
      "data": {
        "name": "Spike Spiegel"
      }
    }
  }'
```

<Note>
  The `"to"` field in your send request corresponds to the `"profile"` object from your [test event](#preparing-a-test-event-to-configure-data-and-recipients); add your recipient's email or other profile fields inside `"to"` just as shown under `"profile"`.
</Note>

After you've sent this API request, you can monitor the status and delivery details of your notification by visiting the [message logs](/platform/analytics/message-logs). The message logs provide valuable insights into each message event, including delivery status, engagement, and any potential errors.

Once you are comfortable that your test notification is rendering and sending to the correct channels, you can use this same API request as a building block to integrate Courier notifications directly into your application's backend or workflow. Happy sending!

## Sending with Courier SDKs

Instead of making raw HTTP requests, you can use Courier's server-side SDKs to send notifications directly from your application code. The SDKs handle authentication, request formatting, and error handling for you. Here's how to implement the same send request from the cURL example above using Courier SDKs:

<CodeGroup>
  ```node-js Node.js theme={null}
  import Courier from '@trycourier/courier';

  const client = new Courier({ apiKey: "YOUR_AUTH_TOKEN" });

  const response = await client.send.message({
    message: {
      to: {
        email: "YOUR_EMAIL"
      },
      template: "YOUR_TEMPLATE_ID",
      data: {
        name: "Spike Spiegel"
      }
    }
  });
  ```

  ```python Python theme={null}
  from courier import Courier

  client = Courier(api_key="YOUR_AUTH_TOKEN")

  response = client.send.message(
      message={
          "to": {
              "email": "YOUR_EMAIL"
          },
          "template": "YOUR_TEMPLATE_ID",
          "data": {
              "name": "Spike Spiegel"
          }
      }
  )
  ```

  ```ruby Ruby theme={null}
  require 'trycourier'

  client = Trycourier::Client.new(api_key: "YOUR_AUTH_TOKEN")

  response = client.send_.message(
    message: {
      to: {
        email: "YOUR_EMAIL"
      },
      template: "YOUR_TEMPLATE_ID",
      data: {
        name: "Spike Spiegel"
      }
    }
  )
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "github.com/trycourier/courier-go/v4"
      "github.com/trycourier/courier-go/v4/option"
  )

  func main() {
      client := courier.NewClient(
          option.WithAPIKey("YOUR_AUTH_TOKEN"),
      )

      requestBody := map[string]interface{}{
          "message": map[string]interface{}{
              "to": map[string]interface{}{
                  "email": "YOUR_EMAIL",
              },
              "template": "YOUR_TEMPLATE_ID",
              "data": map[string]interface{}{
                  "name": "Spike Spiegel",
              },
          },
      }

      var response map[string]interface{}
      err := client.Post(
          context.Background(),
          "/send",
          requestBody,
          &response,
      )
  }
  ```

  ```java Java theme={null}
  import com.courier.client.CourierClient;
  import com.courier.client.okhttp.CourierOkHttpClient;
  import com.courier.core.JsonValue;
  import com.courier.models.send.SendMessageParams;

  CourierClient client = CourierOkHttpClient.builder()
      .apiKey("YOUR_AUTH_TOKEN")
      .build();

  SendMessageParams params = SendMessageParams.builder()
      .message(SendMessageParams.Message.builder()
          .to(JsonValue.from(java.util.Map.of("email", "YOUR_EMAIL")))
          .template("YOUR_TEMPLATE_ID")
          .data(JsonValue.from(java.util.Map.of("name", "Spike Spiegel")))
          .build())
      .build();

  var response = client.send().message(params);
  ```

  ```php PHP theme={null}
  <?php

  use Courier\Client;

  $client = new Client(apiKey: "YOUR_AUTH_TOKEN");

  $response = $client->send->message([
      'message' => [
          'to' => [
              'email' => 'YOUR_EMAIL'
          ],
          'template' => 'YOUR_TEMPLATE_ID',
          'data' => [
              'name' => 'Spike Spiegel'
          ]
      ]
  ]);
  ```

  ```csharp C# theme={null}
  using System.Collections.Generic;
  using System.Text.Json;
  using Courier;
  using Courier.Models;
  using Courier.Models.Send;

  var client = new CourierClient { APIKey = "YOUR_AUTH_TOKEN" };

  var parameters = new SendMessageParams
  {
      Message = new Message
      {
          To = new UserRecipient { Email = "YOUR_EMAIL" },
          Template = "YOUR_TEMPLATE_ID",
          Data = new Dictionary<string, JsonElement>
          {
              { "name", JsonSerializer.SerializeToElement("Spike Spiegel") }
          }
      }
  };

  var response = await client.Send.Message(parameters);
  ```
</CodeGroup>

To get started with a specific SDK, install it using your language's package manager and replace `YOUR_AUTH_TOKEN` with your [Courier API key](/platform/workspaces/environments-api-keys). For more complete examples and advanced use cases, check out the [Courier SDK samples repository](https://github.com/trycourier/courier-samples#server).

## What's Next

<CardGroup cols={2}>
  <Card title="Brand Your Notifications" icon="copyright" href="/tutorials/content/how-to-create-and-use-brands">
    Apply logos, colors, and footers with Courier Brands
  </Card>

  <Card title="Configure Multi-Channel Routing" icon="list-tree" href="/tutorials/sending/how-to-configure-multi-channel-routing">
    Set up channel priority and failover rules
  </Card>

  <Card title="Send Bulk Notifications" icon="envelopes-bulk" href="/tutorials/sending/how-to-send-bulk-notifications">
    Send notifications to many recipients at once
  </Card>

  <Card title="Send API Reference" icon="code" href="/api-reference/send/send-a-message">
    Full API documentation for the Send endpoint
  </Card>
</CardGroup>
