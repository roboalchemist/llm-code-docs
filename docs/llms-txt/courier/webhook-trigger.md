# Source: https://www.courier.com/docs/platform/automations/webhook-trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhook Trigger

> Use Webhook Triggers to launch Automations from external systems. Pass JSON payloads, access event/user data, and trigger templates or workflows directly—ideal for real-time integrations with full context.

<Note>
  Webhook triggers require an Enterprise plan. Contact [Courier Support](mailto:support@courier.com) to enable this feature.
</Note>

## Register an Inbound Webhook

1. Go to Settings > Inbound Webhooks and click the "Add Inbound Webhook" button.
2. You will be prompted to enter a name and description for the webhook.

After you save the webhook, you will be presented with a unique URL that you can use to send events to Courier. When you set up the webhook trigger in Automations, you will see a list of all of your registered inbound webhooks by the name. The events are tied to the name you select, and you cannot change the name after you save the webhook.

### Configure the Webhook

Use the webhook URL that was generated in the previous step to configure the webhook in your system. Exercise a normal workflow to trigger various events to Courier, which will enable them as configuration options in the Automation trigger.

### Inbound Webhook Payload

Courier accepts any payload up to 6Mb in size.

If the payload is a JSON object, Courier will parse the payload and make the data available to you in the Automation. If the payload is not a JSON object, Courier will make the entire payload available to you in the Automation as a raw string.

If the JSON object is an array, Courier will parse each object in the array and trigger an automation for each incoming event.

For JSON objects, Courier will extract the following fields if they are present.

* `event` - The name of the event that triggered the webhook. You can filter by the name when you set up the webhook trigger in Automations. If no string field named event is present, Courier will use "Custom" as the default name.
* `userId` - A user identifier attached to the event. Courier will use this value to identify the user in the Automation, and automatically load associated profile data into the automation context.
* `properties.courier.automation` - A JSON object containing one of the following fields:
  * `template` - The id of an existing automation template to invoke, instead of using a configured webhook trigger.
  * `steps` - A JSON object containing the steps for an ad-hoc automation to execute.

If your webhook payload uses different field names for the event name or user ID, contact [Courier Support](mailto:support@courier.com) to configure the field mapping.

## Using the Webhook trigger in an Automation

1. Go to Automations and create a new automation
2. Drag and drop "Webhook" from the list of triggers.
3. In the Source field, select your registered inbound webhook name.
4. After you select the webhook, you can select the event name from a list of any received events, or Custom if your payload did not contain named events.

The data payload in the webhook will be available to you in the Automation in the normal data object, accessed with `refs.data`.

If you don't see any options in the Event field, make sure you have sent at least one event to the webhook from the source system.

## Related Resources

<CardGroup cols={2}>
  <Card title="Automation Designer" href="/platform/automations/designer" icon="pen-ruler">
    Build workflows visually
  </Card>

  <Card title="Inbound Events" href="/platform/automations/inbound-events" icon="arrow-right-to-bracket">
    Trigger automations from CourierJS, Segment, or Rudderstack
  </Card>
</CardGroup>
