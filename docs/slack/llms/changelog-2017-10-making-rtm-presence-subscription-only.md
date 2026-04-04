Source: https://docs.slack.dev/changelog/2017-10-making-rtm-presence-subscription-only

# Making RTM presence subscription only

October 1, 2017

RTM API Presence is now only available via subscription.

As of January 2018, [`presence_change`](/reference/events/presence_change) events are not dispatched without [_presence subscriptions_](/apis/web-api/user-presence-and-status) established with [`presence_sub`](/reference/events/presence_sub). Relatedly, current user presence status is no longer communicated in [`rtm.start`](/reference/methods/rtm.start). [Learn more](/changelog/2018-01-presence-present-and-future).

**Beginning November 15, 2017, the RTM API's [`presence_sub`](/reference/events/presence_change) event will be available via presence subscription only.**

[Back in June](/changelog/2017-06-batch-presence-and-presence-subscriptions), we introduced new ways to track user presence and the [`presence_change`](/reference/events/presence_change) event in the [RTM API](/legacy/legacy-rtm-api).

Dispatching presence events for all users in a workspace is an expensive operation for Slack. A flood of presence events from large workspaces can also disrupt your app's ability to process more useful, timely messages.

By subscribing only to the presence events your app needs to provide presence-dependent functionality, you can reduce unnecessary websocket traffic.

## What's changing? {#whats-changing}

Slack will stop automatically dispatching `presence_change` events over [RTM](/legacy/legacy-rtm-api) websockets as [user presence](/apis/web-api/user-presence-and-status) changes in a workspace.

To continue receiving `presence_change` events you must:

1. Enable presence subscriptions for your RTM streams by passing the `batch_presence_aware=1` argument to `rtm.start` or `rtm.connect`.
2. Post [`presence_sub`](/reference/events/presence_sub) events to the websocket, noting which user IDs your app wants to track presence status for.
3. Consume the `users` array attached to batched `presence_change` events, dispatched when presence changes for users your app is subscribed to.

In addition, [`rtm.start`](/reference/methods/rtm.start) will no longer include user `presence` and `online` field information in its initial preamble JSON. You'll need to use [`users.getPresence`](/reference/methods/users.getPresence) to determine initial presence status instead.

## What isn't changing? {#what-isnt-changing}

Presence events are not currently issued as part of the [Events API](/apis/events-api/), therefore nothing is changing on the Events API.

## What happens if I do nothing? {#what-happens-if-i-do-nothing}

Your app will stop receiving `presence_change` events on any websockets your app is connected to beginning November 15, 2017. If your app uses those presence events to direct functionality, your app might not do what it's supposed to do without that information.

Your app will no longer receive the current state of `presence` and `online` information for workspace users when connecting via `rtm.start`.

## When is this happening? {#when-is-this-happening}

Presence subscriptions will become mandatory on **November 15, 2017**.

**Tags:**

* [Breaking change](/changelog/tags/breaking-change)
* [Announcement](/changelog/tags/announcement)
