# Source: https://smartcar.com/docs/api-reference/vehicles-api-intro.md

# Vehicles API Overview

> The Vehicles API is Smartcar’s core API for accessing standardized vehicle data and sending remote commands to connected vehicles. It enables you to build applications that interact with a wide range of makes and models through a single, unified interface.

## What You Can Do

* Retrieve last known vehicle signals (e.g., battery level, odometer, fuel, tire pressure)
* Access vehicle attributes (make, model, year, VIN, etc.)
* Send remote commands (lock/unlock, start/stop charging, etc.)

The Vehicles API is designed primarily for exploration and non-frequent data retrieval. This API is not designed for continuous polling or real-time monitoring. Data is typically updated once every 24 hours unless the vehicle is actively subscribed to a webhook, which enables more frequent updates. For most use cases, you should avoid polling the Vehicles API at high frequency leverage [webhooks](/integrations/webhooks/overview) instead.

## Authentication

All requests require an OAuth2 access token, which is obtained by having the vehicle owner authorize your app via [Smartcar Connect](/connect/what-is-connect).

* Learn how to get an access token in our [Getting Started guide](/getting-started/how-to/get-an-access-token).
* Learn more about the [Auth Token Exchange](/api-reference/authorization/auth-code-exchange) process.

## Base URL

```
https://vehicle.api.smartcar.com/v3
```

## Key Resources

* [Signal Schema](/api-reference/signals/schema)
* [Permissions](/api-reference/permissions)
* [Error Codes](/api-reference/api-errors)

## Example Use Cases

* Fleet management and telematics
* Insurance and mileage tracking
* EV charging and energy management
* Car sharing and rental platforms

<Info>
  For a step-by-step guide to integrating with the Vehicles API, see [Getting Started](/getting-started/introduction).
</Info>
