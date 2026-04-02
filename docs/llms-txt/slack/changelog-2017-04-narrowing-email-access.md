Source: https://docs.slack.dev/changelog/2017-04-narrowing-email-access

# Narrowing email access

April 1, 2017

Back in November 2016, we [introduced](/changelog/2016-11-10-addressing-email-addresses) the `users:read.email` OAuth permission scope, allowing more explicit access to email addresses.

To help developers with the transition, we automatically grandfathered apps asking for `users:read` created before January 4th, 2017.

We'd like to complete this transition and remove this grandfathering **entirely** on August 21, 2018 October 16, 2018 a _future date_ we'll one day announce.

Apps created before January 4th, 2017 with user tokens granted only the `users:read` scope will no longer receive the `email` field in user objects.

If you want access to email addresses, you'll need the new [OAuth permission scope](/legacy/legacy-authentication/legacy-oauth-scopes), `users:read.email`. It provides an explicit, additive way to request access to team email addresses.

Additionally, the `bot` scope will no longer grant [bot user](/legacy/legacy-bot-users) tokens access to email addresses. Bot users must utilize a user token and the `users:read.email` scope instead.

Don't need access to email address but do need access to user data? `users:read` should be all you need.

## What's changing? {#whats-changing}

All Slack apps must request the `users:read.email` OAuth scope to access the `email` field in [user objects](/reference/objects/user-object) returned by the [`users.list`](/reference/methods/users.list) and [`users.info`](/reference/methods/users.info) web API methods. `users:read` will no longer be a sufficient scope for this data field.

Eventually, even apps that were previously grandfathered will have that grandfathering removed. Bot user tokens will no longer be granted access to the `email` field and user tokens granted through the application installation flow must be used instead.

## What isn't changing? {#what-isnt-changing}

`users:read` is still required to use `users.info` and `users.list`. You must still request `users:read` in addition to `users:read.email`.

Additionally, the OAuth scope `users.profile:read` can also be used to obtain access to email addresses, as they are considered part of the user's profile obtained via [`users.profile.get`](/reference/methods/users.profile.get).

Furthermore, [Sign in with Slack](/authentication/sign-in-with-slack/) continues to operate the same way it does today — email address is yielded for the current user signing in to your application via the `identity.email` scope.

## How do I prepare? {#how-do-i-prepare}

Add the `users:read.email` scope when using the OAuth flow or [Add to Slack](/legacy/legacy-slack-button).

Building an open source library or toolkit that uses `email`? Configure it to ask for `users:read.email` by default.

`users:read` and `users:read.email` must be requested _together_ as a delightful pair within the same authorization attempt.

## When is this happening? {#when-is-this-happening}

Our new OAuth scope, `users:read.email`, has been available since November 2016. On August 21, 2018 October 16, 2018 _some day_ in the future, we'll end grandfathering of apps created before January 4th, 2017.

If your app uses a "bot user" token to retrieve email address today, you must modify those requests to utilize a "user token" granted the `users:read.email` [OAuth scope](/legacy/legacy-authentication/legacy-oauth-scopes) instead, which you receive as part of the [OAuth installation process](/authentication).

"Bot user" tokens beginning with `xoxb-` no longer have access the `email` field.

## When is this happening? {#when-is-this-happening-1}

Our new OAuth scope, `users:read.email`, has been available since November 2016. August 21, 2018 October 16, 2018 _Some day_ we'll end grandfathering of apps and bot user tokens created before January 4th, 2017.

**Tags:**

* [Announcement](/changelog/tags/announcement)
