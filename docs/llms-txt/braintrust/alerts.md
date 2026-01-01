# Source: https://braintrust.dev/docs/guides/automations/alerts.md

# Alerts

Alerts let you trigger an action when conditions are met on new logs in Braintrust. You can trigger an action to a webhook URL or to a Slack channel via Braintrust's Slack integration.

<Note>
  If you are on a hybrid deployment, alerts are available starting with `v0.0.72`. The Slack integration is available starting with `v1.1.29`.
</Note>

## Create an alert

<Note>
  Enable the Slack integration in **Settings** > **Integrations** before creating an alert to send to a Slack channel.
</Note>

1. Go to **Configuration > Alerts**.
2. Enter a name for your alert.
3. Optionally, enter a BTQL filter clause. If included, the alert will trigger when a logged event matches the filter.
4. Select the interval for how frequently the alert should check for matching events
5. Select the action to take when the alert is triggered. For webhooks, enter the Webhook URL in the **Webhook URL** field. For Slack, enter the Slack channel ID in the **Slack channel** field. To find the channel ID in Slack, right-click the channel and select **View channel details**.

## Webhook payload

When a webhook alert is triggered, it sends a `JSON` payload to your webhook URL with the following structure:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "organization": {
    "id": "org_123",
    "name": "your-organization"
  },
  "project": {
    "id": "proj_456",
    "name": "your-project"
  },
  "automation": {
    "id": "c5b32408-8568-4bff-9299-8cdd56979b67",
    "name": "High-Priority Factuality",
    "description": "Alert on factuality scores for logs with priority 0 in metadata",
    "event_type": "logs",
    "btql_filter": "metadata.priority = 0 AND scores.Factuality < 0.9",
    "interval_seconds": 3600,
    "url": "https://braintrust.dev/app/your-organization/p/your-project/configuration/alerts?aid=c5b32408-8568-4bff-9299-8cdd56979b67"
  },
  "details": {
    "is_test": false,
    "message": "High-Priority Factuality: 5 logs triggered alert in the last 1 hour",
    "time_start": "2025-05-12T10:00:00.000Z",
    "time_end": "2025-05-12T11:00:00.000Z",
    "count": 5,
    "related_logs_url": "https://braintrust.dev/app/your-organization/p/your-project/logs?search=..."
  }
}
```

## Test alerts

Before saving or updating an alert, you can test it to confirm behavior with the **Test alert** button. Braintrust will trigger the alert as if the initiating event occurred, running it through the BTQL filter on recent data. If matching logs are found, a test payload will be sent to your webhook URL.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=a433406ea1228135bc94168b951ab130" alt="Test webhook alert" data-og-width="1394" width="1394" data-og-height="1036" height="1036" data-path="guides/automations/test-alert.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=9f6fb39ffbb5c17e9862cdcf703fb3ce 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=684d00bc4aed2cb2808d519830d58c0d 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=6f539b5c4ecc3ed01fcb077aed2f113d 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=6721feaec318cd1126973af386d97814 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=9bb0381d2b68d77ebe2559f8c2f04bfd 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=9787dff556f1e458a9fb96381c8f5b8e 2500w" />

If no matching logs are found, you may need to adjust your BTQL filter or the alert interval.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert-failed.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=b94c45083bb590b758316da67c1ff82e" alt="Test webhook alert failed" data-og-width="1394" width="1394" data-og-height="1036" height="1036" data-path="guides/automations/test-alert-failed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert-failed.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=302e9f3bb73c53be5619ba7f1f303889 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert-failed.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=67b2bc263a19d901b4e88a71a6ca28fb 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert-failed.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=f7b09c6f9c2f4b34bd6e5eed65da7828 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert-failed.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=7aabf054aa7dc997ad56ecd986e7d1f9 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert-failed.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=3a6ecdeb5840aff5eb04d17a83161d6b 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/test-alert-failed.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=f46ec748ee2e4336166b1cb92d45932e 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt