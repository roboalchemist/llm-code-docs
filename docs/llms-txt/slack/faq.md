# Slack developer FAQ

We know there's a lot to learn and read about all the integration points of the Slack platform. Here is a little more information you might find helpful!

## General

### How do I build a bot using Slack APIs?

We have a [quickstart](/quickstart) guide that will walk you through the process!

### How do I set up a developer environment to build a Slack app?

You can provision sandbox environments by joining the [Slack Developer Program](https://api.slack.com/developer-program). Once you're ready to deploy your app, distributing the app will allow you to install it in other workspaces.

Start by [building a Slack app](/app-management/quickstart-app-settings) to contain all of your work—by default, it can only be installed on your own workspace. Follow the instructions in the UI to add features—most require that you provide a HTTP server Slack can reach.

Have more questions? Check out our [developer sandbox FAQs](/tools/developer-sandboxes#faqs)!

Are you a partner with us? The [Slack Partner Developer Program](https://api.slack.com/developer-program/partners) offers [partner sandboxes](/tools/partner-sandboxes).

### Is Slack down?

Of course we want Slack to be fully functional for users and developers at all times. Here are some tips in the unfortunate event you're having trouble and need to determine the cause of a Slack-related issue.

When possible, we report current status promptly on [status.slack.com](https://status.slack.com/) with any service disruption advisories, but you can also use the following methods:

- Use the [Slack Status API](/reference/slack-status-api).
- Send a HTTP GET request to the [`https://slack.com/api/api.test`](/reference/methods/api.test) API method. A HTTP 200 `application/json` response of `{"ok":true}` indicates at least part of the Slack [Web API](/apis/web-api/) is available.
- Send a more complex, [authenticated](/authentication) request to [`https://slack.com/api/auth.test`](/reference/methods/auth.test) using a bot, user, or legacy [token](/authentication/tokens). Using this method exercises the authorization and API layer further than `api.test` and may grant you the serenity of greater confidence in Slack availability.
- If using the legacy [Real Time Messaging (RTM) API](/legacy/legacy-rtm-api), try using [`rtm.connect`](/reference/methods/rtm.connect) to generate a WebSocket URL using a token with the proper permissions, then open the socket using a tool like [this browser-based WebSocket client for Google Chrome](https://chrome.google.com/webstore/detail/simple-websocket-client/pfdhoblngboilpfeibdedpjgfnlcodoo?hl=en).

Still unsure if Slack is down? Contact our enthusiastic [support team](https://my.slack.com/help/requests/new).

### How do I integrate a third-party service with Slack?

Check whether there is an app for a third-party service in the Slack Marketplace. If all else fails, you'll need to [code one for yourself](/quickstart).

You can also add [connector functions](/tools/deno-slack-sdk/reference/connector-functions) to your automations workflows. A growing library of third-party services are available.

### Apps vs. workflows

Building a Slack app? Start [here](/quickstart). Building a workflow? Start [here](/workflows). For more about workflows and custom workflow steps, jump to [this section](#automations-workflow-apps).

## Authentication

### How do I authenticate my requests to Slack?

#### By token

When working with Slack apps or the [Web API](/apis/web-api/), you'll often need to send access tokens, also known as bearer tokens, along with inbound requests within the authorization header. When creating an app for the first time, you'll be given your own user and bot token while going through the app creation process. In order to obtain other users' tokens, you'll need to send users through the [OAuth 2.0 authentication flow](/authentication). When you're working with Slack apps, you'll be awarded access tokens after a user approves your application.

#### By private URL

Your [incoming webhook](/messaging/sending-messages-using-incoming-webhooks) URLs are unique to your integration or application and do not require token-based authentication. [Slash command response URLs](/interactivity/implementing-slash-commands#responding_to_a_command) also already encode your integration's or application's identity.

### How do I authenticate requests from Slack to me?

Use the [signing secret](/authentication/verifying-requests-from-slack) to compute a signature, and verify that the signature on the request matches. This process is _strongly_ preferred over the use of deprecated verification tokens.

You can also use [Mutual TLS](/authentication/verifying-requests-from-slack#mutual_tls). Mutual TLS verifies the identity of Slack in a TLS-terminating server, before a request reaches your application code.

### How does Slack authenticate its requests to my servers?

When you configure [Slash commands](/interactivity/implementing-slash-commands), you specify a URL for Slack to send requests to when qualifying conditions are met. Slack also provides you a token related to that integration.

Slack sends that URL a JSON payload containing a `token` field. Compare that field to values you've received from Slack. Refer to [validating slash commands](/interactivity/implementing-slash-commands#validating_the_command) for more information.

### When do authorization codes expire?

Authorization codes must be exchanged for an access token within 10 minutes by calling the [oauth.access](/reference/methods/oauth.access) API method as part of the [authorization flow](/authentication). Otherwise, the authorization code will expire, and you'll need to ask the user to go through the OAuth flow again.

### How do I revoke a token?

Use the [`apps.uninstall`](/reference/methods/apps.uninstall) API method to uninstall an app completely, revoking all tokens. If you want to dispose of a single OAuth access token, use the [`auth.revoke`](/reference/methods/auth.revoke) API method; it works with tokens from [Sign in with Slack](/authentication/sign-in-with-slack/) as well as from [legacy](/legacy/legacy-slack-button/Add-to-Slack).

For classic apps, revoking the last token associated between your application and a workspace effectively uninstalls the app for that workspace.

Members and administrators can remove your app through their [workspace administration interface](https://my.slack.com/apps/manage).

Though it's somewhat of a nuclear option, you also have the ability to revoke all tokens from your [developer dashboard](https://api.slack.com/apps) by selecting your application and clicking **Revoke all tokens**.

### How do I reset my client secret?

To reset your client secret, go to your [developer dashboard](https://api.slack.com/apps), select the application, and click the **Change secret** button.

Don't forget to use your new secret when exchanging authorization codes for access tokens while authorizing users and workspaces with [OAuth 2.0](/authentication).

## Slash commands

### Why does Slack never reach my slash command URL?

Typically, if Slack cannot reach your slash command URL it's because it's inaccessible, does not have a valid or verifiable SSL certificate, or our request is timing out for some reason.

Slack invokes slash command URLs from its servers rather than from a Slack client app like Slack for Mac. This means that the URL we're trying to reach must be accessible to Slack's servers.

To determine whether your certificate is valid, consider using [this tool](https://www.ssllabs.com/ssltest/index.html) provided by SSL Labs.

### How do I validate a slash command's origin?

Keep track of the validation tokens and team IDs Slack gives you when commands are created and teams approve your app. Always validate that the `token` field in an incoming slash command request has been issued to you by Slack, and scope your data for that workspace.

## Incoming webhooks

### Why can't I override the channel, icon, or user name of my incoming webhook?

You won't be able to override any of these fields when using an [incoming webhook](/messaging/sending-messages-using-incoming-webhooks) attached to a Slack app. Instead, those values will be provided from your Slack app configuration and any configuration provided by the team.

## Interactive messages

### Can I use a self-signed certificate for my action URL?

No, SSL certificates must be signed by a reputable certificate authority. You may want to consider using one of the following low-cost providers:

- [Let's Encrypt](https://letsencrypt.org/)
- [CloudFlare](https://www.cloudflare.com/ssl/)

## Web API

### Can I send JSON when using HTTP POST?

Yes, the [Web API](/apis/web-api/) accepts both `application/x-www-form-urlencoded` POSTs as well as `application/json`.

Refer to [POST bodies](/apis/web-api/#post_bodies) for more information.

### How is the Web API rate limited?

Refer to our [rate limiting guide](/apis/web-api/rate-limits) for specific information on rate limits.

### How do I work with files?

Refer to our [working with files guide](/messaging/working-with-files) for specific information on working with files.

### How do I find a channel's ID if I only have its #name?

There are currently no methods to directly look up channels by name. Use the [`conversations.list`](/reference/methods/conversations.list) API method to retrieve a list of channels. The list includes each channel's `name` and `id` fields.

Many developers keep the list of channels in memory for swifter lookups. Poll the method occasionally to refresh your inventory or keep it updated with the [Events API](/apis/events-api/).

### How do I find a channel's name if I only have its ID?

You can use similar instructions to the question above, or you can use the [`conversations.info`](/reference/methods/conversations.info) API method to obtain a specific channel's information, including its `name`.

### Do channel IDs stay the same when the name of the channel changes?

Channel IDs remain the same, even when names are changed.

### Do channel IDs stay the same when moving between public and private?

As of [September 2018](https://docs.slack.dev/changelog/2018/09/01/more-reasons-to-be-a-conversations-api-convert), channel IDs remain static even when a channel is converted between public and private.

Use the [Conversations API](/apis/web-api/using-the-conversations-api) to safely work with channels that have transitioned between public and private.

### How do I retrieve a single message?

Use the [`conversations.history`](/reference/methods/conversations.history) API method and a token with the [`channels:history`](/reference/scopes/channels.history) scope to retrieve a specific message in a public channel. [Learn more about this approach](/messaging/retrieving-messages#individual_messages).

## Events API

### How do I re-enable event subscriptions for my app?

If your app's subscriptions are disabled due to exceeding the Events API [failure limits](/apis/events-api/#failure_limits), manually re-enable them by visiting your [application's settings](https://api.slack.com/apps). If your app is part of the Slack Marketplace, use your **Live App Settings** instead of your development app.

### When should I use the Events API and when should I use Socket Mode or the legacy RTM API?

Choose the [Events API](/apis/events-api/) if:

1. You want to precisely [scope](/reference/scopes) the data you receive to just what your app needs.
2. You prefer or must use an inbound request model due to one of the following:
   a) your hosting service is not able to maintain an outbound WebSocket connection, or
   b) you prefer to scale your application on an inbound request model instead of maintaining multiple long-lived WebSocket connections.
3. You're converting an [outgoing webhook](/legacy/legacy-custom-integrations/legacy-custom-integrations-outgoing-webhooks) integration into something installable as a Slack app.
4. You find the [retry behavior](/apis/events-api/#errors) reassuring for redundancy reasons.

Choose [Socket Mode](/apis/events-api/using-socket-mode) if:

1. You're building an on-premise integration or have no ability to receive external HTTP requests.
2. You're working on a distributed or mobile application without a server backend.
3. You just prefer working with WebSockets. That's cool.
4. You want data feed redundancy by opening additional WebSocket connections.
5. You want messages to be delivered to you in real time.

Finally, choose the legacy [RTM API](/legacy/legacy-rtm-api) _only_ if:

1. You have very specific needs that only the RTM API solves.
2. You already have a classic app, as they can longer be created.
3. You are okay with your app not working in the somewhat-near future, [as classic apps are slated to be deprecated.](/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation)

### How do I make my bot appear active and present?

The answer depends on whether you're using the Events API with or without the legacy RTM API:

- With the Events API, you must toggle your presence by [managing your app](https://api.slack.com/apps)'s bot user config.
- With the legacy RTM API, your bot is marked `active` while connected to a WebSocket.

Therefore, the presence of the bot depends on whether you are using the legacy RTM API (the bot is online when it's connected through the WebSocket), or it's always online when you turn this setting on. Refer to [bot presence](/apis/web-api/user-presence-and-status#bot_presence) for more information.

## Socket Mode

[Socket Mode](/apis/events-api/using-socket-mode) allows you to use the [Events API](/apis/events-api/) and [interactive features of the platform](/interactivity), without exposing a static HTTP endpoint to receive payloads. Instead, you use the WebSocket protocol and generate a URL at runtime.

The legacy [RTM API](/legacy/legacy-rtm-api) is another way of connecting your application to Slack. For most applications that can't use a static HTTP endpoint, [Socket Mode](/apis/events-api/using-socket-mode) is preferred over RTM.

## Legacy RTM API

### Can I start using the RTM API?

Most likely not. Classic apps can no longer be created, and the newer, granular permissions apps cannot access the RTM API. Try the [Events API](/apis/events-api/)!

### Can I keep using the RTM API?

You can! But not forever. [Legacy classic apps are set to be deprecated November 2026](/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation). Without those legacy apps, there will be no way to access the RTM API. Try the [Events API](/apis/events-api/) instead!

## App approvals

### How does my app get approved for the Slack Marketplace?

Refer to the following guide: [Slack Marketplace review guide](/slack-marketplace/slack-marketplace-review-guide).

### What happens if I make changes to an application that has been approved for the Slack Marketplace?

If you need to update your approved app to request new [OAuth scopes](/authentication/installing-with-oauth#asking) or to include new features, find your application's settings page at [https://api.slack.com/apps](https://api.slack.com/apps). Any changes you make here will not affect the published app.

Once you're ready to apply these changes to the published app, you'll need to [resubmit it for review](/slack-marketplace/slack-marketplace-review-guide).

### What kind of changes to my app will require being reviewed again?

If you've submitted your app to the Slack Marketplace but need to make changes to how your app or bot is described, to the integration types packed into your app, or to request additional permissions, you'll need your app to be reviewed again.

## App approvals

### How does my app get approved for the Slack Marketplace?

Refer to the following guide: [Slack Marketplace review guide](/slack-marketplace/slack-marketplace-review-guide).

### What happens if I make changes to an application that has been approved for the Slack Marketplace?

If you need to update your approved app to request new [OAuth scopes](/authentication/installing-with-oauth#asking) or to include new features, find your application's settings page at [https://api.slack.com/apps](https://api.slack.com/apps). Any changes you make here will not affect the published app.

Once you're ready to apply these changes to the published app, you'll need to [resubmit it for review](/slack-marketplace/slack-marketplace-review-guide).

### What kind of changes to my app will require being reviewed again?

If you've submitted your app to the Slack Marketplace but need to make changes to how your app or bot is described, to the integration types packed into your app, or to request additional permissions, you'll need your app to be reviewed again.