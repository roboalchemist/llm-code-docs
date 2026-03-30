# Source: https://docs.firehydrant.com/docs/pagerduty-event-source.md

# PagerDuty Event Source

### Configuring PagerDuty Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL that you will use when creating a webhook in PagerDuty.

   <Image align="center" src="https://files.readme.io/af1c59c-pagerduty-webhook.jpg" />
2. In PagerDuty, navigate to Integrations > Generic Webhooks (V3). Click the "New Webhook" button to create a new webhook.
3. Add the URL from step 1 to your webhook.
4. Select the events that you want to trigger Signals in FireHydrant.
5. Click “Add Webhook” to save your webhook.
6. You can learn more about PagerDuty webhooks by reading their Webhooks documentation.

### Testing your PagerDuty Webhook

1. After you have saved your webhook, click into the webhook (either the title of the Manage option). At the bottom of the page, click "Send Test Event."
2. Confirm that FireHydrant received your webhook by visiting Alerting > Webhook Logs in the web app. You should see a new event created. You can open the drawer to see the full payload from PagerDuty.

<Image align="center" src="https://files.readme.io/544447d-logs.jpg" />

## Field Mappings/Behaviors

The payload from PagerDuty will be directly mapped to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model). The following table explains the behavior once the payload hits our system:

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
        `event.id`
      </td>

      <td>
        `idempotency_key`
      </td>
    </tr>

    <tr>
      <td>
        `event.data.title`\
        *-OR-*\
        `event.data.message`
      </td>

      <td>
        `summary` - Checks if the payload contains `event.data.title`, otherwise uses `event.data.message`. If neither exist, will be hard-coded to `No summary provided`.
      </td>
    </tr>

    <tr>
      <td>
        `event.data.message`
      </td>

      <td>
        `body` - Uses `event.data.message` if exists, otherwise is empty
      </td>
    </tr>

    <tr>
      <td>
        `event.data.html_url`
      </td>

      <td>
        `links`
      </td>
    </tr>

    <tr>
      <td>
        `event.data.priority.summary`\
        `event.data.urgency`
      </td>

      <td>
        `annotations['priority']`\
        `annotations['urgency']`
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        `status` - Closed on FireHydrant if `event.data.status` is "resolved", otherwise Open
      </td>
    </tr>
  </tbody>
</Table>

These mappings mean that an inbound webhook from PagerDuty with the following content:

```json PD Payload
{
  "event": {
    "id": "6NI370K25HZYH3UTP41AFF5ZFN",
    "event_type": "incident.triggered",
    "resource_type": "incident",
    "occurred_at": "2024-01-19T02:56:50.174Z",
    "data": {
      "id": "Q2DGVPTAGDY34J",
      "type": "incident",
      "self": "https://api.pagerduty.com/incidents/6NI370K25HZYH3UTP",
      "html_url":"https://sample.pagerduty.com/incidents/6NI370K25HZYH3UTP",
      "number": 6328286,
      "status": "triggered",
      "incident_key": null,
      "created_at": "2024-01-19T02:56:50Z",
      "title": "Test - No action Required",
      "service": {
        "html_url": "https://sample.pagerduty.com/services/PYOQREP",
        "id": "PYOQREP",
        "self": "https://api.pagerduty.com/services/PYOQREP",
        "summary": "Incident SFDC Email Notification",
        "type": "service_reference"
      },
      "assignees": [
        {
          "html_url": "https://sample.pagerduty.com/users/Y5ML0GA",
          "id": "Y5ML0GA",
          "self": "https://api.pagerduty.com/users/Y5ML0GA",
          "summary": "Random User",
          "type": "user_reference"
        }
      ],
      "escalation_policy": {
        "html_url": "https://sample.pagerduty.com/escalation_policies/OP56E0H",
        "id": "OP56E0H",
        "self": "https://api.pagerduty.com/escalation_policies/OP56E0H",
        "summary": "Incident SFDC Email Notification-ep",
        "type": "escalation_policy_reference"
      },
      "teams": [
        {
          "html_url": "https://sample.pagerduty.com/teams/BY0RZ1A",
          "id": "BY0RZ1A",
          "self": "https://api.pagerduty.com/teams/BY0RZ1A",
          "summary": "GCS Incident Management Team",
          "type": "team_reference"
        }
      ],
      "priority": {
        "html_url": "https://sample.pagerduty.com/account/incident_priorities",
        "id": "PSO75BM",
        "self": "https://api.pagerduty.com/priorities/PSO75BM",
        "summary": "P1",
        "type": "priority_reference"
      },
      "urgency": "high",
      "conference_bridge": null,
      "resolve_reason": null
    }
  }
}
```

Will be transposed to the following FireHydrant Signal:

```json Transposed Signal
{
  "summary": "Test - No action Required",
  "body": "",
  "status": "OPEN",
  "links": [
    {
      "href": "https://sample.pagerduty.com/incidents/6NI370K25HZYH3UTP",
      "text": "PagerDuty Incident"
    }
  ],
  "annotations": {
    "priority": "P1",
    "urgency": "high"
  },
  "idempotency_key": "6NI370K25HZYH3UTP41AFF5ZFN"
}
```