# Source: https://docs.firehydrant.com/docs/pingdom-event-source.md

# Pingdom Event Source

The Pingdom Event Source allows you to configure Pingdom's website monitoring service as an <Glossary>Event Source</Glossary> to alert via FireHydrant's Signals.

## Configuring the Webhook

Pingdom can be configured to fire webhooks to external destinations upon state changes to your uptime checks. In FireHydrant, you can find the Pingdom source URL by going to **Signals** > **Event Sources** and clicking the **Copy URL** button in the Pingdom row.

![](https://files.readme.io/9956645-CleanShot_2024-06-21_at_17.52.14.png)

Copy that URL in FireHydrant, and set this URL as the destination when configuring the webhook in Pingdom. For instructions on configuring a webhook in Pingdom, visit [Pingdom's Webhook Docs](https://www.pingdom.com/resources/webhooks/).

## Field Mappings/Behaviors

The following Pingdom webhook parameters are transposed to FireHydrant's Signals [Events Data Model](https://docs.firehydrant.com/docs/events-data-model):

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Pingdom Parameter
      </th>

      <th>
        Signal Parameter(s)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `check_id`
      </td>

      <td>
        `idempotency_key` AND\
        `annotations.check_id`
      </td>
    </tr>

    <tr>
      <td>
        `description`
      </td>

      <td>
        `summary`
      </td>
    </tr>

    <tr>
      <td>
        `long_description`
      </td>

      <td>
        `body`
      </td>
    </tr>

    <tr>
      <td>
        `check_name`
      </td>

      <td>
        `annotations.check_name`
      </td>
    </tr>

    <tr>
      <td>
        `check_type`
      </td>

      <td>
        `annotations.check_type`
      </td>
    </tr>

    <tr>
      <td>
        `importance_level`
      </td>

      <td>
        `level` - If `HIGH` on Pingdom then the Alert is `ERROR` on FireHydrant. If `LOW` then it is `WARN` on FireHydrant
      </td>
    </tr>

    <tr>
      <td>
        `tags`
      </td>

      <td>
        `tags`
      </td>
    </tr>

    <tr>
      <td>
        `current_state`
      </td>

      <td>
        `status` - If `DOWN` on Pingdom then the Alert is `OPEN` on FireHydrant. Otherwise, the alert is `CLOSED` on FireHydrant
      </td>
    </tr>
  </tbody>
</Table>

Subsequently, the following webhook from Pingdom:

```json Pingdom Payload
{
  "check_id": 12345,
  "check_name": "Name of HTTP check",
  "check_type": "HTTP",
  "check_params": {
    "basic_auth": false,
    "encryption": true,
    "full_url": "https://www.example.com/path",
    "header": "User-Agent:Pingdom.com_bot",
    "hostname": "www.example.com",
    "ipv6": false,
    "port": 443,
    "url": "/path"
  },
  "tags": [
    "service:web",
    "env:production"
  ],
  "previous_state": "UP",
  "current_state": "DOWN",
  "importance_level": "HIGH",
  "state_changed_timestamp": 1451610061,
  "state_changed_utc_time": "2016-01-01T01:01:01",
  "long_description": "Long error message",
  "description": "Short error message",
  "first_probe": {
    "ip": "123.4.5.6",
    "ipv6": "2001:4800:1020:209::5",
    "location": "Stockholm, Sweden"
  },
  "second_probe": {
    "ip": "123.4.5.6",
    "ipv6": "2001:4800:1020:209::5",
    "location": "Austin, US",
    "version": 1
  }
}
```

...will be transposed to the following Signal in FireHydrant:

```json Transposed Signal
{
  "summary": "Short error message",
  "body": "Long error message",
  "level": 2,
  "links": [],
  "images": [],
  "tags": ["service:web", "env:production"],
  "annotations": {
    "check_id": "12345",
    "check_name": "Name of HTTP check",
    "check_type": "HTTP"
  },
  "idempotency_key": "12345",
  "status": 0
}
```