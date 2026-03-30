# Source: https://docs.together.ai/docs/billing-usage-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage Limits & Analytics

> Understanding account tiers, rate limits, model access, and cost analytics on Together AI.

## Build Tiers and Rate Limits

Together AI uses a system of Build Tiers to reward customers as they continue to use our service. The more you do on Together, the higher your limits are!

There are 5 build tiers. If you find yourself running into rate limits once you're on Build Tier 5, a Scale or Enterprise plan may be a better fit for your needs.

### Required Spend and Rate Limits

You can move up to the next build tier by paying your monthly bill, or by purchasing credits.

Build Tiers are based on lifetime spend.

| Build Tiers  | Total Spend | LLMs     | Embeddings | Re-rank   |
| ------------ | ----------- | -------- | ---------- | --------- |
| Build Tier 1 | \$5.00      | 600 RPM  | 3000 RPM   | 500,000   |
| Build Tier 2 | \$50.00     | 1800 RPM | 5000 RPM   | 1,500,000 |
| Build Tier 3 | \$100.00    | 3000 RPM | 5000 RPM   | 2,000,000 |
| Build Tier 4 | \$250.00    | 4500 RPM | 10,000 RPM | 3,000,000 |
| Build Tier 5 | \$1000.00   | 6000 RPM | 10,000 RPM | 5,000,000 |

### Model Access by Build Tier

Some models have minimum Build Tier requirements beyond the standard rate limits.

#### Image Models

* **Build Tier 1 and above:** Access to Flux.1 \[schnell] (free and Turbo), Flux.1 Dev, Flux.1 Canny, Flux.1 Depth, Flux.1 Redux, and Flux.1 Kontext \[dev]

* **Build Tier 2 and above:** Access to Flux Pro models, including Flux.1 \[pro] and Flux1.1 \[pro]

**Note:** Model access requirements may change based on demand and availability. Check the model documentation for the most current access requirements.

### Important Note About Build Tier Access Restrictions

Even with a positive balance and no usage limit set, you may still encounter access restrictions due to Build Tier requirements. Build tiers are determined by actual account spend (purchased credits or platform usage), not free credits.

**Key points to remember:**

* Free credits don't count toward tier upgrades

* Build Tier 1 requires \$5 of actual account spend

* Build Tier 2 requires \$50 of actual account spend

* Some premium models (including Flux Pro 1.1, Flux Pro 1, and other high-end models) are restricted to Build Tier 2 or higher

* Access restrictions apply regardless of your credit balance or usage limit settings

**Common scenarios:**

* If you're seeing "Free tier" access errors despite having credits, you may need to purchase credits to upgrade to Build Tier 1

* If you encounter "tier access" errors for premium models, you may need Build Tier 2 status (\$50 total spend)

If you're experiencing access issues with a positive balance, check whether your credits are free credits or purchased credits and verify your account tier in your billing settings.

### Exceptions

Sometimes due to the popularity of a model we may need to implement custom rate limits or access restrictions. These exceptions will be listed in our documentation.

Keep in mind that once the limit is hit and enforced, any usage of Together AI services will be blocked until you increase the limit or buy a credit pack.

### Understanding Credit Types and Account Tiers

**Important:** Having credits in your balance doesn't automatically upgrade your account tier. There are two types of credits:

* **Free credits** - Promotional credits granted to your account

* **Purchased credits** - Credits you've bought with real money

Even if you have free credits showing in your balance, you may still be on the **Limited tier** and unable to access your API key. Build Tier 1 and higher tiers are unlocked only after **\$5 of actual account spend**

If you're seeing tier-related access errors despite having credits, check whether your credits are free credits or purchased credits. You may need to make an actual purchase to upgrade your tier status.

## Build Tier Update Delay After Purchase

Purchasing Together AI credits can take up to **15 minutes** for our backend to finish updating your account's Build Tier and grant any new model access that comes with it. This delay is normal and does not affect the credits themselves; they are already reserved for you.

### What you may notice while the update is in progress

* Your **credit balance** in the dashboard may still show the old amount.
* **Tier-restricted models** (for example, Flux.Kontext) remain grayed out or return "insufficient tier" errors.
* API calls that require the new tier will continue to be rejected with HTTP 403 until propagation is complete.

### What you should do

1. **Wait up to 15 minutes** after your payment confirmation email arrives.
2. **Refresh the billing page** or re-query the `/v1/models` endpoint after the 15-minute mark.
3. If nothing changes, clear your browser cache or log out and back in to rule out a stale UI state.

**Still no change?** Open a support ticket in the dashboard under **Help > Contact Support** and include the email address used for the purchase and the approximate time of purchase (including time zone). Our team will verify the payment and, if necessary, force-sync your account to the correct Build Tier.

## Cost Analytics

Together AI provides built-in spend analytics so you can track usage and costs across products and models over time.

To access cost analytics, navigate to your [billing settings](https://api.together.ai/settings/billing) and scroll to the **Usage** section. You can also click the **Current Usage** button to see a draft view of your monthly invoice.

<img src="https://mintcdn.com/togetherai-52386018/njNlMJV1kpet7E_h/images/billing-cost-analytics.png?fit=max&auto=format&n=njNlMJV1kpet7E_h&q=85&s=14bab7be7ebb01122ff337722b4a9ecb" alt="Cost analytics dashboard showing daily spend by product" width="2244" height="1222" data-path="images/billing-cost-analytics.png" />

### Filtering and Grouping

The dashboard supports several ways to slice your data:

* **Group by Product** - See daily costs broken down by product (Endpoints, Storage, Serverless Inference)
* **Group by Line Item** - View a more granular breakdown of individual usage line items
* **Filter by Product** - Focus on a specific product to isolate its spend
* **Filter by Time Range** - Adjust the date range to analyze any period of usage history

The chart updates in real time as you change filters, and the total cost for the selected period is shown in the top right of the chart.


Built with [Mintlify](https://mintlify.com).