Source: https://docs.slack.dev/changelog/2018/03/01/great-rate-limits

# Great rate limits

March 1, 2018

Until now, the [rate limits](/apis/web-api/rate-limits) governing the [Slack Web API](/apis/web-api/) have been vague, even sometimes undefined.

This week we are rolling out an evolved rate limiting system granting a greater number of requests to most [methods](/reference/methods) and sets responsible defaults in the few cases where limits were more mysterious or unenforced.

We've granted a brief grace period to a small number of apps & integrations to adjust.

## What's changing {#what}

The week of March 6, 2018 we'll gradually roll out these changes:

Rate limiting was previously undefined beyond a vague "1 message per second" rule for posting messages via [`chat.postMessage`](/reference/methods/chat.postMessage) or [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks).

After analyzing usage patterns over the past several months, we put together a portfolio of [**rate limit tiers**](/apis/web-api/rate-limits#tiers) assigned to each method.

Each API method's assigned tier allows a certain number of requests per minute, with varying support for greater bursts of activity, especially when using [cursor-based pagination](/apis/web-api/pagination).

For most methods, rate limits are higher than they've ever been before. Find your favorite method's assigned tier by browsing the [method catalog](/reference/methods).

### Web API rate limit tiers {#tiers}

Tier

Range

Description

Tier 1

1+ per minute

Access tier 1 methods infrequently. A small amount of burst behavior is tolerated.

Tier 2

20+ per minute

Most methods allow at least 20 requests per minute, while allowing for occasional bursts of more requests.

Tier 3

50+ per minute

Tier 3 methods allow a larger number of requests and are typically attached to methods with paginating collections of conversations or users. Sporadic bursts are welcome.

Tier 4

100+ per minute

Enjoy a large request quota for Tier 4 methods, including generous burst behavior.

Special

## Varies

Rate limiting conditions are unique for methods with this tier. For example, [`chat.postMessage`](/reference/methods/chat.postMessage) generally allows posting one message per second per channel, while also maintaining a workspace-wide limit. Consult the method's documentation to better understand its rate limiting conditions.

These tiers and their allowed number of requests are subject to change.

### How rate limits are evaluated {#how-rate-limits-are-evaluated}

Rate limits were previously evaluated in a per token bucket. Now rate limits are enforced on a per Slack app per workspace basis.

If your app has 10 user tokens and 1 bot user token belong to a single workspace, all 11 tokens draw from the rate limit pool assigned by the method's associated tier.

## How to respond or prepare {#prepare}

We recommend apps make requests to methods and when rate limited, retry and resume requests once the rate limiting period is over.

You may want to evaluate the rate limit tiers assigned to [methods](/reference/methods) and throttle or refactor usage as needed. In some cases, you might remove throttling you've previously put in place for use cases like pagination.

### Responding to rate limiting conditions {#responding-to-rate-limiting-conditions}

When your app is rate limited making a specific request, you'll receive a HTTP response somewhat like this one.

```text
HTTP/1.1 429 Too Many RequestsRetry-After: 30
```text

This response instructs your app to wait 30 seconds before attempting to call the same method with any [token](/authentication/tokens) awarded to your application from this workspace.

Calls to other methods on behalf of this workspace are not restricted. Calls to the same method for other workspaces for this app are not restricted.

By programmatically evaluating the `Retry-After` header you should wait for the indicated number of seconds before retrying the same request or continuing to use that method for this workspace.

See the [rate limiting](/apis/web-api/rate-limits) documentation for more information.

## What happens if I do nothing? {#nothing}

If rate limiting was never a problem for you before, it probably won't be a problem for you now.

If you've already built support for handling HTTP status code 429 (_Too Many Requests_), your code should continue working as expected whenever you enter rate limiting conditions.

If you aren't detecting and responding to rate limit conditions, your application may continue attempting to make requests without waiting the instructed amount of time between requests.

## When is this happening? {#when}

Beginning March 7th, 2018 we'll gradually turn this form of Web API rate limiting on for a small number of Slack apps. By the end of March 9th, 2018 we plan to have all Slack apps using the Web API running on the new rate limiting system.

## Tags:

* [Announcement](/changelog/tags/announcement)
