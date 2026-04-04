# Squarespace Developer Documentation
Source: https://developers.squarespace.com/webhooks/overview

Overview — Squarespace Developers

-

[Home](/)

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

[Custom Code](/custom-code/about)

[Upcoming Changes](/changes/upcoming-changes)

[Get Started](/quick-start)

## Using Webhooks

[Overview](/webhooks/overview)

[Verifying notifications](/webhooks/verifying-notifications)

[Notification delivery](/webhooks/notification-delivery)

## Commerce Order Events

[Order create](/webhooks/events/order-create)

[Order update](/webhooks/events/order-update)

## Extension Events

[Extension uninstall](/webhooks/events/extension-uninstall)

## Webhooks overview

Instead of making repeated API calls, a client may subscribe to notifications from Squarespace for supported system events.

To receive notifications from Squarespace for a merchant site,

create a webhook subscription using the [Webhook Subscriptions API](/commerce-apis/webhook-subscriptions-overview).

You can use the [send test notification](/commerce-apis/send-test-notification) endpoint to test your subscriptions.

## When will a subscription expire?

Subscriptions never expire.

## Which events can I subscribe to?

See "Event notifications" below for a full list.

## How can I verify a notification is from Squarespace?

Every Squarespace notification includes a `Squarespace-Signature` header.

To verify this header, you must have access to the `secret` from a returned `Webhook Subscription`.

`secret` is only returned when [creating a subscription](/commerce-apis/create-webhook-subscription) or when [rotating a secret](/commerce-apis/rotate-subscription-secret).

Read the [Verifying notifications](/webhooks/verifying-notifications) guide for further details about verifying notifications.

## Structure of a Squarespace notification

Squarespace webhook notifications are sent as a request to a subscribed webhook endpoint.

The request always contains headers, including a signature, and a JSON payload.

*Note: Squarespace reserves the right to add properties and fields without a version change. Version changes are reserved for breaking changes only.*

### Headers

- `User-Agent`: "Squarespace/1.0"
- `Content-Type`: "application/json"
- `Squarespace-Signature`: "<an HMAC-SHA256 signature>"

### Payload

```json
{
  // String; unique notification id
  "id": "5c2ba184b63ed3cb411ce2b1",
  // String; Squarespace website id that triggered the notification.
  "websiteId": "5f3c3d55ac435e1a051f77b3",
  // String; unique Webhook Subscription id
  "subscriptionId": "5f3c2155d947844beedda991",
  // String; description of the event that triggered the notification.
  "topic": "extension.uninstall",
  // ISO 8601 UTC date and time string; represents when the notification was created.
  "createdOn": "2020-04-22T22:18+00:00",
  // Object; data associated with the event.
  "data": {...}
}
```

## Event notifications

Below is a list of events that trigger notifications.

Read the [Notification delivery](/webhooks/notification-delivery) guide to learn about the notification lifecycle.

### Extension events

[Extension uninstall](/webhooks/events/extension-uninstall)

### Commerce order events

Commerce order notifications require OAuth access permissions for the Commerce Orders API.

See the Commerce [Authentication and permissions](/commerce-apis/authentication-and-permissions) guide for details.

- [Order create](/webhooks/events/order-create)

- [Order update](/webhooks/events/order-update)

## Squarespace

[Main Site](https://www.squarespace.com)

[Careers](https://www.squarespace.com/about/careers)

## Developers

[Home](/)

[Developer Terms of Use](https://www.squarespace.com/developer-terms)

[Privacy Policy](https://www.squarespace.com/privacy)

[Security Measures](https://www.squarespace.com/measures)

## Documentation

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

## Community

[Circle](https://circle.squarespace.com)

[Specialists](https://specialists.squarespace.com)

[Forum](https://forum.squarespace.com)

## Follow

[Engineering Blog](https://engineering.squarespace.com)

[Github](https://github.com/squarespace)

[NPM](https://www.npmjs.com/org/squarespace)