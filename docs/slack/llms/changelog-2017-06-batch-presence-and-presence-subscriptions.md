Source: https://docs.slack.dev/changelog/2017-06-batch-presence-and-presence-subscriptions

# Batch presence and presence subscriptions

June 1, 2017

RTM API Presence is now only available via subscription.

As of January 2018, [`presence_change`](/reference/events/presence_change) events are not dispatched without [_presence subscriptions_](/apis/web-api/user-presence-and-status) established with [`presence_sub`](/reference/events/presence_sub). Relatedly, current user presence status is no longer communicated in [`rtm.start`](/reference/methods/rtm.start). [Learn more](/changelog/2018-01-presence-present-and-future).

If you've been developing on Slack for awhile you may have noticed a continued theme with updates we make to the platform and APIs: larger teams and evolving use cases mean previous ways of enumerating collections of data become unwieldy and even problematic.

In this exciting edition of the changelog, I'd like to introduce you to new ways to work with `presence_change` events in the [RTM API](/legacy/legacy-rtm-api).

**If you don't work with the RTM API or don't utilize `presence_change` events, there's very little of value for you in this changelog.**

## What's changing? {#whats-changing}

We're introducing two new scalable ways to stay on top of presence change notices in the RTM API.

### 1. Batched presence events {#1-batched-presence-events}

On large teams especially, folks flock like birds and change their presence at the same time to the same things.

Both to help us dispatch these and for you to consume these reliably, we've introduced a `batch_presence_aware=1` parameter to pass to [`rtm.start`](/reference/methods/rtm.start) or [`rtm.connect`](/reference/methods/rtm.connect). Doing so indicates you can receive batched presence events.

These are the [`presence_change`](/reference/events/presence_change) events you're used to except instead of a single `user` field, you'll find a `users` field with an array of user IDs.

### 2. Presence subscriptions {#2-presence-subscriptions}

Maybe your app only needs to know the presence of like five people on a team of thousands. Or five hundred people. Or maybe you need all of those thousands.

Well instead of having no choice but to receive them all, now you can send a `presence_sub=true` parameter to `rtm.start` and `rtm.connect` and you'll tell us that you only want `presence_change` events for users you're establishing subscriptions for. (**Update: the `presence_sub` parameter is no longer required.**)

You then push [`presence_sub`](/reference/events/presence_sub), a write-only event, into the websocket and declare a list of users to subscribe to. There's some more nuance to it that the [presence docs](/apis/web-api/user-presence-and-status#subscriptions) cover for you.

Once subscribed, you'll only get those users' `presence_changed` events. Subscriptions last only the length of an open websocket connection.

## What isn't changing? {#what-isnt-changing}

The Events API isn't changing how it handles user presence events — it still stubbornly doesn't support them at all!

You won't receive bulk `presence_change` events if you don't opt-in to them using the `batch_presence_aware=1` parameter with `rtm.start` or `rtm.connect`.

You won't need to subscribe to `presence_change` events with `presence_sub` unless you opt-in to subscription using the `presence_sub=true` parameter with `rtm.start` or `rtm.connect`.

## What happens if I do nothing? {#what-happens-if-i-do-nothing}

If you don't use the RTM API or don't use `presence_change` events — nothing. Do nothing and nothing also happens. Easy.

On very large teams, like [Enterprise organization](/enterprise) teams, you might miss some `presence_change` events if you don't batch them up. Or you might receive so many at one time that your app blows up.

If you don't use `presence_sub` to manage a smaller concern of `presence_change` events you might receive so many at one time that your bot forgets its name.

## How do I prepare? {#how-do-i-prepare}

If you want to go "all-in" with both subscriptions and batching, you'll want to do _all_ of the following:

1. Read [the docs](/apis/web-api/user-presence-and-status) and decide if these features are right for you.
2. Opt-in to the features by providing the appropriate parameters when preparing to connect to the RTM API
3. Anticipate receiving `presence_change` events with a `users` array instead of a `user` string, and subscribe to these changes using `presence_sub`.

## When is this happening? {#when-is-this-happening}

These new features are available now. Our concern with very large teams is clear and present. Implement them at your leisure, but if you work with [Enterprise organization](/enterprise) teams you may want to migrate sooner than later.

**Tags:**

* [Announcement](/changelog/tags/announcement)
