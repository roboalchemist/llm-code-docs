Source: https://docs.slack.dev/legacy/legacy-custom-integrations/legacy-custom-integrations-migration

# Legacy custom integrations: migration

If you're still reading, we suspect that you either have an existing legacy custom integration, or that you stumbled across this page looking for a general overview of what you can do with apps on Slack.

For developers with those existing legacy integrations, the old docs for each feature are still available, and we'll keep them around in case you need them.

If you're just starting out, we recommend that you learn instead about the replacement for legacy integrations - [Slack apps](/app-management/quickstart-app-settings). You'll find [a section below](#what_can_i_do) filled with tips about the right learning path to take!

If you want to learn how to move your legacy integration to a Slack app, we have some tips for you [below](#migrating_to_apps).

* * *

## What can I do with a Slack app? {#capabilities}

If you dream it, you can do it. The Slack platform offers a range of ways for users and apps to interact, all the APIs you need to read and write data from and to conversations and users, and various methods of distribution.

### Enabling interactions with users {#interactions}

Slack apps can interact with users in lots of different ways, and we leave it up to developers like you to pick the interactions most suited to their audiences.

Empower users to invoke workflows at will using [**slash commands**](/interactivity/implementing-slash-commands).

Let users do things with messages by creating custom [**message actions**](/interactivity/implementing-shortcuts).

Keep things friendly and conversational by turning your app into a [**bot**](/legacy/legacy-bot-users).

Create [**interactive messages**](/legacy/legacy-messaging/legacy-making-messages-interactive) to act as starting points for complex workflows.

### Reading and writing data {#read-write}

Once users start interacting with your Slack app, our APIs will let you retrieve the data you need from the various resources in Slack, and send data back to make updates or publish something new.

* The [Web API](/apis/web-api/) is the best way to access historical data in Slack workspaces, and make changes to them - like sending messages.

* Use the [Events API](/apis/events-api/) to get pushes about all sorts of activities in workspaces the minute they happen.

* Manage and monitor your workspaces programmatically using the [SCIM](/admins/scim-api) and [Audit Logs](/admins/audit-logs-api/).

### Choose how to share your apps {#distribution}

If you want to build an app that's just for your workspace, you can do that. If you want to build an app to share with the wide world, you can do that too.

Build a [single workspace app](/app-management/distribution) and install for your workspace with just one click.

Use [OAuth installation](/authentication) to allow your app to be distributed beyond your workspace.

Prepare your app for the [Slack Marketplace](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements) to boost distribution and discovery.

* * *

## Moving to Slack apps from Custom Integrations {#migrating_to_apps}

If you've built a legacy custom integration in the past, you'll find all of the same functionality available to use in Slack apps. The implementation of these functions has changed though, so below is a handy list of how to replace your legacy features.

### Creating a Slack app {#creating_slack_app}

[Make a new Slack app](/app-management/quickstart-app-settings) and add in any of the features you want.

Slack apps generate a new token for every user, and each user has their own set of permissions granted.

### Incoming Webhooks {#incoming-webhooks}

[Incoming Webhooks](/messaging/sending-messages-using-incoming-webhooks) are a way to post messages from apps into Slack. Creating an [Incoming Webhook](/messaging/sending-messages-using-incoming-webhooks) gives you a unique URL to which you send a JSON payload with the message text and some options.

Using [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) with Slack apps is very similar to the legacy process you're familiar with. Follow our [Getting Started guide](/messaging/sending-messages-using-incoming-webhooks#getting-started) to set up new webhooks for use with Slack apps.

### Slash Commands {#slash-commands}

[Slash Commands](/interactivity/implementing-slash-commands) let users trigger an interaction with your app directly from the message box in Slack. You can create custom commands for Slack apps quickly and easily by [following our Getting Started guide](/interactivity/implementing-slash-commands).

The process of handling and responding to those commands is almost identical compared to the legacy process you might have already built.

### Interactive bots {#bot-users}

Let users converse with your app in Slack by building bots. Our [Handling user interaction in your Slack apps guide](/interactivity/handling-user-interaction) will help you recreate any existing legacy bot functionality you might already have in a Slack app.

### Outgoing Webhooks {#outgoing-webhooks}

The [Events API](/apis/events-api/) provides a fully functional alternative for the features of Outgoing Webhooks.

More specifically, Outgoing Webhooks are used to send a notification to an app about the following activities:

1. A message was posted in a particular public channel
2. A message was posted containing specific trigger words

The [Events API](/apis/events-api/) can be used to replace this by [subscribing](/apis/events-api/#subscriptions) to the [`message.channels`](/reference/events/message.channels) event type. This will push a data payload to an app every time a message is posted to a public channel.

When an app [receives that data payload](/apis/events-api/#receiving_events), it'll be able to see both the source `channel` and the `text` of the posted message. Using `channel` will help replicate the first Outgoing Webhook feature, and looking for the trigger words in the `text` string will replicate the second.

Even better, while Outgoing Webhooks only worked for public channels, the [Events API](/apis/events-api/) can be used with [private channels](/reference/events/message.groups), [direct message conversations](/reference/events/message.im), or [multi-party direct message conversations](/reference/events/message.mpim). There are also [dozens of other event types](/apis/events-api/#event_types) available for subscription, and for your app to react to. Read the [Events API overview](/apis/events-api/) for a better idea of all the things you can use it for.

### Web API {#web-api}

The Slack Web API is an interface for querying information from and enacting change in a Slack workspace. If you were using a legacy token to make calls with the [Web API](/apis/web-api/), you'll need to generate a new one for your Slack app. Follow our [guide to the OAuth flow](/authentication/installing-with-oauth).

Because we strongly recommend you do not use legacy custom integrations anymore, you should instead use Slack apps and [their access tokens](/authentication/tokens). Our [guide to the Web API](/apis/web-api/) will walk you through the process of calling Web API methods in a Slack app.

To simplify testing and development, you can create a new app and install it in two clicks - just follow our [Quickstart guide](/app-management/quickstart-app-settings). Once it's installed, [use the app's settings](https://api.slack.com/apps) to add the permission scopes you need for your testing.
