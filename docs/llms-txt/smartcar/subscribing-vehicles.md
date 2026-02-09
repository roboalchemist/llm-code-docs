# Source: https://smartcar.com/docs/integrations/webhooks/subscribing-vehicles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscribing Vehicles

> Learn how to subscribe and unsubscribe vehicles to webhooks using auto-enrollment, the Dashboard, or the API

Once you've [created a webhook](/integrations/webhooks/creating-webhooks), you need to subscribe vehicles to it before they'll start receiving data. Smartcar offers three methods to manage vehicle subscriptions: automatic enrollment, Dashboard management, and programmatic API control.

<Info>
  Data will only be sent after your webhook has been verified. See [Callback Verification](/integrations/webhooks/callback-verification) for details.
</Info>

***

## Subscription Methods

<CardGroup cols={3}>
  <Card title="Auto-Enrollment" icon="wand-magic-sparkles" href="/integrations/webhooks/subscribing-vehicles#method-1%3A-auto-enrollment-recommended">
    Automatic subscription for all connected vehicles
  </Card>

  <Card title="Dashboard" icon="browser" href="/integrations/webhooks/subscribing-vehicles#method-2%3A-dashboard-management">
    Manual subscription through the Smartcar Dashboard
  </Card>

  <Card title="API" icon="code" href="/integrations/webhooks/subscribing-vehicles#method-3%3A-api-subscription">
    Programmatic subscription via REST API
  </Card>
</CardGroup>

***

## Method 1: Auto-Enrollment (Recommended for Production)

The simplest way to manage subscriptions is to enable auto-enrollment when creating your webhook. This automatically subscribes all vehicles connected to your application.

<Warning>
  **All vehicles will be subscribed immediately.** When you enable auto-enrollment, all currently connected vehicles will be subscribed to the webhook right away. Only enable this feature when you're ready to receive data for all vehicles in your application.
</Warning>

### How It Works

When auto-enrollment is enabled:

* **Existing vehicles** are immediately subscribed to the webhook
* **New connections** are automatically subscribed when users connect vehicles
* **No manual management** required for individual vehicles

### Enable Auto-Enrollment

<Steps>
  <Step title="Navigate to Dashboard">
    Go to the [Smartcar Dashboard](https://dashboard.smartcar.com/integrations) and create or edit a webhook
  </Step>

  <Step title="Enable Auto-Subscribe">
    Check the "Automatically subscribe all vehicles" option during webhook creation
  </Step>

  <Step title="Save Configuration">
    Complete webhook creation - all vehicles will be subscribed automatically
  </Step>
</Steps>

<Check>
  **Best for:** Production deployments where all connected vehicles should receive webhook data
</Check>

***

## Method 2: Dashboard Management

For selective subscription, you can manually subscribe individual vehicles through the Dashboard.

### Subscribe via Dashboard

<Steps>
  <Step title="Access Vehicle List">
    Navigate to [Vehicles](https://dashboard.smartcar.com/vehicles) in the Dashboard
  </Step>

  <Step title="Select Vehicle">
    Click on the vehicle you want to subscribe
  </Step>

  <Step title="Manage Subscriptions">
    In the vehicle details, find the "Webhook Subscriptions" section

    <Frame type="simple" caption="Webhook Subscription in Smartcar Dashboard">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0df1e27487ad5b8116a99e2dd3f80b5c" alt="Webhook Subscription in Smartcar Dashboard" data-og-width="3972" width="3972" data-og-height="1932" height="1932" data-path="images/getting-started/dashboard/subscribe-from-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c7ebca922726f37bef95869e227f2c3a 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5a4ff5c39f80690cd8f50f23ab53117b 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dac53494978cba5d47ed149813c952f9 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5e7d7cd58f719877acb1e8778e02a48a 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=fcdf42ce2444e6d8afcdd5223bb93488 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6687ae24a2eda0e30025de3dcc867301 2500w" />
    </Frame>
  </Step>

  <Step title="Add or Remove">
    Click "Subscribe" to add the vehicle to a webhook, or "Unsubscribe" to remove it
  </Step>
</Steps>

<Check>
  **Best for:** Testing and development, selective vehicle management, or gradual rollouts
</Check>

***

## Method 3: API Subscription

For programmatic control, use the subscribe and unsubscribe API endpoints.

* [Subscribe Endpoint](/api-reference/webhooks/subscribe-webhook) - Full API reference for subscribing vehicles
* [Unsubscribe Endpoint](/api-reference/webhooks/unsubscribe-webhook) - Full API reference for unsubscribing vehicles

<Check>
  **Best for:** Testing and development, dynamic subscription management, custom business logic, or bulk operations
  **Best for:** Dynamic subscription management, custom business logic, or bulk operations
</Check>

***

## Common Questions

<AccordionGroup>
  <Accordion title="Can I use multiple subscription methods together?">
    Yes! You can enable auto-enrollment for most vehicles and use the API or Dashboard for exceptions. However, be aware that auto-enrollment will automatically subscribe new vehicles.
  </Accordion>

  <Accordion title="What happens if I unsubscribe a vehicle?">
    The vehicle immediately stops receiving webhook deliveries. You can re-subscribe at any time, and a new first payload will be sent.
  </Accordion>

  <Accordion title="How do I know which vehicles are subscribed?">
    You can view all vehicle subscriptions in the [Dashboard](https://dashboard.smartcar.com/vehicles) or use the [Management API](/api-reference/management/get-vehicle-connections) to programmatically list subscriptions.
  </Accordion>

  <Accordion title="Is there a limit to how many vehicles I can subscribe?">
    No, you can subscribe as many vehicles as are connected to your application. Webhooks scale automatically to handle your fleet size.
  </Accordion>

  <Accordion title="Do I need different webhooks for different vehicle types?">
    Not necessarily. You can use one webhook for all vehicles and handle signal availability differences using the `VEHICLE_ERROR` events for unsupported signals.
  </Accordion>
</AccordionGroup>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Receiving Webhooks" icon="code" href="/integrations/webhooks/receiving-webhooks">
    Requirements for building your webhook endpoint
  </Card>

  <Card title="Event Reference" icon="list" href="/api-reference/webhooks/events/overview">
    Understand all types of available payloads
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Learn about retry policies and guarantees
  </Card>

  <Card title="Callback URI Verification" icon="shield-check" href="/integrations/webhooks/callback-verification">
    Ensure your endpoint passes Smartcar's verification challenge
  </Card>
</CardGroup>
