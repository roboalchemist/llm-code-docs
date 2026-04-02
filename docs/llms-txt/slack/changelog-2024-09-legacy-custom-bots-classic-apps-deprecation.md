Source: https://docs.slack.dev/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation

# Discontinuing support for legacy custom bots and classic apps

September 30, 2024

We want to let you know about some upcoming changes to support for legacy custom bots and classic apps on the Slack platform.

* Beginning **March 31, 2025**, we will discontinue support for legacy custom bots. For your integrations to continue working, you must create brand new Slack apps.
* In **September 2025** **March 2026** **May 2026** **November 2026**, we will discontinue support for classic apps. For your apps to continue working, you will need to [migrate them to Slack apps](/legacy/legacy-app-migration/migrating-classic-apps). Any custom bots or classic apps you have built will no longer work after these dates.

Classic apps deprecation has been paused

We have paused any changes relating to classic apps at this time. Classic apps will continue to work, but we recommend migrating them to Slack apps to take advantage of their benefits.

It has been over 10 years since we originally launched the Slack Platform. As we [mentioned back in April 2024](/changelog/2024-04-discontinuing-new-creation-of-classic-slack-apps-and-custom-bots), there are just too many ways to create an app, so we're doing our best to streamline this process.

## What's changing {#what}

Beginning **March 31, 2025**, legacy custom bots will no longer function. API calls made by legacy custom bots will be rejected.

Beginning **November 16, 2026**, classic apps will no longer function. API calls made by a classic apps will be rejected. Classic apps will no longer receive [Events API](/apis/events-api/) events.

## How do I prepare? {#prepare}

### How do I tell if my app will be impacted? {#how-do-i-tell}

If you are a developer:

* Legacy custom bots installed on your workspace are listed [here](https://my.slack.com/slack-marketplace/A0F7YS25R-bots), under 'Configuration'.
* Classic apps that you are a collaborator for are listed [here](https://api.slack.com/apps). Any app listed as "Classic" here will be impacted.

If you are an admin:

* You can view a list of impacted apps by heading to your workspace or org's settings page, and then clicking on the "Deprecations" tab.

### Legacy custom bots {#legacy-custom-bots}

* If you have a legacy custom bot and want to keep keep that functionality working, you’ll need to create a new [Slack app](/quickstart) to replace it.
* By default, Slack apps are only available internally within the workspace they were created, just like legacy custom bots.
* If you want to use a Slack app on only one workspace, as how legacy custom bots work, you do not need to implement OAuth. Click [**Install to Workspace**](/quickstart#installing) to obtain a bot token, replace the token in your app’s code with this token, and then you'll be good to go.

Slack apps do not support the [legacy RTM API](/legacy/legacy-rtm-api). If your legacy custom bot was using the legacy RTM API, you will need to configure it to use the [Events API](/apis/events-api/) instead.

* In most cases, any events you received via the RTM API will also available via the Events API. Refer to detailed instructions [here](/legacy/legacy-app-migration/migrating-classic-apps#faq_permissions_rtm_support), and [event types](/reference/events) for a list of supported event types.
* The Events API supports both HTTP and [WebSocket connections](/apis/events-api/using-socket-mode). If you prefer to use the same configuration as the legacy RTM API, you can enable socket mode. In that case, you’ll follow the same pattern as with the legacy RTM API (i.e., call the [`apps.connections.open`](/reference/methods/apps.connections.open) API method to get a URL, open a WebSocket to that URL, and then listen for events).

If you own a legacy custom bot and do nothing, it will stop functioning. API calls made from the app will be rejected. Eventually, your app will be removed from channels, your tokens will be revoked, and your access to its configuration pages will be removed.

### Classic apps {#classic-apps}

Classic apps are not impacted at this time and will continue to work. However, these are considered to be legacy and it is recommended to migrate them to Slack apps.

* To migrate your classic app, follow [these instructions](/legacy/legacy-app-migration/migrating-classic-apps). You can do this from your app’s configuration page within the **Update to Granular Scopes** section.
* The core difference between classic apps and Slack apps is the more granular set of scopes.
* If your app is distributed to other teams using OAuth, you will need to make code changes to support the new [OAuth flow](/authentication/installing-with-oauth). If your app is only used internally, you don’t need to implement OAuth.

## Timeline {#timeline}

* **November 16, 2026**: We will discontinue support for classic apps
* **March 31, 2025**: We will discontinue support for legacy custom bots
* **June 2024**: We blocked creation of new legacy apps and classic apps
* **May 27th, 2022**: We made it a requirement for apps in the Slack Marketplace to use granular permissions
* **December 2020**: We no longer accepted new submissions for classic apps in the Slack Marketplace
* **October 2019**: We launched Slack apps to replace both legacy apps and classic apps
* **November 2015**: We launched classic apps with OAuth scopes

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
