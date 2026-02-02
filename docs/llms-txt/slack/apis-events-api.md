# The Events API

The Events API is a streamlined way to build apps and bots that respond to activities in Slack. When you use the Events API, _Slack_ calls _you_.

You have two options: you can either use [Socket Mode](/apis/events-api/using-socket-mode) or you can designate a public [HTTP endpoint](/apis/events-api/using-http-request-urls) that your app listens on, choose what events to subscribe to, and _voilà_: Slack sends the appropriate events to you. Learn more about the differences between Socket Mode and HTTP [here](/apis/events-api/comparing-http-socket-mode).

All you need is a Slack app and a secure place for us to send your [events](/reference/events). With the Events API, you can do the following:

- Tell Slack where to send your [event types](/reference/events) and we'll deliver them with grace, security, and respect. We'll even retry when things don't work out. The [event types](/reference/events) sent to you are directly tied to the [OAuth permission scopes](/authentication/installing-with-oauth) awarded as users install your Slack app.
- Subscribe to only the [event types](/reference/events) you want; don't worry about the ones you don't need.
- Subscribe your Slack apps to events related to channels and direct messages they are party to. Build bots without a bothersome bevy of [Real Time Messaging (RTM) API](/legacy/legacy-rtm-api) WebSockets.

## Overview

Many apps built using the Events API will follow the same abstract event-driven sequence:

1. A user creates a circumstance that triggers an event subscription to your application.
2. Your server receives a payload of JSON describing that event.
3. Your server acknowledges receipt of the event.
4. Your business logic decides what to do about that event.
5. Your server carries out that decision.

If your app is a bot listening to messages with specific trigger phrases, that event loop may play out something like the following:

1. Members send messages in a channel the bot belongs to—the #random channel. The messages are about lots of things, but some of them contain today's secret word.
2. Your server receives a [`message.channels`](/reference/events/message.channels) event, as per its bot subscription and membership in the #random channel.
3. Your server responds with a swift and confident HTTP 200 OK.
4. Your bot is trained to listen for today's secret word, and having found it, decides to send a message to the channel, encouraging everyone to keep that word secret.
5. Your server uses [`chat.postMessage`](/reference/methods/chat.postMessage) from the Web API to post that message to #random.

Using the Web API with the Events API empowers your app or bot to do much more than just listen and reply to messages.

Let's get started!

---

## Preparing your app to use the Events API

The Events API is recommended over the [RTM API](/legacy/legacy-rtm-api) for most use cases. If you're already familiar with HTTP and are comfortable maintaining your own server, handling the request and response cycle of the Events API should be familiar. If the world of web APIs is new to you, the Events API is a great next step after mastering [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) or the [Web API](/apis/web-api/).

### Is the Events API right for your app?

Before starting, you may want to make a few early decisions about your application architecture and approach to consuming events. The Events API is best used in conjunction with other platform features.

One way to use the Events API is as an alternative to opening WebSocket connections to the [RTM API](/legacy/legacy-rtm-api). Why choose the Events API over the legacy RTM API? Instead of maintaining one or more long-lived connections for each workspace an application is connected to, you can set up one or more endpoints on your own servers to receive events atomically in near real-time.

Some developers may want to use the Events API as a kind of redundancy for their existing WebSocket connections. Other developers will use the Events API to receive information around the workspaces and users they are acting on behalf, to improve their [slash commands](/interactivity/implementing-slash-commands), bot users, [notifications](/messaging), or other capabilities. With [app events](#app_events), you can track app uninstallation, token revocation, Enterprise org migration, and more. Handle anything else your app does by using [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) and other write-based [web API methods](/reference/methods).

### Permission model

The Events API leverages Slack's existing [object-driven OAuth scope system](/authentication/installing-with-oauth) to control access to events. For example, if your app has access to files through the `files:read` scope, you can choose to subscribe to any or none of the file-related events such as [`file_created`](/reference/events/file_created) and [`file_deleted`](/reference/events/file_deleted).

You will only receive events that users who have authorized your app can "see" on their workspace (that is, if a user authorizes access to private channel history, you'll only see the activity in private channels they are a member of, not all private channels across the workspace).

[Bot users](/authentication/tokens#bot) may also subscribe to events on their own behalf. The `bot` scope requested when workspaces install your bot covers events access for both the Events API and the [Real Time Messaging API](/legacy/legacy-rtm-api).

## Subscribing to event types

To begin working with the Events API, you'll need to create a Slack app if you haven't already. While managing your application, find the **Event Subscriptions** setting and use the toggle to turn it on.

![The on switch for the Events API](/assets/images/event_subscriptions-f8d89f09c291f496bcf5646213f50c8a.png)

After a little more configuration, you'll be able to select all the [event types](/reference/events) you want to subscribe to.

Before continuing on to choosing event subscriptions, you will need to choose to use either Socket Mode or an HTTP request URL. For more information on the differences between them, refer to [Exploring HTTP vs Socket Mode](/apis/events-api/comparing-http-socket-mode).

To set up your app to use Socket Mode, refer to the [Socket Mode](/apis/events-api/using-socket-mode) guide. To set up your app to use HTTP request URLs, refer to the [HTTP](/apis/events-api/using-http-request-urls) guide.

### Choosing event subscriptions

After configuring and validating either Socket Mode or your request URL, it's time to subscribe to the [event types](/reference/events) you find fascinating, useful, or necessary.

![The event subscription configuration process](/assets/images/event_subscriptions-f8d89f09c291f496bcf5646213f50c8a.png)

The subscription manager is split into two sections:

- Team Events: these are the events that require a corresponding OAuth scope, and are perspectival to a member installing your application.
- Bot Events: subscribe to events on behalf of your application's [bot user](/authentication/tokens#bot), no additional scopes beyond `bot` required. As with workspace events, you'll only receive events perspectival to your bot user.

Some event types are not available in bot user subscriptions.

### Activating subscriptions

The Events API is backed by the same [OAuth permission scoping system](/authentication/installing-with-oauth) powering your Slack app.

If workspaces have already installed your application, your request URL will soon begin receiving your configured event subscriptions.

For any workspaces that have yet to install your application, you'll need to request the specific OAuth scopes corresponding to the [event types](/reference/events) you're subscribing to. If you're working on behalf of a [bot user](/authentication/tokens#bot), you'll need your bot installed the typical way, using the `bot` OAuth scope.

Authorize users for your Event Consumer app through the standard [OAuth flow](/authentication). Be sure to include all of the necessary scopes for the events your app wants to receive. Consult our index of the [available event types with corresponding OAuth scopes](/reference/events).

With all this due preparation out of the way, it's time to receive and handle all those event subscriptions.

## Receiving events

Your Request URL will receive a request for each event matching your subscriptions. One request, one event.

You may want to consider the number of workspaces you serve, the number of users on those workspaces, their volume of messages, and other activity to evaluate how many requests your Request URL may receive and scale accordingly.

### Events dispatched as JSON

When an event in your subscription occurs in an authorized user's account, we'll send an HTTP POST request to your Request URL. The event will be in the `Content-Type: application/json` format:

```json
{
    "type": "event_callback",
    "token": "XXYYZZ",
    "team_id": "T123ABC456",
    "api_app_id": "A123ABC456",
    "event": {
        "type": "name_of_event",
        "event_ts": "1234567890.123456",
        "user": "U123ABC456",
        ...
    },
    "event_context": "EC123ABC456",
    "event_id": "Ev123ABC456",
    "event_id": "Ev123ABC456"
}