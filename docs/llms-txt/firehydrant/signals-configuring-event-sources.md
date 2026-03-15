# Source: https://docs.firehydrant.com/docs/signals-configuring-event-sources.md

# Configuring Event Sources

An <Glossary>Event</Glossary> is any inbound payload to FireHydrant from your automated monitoring and alerting tools. Incoming Events create a data stream that teams can pull from to create meaningful [Alerts](/docs/signals/alerts)  for their responders. Using [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules), Teams can ensure only the Events they care about will <Glossary>Alert</Glossary> them.

Every organization in FireHydrant gets its own unique set of webhook URLs for sending data to FireHydrant. These webhooks can either be generic or provider-specific.

## Generic Webhook Data Model

FireHydrant is designed to be flexible. Any external tool that allows customization of the payload sent can be used as an <Glossary>Event Source</Glossary>. This adaptability ensures that you can integrate your existing tools seamlessly.

Below is an example of a payload matching the generic data model FireHydrant expects. If you can configure your webhook to send parameters and data in the following format, you can easily integrate with FireHydrant.

```json
{
  "summary": "CPU Utilization Spiking",
  "body": "The production server is experiencing greater than 99% utilizations of compute.",
  "level": "ERROR",
	"images": [
    {
      "src": "https://site.com/images/123.png",
      "alt": "A simple, sample image"
    }
  ],
  "links": [
    {
      "href": "https://site.com/monitors/123",
      "text": "Monitoring Source"
    }
  ],
  "annotations": {
    "policy": "escalatable"
  },
  "received_at": "2023-11-09T18:22:16.000+00:00"
}
```

For more information about each parameter, visit [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

## Transposers

When a provider does not allow customizing the payload, FireHydrant will need a Transposer to modify the incoming Event's payload into a format that the platform expects.

On your [Event Sources page](https://app.firehydrant.io/signals/sources), you can find a list of official providers for which FireHydrant has already written Transposers. If you do not see an out-of-box Event Source for your chosen monitoring or observability tool(s), you may choose to create a [Custom Event Source](https://docs.firehydrant.com/docs/custom-event-source).

Below is an example of how an Event from Honeycomb is transposed into a FireHydrant Event.

```json Honeycomb Payload
// Data format from Honeycomb
{
    "version": "v0.1.0",
    "name": "Sample Honeycomb Alert",
    "id": "",
    "trigger_description": "",
    "status": "triggered",
    "alert_type": "on_change",
    "summary": "",
    "description": "Validate Honeycomb Webhook Integration",
    "operator": "",
    "threshold": 0,
    "result_url": "https://honeycomb.io/sample/trigger",
    "result_groups": null,
    "result_groups_triggered": null,
    "trigger_url": "",
    "is_test": true
  }
```

```json FireHydrant Event
// Data format as an Event
{
    "summary": "Sample Honeycomb Alert",
    "body": "Validate Honeycomb Webhook Integration",
    "links": [
      {
        "href": "https://honeycomb.io/sample/trigger",
        "text": "Honeycomb Trigger"
      }
    ]
  }
```

## Testing Sources and Events

<Image alt="Viewing the example and testing an Event Source" align="center" width="650px" src="https://files.readme.io/1ae8f38-CleanShot_2024-04-25_at_17.09.592x.png">
  Viewing the example and testing an Event Source
</Image>

Within your [Event Sources page](https://app.firehydrant.io/signals/sources), you can expand each row to see example inbound payloads and their resulting outputs once transposed.

There is also a button to send a test event, which will generate an example payload and send that as a test. When you click the button, the new entry will show up on the [Event Logs](https://app.firehydrant.io/signals/logs) page.

<Image alt="Example Event logged from the test button" align="center" width="400px" src="https://files.readme.io/19866f2-CleanShot_2024-04-25_at_17.14.252x.png">
  Example Event logged from the test button
</Image>

## Next Steps

Now that you know about Events, learn more about [Working with Alerts](https://docs.firehydrant.com/docs/signals-working-with-alerts).