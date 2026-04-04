# Source: https://smartcar.com/docs/integrations/webhooks/responses.md

# Webhook Response Payloads

> Receive a seamless data stream from your vehicles via webhooks with optimized vehicle updates, ensuring you always have the most current information available for all of your vehicles.

## Vehicle State

When a vehicle is first subscribed to a webhook, Smartcar will send an initial payload that attempts to get all the signals you're subscribed to for that vehicle with a `VEHICLE_STATE` type. Subsequent events will contain a payload with the same event type but only the relevant signals based on your webhook configuration. (i.e, when a signal changes, on a schedule, etc.)

Vehicle state payloads will contain the following object types for the `triggers` array:

* `SIGNAL_UPDATED`: indicates that a signal value has changed since the last payload was sent. The `signal` object will contain the `code` of the signal that was updated.
* `FIRST_DELIVERY`: indicates that this is the first payload sent for this vehicle. This trigger will only be present in the initial payload sent when a vehicle is first subscribed to a webhook, unsubscribed and then resubscribed to your webhook, or if your application is not responding with a 200 status code, we will attempt to deliver this webhook again.

If you request a signal as part of your webhook payload data that the vehicle is not capable of, Smartcar will still include it in the `VEHICLE_STATE` payload, but the signal will contain an error object instead of data as shown in the example below.

```json  theme={null}
{
    "eventId": "5a537912-9ad3-424b-ba33-65a1704567e9",
    "eventType": "VEHICLE_STATE",
    "data": {
        "user": {
            "id": "93b3ea96-ca37-43a9-9073-f4334712dbc7"
        },
        "vehicle": {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "make": "Test Make",
            "model": "Test Model",
            "year": 2020
        },
        "signals": [
            {
                "code": "location-preciselocation",
                "name": "PreciseLocation",
                "group": "Location",
                "body": {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
                "status": {
                  "value": "SUCCESS"
                },
                "meta": {
                  "retrievedAt": 1758668712404,
                  "oemUpdatedAt": 1758668712404
                }
            },
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
            },
            {
                "code": "tractionbattery-stateofcharge",
                "name": "StateOfCharge",
                "group": "TractionBattery",
                "body": {
                    "unit": "percent",
                    "value": 75
                },
                "status": {
                  "value": "SUCCESS"
                },
                "meta": {
                  "retrievedAt": 1758668712404,
                  "oemUpdatedAt": 1758668712404
                }
            }
        ]
    },
    "triggers": [
        {
            "type": "SIGNAL_UPDATED",
            "signal": {
                "name": "StateOfCharge",
                "group": "TractionBattery",
                "code": "tractionbattery-stateofcharge"
            }
        }
    ],
    "meta": {
        "version": "4.0",
        "deliveryId": "48b25f8f-9fea-42e1-9085-81043682cbb8",
        "deliveredAt": 1761896351529,
        "webhookId": "123e4567-e89b-12d3-a456-426614174000",
        "webhookName": "My First Webhook",
        "signalCount": 3,
        "mode": "LIVE"
    }
}
```

For each signal, you will have a `meta` object that contains the following fields:

* `retrievedAt`: The timestamp (in milliseconds since epoch) of when the data was retrieved from the vehicle by Smartcar.
* `oemUpdatedAt`: The timestamp (in milliseconds since epoch) of when the data was last recorder by the vehicle.

You'll also see a `code` with the unique signal code that can be used to retrieve that signal from the API by calling the [`GET` Signal endpoint](/api-reference/get-signal).
The `name` and `group` fields correspond to the signal's name and group respectively as defined in the [Signal Schema](/api-reference/signals/schema).

## Vehicle connection or compatibility issues

There may be times when Smartcar is unable to get vehicle data because there is
an issue with our connection to the vehicle that requires vehicle owner
interaction, or because the subscribed vehicle does not support some of the signals you have configured.

Smartcar will allow you to subscribe any vehicle to your webhook. When processing
the initial payload, we will report compatibility issues to your error callback
URI. For example, if a vehicle is not capable of the `nickname` signal we would
send data for other signals as normal, but send the following payload for the `nickname` signal instead.

When either of these happens, we'll send a `VEHICLE_ERROR` payload to your vehicle error callback URI. If you don't specify a callback URI for errors, Smartcar will send them to the same vehicle data callback URI.

For a list of possible errors, please refer to the [API Errors](/errors/api-errors) section.

```json  theme={null}
{
    "eventId": "5a537912-9ad3-424b-ba33-65a1704567e9",
    "eventType": "VEHICLE_ERROR",
    "data": {
        "user": {
            "id": "93b3ea96-ca37-43a9-9073-f4334719iok7"
        },
        "errors": [
            {
                "type": "COMPATIBILITY",
                "code": "VEHICLE_NOT_CAPABLE",
                "state": "ERROR",
                "description": "The vehicle is incapable of performing your request.",
                "suggestedUserMessage": "Your car is unable to perform this request.",
                "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#vehicle-not-capable",
                "resolution": {
                    "type": "CONTACT_SUPPORT"
                },
                "signals": [
                  {
                    "code": "location-preciselocation",
                    "name": "PreciseLocation",
                    "group": "Location"
                  },
                  {
                    "code": "tractionbattery-stateofcharge",
                    "name": "StateOfCharge",
                    "group": "TractionBattery"
                  }
                ]
            }
        ],
        "vehicle": {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "make": "TESLA",
            "model": "Model 3",
            "year": 2020
        }
    },
    "meta": {
        "version": "4.0",
        "deliveryId": "48b25f8f-9fea-42e1-9085-81043682cbb8",
        "deliveredAt": 1761896351529,
        "webhookId": "123e4567-e89b-12d3-a456-426614174000",
        "webhookName": "Bad Webhook",
        "mode": "LIVE"
    }
}
```

While a vehicle is in one of these states, you may be unable to receive data from the
vehicle until the owner has taken the necessary steps to re-establish
the connection.

Upon resolution of the issue, Smartcar will send another payload to your error callback URI with `state`
set to `RESOLVED`. If you don't specify a callback URI for errors, Smartcar will send them to the same vehicle data callback URI.
