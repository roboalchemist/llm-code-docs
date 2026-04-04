# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/order-updates/tracking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Order Tracking

> How to retrieve tracking information for your orders

Once an order has been placed with a retailer, tracking information becomes available as shipments are dispatched. Tracking numbers are automatically extracted from retailer shipping notifications and associated with your order.

## How Tracking Works

1. Your order is successfully placed with the retailer
2. The retailer ships the item and sends a shipping notification
3. We automatically extract tracking numbers from the notification
4. Tracking information appears in the order response

<Info>
  Tracking numbers are added to orders automatically. There is no separate endpoint to create or manage tracking numbers.
</Info>

## Tracking in Order Response

Tracking information is returned as part of the order response when you retrieve an order:

```json  theme={null}
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "tracking_numbers": [
    {
      "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "carrier": "ups",
      "tracking_number": "1Z999AA10123456784",
      "created_at": "2026-01-15T14:30:00Z"
    }
  ],
  ...
}
```

### Tracking Number Fields

| Field             | Type              | Description                                     |
| ----------------- | ----------------- | ----------------------------------------------- |
| `id`              | string (UUID)     | Unique identifier for the tracking record       |
| `carrier`         | string            | Shipping carrier (see supported carriers below) |
| `tracking_number` | string            | The carrier's tracking number                   |
| `created_at`      | string (ISO 8601) | When the tracking number was extracted          |

## Supported Carriers

The following carriers are automatically detected:

| Carrier          | `carrier` value | Example Format           |
| ---------------- | --------------- | ------------------------ |
| UPS              | `ups`           | `1Z999AA10123456784`     |
| FedEx            | `fedex`         | `123456789012`           |
| USPS             | `usps`          | `9400111899223033005001` |
| Amazon Logistics | `amazon`        | `TBA123456789000`        |
| DHL              | `dhl`           | `1234567890`             |

## Multiple Tracking Numbers

An order may have multiple tracking numbers if:

* Items ship separately from the retailer
* Multiple products in the order ship from different fulfillment centers

```json  theme={null}
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "tracking_numbers": [
    {
      "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "carrier": "ups",
      "tracking_number": "1Z999AA10123456784",
      "created_at": "2026-01-15T14:30:00Z"
    },
    {
      "id": "8d0f7780-8536-51ef-055c-f18fd2g01bf8",
      "carrier": "amazon",
      "tracking_number": "TBA123456789000",
      "created_at": "2026-01-16T09:15:00Z"
    }
  ]
}
```

## Tracking Links

You can construct tracking URLs for each carrier:

| Carrier | Tracking URL                                                                    |
| ------- | ------------------------------------------------------------------------------- |
| UPS     | `https://www.ups.com/track?tracknum={tracking_number}`                          |
| FedEx   | `https://www.fedex.com/fedextrack/?trknbr={tracking_number}`                    |
| USPS    | `https://tools.usps.com/go/TrackConfirmAction?tLabels={tracking_number}`        |
| Amazon  | `https://www.amazon.com/progress-tracker/package/?trackingId={tracking_number}` |
| DHL     | `https://www.dhl.com/us-en/home/tracking.html?tracking-id={tracking_number}`    |

## When Tracking Is Available

Tracking numbers appear after the order status changes to `order_placed` and the retailer has shipped the item. The timing depends on:

* Retailer processing time
* Shipping method selected
* Product availability

<Warning>
  Tracking numbers may not be available immediately after an order is placed. Check the order periodically to retrieve tracking information once items have shipped.
  Webhook events for tracking and shipping notifications are coming soon.
</Warning>


Built with [Mintlify](https://mintlify.com).