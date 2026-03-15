# Source: https://docs.firehydrant.com/docs/site24x7-event-source.md

# Site24x7 Event Source

The Site24x7 Event Source allows you to configure Site24x7's website monitoring service as an <Glossary>Event Source</Glossary> to alert via FireHydrant's Signals.

You can configure [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) for your teams to subscribe specifically to events they care about and receive alerts.

## Configuring the Webhook

Site24x7 can be configured to fire webhooks to external destinations.

1. In FireHydrant, copy the Site24x7 ingest URL by going to **Signals** > **Event Sources** and clicking the **Copy URL** button for Site24x7.
2. Follow Site24x7's documentation on [webhooks integration](https://www.site24x7.com/help/admin/third-party-integration/webhooks.html) and paste the URL copied above into **Hook URL** and ensure you check **Post as JSON**.

## Field Mappings

The following Site24x7 webhook parameters are transposed to FireHydrant's Signals [Events Data Model](https://docs.firehydrant.com/docs/events-data-model):

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Site24x7 Parameter
      </th>

      <th>
        Signal Parameter(s)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `MONITOR_ID`
      </td>

      <td>
        `idempotency_key`
      </td>
    </tr>

    <tr>
      <td>
        `MONITORNAME` `STATUS`
      </td>

      <td>
        `summary` - "\{MONITORNAME} is \{STATUS}" or "No Monitor Name"
      </td>
    </tr>

    <tr>
      <td>
        `INCIDENT_DETAILS`
      </td>

      <td>
        `body` - "\{INCIDENT\_DETAILS}" or "No details provided."
      </td>
    </tr>

    <tr>
      <td>
        `MONITOR_DASHBOARD_LINK`\
        `MONITORURL`
      </td>

      <td>
        `links['Monitor Dashboard Link']`\
        `links['Monitor URL']`
      </td>
    </tr>

    <tr>
      <td>
        `TAGS`
      </td>

      <td>
        `tags`
      </td>
    </tr>

    <tr>
      <td>
        `STATUS`
      </td>

      <td>
        `status` - if `UP` on Site24x7, then `CLOSED` on FireHydrant, otherwise`OPEN`.
      </td>
    </tr>
  </tbody>
</Table>

Subsequently, the following webhook from Site24x7:

```json Site24x7 Payload
{
  "MONITOR_DASHBOARD_LINK": "https://site24x7.com",
  "MONITORTYPE": "URL",
  "MONITOR_ID": 107164000000025001,
  "STATUS": "DOWN",
  "MONITORNAME": "Zylker Monitor",
  "FAILED_LOCATIONS": "California-US",
  "INCIDENT_DETAILS": "Service Unavailable",
  "INCIDENT_REASON": "Service Unavailable",
  "OUTAGE_TIME_UNIX_FORMAT": 1705551700037,
  "GROUP_TAGS": [
    "ZylkerGrp",
    "URL"
  ],
  "MONITORURL": "http://zylker.com",
  "MONITOR_GROUPNAME": "Zylker Web Group",
  "POLLFREQUENCY": 1,
  "TAGS": [
    "zylker",
    "website"
  ],
  "INCIDENT_TIME": "18 Jan 2024 03:21:35 AEDT",
  "INCIDENT_TIME_ISO": "2024-01-17T20:21:35-0800"
}
```

...will be transposed to the following Signal in FireHydrant:

```json Transposed Signal
{
  "summary": "Zylker Monitor is DOWN",
  "body": "Service Unavailable",
  "status": "OPEN",
  "links": [
    {
      "href": "https://site24x7.com",
      "text": "Monitor Dashboard Link"
    },
    {
      "href": "http://zylker.com",
      "text": "Monitor URL"
    }
  ],
  "tags": ["zylker", "website"],
  "idempotency_key": "1.0716400000002501e+17"
}
```