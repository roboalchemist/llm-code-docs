# Source: https://smartcar.com/docs/integrations/webhooks/creating-webhooks.md

# Creating Webhooks

> Step-by-step guide to creating and configuring webhook integrations in the Smartcar Dashboard

Head over to the [Smartcar Dashboard](https://dashboard.smartcar.com/integrations) to set up your webhook integration. There are four main steps to create a webhook in Smartcar:

<Frame type="simple" caption="Integrations in Smartcar Dashboard">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d3af48b5bc08ad44ee8570b8687ddb8d" alt="Application Configuration in Smartcar Dashboard" data-og-width="3420" width="3420" data-og-height="2080" height="2080" data-path="images/getting-started/integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c570d45ab5e11c646ae694f07f4782e 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4385dc02cfe9a0f737a08afa6cb1a248 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c0d60e6c8328c7c511070c8491eab7e 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=95eecd2c084428179e4acfae1040f730 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1e5d939db4bba88fa2af6c391bf3729a 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3b99e85bc4f6c2b4b1159c28d2a7779b 2500w" />
</Frame>

<Steps>
  <Step title="Select an Integration Type">
    From the integrations page, start by creating a new integration and choosing webhook. For most use cases, webhooks are the recommended option.
  </Step>

  <Step title="Choose a Trigger">
    Define **when** Smartcar should send you a webhook. This is the vehicle event or condition that causes data to be delivered.

    **Example triggers:**

    * Vehicle's battery percentage changes
    * Vehicle is plugged in or unplugged
    * Odometer changes
    * Doors or windows open
    * Vehicle location changes
  </Step>

  <Step title="Select the Data (Signals)">
    After choosing a trigger, specify **what** vehicle data ("signals") should be included in the webhook payload. Browse the complete [Vehicle Signals catalog](/api-reference/signals/schema) to see all available data points.

    <Note>
      **All selected signals are delivered in every webhook event**, not just the signals that triggered it. This ensures you always receive complete vehicle state data.
    </Note>

    Your selection directly maps to the permissions that the vehicle owner granted your application during the connection process. Smartcar offers over 20 specific [permissions](https://smartcar.com/docs/api-reference/permissions) for granular control.
  </Step>

  <Step title="Provide a Callback URI & Verify Your Webhook">
    Enter the destination URL where Smartcar should send the data. This should be your application's endpoint to receive webhook payloads.

    Your callback URI must handle the `"eventType": "VERIFY"` received in the request payload and respond with a `200` status code and a `{"challenge": "{HMAC}"}` body.

    <Info>
      **Optional: Separate Error Callback URI**

      You can optionally configure a separate callback URI specifically for `VEHICLE_ERROR` events. If not specified, all events (`VEHICLE_STATE` and `VEHICLE_ERROR`) will be sent to the same callback URI.
    </Info>

    **Resources:**

    * [Callback Verification Guide](/integrations/webhooks/callback-verification) - Learn how to verify your endpoint
    * [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) - Deploy a pre-built, verified receiver
    * [Receiving Webhooks](/integrations/webhooks/receiving-webhooks) - Build your own receiver from scratch
  </Step>
</Steps>

***

## Next Steps

After creating your webhook, you'll need to subscribe vehicles to start receiving data.

<Card title="Subscribe Vehicles to Your Webhook" icon="car" href="/integrations/webhooks/subscribing-vehicles">
  Learn how to subscribe vehicles using auto-enrollment, the Dashboard, or the API
</Card>

<CardGroup cols={2}>
  <Card title="Receiving Webhooks" icon="code" href="/integrations/webhooks/receiving-webhooks">
    Learn how to handle incoming webhook deliveries
  </Card>

  <Card title="Event Reference" icon="list" href="/api-reference/webhooks/events/overview">
    Complete reference of webhook events and payloads
  </Card>

  <Card title="Verify Your Webhook" icon="shield-check" href="/integrations/webhooks/callback-verification">
    Secure your webhook endpoint with verification
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Understand retry policies and delivery guarantees
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://smartcar.com/docs/llms.txt