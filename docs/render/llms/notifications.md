# Source: https://render.com/docs/notifications.md

# Email and Slack Notifications — Receive updates about important Render service events.

Render can notify you via email and/or Slack when certain events occur (such as when your service's deploy fails). You can [set workspace-level defaults](#setting-workspace-defaults) for notifications, and you can also [customize notifications](#customizing-per-service) for individual services.

> *Want to trigger custom workflows from a wide variety of platform events?*
>
> See [Webhooks](webhooks).

## Supported notifications

Render can notify you of the following events, depending on which notification level you set (*Only failure notifications* or *All notifications*):

| Event | Minimum Notification Level |
| --- | --- |
| A service build or deploy fails. | Only failure notifications |
| A Docker [image pull](/deploying-an-image) fails. | Only failure notifications |
| A [cron job](cronjobs) execution fails. | Only failure notifications |
| A [one-off job](one-off-jobs) execution fails. | Only failure notifications |
| A running service becomes unhealthy. | Only failure notifications |
| A deploy successfully goes live. | All notifications |
| An unhealthy service becomes healthy. | All notifications |

To request notification support for additional events, please [submit a feature request](https://feedback.render.com/features).

## Setting workspace defaults

From your workspace home in the [Render Dashboard](https://dashboard.render.com), click *Integrations > Notifications* in the left pane:

[image: Notifications settings in the Render Dashboard]

From here, you can configure the following:

------

###### Setting

*Notification Destination*

###### Description

Receive notifications via *Email*, *Slack*, or both. To receive via Slack, you must first [connect your Slack workspace](#connecting-to-slack).

---

###### Setting

*Default Service Notifications*

###### Description

Specifies which [supported notifications](#supported-notifications) Render sends for your services. Options include:

- *Only failure notifications.* Render sends notifications only for failures (includes failed deploys, cron jobs, and running services).
- *All notifications.* Render sends _all_ supported notifications, including for successful deploys.
- *None.* Render does not send any notifications.

---

###### Setting

*Preview Notifications*

###### Description

If *Enabled*, Render sends the same set of notifications for a [service preview](service-previews) or [preview environment](preview-environments) that it does for the preview's base service. This setting requires a *Professional* workspace or higher.

------

### Connecting to Slack

From your workspace's *Integrations > Notifications* page, click *Connect Slack* under the *Notification Destination* setting:

[image: Connecting Slack in the Render Dashboard]

Proceed through the authorization flow to connect your Slack account.

## Customizing per service

You can customize notification settings for an individual service. Doing so overrides your workspace's [default notification settings](#setting-workspace-defaults) for that service.

In the [Render Dashboard](https://dashboard.render.com), go to your service's *Settings* page and scroll down to *Notifications*:

[image: Overriding notification settings for an individual service in the Render Dashboard]

For any setting, choose a value besides *Use workspace default* to customize the service's notification behavior.

After you customize notification settings for a service, that service appears in your workspace's *Integrations > Notifications* page, under *Notification Overrides*:

[image: List of services that override notification settings in the Render Dashboard]

