# Source: https://docs.gitguardian.com/honeytoken/configure-alerts.md

# Configure your alerts

> Describes how to configure email notifications, Slack alerts, and custom webhooks for honeytoken trigger events.

If a honeytoken is in an Active status, any new event will change the status to Triggered.

## Email notifications

Managers will receive an email notification whenever a honeytoken's status is changed to Triggered.

This notification can be deactivated in Settings > Personal: Notifications > [Email preferences](https://dashboard.gitguardian.com/settings/personal/notifications).

## Slack notifications

You can configure Slack notifications to receive honeytoken alerts directly in your Slack channels. This provides real-time visibility into honeytoken activity alongside your other security notifications.

Slack notifications support:
- **Honeytoken Triggered**: When a honeytoken status changes to triggered
- **New Honeytoken Event**: When a new honeytoken usage is detected

To set up Slack notifications, configure your [Slack integration](/platform/configure-alerting/notifiers-integrations/slack) and select the honeytoken event types you want to receive.
 
:::info
Honeytoken slack notifications can only be configured in the All-incidents team.
:::

## Custom webhooks

It is possible to configure custom webhooks to receive alerts when honeytokens are triggered or when a new event appears. This allows you to integrate and manage the information directly within your SIEM or other security systems.

You can create dedicated webhooks or use the same ones for secrets detection events and refine the "Event Subscription" scopes as needed.

![Custom webhooks for honeytokens](/img/honeytoken/custom-webhooks-honeytoken.png)

The possible event subscriptions are:
- Honeytoken > Triggers: get a webhook event whenever the status of a honeytoken gets changed to Triggered.
- Honeytoken > Events: get a webhook event whenever a new honeytoken event is received.

### Payload structure

<details>
<summary>Payload for new trigger</summary>

#### Honeytoken triggered
```json
{
  "source": "GitGuardian",
  "timestamp": "2023-04-20T08:22:19.913732Z",
  "action": "honeytoken_triggered",
  "message": "This honeytoken has been triggered.",
  "target_user": null,
  "honeytoken": {
    "id": "12d14831-6b2b-4bd6-881b-53c83a09f07b",
    "name": "ht27",
    "description": "",
    "created_at": "2023-04-12T10:21:28.972903Z",
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/honeytokens/12d14831-6b2b-4bd6-881b-53c83a09f07b",
    "status": "triggered",
    "triggered_at": "2023-04-20T08:22:19.838234Z",
    "revoked_at": null,
    "open_events_count": 1,
    "type": "AWS",
    "creator_id": 397542,
    "creator_api_token_id": null,
    "revoker_id": null,
    "revoker_api_token_id": null
  }
}
```

</details>
<details>
<summary>Payload for new honeytoken event</summary>

#### New event
``` json
{
  "source": "GitGuardian",
  "timestamp": "2023-04-07T15:56:42.171075Z",
  "action": "new_honeytoken_event",
  "message": "A new honeytoken event has been received.",
  "target_user": null,
  "honeytoken_event": {
    "id": "2bdc644e-ce7e-49e8-a3a6-56fca0364a63",
    "honeytoken_id": "12d14831-6b2b-4bd6-881b-53c83a09f07b",
    "triggered_at": "2023-04-07T15:56:37Z",
    "status": "open",
    "ip_address": "54.39.187.211",
    "action": "GetCallerIdentity",
    "data": {
      "event_id": "98a080cf-a268-4a2e-b013-6259122b8a05",
      "user_agent": "python-requests/2.28.2"
    },
    "tags": []
  }
}
```

</details>
