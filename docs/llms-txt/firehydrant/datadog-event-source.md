# Source: https://docs.firehydrant.com/docs/datadog-event-source.md

# Datadog Event Source

The Datadog Integration for Signals allows users to create events in FireHydrant from monitors in Datadog. Anytime Datadog sends an event to FireHydrant, we’ll evaluate the event payload to see if it matches a rule one of your teams set up. If a rule matches, we’ll alert the team. Learn more about [Alert Rules](https://docs.firehydrant.com/docs/alert-rules) here.

## Configuring Datadog Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL you will use when creating a webhook in Datadog.

<Image alt="Copy the Datadog URL" align="center" width="800px" src="https://files.readme.io/59f4121-datadog-webhook.jpg">
  Copy the Datadog URL
</Image>

2. In Datadog, visit the Integrations Page and navigate to the Webhooks Integration. If you haven’t installed it, go ahead and install it.

<Image alt="Add the webhook in Datadog" align="center" width="650px" src="https://files.readme.io/fd5a953-signals-datadog-webhook.png">
  Add the webhook in Datadog
</Image>

3. In the left-hand column of Webhooks, click the “+ New” button to add a new webhook. In the `Name` field, enter a name that you will later use to reference the webhook when setting up notifications for your monitor. In the `URL` field, paste in the webhook from FireHydrant that we covered in Step 1.
4. In the Payload field, we recommend using the following format:

```json
{
    "summary": "$EVENT_TITLE",
    "body": "$EVENT_MSG",
    "unique_key": "$ALERT_ID",
    "level": "$ALERT_TYPE",
    "status": "$ALERT_TRANSITION",
    "links": [{"href": "$LINK", "text": "Datadog Monitor"}],
    "images": [{"src": "$SNAPSHOT", "alt": "Snapshot from $EVENT_TITLE"}],
    "tags": "$TAGS",
    "annotations": {
      "datadog/priority": "$PRIORITY"
      ...(any other annotations/data you want from Datadog here)
    }
}
```

(See “Fields in a Signals” for more details on how you can customize this payload in combination with [Datadog’s built-in variables](https://docs.Datadoghq.com/integrations/webhooks/#usage)).

Click Save to add your new webhook.

## Using Webhook as Notification Target

1. Visit any monitor where you’d like to send alerts to FireHydrant as Signals and click Edit.

2. For Monitors, scroll to step 3, “Notify your team” and type `@` followed by the name of your webhook in the notification message. This should bring up a list of possible notification targets. Click on your new webhook.

   If you’re working with a synthetic monitor, you will add the webhook in Step 6, “Configure the monitor for this test.”

3. Click “Save” at the bottom of your page.

## Create a test Signal from Datadog

1. For Monitors, you can send a test alert when editing the monitor. Visit the monitor you’d like to test and click Edit in the menu in the top right corner.

2. At the bottom of the page, click “Test Notifications.” In the ensuing modal, select any alert level you’d like and click “Run Test.”

<Image alt="Send a test alert from Datadog" align="center" width="650px" src="https://files.readme.io/9353e1a-signals-datadog-test.png">
  Send a test alert from Datadog
</Image>

3. Visit the Signal Logs in your FireHydrant app to see if a Signal was successfully created.

<Image alt="A log of successful Signals" align="center" width="800px" src="https://files.readme.io/cb9a5ef-logs.jpg">
  A log of successful Signals
</Image>

<br />

## Field Mappings/Behaviors

The payload above directly maps to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model). The following table explains the behavior once the payload hits our system:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Inbound Parameter
      </th>

      <th>
        FireHydrant Parameter
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `payload.unique_key`
      </td>

      <td>
        `idempotency_key`
      </td>
    </tr>

    <tr>
      <td>
        `payload.summary`\
        *-OR-*\
        "Alert from Datadog"
      </td>

      <td>
        `summary` - FireHydrant will check for a `summary` parameter in the payload, otherwise it will generically say "Alert from Datadog"
      </td>
    </tr>

    <tr>
      <td>
        `payload.body`\
        *-OR-*\
        "No information provided"
      </td>

      <td>
        `body` - FireHydrant will check for a `body` parameter in the payload, otherwise it will generically say "No information provided"
      </td>
    </tr>

    <tr>
      <td>
        `payload.level`
      </td>

      <td>
        `level` - `error` on Datadog maps to `ERROR` on FireHydrant, `warning` maps to `WARN` on FireHydrant, and `success` and all other levels from Datadog map to `INFO` on FireHydrant
      </td>
    </tr>

    <tr>
      <td>
        `payload.links`
      </td>

      <td>
        `links` - Directly maps links from the payload to the array of link objects in FireHydrant
      </td>
    </tr>

    <tr>
      <td>
        `payload.images`
      </td>

      <td>
        `images` - Directly maps images from the payload to the array of image objects in FireHydrant
      </td>
    </tr>

    <tr>
      <td>
        `payload.tags`
      </td>

      <td>
        `tags` - Maps a comma-delimited string of tags to an array of tags in FireHydrant
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        `status` - Closed on FireHydrant if `status` is "Recovered", otherwise Open
      </td>
    </tr>
  </tbody>
</Table>

These mappings mean that an inbound webhook from Datadog with the following content:

```json Datadog Payload
{
  "unique_key": "18913k2b63ifs",
  "level": "warning",
  "summary": "[P2] [Triggered] [TEST] Test Monitor",
  "body": "This is the content of the monitor.",
  "annotations": {},
  "images": [
    {
      "src": "null",
      "alt": "This should not come through"
    },
    {
      "src": "https://example.com/pic.png",
      "alt": "Snapshot from [P2] [Triggered] [TEST] Signals Test Monitor"
    }
  ],
  "links": [
    {
      "href": "https://datadoghq.com/event/event?id=238472398472582",
      "text": "Datadog Monitor"
    }
  ],
  "tags": "monitor, name:myService, role:computing-node, region:us-west2",
  "status": "Recovered",
  "received_at": "2023-11-08T21:56:54.000+00:00"
}
```

Will be transposed to the following FireHydrant Signal:

```json Transposed Output
{
  "summary": "[P2] [Triggered] [TEST] Test Monitor",
  "body": "This is the content of the monitor.",
  "level": 1,
  "links": [
    {
      "href": "https://datadoghq.com/event/event?id=238472398472582",
      "text": "Datadog Monitor"
    }
  ],
  "images": [
    {
      "src": "https://example.com/pic.png",
      "alt": "Snapshot from [P2] [Triggered] [TEST] Signals Test Monitor"
    }
  ],
  "tags": ["monitor", "name:myService", "role:computing-node", "region:us-west2"],
  "idempotency_key": "18913k2b63ifs",
  "status": 1
}
```