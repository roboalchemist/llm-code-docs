Source: https://docs.slack.dev/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps

# Differences between classic apps and granular Slack apps

This quickstart guide explains how Slack apps differ from [classic apps](/legacy/legacy-bot-users).

If you'd like to learn from the ground up, start with our [installation guide for Slack apps](/app-management/quickstart-app-settings). Otherwise, read on.

* * *

## Getting started {#overview}

You can create a Slack app with the click of a button. This button, specifically:

[Create an app](https://api.slack.com/apps?new_app=1)

With a created app, you can now follow along.

* * *

## Configuring your app {#configuring}

Slack apps use **bot users** as the basis for API calls. You'll notice some resulting changes while developing your app.

First things first: select the **OAuth & Permissions** sidebar in your [app management page](https://api.slack.com/apps). You'll see some changes:

* You can now select individual scopes for your bot token, rather than just one umbrella [`bot`](/reference/scopes/bot) scope that grants access to many methods, some of which you may not need.
* If you select a scope under the `Bot Token Scopes` selector, and then click to install your app, you'll automatically gain a **Bot User OAuth Access Token**, with no corresponding user tokens.

## Always assign scopes to your bot user token, rather than a user token. User token scopes should be selected only for user impersonation.

New bot user API access tokens **may not access** [RTM](/legacy/legacy-rtm-api). For most apps, the [Events API](/apis/events-api/) lets your app listen to Slack goings-on in a more structured, safe way. If you require access to RTM (say, because you're building your app behind a corporate firewall), continue to use a classic app bot token to call [`rtm.connect`](/reference/methods/rtm.connect).

* * *

## Installing your app {#installing}

When you want to install your Slack app on other workspaces using [OAuth](/authentication/installing-with-oauth), your app should redirect users to a new OAuth `v2/authorize` URL: `slack.com/oauth/v2/authorize`.

Once the user checks out the scopes you've requested and okays them, the user is redirected back to your app along with a temporary access code. Exchange the code for an API access token by calling a new OAuth `v2.access` method: [`oauth.v2.access`](/reference/methods/oauth.v2.access).

[Dive deeper into the new OAuth flow with this in-depth guide](/authentication/installing-with-oauth).

Here's the response you'll see from the `v2.access` method:

```json
{    "ok": true,    "access_token": "xoxb-123abc...",    "token_type": "bot",    "scope": "commands,incoming-webhook",    "bot_user_id": "U123ABC456",    "app_id": "A123ABC456",    "team": {        "name": "Slack Softball Team",        "id": "T123ABC456"    },    "enterprise": {        "name": "slack-sports",        "id": "E123ABC456"    },    "authed_user": {        "id": "U222ABC222",        "scope": "chat:write",        "access_token": "xoxp-123abc...",        "token_type": "user"    }}
```text

Here are a few important things to note:

* The response from `oauth.v2.access` has a slightly different shape than from the [previous, non-V2 endpoint](/reference/methods/oauth.access). That's because we now present the bot user access token at the top level, not the user token. Check out the [method documentation page](/reference/methods/oauth.v2.access) for more detail.
* Once you initiate OAuth with the new OAuth `v2/authorize` URL, you have to complete it with the new `v2.access` method—you can't combine the `v2/authorize` URL with the old V1 `access` method.

* * *

## Making API calls {#calling}

Unlike tokens imbued with the old [`bot`](/reference/scopes/bot) scope, your new API access token requests **granular [scopes](/reference/scopes) for each method it wishes to call**.

The granular scopes work exactly like the scopes applied to the old user token. However, your new API access token is a bot token, and as such it isn't tied to a specific user.

One effect worth noting: [`chat.postMessage`](/reference/methods/chat.postMessage) and other `chat.*` methods no longer mess around with the `as_user` parameter. You're granted a single [`chat:write`](/reference/scopes/chat.write) scope (no `:user` or `:bot` is appended). If you call the `chat.postMessage` method with your bot token, you post as the bot. If you've obtained a user token through the new install flow, and you call the method with your user token, you post as the user.

New bot user API access tokens **may not access** [RTM](/legacy/legacy-rtm-api). For most apps, the [Events API](/apis/events-api/) lets your app listen to Slack goings-on in a more structured, safe way. If you require access to RTM (say, because you're building your app behind a corporate firewall), continue to use a classic app bot token to call [`rtm.connect`](/reference/methods/rtm.connect).

* * *

## Receiving events {#receiving}

Your app receives only the [events](/apis/events-api/) it has scopes to listen for. For example, subscribing to the [`channel_created`](/reference/events/channel_created) event automatically means that your app requests the [`channels:read`](/reference/scopes/channels.read) scope.

* * *

## Using Slash commands {#commands}

**New**: Bot users in Slack apps may request the [`commands`](/reference/scopes/commands) scope, allowing them to implement [Slash commands](/interactivity/implementing-slash-commands).

Similar to the way that user deactivation for an installing user could deactivate a Slash command with older Slack apps, revoking the bot user token may cause the Slash command to be removed from a workspace.

* * *

## Using Incoming Webhooks {#webhooks}

**New**: Bot users in Slack apps may request the [`incoming-webhook`](/reference/scopes/incoming-webhook) scope, allowing them to post messages via [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks).

Similar to the way that user deactivation for an installing user could deactivate a webhook with older Slack apps, revoking the bot user token may cause the webhook to be removed from a workspace.

* * *

## Using channels:join and channels:manage {#channels}

Request the [`channels:join`](/reference/scopes/channels.join) scope to allow your app to join public channels.

Request the [`channels:manage`](/reference/scopes/channels.manage) scope to allow your app to create new channels and manage the ones it's already part of.

* * *

## Deprecating perspectival scopes {#perspective}

Scopes that indicate a "perspective" by appending either `:user` or `:bot` are deprecated. Slack apps nearly always act on their own behalf, rather than doing actions in the name of a human user.

Specifically, the [`chat:write`](/reference/scopes/chat.write) scope replaces the `chat:write:user` scope and `chat:write:bot`, and the [`files:write`](/reference/scopes/files.write) scope replaces the `files:write:user` scope.

Perspectival scopes are deprecated for all bot and user tokens created through the new OAuth flow. This means the `as_user` field for the [`chat.postMessage`](/reference/methods/chat.postMessage) method is also no longer necessary for Slack apps.

* * *

## Link unfurling {#unfurling}

You can request the [`links:read`](/reference/scopes/links.read) and [`links:write`](/reference/scopes/links.write) scopes so that your app can handle unfurls.

A link shared in a channel will only be unfurled if the token with `links:write` has access to the message that contains the link. For example, if you have a Slack app and an installing user shares a link to a private channel, but the Slack app is not in that private channel, that link will not unfurl.

* * *

## Miscellaneous {#misc}

### Effects of user deactivation on tokens {#deactivation}

Here's one big step forward for bots in Slack apps: **deactivation of an installing user no longer has an effect on the app**.

### Posting in public channels and customizing message authorship {#public}

Slack apps **do not** begin life with the ability to post to any public channel without joining, as [classic bots did](/reference/scopes/bot). Nor do they start with the ability to adjust username or icon when posting messages.

Good news: with two special scopes, you can gain those abilities by asking for them explicitly. Request the [`chat:write.public`](/reference/scopes/chat.write.public) scope and [`chat:write.customize`](/reference/scopes/chat.write.customize) scope, respectively, to gain the ability post in all public channels and adjust your app's message authorship.

Check out the [`chat.postMessage` documentation](/reference/methods/chat.postMessage#authorship) for more details.

### Revoking tokens {#revoking}

For a Slack app, bot user API access tokens are still revoked in the same way, via the [`auth.revoke`](/reference/methods/auth.revoke) method. When that happens:

* The bot token no longer works.
* The bot user is removed from the workspace.
* Slash commands associated with the bot token will be removed from the workspace if no user tokens for the same app exist and carry the `commands` scope.
* Incoming webhooks that were installed and associated with the bot token will be removed.
* If no user tokens for the same app exist, the app will appear to be uninstalled from the workspace.

### Migration {#migration}

In November 2026, we will discontinue support for classic apps

For your apps to continue working, you will need to migrate them to Slack apps.

Any custom bots or classic apps you have built will no longer work after these dates. Refer to [this changelog article](/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation) for more details.

Check out our [guide](/legacy/legacy-app-migration/migrating-classic-apps) to migrating your classic app to a Slack app.
