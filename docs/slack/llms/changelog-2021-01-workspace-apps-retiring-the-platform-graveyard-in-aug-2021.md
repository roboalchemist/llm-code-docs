Source: https://docs.slack.dev/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021

# Goodbye, workspace apps

January 30, 2021

On **August 24, 2021, legacy workspace apps** were retired. Workspace apps were part of a brief developer preview we elected to not fully release. Since October 2018, existing workspace apps have remained functional but on August 24, 2021 workspace apps will be retired and no longer function.

Please read on if you were the developer, maintainer, administrator, or user of a vintage workspace app.

Don't know if you have a workspace app? Make sure you're signed in to all your workspaces and visit our [**deprecation center**](https://api.slack.com/apps). Each workspace app you own or collaborate on will be listed.

## What changed {#changed}

Workspace apps are actually a kind of Slack app that use _workspace tokens_ instead of bot tokens to represent and assert the identity of the app itself. ([Learn more about the different token types](/authentication/tokens).)

* When workspace apps retire, workspace tokens will become non-functional.
* All API calls using a workspace token will fail with `invalid_auth` and a message stating the token type is retired.
* All API methods used solely by workspace app tokens will fail with a `method_deprecated` error, though your app won't see it because the workspace token you'd use to call it will already fail for the reasons above.
* Apps using workspace apps token rotation will no longer be able to rotate those tokens, as their refresh tokens and the entire workspace apps refresh token system will be shut down until the Slack app replacement is released in Summer 2021.

### Deprecated methods {#methods}

These methods were all used as part of the workspace apps permissions API. There are no direct equivalents in Slack apps.

To determine which scopes a token has with a Slack app, note the `x-oauth-scopes` HTTP header included in the response to each Web API method, such as [`auth.test`](/reference/methods/auth.test).

* `apps.permissions.resources.list`
* `apps.permissions.scopes.list`
* `apps.permissions.users.list`
* `apps.permissions.users.request`
* `apps.permissions.info`
* `apps.permissions.request`

### Deprecated events {#events}

Workspace apps' progressive permissions system emitted these events. There are no direct equivalents in Slack apps.

* `resources_added`
* `resources_removed`
* `scope_denied`
* `scope_granted`

## How to respond or prepare {#prepare}

If you started developing Slack apps _after_ October 2018, then it's unlikely you have a workspace app and you need do nothing to prepare.

Don't know if you have a workspace app? Make sure you're signed in to all your workspaces and visit our [**deprecation center**](https://api.slack.com/apps). Each workspace app you own or collaborate on will be listed.

If you know you have a workspace app and it's installed on a single workspace or just a small number of workspaces, we recommend you manually migrate your app to a Slack app.

For single workspace apps, your migration path will mostly be limited to:

1. Noting the channels your app is in today
2. [Create a Slack app](https://api.slack.com/apps?new_app=1)
3. Select the equivalent scopes your app needs to perform its activities
4. Install your app and store the bot token
5. Invite your app to the channels you originally noted
6. Use the bot token instead of the workspace app token for requests to the Web API

For _larger_ installations, we plan to offer migration services in Summer 2021.

### How to achieve workspace apps goals with Slack apps {#goals}

Here is how to accomplish common workspace apps goals in Slack apps:

> I want to install apps on the "workspace level" and not have apps uninstalled when an installer leaves a workspace

Slack apps take care of this through each app's "bot user token," which will persist as long as the app is installed in the workspace, regardless of the installer's membership. Slack apps may also be [installed _organization-wide_](/enterprise/organization-ready-apps).

> I want users to choose which channels my app is installed in

Slack apps give users this choice through the familiar conversation invite flows built in to Slack. Additionally, bot users may ask for the [`channels:manage`](/reference/scopes/channels.manage) and [`chat:write.public`](/reference/scopes/chat.write.public) permissions to self-manage public channel membership and conversational abilities.

> I want a bot user token with granular permissions capable of taking action across a whole workspace

Slack apps are built with [a granular permission model](/authentication) for bot user tokens applied at the workspace level. Map the permissions you use in workspace apps to those available for bot users and you'll find most capabilities carry over to similarly-named scopes.

> I want app home conversations with the installing user

Slack apps offer [a richer App Home experience](/surfaces/app-home) including a [rich Block Kit canvas](/block-kit) and access to a direct message conversation with each user in a workspace.

> I want to ask for permissions progressively

While there's no conversational UI flow to request elevated permissions, Slack apps can still progressively request permissions by sending users through installation flows multiple times.

> I want to limit the resources apps may access

The bot user component of Slack apps is largely governed by a combination of channel membership and granular permissions. While an app isn't granted to specific resources like channels and users, the type of data a bot token can access can be further narrowed by asking only for a restrictive set of scopes.

> I want to rotate my access tokens programmatically

Slack apps can't do this yet. We plan to offer token rotation for Slack apps in Summer 2021.

> I want to run my app securely behind the firewall

Workspace apps couldn't do this but Slack apps can -- with [Socket Mode](/apis/events-api/using-socket-mode)!

### Complications with private channel membership {#private}

One of the largest issues to consider during migration is transferring channel membership for private channels.

The only users who may invite a bot user into a private channel are the members of that channel.

As you migrate to a Slack app, you'll have to inform users of your existing workspace app that they'll need to invite your new app's bot user to each private channel they want your app to serve in.

## What happens if I do nothing? {#happens}

If you have a workspace app and do nothing, the app will stop working. API calls it makes will not succeed. Eventually, your app's membership in channels will disappear. Finally, your app's official record in our database and access in application management will be completely removed.

## When is this happening? {#when}

We completed the retirement on **August 24, 2021**.

Slack apps are ready for you to migrate to today.

### Timeline {#timeline}

Here's a timeline detailing the various announcements we've made about the life & death of workspace apps over the years.

* August 2017 - We opened the workspace apps developer preview for testing and exploration.
* October 2018 - We announced that the workspace apps developer preview had ended and that existing apps would have until October 2019 to migrate away from the discontinued app type.
* March 2021 - We're using this changelog to announce a firm timeline for the complete retirement of workspace apps.
* **Summer 2021** - Slack will have detailed plans for assisting large workspace apps installations in migrating to Slack apps at scale.
* **Summer 2021** - Slack will release a new implementation of "token rotation" for app-level, user, and bot tokens in Slack apps.
* **August 24, 2021** - Workspace apps will be completely retired.

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
