# Source: https://www.courier.com/docs/tutorials/journeys/how-to-create-your-first-journey.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Create Your First Journey

> Build a journey from scratch: choose a trigger, define a schema, add a send node, design a message, publish, and invoke.

This tutorial walks you through creating a simple journey end-to-end: one trigger, one send node, one email. By the end, you'll have a working journey that sends an email when invoked via API.

<Tip>
  Journeys can do much more than send a single email. Add [delays](/platform/journeys/nodes/delay) to space out messages, [branches](/platform/journeys/nodes/branch) to send users down different paths, [fetch nodes](/platform/journeys/nodes/fetch-data) to pull in data from external APIs, or [throttles](/platform/journeys/nodes/throttle) to prevent over-messaging. Once you're comfortable with the basics, check out [Build an Onboarding Journey](/tutorials/journeys/how-to-build-a-multi-step-onboarding-journey) for a more advanced example.
</Tip>

## Prerequisites

* A [Courier account](https://app.courier.com/) with at least one email provider configured (e.g., SendGrid, Postmark, Amazon SES)
* Your Courier API key (found in [Settings > API Keys](https://app.courier.com/settings/api-keys))

## Build the Journey

<Steps>
  <Step title="Create a new journey">
    Navigate to [Journeys](https://app.courier.com/journeys) and click **New Journey**. You'll see the trigger selection screen.

    <Frame caption="The trigger selection screen: choose Segment event or API">
      <img src="https://mintcdn.com/courier-4f1f25dc/Dtl1DGeq8V31J3OW/assets/platform/journeys/new-journey-page.png?fit=max&auto=format&n=Dtl1DGeq8V31J3OW&q=85&s=53a6373d19d2aee2f4d195a2cf4192c8" width="1722" height="1044" data-path="assets/platform/journeys/new-journey-page.png" />
    </Frame>
  </Step>

  <Step title="Choose the API trigger">
    Click **API**. This creates a journey that starts when your code sends a POST request. Courier adds a trigger node to the canvas and opens its configuration panel.
  </Step>

  <Step title="Define schema fields">
    Schema fields define the data contract between your application and this journey. Every invocation must include these fields.

    Add two fields:

    | Field name      | Type   |
    | --------------- | ------ |
    | `user_name`     | String |
    | `signup_source` | String |

    Click **Add Field** for each one, enter the name, select the type, and save. These fields will be available as variables throughout the journey.

    <Frame caption="API trigger with user_name and signup_source schema fields defined">
      <img src="https://mintcdn.com/courier-4f1f25dc/US23xPO8q7EoK5r0/assets/tutorials/journeys/first-journey-schema.png?fit=max&auto=format&n=US23xPO8q7EoK5r0&q=85&s=f9637b2f289f65ac9b8727d8e6d3e93a" width="3456" height="1822" data-path="assets/tutorials/journeys/first-journey-schema.png" />
    </Frame>
  </Step>

  <Step title="Add a Send Email node">
    Drag a **Send** node from the palette onto the canvas below the trigger, or click the **+** button on the edge below the trigger node. Select **Email** as the channel.
  </Step>

  <Step title="Create the message template">
    In the send node's configuration panel, click **+ Create** next to "Message." Courier creates a new template and opens the template designer.

    Design your welcome email:

    1. In the **Subject** field at the top, type `Welcome,` then insert the `user_name` variable so it reads `Welcome, {{user_name}}!`
    2. In the body editor, add a **Text** block and write something like `Thanks for signing up via {{signup_source}}. We're glad you're here.`

    Close the designer when you're done. The send node now shows the template name.

    <Frame caption="Send node with the welcome email template linked">
      <img src="https://mintcdn.com/courier-4f1f25dc/9dg9CqK7u26CvUgl/assets/tutorials/journeys/send-node-with-template.png?fit=max&auto=format&n=9dg9CqK7u26CvUgl&q=85&s=2bac5d5ccfa73e3371b16675699986dd" width="3456" height="1822" data-path="assets/tutorials/journeys/send-node-with-template.png" />
    </Frame>
  </Step>

  <Step title="Publish the journey">
    Click **Publish** in the top-right corner. The journey is now live and ready to receive invocations.
  </Step>
</Steps>

## Invoke the Journey

Copy the journey ID from the URL bar (`app.courier.com/journeys/:journeyId/design`) and invoke it with your schema fields.

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/journeys/YOUR_JOURNEY_ID/invoke \
    -H "Authorization: Bearer $COURIER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "user_id": "user_123",
      "data": {
        "user_name": "Jane",
        "signup_source": "homepage"
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  import Courier from "@trycourier/courier";

  const client = new Courier({ apiKey: "your_api_key" });

  const { runId } = await client.journeys.invoke("YOUR_JOURNEY_ID", {
    userId: "user_123",
    data: {
      user_name: "Jane",
      signup_source: "homepage",
    },
  });

  console.log("Run ID:", runId);
  ```

  ```python Python icon="python" theme={null}
  from courier import Courier

  client = Courier(api_key="your_api_key")

  response = client.journeys.invoke(
      "YOUR_JOURNEY_ID",
      user_id="user_123",
      data={
          "user_name": "Jane",
          "signup_source": "homepage",
      },
  )

  print("Run ID:", response.run_id)
  ```
</CodeGroup>

You should get a `202` response with a `runId`.

<Note>
  Make sure user `user_123` has an email address in their Courier profile, or include it in the `profile` field of the request. Without an email, the send node won't have a delivery address.
</Note>

## Inspect the Run

Open your journey and click the **Logs** tab. You should see the run you just triggered. Click it to open the detail view.

The run detail overlays execution status on the journey canvas. You can see that the trigger node started the run and the send node delivered (or attempted to deliver) the email. Click the send node to inspect the payload and delivery status.

See [Run Inspection](/platform/journeys/run-inspection) for a full guide on debugging runs.

## What's Next

<CardGroup cols={2}>
  <Card title="Build an Onboarding Journey" href="/tutorials/journeys/how-to-build-a-multi-step-onboarding-journey" icon="sitemap">
    Multi-step journey with delays, branching, and data enrichment
  </Card>

  <Card title="Starting a Journey" href="/platform/journeys/invocation" icon="bolt">
    Full reference for API and Segment triggers
  </Card>

  <Card title="Building Your Journey" href="/platform/journeys/building-journeys" icon="arrow-progress">
    Reference for all node types: branch, delay, fetch, throttle
  </Card>

  <Card title="Channels & Send" href="/platform/journeys/channels" icon="paper-plane">
    Configure recipients, conditions, and send windows
  </Card>
</CardGroup>
