# Source: https://docs.firehydrant.com/docs/webhooks.md

# Webhooks

FireHydrant enables you to create webhooks that respond to internal events or custom commands to send information to external systems.

## Prerequisites

* You will need <Glossary>Owner</Glossary> permissions to access webhooks settings

## Creating a webhook

<Image alt="Webhooks page under Settings" align="center" width="650px" src="https://files.readme.io/bdddb15-Screenshot_2024-01-18_at_6.22.15_PM.png">
  Webhooks page under Settings
</Image>

1. Navigate to **Settings** in FireHydrant and click on **Webhooks**.
2. Click **+ Add webhook** on the webhooks page.
3. On the next page, you'll be presented with a few different fields depending on what kind of Webhook you're trying to create:
   1. **URL** - The single endpoint URL that this webhook should be sent to. Each webhook configuration sends to one destination endpoint. To send webhooks to multiple destinations, create multiple webhook configurations.
   2. **Secret** - An extra parameter sent so your destination endpoint can validate the signature. See the [Verifying Requests](#verifying-requests) section below.
   3. **Status** - **Active** or **Inactive**. You can inactivate a webhook to prevent anyone from using it but still keep it around in case it is needed later.
   4. **Event Subscriptions** - This configures which FireHydrant events will trigger this webhook payload. If you are creating a Webhook to be used with [Command Extensions](https://docs.firehydrant.com/docs/command-extensions), then you can leave all of these unchecked.
      1. **Change Events** - Fires this webhook to the destination URL whenever a new Change Event is created within FireHydrant
      2. **Incidents** - Fires this webhook to the destination URL whenever any changes on any (public) incidents occur.
      3. **Incidents (Private)** - The same as previous, but specifically for private incidents.
      4. **Signals (BETA)** - This webhook will fire upon any Signals/alert activities, including when alerts change states
4. Click **Add webhook** to persist these changes and create the webhook.

### Verifying Requests

It's essential to make sure that the requests you're getting on your webhook URL are coming from FireHydrant. To do this, compare the signature in the request's headers to an HMAC signature generated from the request body sent to you. FireHydrant uses hex digest.

For example, this is the pseudocode for verifying the request:

```ruby Pseudocode
signature = request.headers['fh-signature']
body = request.body
secret = 'your webhook secret set above'
if HMAC.hexdigest('sha256', secret, body) == signature
  // request is valid
end
```

Some tools, like [HMAC generator](https://www.freeformatter.com/hmac-generator.html), help generate signatures for testing while you develop an endpoint.

## Webhook-Triggering Events

For **Incidents** and **Incidents (Private)** webhooks, the following events/changes on incidents will trigger a webhook to the destination:

* **Chat events** - When a new chat message is posted directly into the FireHydrant timeline from web UI or from an incident channel in your chat application
* **Follow-up updates** - When follow-ups are updated (e.g., marked done, created, etc.) on incidents
* **General updates** - Any changes to any fields on an incident, including Custom Fields
* **Milestone changes** - Any change to the current milestone
* **Milestone timestamp changes** - When making edits to any timestamps for other milestones, regardless of what the current milestone is
* **Notes and infrastructure updates** - When posting incident notes or changing impacted infrastructure on the incident
* **Role assignments** - When users are assigned or de-assigned roles on incidents
* **Task updates** - When tasks are updated (e.g., marked done, created, etc.) on incidents
* **Team assignments** - When teams are assigned/unassigned from incidents

## Example Payloads

The payload examples here are for event-triggered webhooks (e.g. if you selected one or more event subscriptions when creating the Webhook above).

### Incident Event Payload

```json
{
  "data": {
    "incident": {
      "conference_bridges": [
        {
          "id": "efb3a79f-5d11-45dc-94cc-955bbc72afb5",
          "name": "Webex Bridge",
          "url": "https://meet123.webex.com/meet191/j.php"
        }
      ],
      "counts": {
        "starred_events": 0,
        "starred_messages": 0
      },
      "created_at": "2023-07-25 13:34:49 UTC",
      "current_milestone": "resolved",
      "customer_impact_summary": "",
      "description": "",
      "follow_ups": [],
      "id": "04d9fd1a-ba9c-417d-b396-58a6e2c374de",
      "impacts": [],
      "incident_channels": [
        {
          "id": "C05J7JSEA23",
          "name": "inc-602-hark-i-hear-an-incident-subscription-webhook",
          "source": "slack",
          "status": "operational",
          "url": "https://app.slack.com/client/TABC123/CABC123"
        }
      ],
      "labels": [],
      "milestones": [
        {
          "created_at": "2023-07-25 13:34:49 UTC",
          "duration": "",
          "occurred_at": "2023-07-25 13:34:49 UTC",
          "type": "started",
          "updated_at": "2023-07-25 13:34:49 UTC",
          "updated_by_id": "2af3339f-9d81-434b-a208-427d6d85c124",
          "updated_by_type": "User"
        },
        {
          "created_at": "2023-07-25 13:34:49 UTC",
          "duration": "0",
          "occurred_at": "2023-07-25 13:34:49 UTC",
          "type": "acknowledged",
          "updated_at": "2023-07-25 13:34:49 UTC",
          "updated_by_id": "2af3339f-9d81-434b-a208-427d6d85c124",
          "updated_by_type": "User"
        },
        {
          "created_at": "2023-07-25 13:37:04 UTC",
          "duration": "134",
          "occurred_at": "2023-07-25 13:37:04 UTC",
          "type": "mitigated",
          "updated_at": "2023-07-25 13:37:04 UTC",
          "updated_by_id": "2af3339f-9d81-434b-a208-427d6d85c124",
          "updated_by_type": "User"
        },
        {
          "created_at": "2023-07-25 13:38:17 UTC",
          "duration": "73",
          "occurred_at": "2023-07-25 13:38:17 UTC",
          "type": "resolved",
          "updated_at": "2023-07-25 13:38:17 UTC",
          "updated_by_id": "2af3339f-9d81-434b-a208-427d6d85c124",
          "updated_by_type": "User"
        }
      ],
      "name": "Hark I hear an incident subscription webhook",
      "number": 602,
      "priority": {
        "description": "",
        "slug": "P3"
      },
      "private_status_page_url": "https://app.firehydrant.io/incidents/internal/status_page/OBSCURE_SLUG_HERE",
      "role_assignments": [],
      "severity": {
        "description": "Primary product functionality is severely impacted and unusable. Customers are unable to utilize a common feature to its fullest ability. Data may not be displayed as expected but not lost. There is no workaround for customers.",
        "slug": "SEV2",
        "type": "unexpected_downtime"
      },
      "started_at": "2023-07-25 13:34:49 UTC",
      "summary": "",
      "tags": [],
      "tasks": [
        {
          "assigned_to": [],
          "state": "open",
          "summary": "Post an update to the internal status page"
        },
        {
          "assigned_to": [],
          "state": "open",
          "summary": "Assign a role for a mitigator"
        }
      ],
      "team_assignments": [],
      "updated_at": "2023-07-25 13:38:17 UTC"
    }
  },
  "event": {
    "operation": "UPDATED",
    "resource_type": "incident"
  }
}
```

### Change Event Payload

In a change event JSON payload, you receive 2 top-level keys: **event** and **data**. The **event** key contains the operation type and resource type. You can use these to determine which type of event notification you just received.

```json
{
  "data": {
    "attachments": [],
    "created_at": "2019-05-31T16:16:11.728Z",
    "description": "",
    "duration_iso8601": null,
    "duration_ms": null,
    "ends_at": null,
    "environments": [
      {
        "created_at": "2019-04-17T12:00:54.620Z",
        "description": "",
        "id": "b73d1a05-6e6f-4e17-9c3e-2b119342c583",
        "name": "Production"
      }
    ],
    "id": "489d7b90-a9d7-43d2-99be-d33c5acb59f8",
    "identities": [],
    "labels": {
      "stack": "rails"
    },
    "related_changes": [],
    "services": [
      {
        "created_at": "2019-04-17T12:00:54.772Z",
        "description": "",
        "functionalities": [
          {
            "created_at": "2019-04-17T13:38:06.631Z",
            "description": "",
            "id": "cf13435c-b246-4ffc-9f04-55552cca3d53",
            "services": [
              {
                "created_at": "2019-04-17T12:00:54.772Z",
                "description": "",
                "id": "355411a9-bbb0-4b58-ad2c-0257d8995f9d",
                "labels": {},
                "name": "firehouse",
                "slug": "firehouse",
                "updated_at": "2019-04-17T12:00:54.772Z"
              },
              {
                "created_at": "2019-04-17T13:38:41.625Z",
                "description": "",
                "id": "bd865254-aea2-4aa0-afa4-2bfb659f0252",
                "labels": {},
                "name": "laddertruck",
                "slug": "laddertruck",
                "updated_at": "2019-04-17T13:38:41.625Z"
              }
            ],
            "summary": "REST API",
            "updated_at": "2019-04-17T13:38:06.631Z"
          },
          {
            "created_at": "2019-04-17T13:39:18.147Z",
            "description": "",
            "id": "95db369a-186f-4245-86e1-e13dead5cd73",
            "services": [
              {
                "created_at": "2019-04-17T12:00:54.772Z",
                "description": "",
                "id": "355411a9-bbb0-4b58-ad2c-0257d8995f9d",
                "labels": {},
                "name": "firehouse",
                "slug": "firehouse",
                "updated_at": "2019-04-17T12:00:54.772Z"
              },
              {
                "created_at": "2019-04-17T13:38:41.625Z",
                "description": "",
                "id": "bd865254-aea2-4aa0-afa4-2bfb659f0252",
                "labels": {},
                "name": "laddertruck",
                "slug": "laddertruck",
                "updated_at": "2019-04-17T13:38:41.625Z"
              }
            ],
            "summary": "Web UI",
            "updated_at": "2019-04-17T13:39:18.147Z"
          }
        ],
        "id": "355411a9-bbb0-4b58-ad2c-0257d8995f9d",
        "labels": {},
        "name": "firehouse",
        "slug": "firehouse",
        "updated_at": "2019-04-17T12:00:54.772Z"
      }
    ],
    "starts_at": "2019-06-01T00:12:12.000Z",
    "summary": "Production Deploy ",
    "updated_at": "2019-05-31T16:33:26.932Z"
  },
  "event": {
    "operation": "updated",
    "resource_type": "change_event"
  }
}
```

### Signals Activity Payload (BETA)

In a Signals update payload, we similarly have `data` and `event` top-level keys. Payloads come in the following format:

```json JSON
{
  "data": {
    "alert": {
      "body": "This is the description of the Alert, if there is one",
      "decision": null,
      "id": "6f767579-0015-400e-8c6e-cb481d5760c2",
      "starts_at": "2024-03-29 22:50:07 UTC",
      "status": "opened",
      "summary": "This is the Summary/Title of the Alert"
    }
  },
  "event": {
    "operation": "CREATED",
    "resource_type": "signals_alerts"
  }
}
```

The key parameters that will differ between webhooks are as follows:

* `data.alert.decision` - The action the system or an on-call responder takes. The possible values here are:
  * `null` - When an alert is first created, this will be `null`.
  * `ACKNOWLEDGE` - A user either acknowledged the alert or opened an incident (which also acknowledges the alert).
  * `ESCALATE` - A user escalated the alert.
  * `RESOLVE` - A user resolved the alert.
  * `DISMISS` - A user dismissed/ignored the alert.
  * `TIMEOUT` - The Escalation Policy reached the next step or handed off after no other action.
* `data.alert.status` - The new status of the alert. This will depend on the `decision` parameter above. Possible values are:
  * `opened` - Default state until someone acknowledges, ignores, or resolves the alert.
  * `acknowledged` - Alert is acknowledged.
  * `resolved` - Alert is resolved.
  * `ignored` - Alert is ignored.
* `event.operation` - Either `CREATED` on the alert's creation or `UPDATED` for all other actions.

## Using Webhooks with Command Extensions

[Command Extensions](https://docs.firehydrant.com/docs/command-extensions) allow you to create custom Slack commands that can request external systems using Webhooks. To learn more, visit the documentation linked.

## Next Steps

* If you would like webhooks automated, you may instead be interested in the [Send a Webhook](https://docs.firehydrant.com/docs/runbook-step-send-a-webhook) Runbook step
* Learn more about [Command Extensions](https://docs.firehydrant.com/docs/command-extensions) and how you can use custom Slack commands to send requests to other systems
* Browse our [native integrations](https://docs.firehydrant.com/docs/integrations-overview) or visit [our API](https://docs.firehydrant.com/reference/firehydrant-api)