# Source: https://docs.datafold.com/integrations/notifications/pagerduty.md

# PagerDuty

> Receive notifications for monitors in PagerDuty.

## Prerequisites

* PagerDuty access with permissions to manage `Services`
* A Datafold account with admin privileges

## Configure the Integration

1. In Datafold, go to Settings > Integrations > Notifications
2. Click "Add New Integration"
3. Select "PagerDuty"
4. Go to the PagerDuty console and [create a new `Service`](https://support.pagerduty.com/main/docs/services-and-integrations#create-a-service)
5. Select `Events API V2` as a service integration
6. Go to your service's `Integrations` page and copy the `Integration Key` (or [generate a new one](https://support.pagerduty.com/main/docs/services-and-integrations#generate-a-new-integration-key))
7. Return to Datafold and provide `Service Name` and `Integration Key`
8. Save the integration settings in Datafold

You're all set! When you configure a monitor in Datafold, you'll now have the option to send notifications to the PagerDuty integration you configured.

## Need help?

If you have any questions about integrating with PagerDuty, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
