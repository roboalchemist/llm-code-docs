Source: https://docs.slack.dev/changelog/2021-02-how-we-broke-your-slack-app

# How we broke your Slack app

February 24, 2021

Hello! You are here because three monumental things changed on the Slack platform today, February 24, 2021.

## What changed {#what-changed}

These deprecation and retirements are rolling out gradually on February 24, 2021. Your apps or integrations may work fine in one workspace but break in another. [Stay tuned to our Twitter account](https://twitter.com/slackapi) for live updates about the retirement.

### Retired Web API methods {#retired-web-api-methods}

We retired every [Web API](/apis/web-api/) method in the `channels.*`, `im.*`, `mpim.*`, and `groups.*` namespaces. Requests to these methods now return a `method_deprecated` error.

* Here's [everything you need to know](/changelog/2020-01-deprecating-antecedents-to-the-conversations-api).
* This is the [list of the deprecated methods and their replacements](/changelog/2020-01-deprecating-antecedents-to-the-conversations-api#methods)
* Upgrading to the [latest Slack SDKs and tools](/tools) may not be enough. You should review all your Web API method executions to verify you aren't using retired APIs like `channels.*`.

### Events API event envelope changes {#events-api-event-envelope-changes}

In the [Events API](/apis/events-api/), `authed_users` & `authed_teams` are now truncated to a single entry.

* Here's [what to consider about the Events API changes](/changelog/2020-09-15-events-api-truncate-authed-users).
* The new [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) method replaces relying on `authed_users` and `authed_teams` in the Events API.
* SDKs and tools don't use these fields by default. If you've written code that uses them directly, you'll want to investigate.
* If your app only uses bot/app subscriptions and is only installed on one workspace, you shouldn't have anything to worry about.

### Web API method authentication changes {#web-api-method-authentication-changes}

Newly created Slack apps and custom integrations may no longer send `token` as a query string parameter and must send it instead as a POST parameter or better yet, a HTTP Authorization header. Existing apps may continue doing what they already do.

* Here's [what you need to know](/changelog/2020-11-no-more-tokens-in-querystrings-for-newly-created-apps).
* If you create a new app or legacy custom integration-based bot (or hubot), you'll need to send `token` to us the preferred way.
* If you use a rare kind of blueprint-based app, newly created apps from that blueprint must also follow this rule.
* There is no impact to existing apps.

## Need help? {#need-help}

We hope this is enough information for you to help yourself should any of this have taken you by surprise.

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
