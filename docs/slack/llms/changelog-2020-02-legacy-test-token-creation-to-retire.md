Source: https://docs.slack.dev/changelog/2020-02-legacy-test-token-creation-to-retire

# Legacy test token creation to retire

February 1, 2020

Legacy tester tokens may no longer be created.

We're deprecating [legacy test tokens](/legacy/legacy-custom-integrations/legacy-custom-integrations-tokens) and will disallow the creation of new test tokens beginning **May 5th, 2020**.

We launched Slack apps over four years ago as a replacement to the number of ways one could obtain overly-permissive tokens to integrate with Slack.

If you or a software product you author relies on test token creation, you will need to migrate to using Slack apps with specifically named scopes instead.

Existing tester tokens will continue functioning but tokens left unused are subject to periodic revocation.

## What's changing {#changed}

On May 5th, 2020, you will no longer be able to create _new_ legacy tester tokens.

Existing legacy tester tokens will continue functioning, provided they remain in use.

Third party applications and integrations instructing users to create legacy tester tokens will need to be revised to work with more granular permissions.

## How to respond or prepare {#prepare}

[Create a Slack app](https://api.slack.com/apps) and ask for the [permission scopes](/reference/scopes) corresponding to your goals. You can install your app without implementing OAuth by copying and pasting the displayed token to your preferred programming environment.

### What scopes do tester tokens support? {#what-scopes-do-tester-tokens-support}

Tester tokens have more permissions than can be completely described with individual scopes. We don't recommend taking shortcuts by using legacy scopes.

Evaluate the [scopes catalog](/reference/scopes) and choose the bot scopes your app needs—common use cases include posting messages ([`chat:write`](/reference/scopes/chat.write)), listing users ([`users:read`](/reference/scopes/users.read)) or public channels ([`channels:read`](/reference/scopes/channels.read)).

For apps currently using the RTM API with tester tokens, we recommend moving to the [Events API](/apis/events-api/). If you _must_ continue using the legacy RTM API, [classic apps](https://api.slack.com/apps?new_classic_app=1) can still be created and work with [`rtm.connect`](/reference/methods/rtm.connect). This approach involves trading a deprecated approach for a legacy one and is discouraged.

## What happens if I do nothing? {#nothing}

There's nothing you need to do if you don't create or ask people to create tester tokens.

If you use tester tokens to write quick scripts or perform other tasks with the Web API and don't migrate to Slack apps, you won't be able to create new tester tokens after May 5th, 2020.

If you tell users to create tester tokens to use in software you develop, those users will no longer be able to follow your instructions.

If you have already issued tester tokens, you must continue using them to prevent their revocation.

## When is this happening? {#when}

We'll stop allowing the creation of new legacy tester tokens beginning May 5th, 2020. We'll also more regularly revoke unused legacy tester tokens on that day as well.

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
