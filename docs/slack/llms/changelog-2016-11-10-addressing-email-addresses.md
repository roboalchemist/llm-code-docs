Source: https://docs.slack.dev/changelog/2016-11-10-addressing-email-addresses

# Addressing email addresses

November 10, 2016

Accessing Email Addresses

The [`users:read.email`](/reference/scopes/users.read.email) OAuth scope is now required to access the `email` field in user objects returned by the [`users.list`](/reference/methods/users.list) and [`users.info`](/reference/methods/users.info) web API methods. [`users:read`](/reference/scopes/users.read) is no longer a sufficient scope for this data field. [Learn more](/changelog/2017-04-narrowing-email-access).

This original plan has been updated

Grandfathering is no longer in effect. Please see [this post from April 2017](/changelog/2017-04-narrowing-email-access) for more information.

We've added a new [OAuth permission scope](/legacy/legacy-authentication/legacy-oauth-scopes) called `users:read.email` and it provides a new explicit, additive way to request access to team email addresses. If you don't need email addresses but do need other user info, `users:read` is still all you need.

Apps created before **January 4th, 2017** are grandfathered and will continue behaving in a backwards-compatible way. Apps created after that date must request the new `users:read.email` scope. Regardless of creation date, we encourage all apps to migrate to this new scope.

## What's changing? {#whats-changing}

Slack apps created after the cut off date must request the new `users:read.email` OAuth scope to access the `email` field in [user objects](/reference/objects/user-object) returned by the [`users.list`](/reference/methods/users.list) and [`users.info`](/reference/methods/users.info) web API methods. `users:read` will no longer be a sufficient scope for this data field.

### Have code you're planning to re-use in a new app? {#have-code-youre-planning-to-re-use-in-a-new-app}

If you have code you plan to re-use in a new application record and that code only asks for `users:read`, you won't find email addresses in these methods.

You'll need to request both `users:read` and `users:read.email` while installing the app.

## What isn't changing? {#what-isnt-changing}

`users:read` is still required to use `users.info` and `users.list`.

We're grandfathering existing Slack apps so these methods will continue including `email` when you've only requested or are requesting `users:read`.

Your vintage scope retains its data-inclusive approach. You've already requested and earned that permission.

That said, we encourage you to use the new scopes anyway!

Additionally, the OAuth scope `users.profile:read` can also be used to obtain access to email addresses, as they are considered part of the user's profile obtained via [`users.profile.get`](/reference/methods/users.profile.get).

Furthermore, [Sign in with Slack](/authentication/sign-in-with-slack/) continues to operate the same way it does today — email address is yielded for the current user signing in to your application via the `identity.email` scope.

## How do I prepare? {#how-do-i-prepare}

If you're building an application consuming the `email` field in 2017 and beyond, you'll need to add the `users:read.email` scope when using the OAuth flow or [Add to Slack](/legacy/legacy-slack-button).

Building an open source library or toolkit that uses `email`? Configure it to ask for `users:read.email` by default.

`users:read` and `users:read.email` must be requested _together_ as a delightful pair within the same authorization attempt.

### Apps created before the cut off date needn't do anything at all. {#apps-created-before-the-cut-off-date-neednt-do-anything-at-all}

Regardless of when your app was created, if email addresses are important for your app, we strongly recommend you also request `users:read.email` as team members install your app.

For non-grandfathered apps, you must request `users:read.email` to enable the `email` field to appear in [user objects](/reference/objects/user-object) presented in methods like [`users.info`](/reference/methods/users.info) and [`users.list`](/reference/methods/users.list).

## When is this happening? {#when-is-this-happening}

Our new OAuth scope, `users:read.email`, is available now.

Apps created after **January 4th, 2017** will need to request this scope to receive the email addresses in these Web API methods. Apps from yesteryear will do as they've always done.

**Tags:**

* [Announcement](/changelog/tags/announcement)
