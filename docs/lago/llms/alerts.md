# Source: https://getlago.com/docs/guide/alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerts

> Alerts allow you to monitor your subscriptions' usage and billing by firing notifications when certain conditions are met.

## Overview

Usage alerts are essential for effectively monitoring customer activity and managing billing. They help ensure that customers stay within their usage limits and prevent unexpected charges. Below are some key use cases where alerts can be beneficial:

1. Allow customers to set and manage their own usage limits and budgets, empowering them to control their consumption;
2. Alert customers with sky-rocketing usage to prevent unexpected costs or overages on their bills; or
3. Implement entitlement logic to halt usage tracking when a customer reaches their predefined limit, ensuring accurate billing and compliance.

## Create an alert

<Tabs>
  <Tab title="Dashboard">
    An alert must be tied to a specific subscription. To create an alert for a particular subscription, follow these steps:

    1. Access the specific subscription view;
    2. Click on the **Alerts** tab;
    3. Click on the **Add an alert** button;
    4. Select the type of alert (e.g., Lifetime Usage Amount);
    5. Set the progressive thresholds and code for the alert;
    6. Define the optional recurring threshold for the alert; and
    7. Click on the **"Create alert"** button to confirm.

    <Info>
      The alert threshold `code` helps distinguish between different types of alert notifications. For example, some notifications may indicate a `soft` limit, while others may trigger a `hard` limit, each with different levels of urgency or action required.
    </Info>

    <Frame caption="Create an alert">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/create-alerts.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=3a8b084fe9890415661ac49eab3fc022" data-og-width="2366" width="2366" data-og-height="1944" height="1944" data-path="guide/images/create-alerts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/create-alerts.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=c9690ddf2baff17f90317fb5ae76476c 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/create-alerts.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=94d649bfb3d26ad51a6379dc44bd0ac5 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/create-alerts.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=50c6d33b197ccc8395c379c59bf8ee1d 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/create-alerts.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=3f3ecdbbaa59d19a9089540741bc50c3 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/create-alerts.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=530cb8014e64b6cd66e77ead2e1b6512 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/create-alerts.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=612eaf0dd3f0f5be8a78a31a16c2d03c 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Lifetime usage amount alert creation theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request POST "$LAGO_URL/api/v1/subscriptions/:external_id/alerts" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
              "alert": {
                  "alert_type": "lifetime_usage_amount",
                  "code": "lifetime_usage_alerts",
                  "name": "Lifetime Usage Alerts",
                  "thresholds": [
                      {
                          "code": "soft",
                          "value": "1000.0",
                          "recurring": false
                      },
                      {
                          "code": "soft",
                          "value": "2000.0",
                          "recurring": false
                      },
                      {
                          "code": "hard",
                          "value": "15000.0",
                          "recurring": false
                      }
                  ],
                  "billable_metric": null
              }
          }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Alert types

Lago supports the following alert types:

* **Lifetime Usage Amount**: Triggered when a subscription's lifetime usage exceeds predefined thresholds.
* **Current Usage Amount**: Triggered when a subscription's usage exceeds predefined thresholds for the current billing period.
* **Billable Metric Current Usage Amount**: Triggered when the usage of a specific billable metric exceeds predefined thresholds for the current billing period.
* **Billable Metric Current Usage Units**: Triggered when the usage of a specific billable metric units exceeds predefined thresholds for the current billing period.

## Alert notifications

After configuring an alert and starting to ingest usage, you can listen for the `alert.triggered` webhook message. These webhooks serve as notifications sent to your system, indicating when an alert threshold has been crossed, along with all the relevant alert details.

```json  theme={"dark"}
{
  "webhook_type": "alert.triggered",
  "object_type": "triggered_alert",
  "triggered_alert": {
    "lago_id": "ff604dc4-2223-412a-a8f4-8fde7dfd3346",
    "lago_alert_id": "98d00d14-dc17-40c8-81c2-701b7cdbb038",
    "lago_subscription_id": "0705ad6b-c063-421a-87b6-a6c25f98c842",
    "billable_metric_code": null,
    "alert_name": "Total Usage Alerts",
    "alert_code": "total_usage",
    "alert_type": "usage_amount",
    "current_value": "100.0",
    "previous_value": "0.0",
    "crossed_thresholds": [
      {
        "code": "hard_limit",
        "value": "100.0",
        "recurring": false
      }
    ],
    "triggered_at": "2025-05-27T19:25:02Z"
  }
}
```

## Limitations

Please consider the following limitations for usage alerts:

* Alerts only evaluate usage data reported after their creation;
* Alerts run on a default 5-minute interval clock. Contact the team if you need a different frequency; and
* Identical alerts cannot be created more than once.
