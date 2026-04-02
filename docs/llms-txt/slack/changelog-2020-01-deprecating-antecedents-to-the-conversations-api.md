Source: https://docs.slack.dev/changelog/2020-01-deprecating-antecedents-to-the-conversations-api

# Deprecating antecedents to the conversations API

January 7, 2020

We released the [Conversations API](/apis/web-api/using-the-conversations-api) in September 2017 as a one-size-fits-all replacement for a variety of APIs used to read and write information about channels, private channels, direct messages, and multi-party direct messages.

Today we are announcing the deprecation of the methods that preceded the Conversations API (`channels.*`, `groups.*`, `im.*`, & `mpim.*`). On November 25th, 2020 **February 24th, 2021** these methods will retire and cease functioning.

If users expect your app to work in channels of any kind, you'll want to verify you're using the Conversations API for all channel types.

The final date for existing apps and custom integrations is now February 24th, 2021

We'll stop allowing _newly created_ Slack apps to use these deprecated APIs beginning June 10th, 2020.

All `channels.*`, `groups.*`, `im.*`, & `mpim.*` methods will return [deprecation warnings](#warnings) beginning June 10th, 2020.

## We resolutely recommend migrating to the Conversations API immediately.

## What's changing {#changed}

We're marking all [Web API methods](/reference/methods) in the `channels`, `im`, `groups`, and `mpim` namespaces as _deprecated_. They will retire and cease functioning on February 24th, 2021.

**Any** usage of those methods should be transferred to the newer [Conversations API](/reference/methods?family=conversations) equivalents. This includes legacy custom integration-based bots and legacy tester tokens.

You'll especially want to migrate promptly if your app works with private channels or shared channels, as the deprecated methods function poorly or not at all with them.

As February 24th, 2021 approaches, these deprecated methods will continue to degrade as they have in the past. We are certain that the `groups.*` methods in particular will cease functioning with newly created private channels in the coming weeks and months.

_Update_: On June 10th, 2020, newly created Slack apps will no longer be able to use these deprecated methods. Apps created before June 10th, 2020 will continue having access until February 24th, 2021.

### Deprecated / retiring methods {#methods}

CONVERSATION\_ANTECEDENTS\_METHOD\_LIST

### Deprecation warnings {#warnings}

When you issue a request to one of these deprecated methods, beginning June 10th, 2020 you'll receive a `method_deprecated` warning included in every response.

Examine the `response_metadata` for textual hints on how to resolve the warning. The text will mention the retirement date. If there's a method you should use instead of the one you're attempting, we'll mention that in the warning too.

For example, if you request a `channels.*` API method, you'll see a warning like this:

```json
{    "ok": true,    // ...    "warning": "method_deprecated",    "response_metadata": {        "warnings": [            "[WARN] This method is deprecated and is scheduled to cease functioning on 2021-20-24. Please use conversations.* instead. Learn more: https://docs.slack.dev/changelog/2020-01-deprecating-antecedents-to-the-conversations-api",        ]    }}
```text

One day this warning will become an error...

## How to respond or prepare {#prepare}

To verify you're prepared for this retirement first **review** whether your app uses any methods in the `channels`, `mpim`, `groups`, or `im` namespaces. In SDKs these might be calls like `client.channels.*` or `api.im.*`.

Then:

1. If you're using calls to `conversations` namespaced APIs, like `conversations.list` or `conversations.open`, you're using the newest APIs and are good to go!
2. If you're using calls to methods in the deprecated `channels`, `mpim`, `groups`, or `im` namespaces, you must **migrate** those calls to equivalent [Conversations API methods](#methods).

Conversations API methods have similar, but not identical, responses and parameters as their deprecated equivalents. Pay attention to the differences between methods.

Rate limiting scenarios may be different depending on your use cases.

### Finding the right method {#finding_method}

Almost every method beginning with `channels.`, `mpim.`, `groups.`,`im` will have a corresponding method in `conversations.`.

For example, if you make requests to `channels.*`, `mpim.*`, `groups.*` or `im.*`, you will use `conversations.*` instead. Using the `type` parameter you can limit results by just private channels, or just direct messages, or a hybrid of some or all conversation types.

**Each** `conversations.*` equivalent has response shapes standardized across conversation types. While migrating, you will encounter new fields and data structures so you'll want to review how you're treating the response as well.

If you need the members of a specific channel or conversation, use [`conversations.members`](/reference/methods/conversations.members). If you need a list of conversations a specific user is party to, use [`users.conversations`](/reference/methods/users.conversations).

Shared channels are only supported by migrating to the Conversations API. Channels that have had their permissions type changed between public and private may only be accessed with the Conversations API. One day, newly created private channels will only be accessible with the Conversations API.

Look [above at the list of method conversions](#methods) to find the right methods to migrate to.

## What happens if I do nothing? {#happens}

If your app doesn't use the Web API, or doesn't rely on the first letter of a channel ID to determine behavior, or if you don't use any of the [deprecated methods](#methods) — your app should continue functioning without modification.

If you use these methods in the days and weeks leading up to February 24th, 2021, your app may continue functioning but won't work with certain kinds of channels like [shared channels](/apis/slack-connect/) or channels that have converted their privacy status.

If you use any of the private channel methods (`groups.*`), you will at some point in the future lose access to the most recently created kinds of private channels, which only work with the Conversations API.

If you create Slack apps often, your newly created Slack apps won't be able to access the deprecated methods after June 10th, 2020.

## We strongly encourage you to migrate to the Conversations API as soon as possible.

## When is this happening? {#when}

Today, January 7, 2020 [these methods](#methods) are officially deprecated. That means they are not only _discouraged_ but have an explicit retirement date where they will cease functioning.

On June 10, 2020, [these methods](#methods) won't be usable by newly created Slack apps.

On February 24th, 2021, [these methods](#methods) will become retired and no longer function. You must use `conversations.*` equivalents by that date or risk service interruptions for your app.

Between now and February 24th, 2021, expect these methods to continue to degrade and become incompatible with evolving channel types on Slack.

## Tags:

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
