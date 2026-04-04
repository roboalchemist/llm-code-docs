# Source: https://smartcar.com/docs/api-reference/webhooks/events/vehicle-state.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VEHICLE_STATE Event

> Signal data delivery when trigger conditions are met

Triggered when one or more signals you've configured as triggers change their value. This event delivers the updated signal data for all subscribed signals in the payload.

<Warning>
  **All Configured Signals Are Always Included**

  Every `VEHICLE_STATE` event contains **all** signals you configured in your webhook subscription, regardless of which signal(s) triggered the event. This ensures you always have complete vehicle state data.

  Example: If your webhook subscribes to 10 signals but only 1 trigger changes, you'll receive all 10 signals in the payload.
</Warning>

## When This Event Fires

The `VEHICLE_STATE` event fires when Smartcar detects a signal value change for any trigger signal configured in your webhook.

### Trigger Configuration

You configure which signals should trigger this event through the Smartcar Dashboard when creating or editing a webhook. For example:

**Triggers:**

* `TractionBattery.StateOfCharge` (code: `tractionbattery-stateofcharge`)
* `Charge.IsCharging` (code: `charge-ischarging`)
* `Location.PreciseLocation` (code: `location-preciselocation`)

**Subscribed Signals:**

* `TractionBattery.StateOfCharge`
* `Charge.IsCharging`
* `Location.PreciseLocation`
* `Charge.Voltage`
* `Odometer.TraveledDistance`

If any of the trigger signals change, a `VEHICLE_STATE` event is delivered containing **all five subscribed signals**.

***

## Identifying Which Triggers Fired

The webhook payload includes a `triggers` field that specifies which trigger signal(s) changed to prompt this delivery. This helps you identify what caused the event without comparing all signal values.

### Trigger Types

<AccordionGroup>
  <Accordion title="Signal Change Triggers" icon="arrows-rotate">
    When a monitored trigger signal changes value, the `triggers` array contains the signal(s) that changed.

    ```json  theme={null}
    {
      "triggers": [
        {
          "code": "tractionbattery-stateofcharge",
          "name": "StateOfCharge",
          "group": "TractionBattery"
        }
      ]
    }
    ```

    If multiple triggers change simultaneously, all will be included in the array.
  </Accordion>

  <Accordion title="First Delivery Trigger" icon="flag-checkered">
    When a webhook subscription is first created, a `FIRST_DELIVERY` trigger is sent to provide the initial state of the vehicle.

    ```json  theme={null}
    {
      "triggers": [
        {
          "code": "FIRST_DELIVERY"
        }
      ]
    }
    ```

    This initial delivery:

    * Occurs after vehicle subscription to a webhook
    * Contains all subscribed signals at their current values
    * Does not indicate any signal value changes
    * Helps establish baseline state for your application

    **When FIRST\_DELIVERY is sent again:**

    * When a vehicle is unsubscribed and then resubscribed to your webhook
    * If your endpoint fails to respond with a 2xx status code, Smartcar will retry delivery with the same `FIRST_DELIVERY` trigger
  </Accordion>
</AccordionGroup>

<Tip>
  Use the `triggers` field to determine the delivery reason. Check for `"code": "FIRST_DELIVERY"` to identify initial state deliveries versus change-triggered deliveries.
</Tip>

***

## Payload Structure

<ResponseField name="eventId" type="string" required>
  Unique identifier for this event. Use this for idempotency to prevent duplicate processing.
</ResponseField>

<ResponseField name="eventType" type="string" required>
  Always `"VEHICLE_STATE"` for this event type.
</ResponseField>

<ResponseField name="vehicleId" type="string" required>
  Smartcar vehicle ID for the vehicle this event relates to.
</ResponseField>

<ResponseField name="data" type="object" required>
  Container for event data.

  <Expandable title="data object">
    <ResponseField name="user" type="object" required>
      Information about the user who connected the vehicle.

      <ResponseField name="id" type="string">
        Smartcar user ID
      </ResponseField>
    </ResponseField>

    <ResponseField name="vehicle" type="object" required>
      Vehicle information

      <ResponseField name="id" type="string">
        Smartcar vehicle ID
      </ResponseField>

      <ResponseField name="make" type="string">
        Vehicle manufacturer (e.g., `"TESLA"`, `"FORD"`, `"BMW"`)
      </ResponseField>

      <ResponseField name="model" type="string">
        Vehicle model (e.g., `"Model 3"`, `"Mustang Mach-E"`)
      </ResponseField>

      <ResponseField name="year" type="integer">
        Vehicle model year
      </ResponseField>
    </ResponseField>

    <ResponseField name="triggers" type="array" required>
      Array of trigger signal objects that changed to prompt this delivery. Helps identify which configured triggers actually fired.

      <ResponseField name="code" type="string">
        Kebab-case signal identifier (e.g., `"tractionbattery-stateofcharge"`) or `"FIRST_DELIVERY"` for initial deliveries
      </ResponseField>

      <ResponseField name="name" type="string">
        Human-readable signal name (e.g., `"StateOfCharge"`)
      </ResponseField>

      <ResponseField name="group" type="string">
        Signal category (e.g., `"TractionBattery"`)
      </ResponseField>
    </ResponseField>

    <ResponseField name="signals" type="array" required>
      Array of signal objects containing data for **all** signals configured in your webhook subscription. This array always includes every subscribed signal, even if only one trigger changed to fire this event.

      <ResponseField name="code" type="string">
        Kebab-case signal identifier (e.g., `"tractionbattery-stateofcharge"`)
      </ResponseField>

      <ResponseField name="name" type="string">
        Human-readable signal name (e.g., `"StateOfCharge"`)
      </ResponseField>

      <ResponseField name="group" type="string">
        Signal category (e.g., `"TractionBattery"`, `"Charge"`, `"Location"`)
      </ResponseField>

      <ResponseField name="body" type="object">
        Signal-specific data structure. See [Signals Reference](/api-reference/signals/schema) for complete schemas.

        Each signal type has a unique body structure. Common examples:

        * Battery state of charge: `{ "unit": "percent", "value": 78 }`
        * Charging status: `{ "value": true }`
        * Location: `{ "latitude": 37.4292, "longitude": -122.1381 }`
      </ResponseField>

      <ResponseField name="meta" type="object">
        Signal metadata with timestamp information

        <ResponseField name="oemUpdatedAt" type="integer">
          Unix timestamp (milliseconds) when the vehicle manufacturer last updated this signal
        </ResponseField>

        <ResponseField name="fetchedAt" type="integer">
          Unix timestamp (milliseconds) when Smartcar retrieved this signal from the vehicle manufacturer
        </ResponseField>
      </ResponseField>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="meta" type="object" required>
  Webhook delivery metadata. See [Event Reference Overview](/api-reference/webhooks/events/overview#common-fields) for complete `meta` object schema.

  <Expandable title="meta object (VEHICLE_STATE-specific fields)">
    <ResponseField name="signalCount" type="integer">
      Number of signals included in this `VEHICLE_STATE` event. Only present for `VEHICLE_STATE` events.
    </ResponseField>
  </Expandable>
</ResponseField>

***

## Example Payloads

<Tabs>
  <Tab title="Signal Change Trigger">
    Delivered when a configured trigger signal changes value.

    ```json  theme={null}
    {
      "eventId": "550e8400-e29b-41d4-a716-446655440000",
      "eventType": "VEHICLE_STATE",
      "vehicleId": "9af13248-3b73-4c9d-9a4b-d937ce6bc8e2",
      "data": {
        "user": {
          "id": "93b3ea96-ca37-43a9-9073-f4334719iok7"
        },
        "vehicle": {
          "id": "9af13248-3b73-4c9d-9a4b-d937ce6bc8e2",
          "make": "TESLA",
          "model": "Model 3",
          "year": 2020
        },
        "triggers": [
          {
            "code": "tractionbattery-stateofcharge",
            "name": "StateOfCharge",
            "group": "TractionBattery"
          }
        ],
        "signals": [
          {
            "code": "tractionbattery-stateofcharge",
            "name": "StateOfCharge",
            "group": "TractionBattery",
            "body": {
              "unit": "percent",
              "value": 78
            },
            "meta": {
              "oemUpdatedAt": 1731940328000,
              "fetchedAt": 1731940330000
            }
          },
          {
            "code": "charge-ischarging",
            "name": "IsCharging",
            "group": "Charge",
            "body": {
              "value": true
            },
            "meta": {
              "oemUpdatedAt": 1731940328000,
              "fetchedAt": 1731940330000
            }
          },
          {
            "code": "charge-voltage",
            "name": "Voltage",
            "group": "Charge",
            "body": {
              "unit": "volts",
              "value": 240
            },
            "meta": {
              "oemUpdatedAt": 1731940328000,
              "fetchedAt": 1731940330000
            }
          }
        ]
      },
      "meta": {
        "version": "4.0",
        "deliveryId": "48b25f8f-9fea-42e1-9085-81043682cbb8",
        "deliveredAt": 1731940328000,
        "webhookId": "abde94ff-d57d-43b9-8d09-6020db2d977a",
        "webhookName": "Battery Monitoring",
        "signalCount": 3,
        "mode": "LIVE"
      }
    }
    ```
  </Tab>

  <Tab title="First Delivery">
    Delivered immediately after webhook subscription creation to provide initial vehicle state.

    ```json  theme={null}
    {
      "eventId": "7c8d9e10-f2a3-4b5c-6d7e-8f9a0b1c2d3e",
      "eventType": "VEHICLE_STATE",
      "vehicleId": "9af13248-3b73-4c9d-9a4b-d937ce6bc8e2",
      "data": {
        "user": {
          "id": "93b3ea96-ca37-43a9-9073-f4334719iok7"
        },
        "vehicle": {
          "id": "9af13248-3b73-4c9d-9a4b-d937ce6bc8e2",
          "make": "TESLA",
          "model": "Model 3",
          "year": 2020
        },
        "triggers": [
          {
            "code": "FIRST_DELIVERY"
          }
        ],
        "signals": [
          {
            "code": "tractionbattery-stateofcharge",
            "name": "StateOfCharge",
            "group": "TractionBattery",
            "body": {
              "unit": "percent",
              "value": 65
            },
            "meta": {
              "oemUpdatedAt": 1731926100000,
              "fetchedAt": 1731926102000
            }
          },
          {
            "code": "charge-ischarging",
            "name": "IsCharging",
            "group": "Charge",
            "body": {
              "value": false
            },
            "meta": {
              "oemUpdatedAt": 1731926100000,
              "fetchedAt": 1731926102000
            }
          },
          {
            "code": "charge-voltage",
            "name": "Voltage",
            "group": "Charge",
            "body": {
              "unit": "volts",
              "value": 0
            },
            "meta": {
              "oemUpdatedAt": 1731926100000,
              "fetchedAt": 1731926102000
            }
          }
        ]
      },
      "meta": {
        "version": "4.0",
        "deliveryId": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        "deliveredAt": 1731926100000,
        "webhookId": "abde94ff-d57d-43b9-8d09-6020db2d977a",
        "webhookName": "Battery Monitoring",
        "signalCount": 3,
        "mode": "LIVE"
      }
    }
    ```
  </Tab>
</Tabs>

***

## Signal Reference

The `signals` array contains data structured according to the [Signals Schema Reference](/api-reference/signals/schema). Each signal type has a specific shape:

<CardGroup cols={3}>
  <Card title="Charge Signals" href="/api-reference/signals/charge">
    Battery charging status and metrics
  </Card>

  <Card title="Battery Signals" href="/api-reference/signals/tractionbattery">
    State of charge and battery health
  </Card>

  <Card title="Location Signals" href="/api-reference/signals/location">
    GPS coordinates and location data
  </Card>

  <Card title="Odometer" href="/api-reference/signals/odometer">
    Distance traveled
  </Card>

  <Card title="Fuel Tank" href="/api-reference/get-fuel-tank">
    Fuel level for ICE vehicles
  </Card>

  <Card title="All Signals" href="/api-reference/signals/schema">
    Complete signal catalog
  </Card>
</CardGroup>

***

## Signal-Level Errors

Individual signals within a `VEHICLE_STATE` payload can contain errors if the vehicle doesn't support that signal or if retrieval fails. When this occurs, the signal will have a `status` object with error details instead of a `body` with data:

```json Signal with Error theme={null}
{
  "code": "location-isathome",
  "name": "IsAtHome",
  "group": "Location",
  "status": {
    "error": {
      "code": "VEHICLE_NOT_CAPABLE",
      "type": "COMPATIBILITY"
    },
    "value": "ERROR"
  }
}
```

<Info>
  **Partial data delivery**: When some signals succeed and others fail, you'll receive a `VEHICLE_STATE` event with successful signals containing `body` data and failed signals containing `status` errors. This allows you to process available data even when some signals are unavailable.
</Info>

For complete error handling, see the [VEHICLE\_ERROR Event](/api-reference/webhooks/events/vehicle-error) documentation.

***

## Processing VEHICLE\_STATE Events

### Basic Handler

```javascript  theme={null}
function handleVehicleState(payload) {
  const { vehicleId, data } = payload;
  const { signals, triggers } = data;
  
  // Check if this is first delivery
  const isFirstDelivery = triggers.some(t => t.code === 'FIRST_DELIVERY');
  
  // Process each signal
  signals.forEach(signal => {
    if (signal.body) {
      // Signal has data
      console.log(`${signal.name}: ${JSON.stringify(signal.body)}`);
      updateDatabase(vehicleId, signal.code, signal.body);
    } else if (signal.status) {
      // Signal has error
      console.error(`${signal.name} error: ${signal.status.error.code}`);
      handleSignalError(vehicleId, signal);
    }
  });
}
```

### Best Practices

<AccordionGroup>
  <Accordion title="Use eventId for deduplication" icon="fingerprint">
    Always check if you've already processed an `eventId` before updating your database. Retries will have the same `eventId` but different `deliveryId`.

    ```javascript  theme={null}
    async function processWebhook(payload) {
      const { eventId } = payload;
      
      // Check if already processed
      if (await isProcessed(eventId)) {
        console.log(`Already processed ${eventId}`);
        return;
      }
      
      // Process the event
      await handleVehicleState(payload);
      
      // Mark as processed
      await markProcessed(eventId);
    }
    ```
  </Accordion>

  <Accordion title="Check timestamp freshness" icon="clock">
    Use `signals[].meta.oemUpdatedAt` to determine if incoming data is newer than your stored state. Events can arrive out of order.

    ```javascript  theme={null}
    function shouldUpdate(currentData, newSignal) {
      if (!currentData) return true;
      
      return newSignal.meta.oemUpdatedAt > currentData.timestamp;
    }
    ```
  </Accordion>

  <Accordion title="Handle partial failures gracefully" icon="shield-halved">
    Some signals may succeed while others fail. Process available data and log errors for unavailable signals.

    ```javascript  theme={null}
    signals.forEach(signal => {
      if (signal.body) {
        updateVehicleData(signal);
      } else if (signal.status) {
        logSignalUnavailable(signal);
        // Don't block processing of other signals
      }
    });
    ```
  </Accordion>

  <Accordion title="Differentiate FIRST_DELIVERY from changes" icon="flag">
    Use the `triggers` field to identify initial state deliveries vs. actual signal changes.

    ```javascript  theme={null}
    const isFirstDelivery = payload.data.triggers.some(
      t => t.code === 'FIRST_DELIVERY'
    );

    if (isFirstDelivery) {
      // Initialize vehicle state
      initializeVehicle(payload.data);
    } else {
      // Update changed signals
      updateVehicleState(payload.data);
    }
    ```
  </Accordion>
</AccordionGroup>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="VEHICLE_ERROR Event" icon="triangle-exclamation" href="/api-reference/webhooks/events/vehicle-error">
    Handle error notifications
  </Card>

  <Card title="Signals Reference" icon="list" href="/api-reference/signals/schema">
    Complete signal schemas and data structures
  </Card>

  <Card title="Best Practices" icon="star" href="/integrations/webhooks/best-practices/reliability">
    Implement idempotency and ordering
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Understand retry policies
  </Card>
</CardGroup>
