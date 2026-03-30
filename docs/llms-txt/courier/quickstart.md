# Source: https://www.courier.com/docs/getting-started/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Send your first notification with one API call. No dashboard setup required.

## Send your first notification

Send a notification in under two minutes. All you need is an API key.

<Steps>
  <Step title="Get your API key">
    Sign up or log in to [Courier](https://app.courier.com), then copy your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys).
  </Step>

  <Step title="Send a message">
    One API call sends an email. Use cURL, the [CLI](/tools/cli), or any of our [server SDKs](/sdk-libraries/sdks-overview). Replace `YOUR_API_KEY` with your key and `you@example.com` with your email address.

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST https://api.courier.com/send \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "message": {
            "to": { "email": "you@example.com" },
            "content": {
              "title": "Hello from Courier!",
              "body": "You just sent your first notification. Nice work, {{name}}."
            },
            "data": { "name": "Developer" },
            "routing": {
              "method": "single",
              "channels": ["email"]
            }
          }
        }'
      ```

      ```bash CLI theme={null}
      # npm install -g @trycourier/cli
      export COURIER_API_KEY=YOUR_API_KEY

      courier send message \
        --message.to.email "you@example.com" \
        --message.content.title "Hello from Courier!" \
        --message.content.body "You just sent your first notification. Nice work, {{name}}." \
        --message.data '{"name": "Developer"}' \
        --message.routing.method "single" \
        --message.routing.channels '["email"]'
      ```

      ```javascript Node.js theme={null}
      // npm install @trycourier/courier
      import { CourierClient } from "@trycourier/courier";

      const courier = new CourierClient({ authorizationToken: "YOUR_API_KEY" });

      const { requestId } = await courier.send({
        message: {
          to: { email: "you@example.com" },
          content: {
            title: "Hello from Courier!",
            body: "You just sent your first notification. Nice work, {{name}}.",
          },
          data: { name: "Developer" },
          routing: { method: "single", channels: ["email"] },
        },
      });

      console.log("Sent! Request ID:", requestId);
      ```

      ```python Python theme={null}
      # pip install trycourier
      from courier.client import Courier

      client = Courier(authorization_token="YOUR_API_KEY")

      response = client.send(
        message={
          "to": {"email": "you@example.com"},
          "content": {
            "title": "Hello from Courier!",
            "body": "You just sent your first notification. Nice work, {{name}}.",
          },
          "data": {"name": "Developer"},
          "routing": {"method": "single", "channels": ["email"]},
        }
      )

      print("Sent! Request ID:", response.request_id)
      ```

      ```ruby Ruby theme={null}
      # gem install trycourier
      require "trycourier"

      client = Courier::Client.new "YOUR_API_KEY"

      res = client.send({
        message: {
          to: { email: "you@example.com" },
          content: {
            title: "Hello from Courier!",
            body: "You just sent your first notification. Nice work, {{name}}.",
          },
          data: { name: "Developer" },
          routing: { method: "single", channels: ["email"] },
        },
      })
      ```

      ```go Go theme={null}
      // go get github.com/trycourier/courier-go/v2
      import (
        "context"
        "fmt"
        "github.com/trycourier/courier-go/v2"
      )

      client := courier.CreateClient("YOUR_API_KEY", nil)

      requestID, err := client.SendMessage(
        context.Background(),
        courier.SendMessageRequestBody{
          Message: map[string]interface{}{
            "to":      map[string]string{"email": "you@example.com"},
            "content": map[string]string{
              "title": "Hello from Courier!",
              "body":  "You just sent your first notification. Nice work, {{name}}.",
            },
            "data":    map[string]string{"name": "Developer"},
            "routing": map[string]interface{}{
              "method":   "single",
              "channels": []string{"email"},
            },
          },
        },
      )

      fmt.Println("Sent! Request ID:", requestID)
      ```
    </CodeGroup>

    The response includes a `requestId` you can use to track delivery:

    ```json  theme={null}
    { "requestId": "1-67890abc-d1e2f3a4b5c6" }
    ```
  </Step>

  <Step title="Verify delivery">
    Open [Message Logs](https://app.courier.com/logs) in your dashboard. You should see your message with a timeline showing each stage: accepted, routed, rendered, sent, and delivered.

    If the message doesn't appear, double-check that your API key is correct and that you're viewing the right environment (Test vs Production).
  </Step>
</Steps>

That's it. One API call, one notification delivered.

## Building with AI

If you're using an AI coding agent (Claude Code, Cursor, Codex, etc.), Courier's [MCP server](/tools/mcp) gives your agent direct access to the full API; it can send messages, manage users, debug deliveries, and more without leaving your editor. The [CLI](/tools/cli) works the same way from any terminal or CI pipeline. See [Build with AI](/tools/ai-onboarding) for setup instructions.

## FAQ

<AccordionGroup>
  <Accordion title="Do I need to configure a provider first?">
    Not necessarily. Courier includes a built-in email provider, so email works out of the box in Test mode. For production email, SMS, push, or chat you'll need to connect a provider in [Integrations](https://app.courier.com/integrations). The [Inbox](/platform/inbox/inbox-overview) and Toast channels also work without any external provider.
  </Accordion>

  <Accordion title="Can I design templates visually instead of writing content in code?">
    Yes. Courier's [Template Designer](/platform/content/template-designer/template-designer-overview) lets you build notifications visually with drag-and-drop blocks, then reference them by ID in your send call. See the [Design Your First Notification](/tutorials/content/how-to-design-your-first-notification) tutorial for a walkthrough.
  </Accordion>

  <Accordion title="How do I send to SMS, push, or multiple channels at once?">
    Add a provider for the channel you want in [Integrations](https://app.courier.com/integrations), then update the `routing` object in your send call. To send to multiple channels, set `method` to `"all"` and list the channels you want. See [How Sending Works](/platform/sending/sending-overview) for details on routing and fallback behavior.
  </Accordion>

  <Accordion title="Where do I find SDKs for other languages?">
    We have official SDKs for Node.js, Python, Ruby, Go, Java, PHP, and C#, plus mobile SDKs for iOS, Android, React Native, and Flutter. See the full list on the [SDKs overview](/sdk-libraries/sdks-overview). You can also call the [REST API](/api-reference/send/send-a-message) directly from any language.
  </Accordion>
</AccordionGroup>

## What to do next

<CardGroup cols={2}>
  <Card title="How Sending Works" href="/platform/sending/sending-overview" icon="paper-plane">
    Understand routing, channels, and the delivery pipeline
  </Card>

  <Card title="Design a Template" href="/tutorials/content/how-to-design-your-first-notification" icon="palette">
    Build a reusable notification in the visual Template Designer
  </Card>

  <Card title="Add an In-App Inbox" href="/tutorials/inbox/how-to-implement-inbox" icon="inbox">
    Embed a real-time notification feed in your app; no provider needed
  </Card>

  <Card title="Build with AI" href="/tools/ai-onboarding" icon="microchip-ai">
    Connect your AI coding agent to Courier via MCP or CLI
  </Card>
</CardGroup>
