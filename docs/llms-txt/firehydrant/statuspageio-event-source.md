# Source: https://docs.firehydrant.com/docs/statuspageio-event-source.md

# Statuspage.io Event Source

The Statuspage Event Source for Signals allows users to create events in FireHydrant from notifications or updates from Statuspages. When Statuspage sends an event to FireHydrant, we’ll evaluate the event payload to see if it matches a rule one of your teams set up to alert them. Learn more about [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) here.

## Configuring Statuspage Webhook

1. In FireHydrant, navigate to the [Event Sources](https://app.firehydrant.io/signals/sources/integrations) page. Here, copy the ingest URL for Statuspage.io.
2. Navigate to the Statuspage you'd like to subscribe to and follow [Atlassian's documentation](https://support.atlassian.com/statuspage/docs/enable-webhook-notifications/) on how to configure a webhook subscription.
   1. **Note**: This will only be available if the Statuspage's administrator has enabled webhook subscribers in their settings - if not, you will need to contact them to enable it.
3. Paste the URL copied from step 1 into the URL destination for the webhook subscription. If desired, add an email address to receive notification if the endpoint fails.

## Field Mappings

The following Statuspage webhook parameters are transposed to FireHydrant's Signals [Events Data Model](https://docs.firehydrant.com/docs/events-data-model):

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        StatusCake Parameter
      </th>

      <th>
        Signal Parameter(s)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `incident.id`
      </td>

      <td>
        `idempotency_key`
      </td>
    </tr>

    <tr>
      <td>
        `incident.name`
      </td>

      <td>
        `summary`
      </td>
    </tr>

    <tr>
      <td>
        `incident.incident_updates[0].body`
      </td>

      <td>
        `body`
      </td>
    </tr>

    <tr>
      <td>
        `incident.status`
      </td>

      <td>
        `level` - Defaults to `2` (ERROR), unless the `incident.status` is resolved, then it's `0` (INFO)\
        `status` - Closed on FireHydrant if `incident.status` is resolved, otherwise it's Open
      </td>
    </tr>

    <tr>
      <td>
        `incident.shortlink`
      </td>

      <td>
        `links['Statuspage.io Incident']`
      </td>
    </tr>

    <tr>
      <td>
        `incident.components`
      </td>

      <td>
        `tags` - Components are mapped to tags in FireHydrant in the format of `component:[NAME]`
      </td>
    </tr>

    <tr>
      <td>
        `page.id`\
        `incident.id`\
        `incident.created_at`\
        `incident.updated_at`\
        `incident.impact`\
        `incident.status`
      </td>

      <td>
        `annotations['statuspage_page_id']`\
        `annotations['statuspage_incident_id']`\
        `annotations['statuspage_created_at']`\
        `annotations['statuspage_updated_at']`\
        `annotations['statuspage_impact']`\
        `annotations['statuspage_status']`
      </td>
    </tr>
  </tbody>
</Table>

Subsequently, the following webhook from Statuspage:

```json Statuspage Payload
{
  "meta": {
    "unsubscribe": "http://example.statuspage.io/?unsubscribe=123abc",
    "documentation": "https://help.statuspage.io/knowledge_base/topics/webhook-notifications",
    "generated_at": "2024-08-06T14:05:00.000Z"
  },
  "page": {
    "id": "page123",
    "status_indicator": "major",
    "status_description": "Partial System Outage"
  },
  "incident": {
    "name": "API Outage",
    "status": "investigating",
    "created_at": "2024-08-06T14:00:00.000Z",
    "updated_at": "2024-08-06T14:05:00.000Z",
    "monitoring_at": null,
    "resolved_at": null,
    "impact": "major",
    "shortlink": "https://stspg.io/incident123",
    "started_at": "2024-08-06T14:00:00.000Z",
    "id": "inc_123456",
    "page_id": "page123",
    "incident_updates": [
      {
        "status": "investigating",
        "body": "We are investigating reports of API errors.",
        "created_at": "2024-08-06T14:00:00.000Z",
        "updated_at": "2024-08-06T14:00:00.000Z",
        "display_at": "2024-08-06T14:00:00.000Z",
        "id": "update_123",
        "incident_id": "inc_123456",
        "affected_components": [
          {
            "code": "api_component",
            "name": "API",
            "old_status": "operational",
            "new_status": "major_outage"
          }
        ]
      }
    ],
    "components": [
      {
        "status": "major_outage",
        "name": "API",
        "created_at": "2024-01-01T00:00:00.000Z",
        "updated_at": "2024-08-06T14:00:00.000Z",
        "position": 1,
        "description": "Our main API",
        "showcase": true,
        "id": "api_component",
        "page_id": "page123",
        "group_id": null
      }
    ]
  }
}
```

...will be transposed to the following Signal in FireHydrant:

```json Transposed Signal
{
  "summary": "API Outage",
  "body": "We are investigating reports of API errors.",
  "level": 2,
  "links": [
    {
      "href": "https://stspg.io/incident123",
      "text": "StatusPage.io Incident"
    }
  ],
  "tags": [
    "component:API"
  ],
  "idempotency_key": "inc_123456",
  "status": 0,
  "annotations": {
    "statuspage_page_id": "page123",
    "statuspage_incident_id": "inc_123456",
    "statuspage_created_at": "2024-08-06T14:00:00.000Z",
    "statuspage_updated_at": "2024-08-06T14:05:00.000Z",
    "statuspage_impact": "major",
    "statuspage_status": "investigating"
  }
}
```