Source: https://docs.slack.dev/changelog/2018/09/01/more-reasons-to-be-a-conversations-api-convert

# More reasons to be a conversations API convert

September 1, 2018

Unless your app uses the Conversations API, you'll encounter unusual results working with more exotic channel types, like shared channels and those channels converted from public to private.

## What's changing? {#what}

Users have converted channels from public to private for some time. Historically, the channel wouldn't transition so much as _migrate_ from one container type to the other. The channel ID would even change and your app would have scant evidence left behind to understand it.

Recently we began preserving the channel ID of channels converted from public to private. Like shared channels before them, they are no longer listed in legacy methods such as `channels.*` or `groups.*`.

The only way to confidently and reliably determine a channel's "type" and privacy settings is by using the [Conversations API](/apis/web-api/using-the-conversations-api), a family of methods that completely replace all the `channels.*`, `im.*`, `mpim.*`, and `groups.*` API methods.

Let [_conversational booleans_](/apis/web-api/using-the-conversations-api#the_conversational_booleans) like `is_private` guide you in understanding just what kind of conversation you're having — it's important to avoid relying on more heuristics like the first character in a channel ID string.

## How do I prepare? {#how}

Investigate which methods you use when looking up channel information and convert to using the `conversations.*` equivalent.

For example, if you use a `channels.*` API method, replace it with a `conversations.*` API method instead.

Method signatures and responses to these methods are notably different than their ancestors, supporting our [unified pagination scheme](/apis/web-api/pagination) and better decomposition. Some tasks, like retrieving all the members within a channel, are more complex than previously.

## What if I do nothing? {#nothing}

If knowing whether a channel is private or not is important to your app, your app might act inappropriately when it doesn't have all the information it needs.

If you display lists of channels to users and don't use the Conversations API, you might miss channels that have transitioned from public to private or back again.

You will continue to miss out on feature enhancements like shared channels, additional metadata, and simplified approaches to app development.

## When does this happen? {#when}

Channels are already moving between public and private states today. It happens to shared channels and non-shared channels alike.

It's important to use the [Conversations API](/apis/web-api/using-the-conversations-api) to make everything work right.

**Tags:**

* [Breaking change](/changelog/tags/breaking-change)
