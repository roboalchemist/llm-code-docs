# Source: https://www.courier.com/docs/tutorials/automations/how-to-send-an-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Send Automations via API

> Invoke automations via the Courier API by calling a saved automation or defining one inline.

Courier provides two ways to trigger an automation programmatically: invoke a saved automation by ID, or define one inline (ad-hoc). Most use cases start with a saved automation built in the Designer; ad-hoc is useful when the workflow itself needs to change per request.

## Prerequisites

* A [Courier account](https://app.courier.com/) with at least one configured provider
* At least one published notification template
* Your Courier API key (found in [Settings > API Keys](https://app.courier.com/settings/api-keys))

## Saved vs Ad-Hoc Automations

|                   | Saved Automation                                                                       | Ad-Hoc Automation                                |
| ----------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Definition**    | Built and published in the [Automations Designer](https://app.courier.com/automations) | Defined inline in the API request                |
| **Endpoint**      | `POST /automations/:automationId/invoke`                                               | `POST /automations/invoke`                       |
| **Best for**      | Reusable workflows triggered by events or API calls                                    | Dynamic workflows where steps change per request |
| **Visual editor** | Yes; build visually, test with debugger, then invoke via API                           | No                                               |

## Invoke a Saved Automation

When you've built an automation in the [Automations Designer](https://app.courier.com/automations) and published it, invoke it by its ID. The automation defines the steps; you provide the runtime data.

<Steps>
  <Step title="Find the automation ID">
    Open your automation in the Designer. You can find the ID in two places:

    * The **Invoke** tab, which generates a ready-to-use curl command with the ID filled in
    * The URL bar: `app.courier.com/automations/:automationId`

    You can also use an alias if you configured one in Automation Settings.
  </Step>

  <Step title="Invoke with runtime data">
    <CodeGroup>
      ```bash cURL icon="terminal" wrap theme={null}
      curl -X POST https://api.courier.com/automations/AUTOMATION_ID/invoke \
        -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "recipient": "user_123",
          "data": {
            "order_id": "ORD-9042"
          },
          "profile": {
            "email": "jane@example.com"
          }
        }'
      ```

      ```javascript Node.js icon="node-js" theme={null}
      import Courier from "@trycourier/courier";

      const client = new Courier({ apiKey: "your_api_key" });

      const { runId } = await client.automations.invoke.invokeByTemplate(
        "AUTOMATION_ID",
        {
          recipient: "user_123",
          data: { order_id: "ORD-9042" },
          profile: { email: "jane@example.com" },
        }
      );

      console.log("Run ID:", runId);
      ```

      ```python Python icon="python" theme={null}
      from courier import Courier

      client = Courier(api_key="your_api_key")

      response = client.automations.invoke.invoke_by_template(
          "AUTOMATION_ID",
          recipient="user_123",
          data={"order_id": "ORD-9042"},
          profile={"email": "jane@example.com"},
      )

      print("Run ID:", response.run_id)
      ```
    </CodeGroup>

    The `data` and `profile` objects become the automation's run context, accessible in every node via `refs.data.*` and `refs.profile.*`.
  </Step>

  <Step title="Verify in the debugger">
    The response includes a `runId`. Open the [Automations Debugger](https://app.courier.com/automations/debugger) and search for it to see each step's status and any errors.
  </Step>
</Steps>

<Tip>
  New to building automations? Follow [Build and Send Your First Automation](/tutorials/automations/how-to-automate-message-sequences) to create one in the visual designer before invoking it here.
</Tip>

## Invoke an Ad-Hoc Automation

Define the full workflow inline. This is useful when the steps or recipients need to change per request and you don't want to create a saved automation for every variation.

<Steps>
  <Step title="Define the workflow and invoke">
    <CodeGroup>
      ```bash cURL icon="terminal" wrap theme={null}
      curl -X POST https://api.courier.com/automations/invoke \
        -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "automation": {
            "steps": [
              {
                "action": "send",
                "template": "ORDER_CONFIRMATION"
              },
              {
                "action": "delay",
                "duration": "2 hours"
              },
              {
                "action": "send",
                "template": "SHIPPING_UPDATE"
              }
            ]
          },
          "recipient": "user_123",
          "data": {
            "order_id": "ORD-9042",
            "item_name": "Wireless Headphones"
          }
        }'
      ```

      ```javascript Node.js icon="node-js" theme={null}
      import Courier from "@trycourier/courier";

      const client = new Courier({ apiKey: "your_api_key" });

      const { runId } = await client.automations.invoke.invokeAdHoc({
        automation: {
          steps: [
            { action: "send", template: "ORDER_CONFIRMATION" },
            { action: "delay", duration: "2 hours" },
            { action: "send", template: "SHIPPING_UPDATE" },
          ],
        },
        recipient: "user_123",
        data: {
          order_id: "ORD-9042",
          item_name: "Wireless Headphones",
        },
      });

      console.log("Run ID:", runId);
      ```

      ```python Python icon="python" theme={null}
      from courier import Courier

      client = Courier(api_key="your_api_key")

      response = client.automations.invoke.invoke_ad_hoc(
          automation={
              "steps": [
                  {"action": "send", "template": "ORDER_CONFIRMATION"},
                  {"action": "delay", "duration": "2 hours"},
                  {"action": "send", "template": "SHIPPING_UPDATE"},
              ],
          },
          recipient="user_123",
          data={
              "order_id": "ORD-9042",
              "item_name": "Wireless Headphones",
          },
      )

      print("Run ID:", response.run_id)
      ```
    </CodeGroup>

    The response includes a `runId` you can use to track the automation in the [Automations Debugger](/platform/automations/debugger).
  </Step>
</Steps>

<Note>
  The `template` field inside each `send` step refers to a notification template (the content you design in the Template Designer), not an automation. This is the one place where "template" appears in the automations API.
</Note>

## What's Next

<CardGroup cols={2}>
  <Card title="Build and Send Your First Automation" icon="sitemap" href="/tutorials/automations/how-to-automate-message-sequences">
    Build a multi-step workflow in the visual Automations Designer
  </Card>

  <Card title="How to Send Digests" icon="envelope" href="/tutorials/sending/how-to-send-digests">
    Batch notifications into periodic digest messages using automations
  </Card>

  <Card title="Trigger Automations from Segment" icon="sitemap" href="/tutorials/sending/how-to-send-notifications-with-segment">
    Connect Segment events to Courier automations
  </Card>

  <Card title="Automation API Reference" icon="code" href="/api-reference/automations/invoke-an-automation">
    Full API documentation for invoking automations
  </Card>
</CardGroup>
