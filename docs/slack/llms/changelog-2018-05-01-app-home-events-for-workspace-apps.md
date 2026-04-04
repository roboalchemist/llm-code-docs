Source: https://docs.slack.dev/changelog/2018/05/01/app-home-events-for-workspace-apps

# App home events for workspace apps

May 1, 2018

Workspace apps are deprecated

[Learn more](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

We've added the [`message.app_home`](/reference/events/message.app_home) event for workspace apps building on our [developer preview](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021).

If you subscribe to [`message.im`](/reference/events/message.im) events to receive messages between users and your app in the special kinds of 1:1 conversations had in your _app homes_, you **must** add a subscription to `message.app_home` to continue receiving and acting on those messages.

Workspace apps grant apps a dedicated space within Slack where members can interact directly— we call it your **_App Home_**. Apps can use this space for personal notifications, onboarding information, and other helpful features.

## What's changing? {#whats-changing}

We're moving a special type of message from `message.im` into a dedicated subscription type, `message.app_home`.

### We won't dispatch App Home messages to message.im {#we-wont-dispatch-app-home-messages-to-messageim}

[`message.im`](/reference/events/message.im) subscriptions no longer deliver messages from established _app homes_ your workspace app has with users. You'll need to subscribe to `message.app_home` to receive them instead.

### We'll only deliver App Home messages to message.app_home {#well-only-deliver-app-home-messages-to-messageapp_home}

[`message.app_home`](/reference/events/message.app_home) is a new event for subscribing to just the messages in this unique conversation container.

All `message.*` event subscriptions now receive a `channel_type` string field attached to the embedded `event`. `channel` indicates a public channel, `mpim` a multiparty direct message, `group` a private channel, `im` a direct message, and `app_home` signifies these new _app home_ events.

Besides the different `channel_type` values, `message.app_home` events look exactly like the direct messages they were delivered as before and should work as a plug-in replacement for _app home_ messages delivered via `message.im`.

Here's a typical message delivered via `message.app_home`:

```json
{    "token": "one-long-verification-token",    "team_id": "T061EG9R6",    "api_app_id": "A0PNCHHK2",    "event": {        "type": "message",        "user": "U061F7AUR",        "text": "How many cats did we herd yesterday?",        "ts": "1525215129.000001",        "channel": "D0PNCRP9N",        "event_ts": "1525215129.000001",        "channel_type": "app_home"    },    "type": "event_callback",    "authed_teams": [        "T061EG9R6"    ],    "event_id": "Ev0PV52K25",    "event_time": 1525215129}
```text

## What isn't changing? {#what-isnt-changing}

`message.im` subscriptions will continue delivering direct message events from conversations between two parties your app is participating with. Only the 1:1 messages between your app and a person move to `message.app_home`.

## How do I prepare? {#how-do-i-prepare}

Visit the _Event subscriptions_ panel of your [Slack app management console](https://api.slack.com/apps) and subscribe to `message.app_home` events. Differentiate them from other message types by looking for each message `event`'s `channel_type`.

## When did this happen? {#when-did-this-happen}

We launched these changes today, May 3, 2018. [Tell us](https://slack.com/help/requests/new) how we can make your _App Home_ a better place.

## Tags:

* [Breaking change](/changelog/tags/breaking-change)
* [Announcement](/changelog/tags/announcement)
