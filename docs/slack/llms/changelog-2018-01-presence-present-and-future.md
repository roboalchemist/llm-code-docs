Source: https://docs.slack.dev/changelog/2018-01-presence-present-and-future

# Presence present and future

January 30, 2018

The RTM API's `presence_change` event is now **only** available via [presence subscriptions](/apis/web-api/user-presence-and-status#subscriptions) and [`rtm.start`](/reference/methods/rtm.start) **no longer** includes user presence status in its response.

We incrementally announced these changes in [June](/changelog/2017-06-batch-presence-and-presence-subscriptions) and [October](/changelog/2017-10-making-rtm-presence-subscription-only) 2017.

Today, we're _also_ announcing the **deprecation** of the optional `presence` parameter in [`users.list`](/reference/methods/users.list). Beginning **September 26th, 2018**, the `presence` parameter and corresponding fields will no longer be available from `users.list`.

Developers utilizing user presence state in their applications and integrations should review this guide to the many recent and coming changes to presence.

Update: [`users.setActive`](/reference/methods/users.setActive) is also deprecated due to underlying functionality not being available in our most modern message servers.

## What's changing in September 2018 {#future}

The Web API method [`users.list`](/reference/methods/users.list) will no longer accept the optional `presence` parameter, which instructs the method to return a `presence` field with every user object.

Until September 26th 2018, you'll find accurate presence reporting capped at 500 results in large workspaces.

## Recent changes to presence in Winter 2017-2018 {#past}

To recap everything that has changed recently with presence:

* Open websocket connections will no longer receive [`presence_change`](/reference/events/presence_change) events without a subscription.
* [Presence subscriptions](/apis/web-api/user-presence-and-status#subscriptions) must be established using [`presence_sub`](/reference/events/presence_sub).
* [`rtm.start`](/reference/methods/rtm.start) will no longer include initial `presence` fields for each user.
* [`users.list`](/reference/methods/users.list) now caps accurate presence reporting at 500 users per workspace. Use [`users.getPresence`](/reference/methods/users.getPresence) and/or [presence subscriptions](/apis/web-api/user-presence-and-status#subscriptions) instead.
* Use the [`presence_query`](/reference/events/presence_query) write event over RTM to query the current presence status of a list of 500 users.
* We strongly encourage using [batched presence delivery](/apis/web-api/user-presence-and-status#batching), as it will eventually become mandatory and is especially useful when working with large teams.
* [`users.setActive`](/reference/methods/users.setActive) no longer prevents users from being marked inactive and will completely cease functioning May 8, 2018.

## How to respond or prepare {#prepare}

If your app uses `presence_change` events you must subscribe to them before delivery. If you don't need real time presence for every user, use [`users.getPresence`](/reference/methods/users.getPresence) ad-hoc to look up user presence by ID.

If your app uses the `presence` parameter on [`users.list`](/reference/methods/users.list) or relies on the `presence` field in user objects appearing in [`rtm.start`](/reference/methods/rtm.start), you'll want to look up presence on demand using [`users.getPresence`](/reference/methods/users.getPresence) or the [`presence_query`](/reference/events/presence_query) instead.

Neither `presence_query` nor `users.getPresence` are intended for frequent, bulk usage. We recommend reducing your dependency on a complete picture of user presence and instead look up presence ad hoc only when it's absolutely necessary for operations.

* [Learn more](/reference/events/presence_sub) about sending the [`presence_sub`](/reference/events/presence_sub) write event to establish subscriptions.
* [Learn more](/reference/events/presence_query) about using the [`presence_query`](/reference/events/presence_query) write event to report on users' current presence status.

If you relied on `users.setActive` to prevent a user from being set `away`, you'll need to maintain presence another way like opening a RTM connection or using [`users.setPresence`](/reference/methods/users.setPresence).

## What happens if I do nothing? {#nothing}

By not receiving the `presence_change` events your app is looking for, or by not getting the initial state of presence from `rtm.start` or `users.list` with the `presence` parameter, your app won't know whether users are present or not (that is, `active` or `away`).

If your app or bot only contacts users it detects as `active` via `presence`, your bot may have trouble interacting with users.

If your app tracks presence for some other reason, the tracking might not be accurate.

If your app is already using subscriptions but is not batching presence events, you may receive floods of `presence_change` events in large workspaces.

If your app only uses `users.getPresence` to determine presence, nothing changes. `users.getPresence` functions as usual.

If your app sets `presence` to `true` or `1` on `users.list`, you'll need to adapt to using `users.getPresence` and/or presence subscriptions by September 26, 2018. By doing nothing now, your presence results are capped at 500 users.

Your requests to `users.setActive` will appear successful but will not actually prevent a user from being marked `away`. Eventually, the method calls will return a HTTP 400-series code.

## When is this happening? {#what}

As of January 2018, presence subscriptions are already required and `rtm.start` no longer returns `presence` for its list of users.

On May 8, 2018 [`users.setActive`](/reference/methods/users.setActive)will completely cease functioning May 8, 2018. Until then, it is a no-op.

On September 26, 2018, the optional `presence` parameter in `users.list` will no longer function.

**Tags:**

* [Breaking change](/changelog/tags/breaking-change)
