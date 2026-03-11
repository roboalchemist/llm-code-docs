# Source: https://www.courier.com/docs/platform/automations/inbound-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Inbound Event Triggers

> Courier Automations support event triggers from CourierJS, Segment, and Rudderstack. These events—like track and identify—can initiate workflows within Automations via dedicated trigger nodes.

## Courier Inbound Events

The [CourierJS SDK](https://github.com/trycourier/courier-js/tree/main/packages/courier-js) interfaces with the inbound track API to send client-side application events
to Courier that can be used in Automations trigger nodes.

You can also send events directly via the REST API:

```bash  theme={null}
curl --request POST \
  --url https://api.courier.com/inbound/courier \
  --header 'Authorization: Bearer <YOUR_API_KEY>' \
  --header 'Content-Type: application/json' \
  --data '{
  "event": "order-placed",
  "type": "track",
  "userId": "user_123",
  "properties": {
    "order_id": "ORD-98765",
    "total": 59.99
  }
}'
```

The `event` name matches the trigger node's event filter in your automation. The `properties` object is available in the automation context via `refs.data`.

## Segment

With a [Segment third-party integration](/external-integrations/cdp/segment) both [`track`](https://segment.com/docs/connections/spec/track/)
and [`identify`](https://segment.com/docs/connections/spec/identify/) are automatically ingested using the Segment trigger node in Automations.
Refer to [Segment use cases](/platform/automations/segment) for more information.

## Rudderstack

With an existing [RudderStack third-party integration](/external-integrations/cdp/rudderstack) both [`track`](https://www.rudderstack.com/docs/event-spec/standard-events/track/)
and [`identify`](https://www.rudderstack.com/docs/event-spec/standard-events/identify/) are automatically ingested into the Rudderstack trigger node in Automations.

## Related Resources

<CardGroup cols={2}>
  <Card title="Segment Use Cases" href="/platform/automations/segment" icon="chart-line">
    Trigger automations from Segment events
  </Card>

  <Card title="Webhook Trigger" href="/platform/automations/webhook-trigger" icon="globe">
    Trigger automations from external webhooks
  </Card>
</CardGroup>
