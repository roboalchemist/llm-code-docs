# Source: https://smartcar.com/docs/getting-started/how-to/detect-charging-session.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Detect and Process Charging Sessions with Webhooks

> Learn how to use Smartcar webhooks to detect when a vehicle starts and ends charging, and how to process charging session data.

Smartcar webhooks make it easy to detect and process vehicle charging sessions in real time. This guide explains how to configure your webhook, handle charging events, and process charging session data in your backend.

<Steps>
  <Step title="Configure Your Webhook for Charging Events">
    In the [Smartcar Dashboard](https://dashboard.smartcar.com/integrations), create or edit a webhook integration. Under <b>Triggers</b>, select the following events:

    <ul>
      <li>Charge.IsCharging</li>
      <li>Charge.IsChargingCableConnected</li>
    </ul>

    These signals will act as triggers for detecting when a vehicle starts and stops charging and when it is plugged in or unplugged. Whenever these signals change, Smartcar will send a webhook event to your configured endpoint.
    Next, you'll configure your **data**. This is the information you want to receive in your webhook payload every time you receive a webhook event. Triggers are included by default, but you can also add additional signals to the data payload, such as:

    <ul>
      <li>Charge.StateOfCharge (included as a trigger)</li>
      <li>Charge.ChargingCurrent (included as a trigger)</li>
      <li>Charge.ActiveLimit</li>
      <li>Charge.Amperage</li>
      <li>Charge.Voltage</li>
      <li>Charge.Wattage</li>
      <li>Charge.EnergyAdded</li>
      <li>Charge.TimeToComplete</li>
      <li>TractionBattery.Range</li>
      <li>TractionBattery.NominalCapacity</li>
      <li>Location.PreciseLocation</li>
    </ul>

    These data signals will be delivered for every webhook event, allowing you to track the state of charge and other relevant metrics while the vehicle is charging.
    Next, provide your webhook URL where Smartcar will send the events. Make sure your endpoint is publicly accessible and can handle POST requests. You can choose to auto enroll all your vehicles to this webhook or manually subscribe vehicles later (you can do this from the Dashboard). For this guide, select "don't subscribe any vehicles".
    Now it is time to save and verify your webhook.
  </Step>

  <Step title="Validate Webhook Events">
    Smartcar will send a verification request to your endpoint, which you must respond to with a 200 OK status code to complete the setup (see [Webhook Verification guide](/integrations/webhooks/callback-verification)).
    Once verified, you will start to receive vehicle data for the vehicles you have subscribed to this webhook. For this guide, we chose not to auto subscribe vehicles, so let's head over to the [Smartcar Dashboard](https://dashboard.smartcar.com/vehicles) to manually subscribe a vehicle to your webhook.
    Select a vehicle from your list of connected vehicles and click on the three dots action menu to the right of the row and click subscribe. Select your newly created webhook from the options and click subscribe.

    <Frame type="simple" caption="Subscribe a vehicle to a webhook in the Smartcar Dashboard">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=5bd20bb10e660b3297ef2de1dbf4c022" alt="Smartcar Dashboard showing how to subscribe a vehicle to a webhook." data-og-width="3298" width="3298" data-og-height="2048" height="2048" data-path="images/how-to/subscribe-vehicles-from-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=051e639fdee31c606c0980f8f304b8ff 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f4cbba0bde2464efdc3cf1c78ad78bdf 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=782a6977e48b8e3ba1c8e40cd7cc5433 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=953979e3045a081ab1b20c6f792e0b14 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=aa7e740e2f42c98206dd735f89a48286 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=7655f451c559dd4ca247423a4f9884d4 2500w" />
    </Frame>
  </Step>
</Steps>

At this point, your webhook is fully configured to receive charging events from the subscribed vehicle. Now let's handle the incoming webhook events in your backend.

Every webhook will include an `eventId` and an `eventType` field. The `eventType` will indicate the type of event that occurred, such as `VEHICLE_STATE` or `VEHICLE_ERROR`.
Your handler should gracefully handle both event types. For `VEHICLE_STATE` events, you will receive the updated vehicle data. For `VEHICLE_ERROR` events, you may want to log the error.
For `VEHICLE_STATE` events, you will receive the data in a `data` property of the payload. There will also be an array of signals under a `triggers` property that caused the event to be sent. Lastly, you will also receive a `meta` property with additional context about the event, such as the webhook ID, name, delivery ID, delivery timestamp, etc.

### How to track charging sessions

When a vehicle starts charging, you will receive a webhook event with the `eventType` of `VEHICLE_STATE` and the `Charge.IsCharging` signal set to `true`. When the vehicle stops charging, you will receive another event with `Charge.IsCharging` set to `false`. You can use these events to track the start and end of each charging session.

Example event payload:

```json  theme={null}
{
  "eventId": "a7738a15-7ee2-40b3-9815-823d146230cd",
  "eventType": "VEHICLE_STATE",
  "data": {
    "user": {
      "id": "deee49b6-d638-4be4-82dc-121ea613eed9"
    },
    "vehicle": {
      "id": "829e30ab-5a13-40b5-9f8a-8538af86ed95",
      "make": "Tesla",
      "model": "Model 3",
      "year": 2020
    },
    "signals": [
      {
        "code": "charge-ischarging",
        "name": "IsCharging",
        "group": "Charge",
        "body": {
          "value": true
        },
        "status": {
          "value": "SUCCESS"
        },
        "meta": {
          "oemUpdatedAt": 1754365413366,
          "retrievedAt": 1754365413366
        }
      }
    ],
    "triggers": [
      {
        "type": "SIGNAL_UPDATED",
        "signal": {
          "code": "charge-ischarging",
          "name": "IsCharging",
          "group": "Charge"
        }
      }
    ],
    "meta": {
      "webhookId": "f1c2d3e4-5678-90ab-cdef-1234567890ab",
      "webhookName": "My Charging Webhook",
      "deliveryId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
      "deliveryTimestamp": "2024-08-04T17:00:00Z",
      "mode": "LIVE",
      "signalCount": 1
    }
  }
}
```

Tip: Always validate the webhook signature to ensure the request is from Smartcar.

***

## What’s Next

* [How to Configure Permissions](/getting-started/how-to/configure-permissions)
* [How to Manage API Tokens](/getting-started/how-to/manage-api-tokens)
* [API Reference: Webhooks](/api-reference/webhooks/subscribe-webhook)
