# Source: https://smartcar.com/docs/api-reference/management-api-intro.md

# Management API Overview

> The Management API allows you to manage vehicle connections and webhook subscriptions at the application level. It is designed for administrative tasks that go beyond individual vehicle data access.

## What You Can Do

* List all vehicles connected to your application
* Remove (disconnect) vehicles from your app
* Manage webhook subscriptions (subscribe/unsubscribe vehicles)

## Authentication

The Management API uses a management token, which you can generate in your [Smartcar Dashboard](https://dashboard.smartcar.com/).

## Base URL

```
https://api.smartcar.com/management/v2.0
```

## Key Resources

* [Get Vehicle Connections](/api-reference/management/get-vehicle-connections)
* [Delete Vehicle Connections](/api-reference/management/delete-vehicle-connections)
* [Webhook Management](/api-reference/webhooks/unsubscribe-webhook)

## Example Use Cases

* Removing vehicles when a user deletes their account
* Managing webhook event delivery
* Auditing connected vehicles for compliance

<Info>
  For more details on using the Management API, see [Management API Reference](/api-reference/management/get-vehicle-connections).
</Info>
