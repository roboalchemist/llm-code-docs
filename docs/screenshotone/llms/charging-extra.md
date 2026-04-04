# Source: https://screenshotone.com/docs/charging-extra/

# Charging Extra

You can set the hard limit for screenshots higher than the limit in your current plan. And by doing this, you are enabling charging for extra screenshots. The option is available only for paying customers who are organization owners.

![Changing the hard limit](charge-extra.png)

Once the charging extra is enabled (at [your subscription page](https://dash.screenshotone.com/subscription)), you will be charged for successful not cached requests that go over your plan limitation.

## Examples

:::note
**Your price per extra screenshot depends on the plan you have**. You can see all prices at the [ScreenshotOne Pricing page](https://screenshotone.com/pricing) or check out your price at [your subscription page](https://dash.screenshotone.com/billing).
:::

Let's look at different examples of an artificial subscription plan. Imagine you have a limit of 10000 screenshots monthly, and let's assume the price of one extra screenshot is $0.004 (this is an example price, not a real price):

1. The plan limit is 10000, the hard limit is 15000, and you rendered 12000 screenshots. You will be charged for 2000 extra screenshots. $0.004 x 2000 = $8.
2. The plan limit is 10000, the hard limit is 15000, and you rendered 12500 screenshots. You will be charged for 3000 extra screenshots. $0.004 x 3000 = $12.

Why for 3000 extra screenshots?

**It is because extra charges are rounded to the close upper bound of a thousand screenshots.**

If you render only one extra screenshot, you pay for 1000 screenshots. If you render 1001, you pay for 2000, and so on. If you render 999, you pay for 1000, and so on.

## Upgrading subscription

Once you upgrade your subscription, your hard limit is reset. And you need to set it up again.

## Cancelling or downgrading subscription

Before you cancel your subscription, ScreenshotOne will try to charge you for extra screenshots and only then cancel it.

For downgrading, charging happens only when downgrading to a free plan. Otherwise, there is no need.

## When you are charged

ScreenshotOne charges you periodically over the extra usage if needed, usually once per 1000 screenshots.

Or you also might be charged in one "batch" for the extra usage. It depends on the internal logic of the service.

## Maximum hard limit

Every new customer has a maximum hard limit of 100,000 screenshots. If you need to upgrade it and make it higher, feel free to write to `support@screenshotone.com`. Please, describe your use case.

ScreenshotOne is a scalable and highly performant API that has paying customers who make render more than 100,000 screenshots monthly. Still, there is a need to make sure that there is no service abuse and that high-quality service can be delivered. That's why the maximum hard limit for new customers is applied.