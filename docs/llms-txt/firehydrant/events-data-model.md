# Source: https://docs.firehydrant.com/docs/events-data-model.md

# Events Data Model

Signals Events are stored in FireHydrant when a webhook is sent to FireHydrant that matches the correct data model. This guide will help you understand the data model that FireHydrant uses to define Events.

## What makes a valid Signal Event object?

Signal Event object is a dictionary hashmap returned by transposer function that looks like the following:

```javascript
{
  "summary": "CPU usage too high",
  "body": "VM CPU utilization is over 90%",
  "status": "OPEN",
  "idempotency_key": "18913k2b63ifs",
  "tags": [
    "name:myService",
    "region:us-west2"
  ],
  "annotations": {
    "acme-inc/team": "sre"
  },
  "level": "ERROR",
  "images": [
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
  ]
}
```

## Data Model

<Table>
  <thead>
    <tr>
      <th>
        Field Name
      </th>

      <th>
        Type
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `idempotency_key`
      </td>

      <td>
        text
      </td>

      <td>
        A unique identifier used to group/deduplicate open alerts.

        * \*Note\*\*: Max length is 255 chars. Anything longer and the request will fail.
      </td>
    </tr>

    <tr>
      <td>
        `summary`
      </td>

      <td>
        text
      </td>

      <td>
        CPU Utilization Spiking

        * \*Note\*\*: Max length is 255 chars. Anything longer will be truncated to 250 chars, appended with ellipses (`...`), and the rest is inserted into the `body`
      </td>
    </tr>

    <tr>
      <td>
        `body`
      </td>

      <td>
        text
      </td>

      <td>
        Longer description or body of the alert, usually a more detailed message.
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        enum
      </td>

      <td>
        Either `OPEN` (0)  or `CLOSED` (1)
      </td>
    </tr>

    <tr>
      <td>
        `level`
      </td>

      <td>
        enum
      </td>

      <td>
        Accepts either the enum (e.g., `info`, case-insensitive) OR the integer (e.g., `0`)

        * `INFO` (0)
        * `WARN` (1)
        * `ERROR` (2)
        * `FATAL` (3)
      </td>
    </tr>

    <tr>
      <td>
        `annotations`
      </td>

      <td>
        object
      </td>

      <td>
        * \*Note\*\*: Currently, annotations only support string values. Any non-string values (booleans, integers, etc.) should be converted to strings.

        `{ “randomNumber”: "1234" }`
      </td>
    </tr>

    <tr>
      <td>
        `images`
      </td>

      <td>
        array
      </td>

      <td>
        Array of objects containing a `src` (url to image) and an `alt` (alt + display text for image)

        `[ { "src": "https://site.com/images/123.png', "alt": "A simple, sample image" } ]`
      </td>
    </tr>

    <tr>
      <td>
        `links`
      </td>

      <td>
        array
      </td>

      <td>
        Array of objects containing a `href` (url) and `text` (display text for link)

        `[ { "href": "https://site.com/monitors/123', "text": "Monitoring Source" } ]`
      </td>
    </tr>

    <tr>
      <td>
        `tags`
      </td>

      <td>
        array
      </td>

      <td>
        `["tag1", "service:your-service-slug", "environment:production"]`
      </td>
    </tr>

    <tr>
      <td>
        `attachments`
      </td>

      <td>
        array
      </td>

      <td>
        Array of objects containing attachments FireHydrant uploads on behalf of users. For now, it is only used by Live Call Routing. Contains `filename`, `content_type`, `size`, `label`, and `url` keys.

        `[ { "filename": "example.mp3", "content_type": "audio/mpg", "size": 43050, "label": "Voicemail Recording", "url": "https://app.firehydrant.io/signals/attachments/abc-123.mp3"`
      </td>
    </tr>
  </tbody>
</Table>

### Special Annotations

Special annotations are parameters that FireHydrant uses in Annotations for specific functions. These annotations are contained within the `annotations` field of the data model.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Annotation
      </th>

      <th>
        Accepted Values
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `signals.firehydrant.com/notification-priority`
      </td>

      <td>
        `HIGH`, `MEDIUM`, `LOW`
      </td>

      <td>
        This annotation value is used by FireHydrant to set the alert's priority. The alert priority impacts how a user will be paged according to their personal notification preferences. If this annotation is not specified, then the alert defaults to `HIGH`.

        To learn more, visit [Notification Preferences](https://docs.firehydrant.com/docs/signals-notification-preferences).
      </td>
    </tr>

    <tr>
      <td>
        `signals.firehydrant.com/transposer-id`
      </td>

      <td>
        UUID
      </td>

      <td>
        This is automatically set by FireHydrant and only applies to [Custom Event Source](https://docs.firehydrant.com/docs/custom-event-source) created by users.
      </td>
    </tr>

    <tr>
      <td>
        `signals.firehydrant.com/transposer-name`
      </td>

      <td>
        Varies
      </td>

      <td>
        This is automatically set by FireHydrant and will be the slugified value of the Transposer's name. This is useful in [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) for seeing which source an Event came from.

        The exception to this is the [Generic Webhook Event Source](https://docs.firehydrant.com/docs/generic-webhook-event-source), in which case this annotation will not exist.
      </td>
    </tr>
  </tbody>
</Table>

### Private Annotations

Private annotations are values FireHydrant will set internally based on various things. **Do not set these values directly in the payload body, as they are sanitized upon ingestion before FireHydrant sets the values.**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Private Annotation
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `private.signals.firehydrant.com/actor-id`
      </td>

      <td>
        ID of the actor who sent the page. If via chat app, it will be the user's ID in the chat app. If via web UI, it will be the user's UUID in FireHydrant

        ***Only exists for manual alerts.***
      </td>
    </tr>

    <tr>
      <td>
        `private.signals.firehydrant.com/actor-name`
      </td>

      <td>
        Name of the actor (usually a user) who triggered the page.

        ***Only exists for manual alerts.***
      </td>
    </tr>

    <tr>
      <td>
        `private.signals.firehydrant.com/actor-source`
      </td>

      <td>
        The source of the actor who created the page. Possible values are:

        * `firehydrant_user` - For any alerts created from web UI or chat apps
        * `api_key` - For any alerts created via an API call
        * `integration` - For any alerts created via an integration or Event source
      </td>
    </tr>

    <tr>
      <td>
        `private.signals.firehydrant.com/email-source-id`
      </td>

      <td>
        The UUID for the email event source address that received the event. See [Email Event Source](https://docs.firehydrant.com/docs/email-event-source) for more information.

        ***Only exists for alerts that target email event sources.***
      </td>
    </tr>

    <tr>
      <td>
        `private.signals.firehydrant.com/escalation-policy-id`
      </td>

      <td>
        The UUID for the escalation policy being targeted. See [Bypassing Rules](https://docs.firehydrant.com/docs/signals-alert-rules#bypassing-rules)    in Alert Rules documentation on how to directly target escalation policies.

        ***Only exists for alerts that directly target escalation policies.***
      </td>
    </tr>

    <tr>
      <td>
        `private.signals.firehydrant.com/team-id`
      </td>

      <td>
        The UUID for the team being targeted. See [Bypassing Rules](https://docs.firehydrant.com/docs/signals-alert-rules#bypassing-rules)   in Alert Rules documentation on how to directly target teams.

        ***Only exists for alerts that directly target teams OR escalation policies.***
      </td>
    </tr>

    <tr>
      <td>
        `private.signals.firehydrant.com/via`
      </td>

      <td>
        Denotes how the alert was sent. Possible values are:

        * `manually-paged` - When alert is sent via web UI or from Slack's `/fh page`
      </td>
    </tr>
  </tbody>
</Table>

### Understanding the Idempotency Key

The `idempotency_key` is FireHydrant's way of identifying incoming events that need to be deduplicated or tied together. For instance, if your monitoring tool sends FireHydrant two events, one after the other, with a matching key (e.g., `12345`), Signals will not create a new alert on the 2nd event if the first alert/event is still open\*. This prevents opening multiple alerts from the same monitor/alarm or for the same issue.

Another use of the `idempotency_key` is to auto-resolve flappy alerts. If your monitoring tool sends an `OPEN` and then `CLOSED` event to FireHydrant with the same key, FireHydrant will auto-resolve the open alert(s) that were generated from the original event.

Other behaviors to note:

* If the first event with key `12345` is already resolved, then another event that comes in with the same key will open a new alert.
* If 24 hours elapse after an alert with key `12345`, then a subsequent event with the same key will open a new alert regardless of whether the first alert is still open or not.

> 📘 Note:
>
> This is a separate feature from [Alert Grouping](https://docs.firehydrant.com/docs/alert-grouping), which will group alerts based on other parameters in the alert aside from the key.

### Tags and the Service Catalog

Using the service-tagging convention, you can automatically associate any Service Catalog component with your alerts and the incidents that get opened from those alerts. You can reference these components with the following prefixes:

* **Service**: `service:`
* **Environment**: `environment:` or `env:`

These slugs can be found in your Service Catalog on each respective component's page in the **Details** section.

<Image alt="Where to find the slug on a component's details page" align="center" width="650px" src="https://files.readme.io/24057f5-CleanShot_2024-04-25_at_17.21.492x.png">
  Where to find the slug on a component's details page
</Image>

For example, let's take a service called `API Gateway` with a slug of `api-gateway`. It is in the `Production` environment (slug `production`).

The tags to automatically pull these components in would be: `service:api-gateway` and `environment:production`. When you include a catalog component in your payload, any incidents that are opened from Alerts created by that payload will automatically mark those catalog components as impacted when the incident is opened. Below is the example payload:

```json
{
  "summary": "CPU Utilization Spiking",
  "body": "The production server is experiencing greater than 99% utilizations of compute.",
  "level": "ERROR",
  "status": "OPEN",
  "idempotency_key": "ad98rb3b2b",
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
  "tags": ["service:api-gateway", "environment:production", "random-tag"]
}
```

## Return Values

When Events are sent to any of FireHydrant's Event Sources endpoints, there are some basic responses you can watch for:

| Response Code           | Response Body                | Description                                                                  |
| :---------------------- | :--------------------------- | :--------------------------------------------------------------------------- |
| `202 Accepted`          | `{ "success": true }`        | General response when an Event Source ingestion is successful                |
| `400 Bad Request`       | `{ "errors": [ "STRING" ] }` | Array of error messages returned when an Event webhook's payload was invalid |
| `429 Too Many Requests` | -                            | Response when you have exceed the rate limit for ingesting events            |