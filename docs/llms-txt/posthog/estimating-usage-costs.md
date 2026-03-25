# Source: https://posthog.com/docs/billing/estimating-usage-costs.md

# Estimating usage &amp; costs - Docs

It can be daunting to figure out how much a usage-based platform like PostHog will cost, but there are simple ways to estimate your usage and costs.

This guide explains why we price based on usage, how to estimate your usage, and tips on how to reduce your costs.

## Why do we price based on usage?

Really it comes down to this: The more you use PostHog, the more value you get, and the more it costs us to process and store your data. Thus, we charge based on usage.

### What about charging by monthly active users? Isn't that also usage?

Kind of, yes, but actually no. Some users are very valuable. They use your product a ton, they respond to your feedback surveys, and they store a lot of data in your platform. Other users hit your landing page and bounce immediately.

From a value perspective, you shouldn't need to pay the same amount for both of these users. It makes more sense to pay *only for the value you receive*, which is *directly tied to user activity* such as events, session replays, or data.

## How do I estimate my event usage?

If you're already using another tool and want to switch to PostHog (welcome!), your existing tool may have the exact numbers you need. You might need to ask their support for this data directly if it's not easy to find.

Alternatively, you can use one of these two methods.

### Option 1: Sign up for free and get an accurate projected volume in a few days

Each of our products has a very generous free tier. They're also very easy to get set up.

Simply [sign up](https://app.posthog.com/signup) and start to use whichever product you are interested in. After a few days, you'll get a good estimate of your projected volume on your [Organization Billing page](https://app.posthog.com/organization/billing).

If you want a more accurate estimate, give it a week - this way weekdays and weekends will also be taken into account.

> 💡 **PostHog Tip:** If your projects volume is higher than you'd like, we offer ways to "tune" your implementation to only capture or use what's valuable to you. See [How to reduce your PostHog usage](/docs/getting-started/estimating-usage-costs.md#how-to-reduce-your-posthog-costs) for more.

### Option 2: Estimate based on your product category and/or MAUs

Sometimes you can estimate your volumes based on another number that you know, like your monthly active users (MAU).

#### Estimating session replay volume based on MAUs

If you know how manu MAUs you have, and you know the average number of sessions per MAU, you can get your estimated volume by simply multiplying the two together. Easy peasy!

#### Estimating event volume based on MAUs

Events are trickier to estimate based on MAUs because not every type of company has the same type of usage. However, we did a bit of diving into our own data and found that there is a bit of usage consistency within different company categories. Using the table below, take the average number of events per MAU and multiply by the number of MAUs you have to get an estimated event volume.

| Product | B2B / B2C | Monthly events per MAU | Autocapture | Platforms |
| --- | --- | --- | --- | --- |
| PostHog | B2B | 87 | ✔ | Web |
| Financial reporting | B2B | 44 | ✖ | Web |
| Cloud monitoring | B2B | 22 | ✖ | Web |
| Document management | B2B | 54 | ✔ | Web |
| Speech to text API | B2B | 583 | ✖ | API |
| Crypto wallet | B2C | 162 | ✖ | Browser extension |
| Meditation app | B2C | 118 | ✖ | Android, iOS |
| Fashion retail | B2C | 31 | ✔ | Web |
| Event booking | B2C | 8 | ✖ | React Native |
| Restaurant booking | B2B2C | 54 | ✔ | Web, Mobile |

Event counts also vary based upon whether you are using [autocapture](/docs/integrate/ingest-live-data.md#use-autocapture), [custom capture](/docs/integrate/ingest-live-data.md#capture-user-events) or a combination of both. Custom capture may be better if you have lots of users.

## How do I estimate the number of feature flag requests?

Feature flags and experiments are charged based on the number of requests. The way to calculate this depends if you're requesting flags from the frontend or backend.

#### Frontend SDKs

We make a request to fetch feature flags (using the [`/flags` endpoint](/docs/api/flags.md)) when one of the below occurs:

-   The PostHog SDK is initialized
-   A user is [identified](/docs/data/identify.md)
-   A user's [properties](/docs/product-analytics/person-properties.md) are updated
-   You call `posthog.reloadFeatureFlags()` in your code
-   You create a [group](/docs/product-analytics/group-analytics.md)

For the [JavaScript web SDK](/docs/libraries/js.md), you can estimate how many feature flag requests you will make by doing the following:

1.  Check the networks tab in Chrome inspector tools for the number of `/flags` requests
2.  Find out your number of monthly page views
3.  Multiply your number of `/flags` requests by your monthly page views

For example, if on refresh, you see 2 `/flags` requests per pageview and you have ~150,000 pageviews, your monthly feature flag requests should be around ~300,000.

#### Backend SDKs

##### Without local evaluation

If you're not using [local evaluation](/docs/feature-flags/local-evaluation.md), a request to get feature flags is made every time you call `posthog.get_feature_flag()` on your backend. Your estimated usage will be however many times you are calling this code.

##### With local evaluation

If you're using [local evaluation](/docs/feature-flags/local-evaluation.md), each local evaluation request is equivalent to, and charged as, 10 feature flag requests. Local evaluation calls, by default, are made every 30 seconds. Assuming your server is constantly running and making 2 requests per minute, you will be charged `10 * 2 * 60 * 24 * 30 = 864,000 feature flag requests` each month.

> **Note:** This figure is for a single server and a single instance of PostHog. If you have multiple servers, PostHog instances, or a different poll duration, you need to multiply your estimates too.

## How am I billed for data pipelines?

Your data pipelines are billed on two things:

1.  The number of rows exported via [batch exports](/docs/cdp/batch-exports.md)
2.  The number of events triggered under [realtime destinations](/docs/cdp/destinations.md)

Like other products, there is a generous free tier for both categories which can be seen on the [pricing](/pricing.md) page.

## Estimating your monthly bill

Once you've figured your projected event usage and flag requests, you can either:

1.  Use the pricing calculator on our [pricing](/pricing.md) page and calculate your estimated costs for adopting PostHog.
2.  If you're getting your estimated figures from your free PostHog account, you can see your projected volumes and costs right there in your [billing dashboard](https://app.posthog.com/organization/billing).

And don't forget, we have generous free volumes for every one of our products – even if you're on a paid plan!

## How to reduce your PostHog costs

Each product can be tuned to use only the resources you need.

-   For product analytics, read [how to capture fewer unwanted events](/tutorials/fewer-unwanted-events.md)
-   For session replay, read [how to control which sessions you record](/docs/session-replay/how-to-control-which-sessions-you-record.md)
-   For feature flags, read [how to cut feature flag costs](/docs/feature-flags/cutting-costs.md)

You can also optionally set [billing limits](/docs/billing/limits-alerts.md) for every product. When you hit your billing limit, we'll stop ingesting your data and you won't be charged over the set amount.

## Creating a billable usage dashboard

Want to know exactly what's driving your bill? Create a dashboard with the [PostHog billable usage template](/templates/posthog-billable-usage.md) to break down and analyze your usage across different events, SDK libraries, and products.

![PostHog billable usage dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/posthog_billable_usage_b2b494d4bb.png)![PostHog billable usage dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/posthog_billable_usage_b2b494d4bb.png)

This dashboard turns your billing usage into a live, interactive report — so you can create insights, spot spikes, and optimize how you're spending.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better