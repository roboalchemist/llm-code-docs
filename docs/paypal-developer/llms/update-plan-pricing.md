# Update plan pricing

## DOCS CURRENT Last updated: May 14th, 9:07am

### Update pricing for the subscription plan

You can modify subscription pricing for all subscribers at once by changing the pricing at the plan level, without needing to migrate subscriptions individually.

For example, if you provide a video streaming service and offer a subscription plan at $5 per month, you can update the price for future cycles to $7 for all existing subscribers.

## How it works

When you update the plan price:

- New subscribers see the new price.
- Existing subscribers are notified by email about the price change, and given 10 days to modify their subscription.
- If the next billing cycle is within 10 days of the price change, subscribers are not changed the new price until the next billing cycle.

For example, you update the plan price from $20 to $25 on the 10th of the month. An existing subscriber is enrolled on this plan with the next billing cycle starting on the 15th of the month. This subscriber pays $20 for their subscription on the 15th of the month, and on the following month pays $25.

## Modify the code

Replace ACCESS-TOKEN with your access token.

In the URI for the API call, replace the sample subscription ID with the ID for the subscription you want to update. In this example, the subscription ID is P-7GL4271244454362WXNWU5NQ.

---

If you accept cookies, we’ll use them to improve and customize your experience and enable our partners to show you personalized PayPal ads when you visit other sites. [Manage cookies and learn more](https://www.paypal.com/myaccount/privacy/cookiePrefs?locale=en_US)