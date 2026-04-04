# Source: https://docs.together.ai/docs/billing.md

# Billing and Usage Limits

> Understand usage limits, credit packs, build tiers, and billing settings on Together AI.

## Accepted Payment Methods

Together AI accepts all major credit and debit cards on networks including Visa, Mastercard, and American Express. Prepaid cards are not supported.

In some territories, there is a legal requirement for banks to request authorization for every transaction, regardless of whether you have set up recurring billing. In these territories, we send an authorization link to your account's registered email. Please monitor your inbox at the start of the month to approve any outstanding balance payments to avoid service interruption.

## What are Credits Used For?

Together credits are the unit used to measure and charge for usage of Together AI services on your account. Once purchased, credits can be used immediately for:

* API requests
* Dedicated endpoints
* Fine-tuning jobs
* Evaluation jobs
* All other Together AI services

Note that you need sufficient balance to cover the costs of dedicated endpoint creation or fine-tuning/evaluation job creation.

## Free Trial and Access Requirements

Together AI does not currently offer free trials. Access to the Together platform requires a minimum \$5 credit purchase.

A \$100 negative balance limit is being introduced. Users in Build Tiers 1–4 will continue to be billed at the end of the month for usage up to negative \$100. Accruing a balance below negative \$100 in a given month will require prepayment using credits. Current Build Tier 5 users will retain their existing postpaid limits.

## Auto-Recharge Credits

Together supports the ability to automatically purchase additional credits if your account balance falls below a set threshold. To enable this feature, follow these steps:

1. Log into your account by visiting [api.together.ai/settings/billing](https://api.together.ai/settings/billing).

2. Select "Add Credits".

3. Set the following options:

   * **Auto-recharge amount:** The amount of credits to purchase (default \$25).

   * **Auto-recharge threshold:** The account balance at which auto-recharge is triggered.

Note: If you set a threshold above your current balance, auto-recharge will trigger immediately, purchasing credits in increments of your top-up amount until the threshold is met. This may result in multiple purchases if the gap is larger than the top-up amount.

## Credit Expiration

No, prepaid balance credits in your Together.ai account do not currently have an expiration date. You can use your credits at any time after purchase.

If any changes to this policy are made in the future, Together.ai will notify customers in advance through official communications.

At Together AI, we understand that everyone has their own circumstances and we want to make sure that none of our customers are ever put in a tricky situation as a result of an unexpected bill from us.

To try and avoid such a situation, we offer usage based billing and credit packs, which are charged at the time of purchase.

**Important:** Credits purchased after an invoice is generated cannot be used to clear previous invoices or past due balances. Past due balances must be paid separately using a valid payment method, regardless of your available credit balance.

If you don't want to use credit packs, or want to make sure you don't spend any more than you buy in credits you can set a balance limit in your accounts [billing settings](https://api.together.ai/settings/billing). Build Tiers 1-4 have a fixed \$100 limit. Build Tier 5, Scale and Enterprise limits can be higher:

**Important payment method requirements:** When purchasing credit packs or setting up billing, Together.ai only accepts credit or debit cards that are directly tied to a bank account. Pre-paid cards of any kind are not supported by the payment system. If you experience issues with card authorization or declined payments, verify that you're using a standard credit or debit card rather than a pre-paid card.

If you're experiencing access issues with a positive balance, check whether your credits are free credits or purchased credits and verify your account tier in your billing settings.

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

## Managing Payment Cards

Together AI allows you to link only one payment card at a time to your account. You can update this card at any time through your [billing settings](https://api.together.ai/settings/billing).

### Updating Your Payment Card

1. In your billing settings, click the "Update Card" button in the **Payment Info** panel
2. Enter your new card details in the popup window
3. Save and complete any verification steps requested by your card provider

You can follow this flow even if you're updating billing information for the same card, for example if you have a new Tax ID. However, **billing addresses must match your card details due to fraud prevention measures** - you cannot update to a different billing address while keeping the same payment card.

Please note that the Tax ID field won't appear until you have entered your address information.

**Note:** If you need to add your organization name, add a different email address to receive invoices, or add a non-standard Tax ID format, contact Support for assistance. These changes cannot be made through the billing settings interface.

### Removing Payment Cards

When you link a card to Together's systems, it enables updates to your account that allow negative balances, with charges on the 3rd of each month. Due to these account changes, you can only update the linked payment card. You cannot delete the card linked to the account without providing replacement details.

## Viewing Previous Invoices

All of your previous invoices (and current usage) can be viewed and downloaded in your [billing settings](https://api.together.ai/settings/billing).

Just scroll down to billing history.

Note that you may receive \$0 invoices even when using free or pre-purchased credits. These provide a record of your usage, including tokens used and models accessed. You can download the invoice PDF for details.

## Adding Business Details to Invoices

You can add your business name or other details to your invoices. Unfortunately this can't be done through your billing settings at the moment, so reach out to Support and they'll get it sorted for you!

## Troubleshooting Payment Declines

There are many reasons that payments can be declined. If your payment isn't going through, check the following:

* Is there enough money in your account to cover the payment?
* Have you filled in all of the address information when adding the card?
* Is the payment card in date?
* Have you activated the card? (If recently replaced)
* Have you entered the correct CVV number?
* **Have you filled in all of the address information when adding the card?** Ensure the billing address exactly matches what's registered with your card provider, including the zip/post code. Even if your payment provider shows the transaction as approved, address mismatches can still cause declines on our end.
* **Are you using a supported card type?** Together AI only accepts credit or debit cards linked to a bank account. Prepaid cards are not supported and will be declined. Virtual cards are also often blocked by issuing banks for certain types of transactions.
* **Does your card support recurring payments?** Together AI requires payment cards that support recurring payments. Some prepaid cards or cards from certain banks may not support this feature, which can cause payment declines even with valid card information.
* **Are you seeing a \$0 authorization hold from your bank?** This is a normal verification process to confirm your card is active before charging the actual amount. You need to approve this authorization hold in your banking app or with your bank for the real payment to go through.
* **Are you waiting long enough for processing?** Credit purchases can take up to 15 minutes to complete. Avoid re-entering your card details during this processing period, as this may cause multiple credit purchases.
* Is your card frozen/blocked by your bank?
* Does your card have any spending limits that you might have reached?
* Is your bank sending you an additional security prompt that you need to complete?

If you see the error message "We only accept credit or debit cards," this indicates you're trying to use an unsupported payment method. Make sure you're using a regular credit or debit card linked to a bank account, not a prepaid card, virtual card, or alternative payment method.

## Understanding Pending Payments

There are a number of stages to every payment made on the Together AI platform.

First, our payment processor contacts your bank to approve the payment.

When it's approved and the payment has gone through we then generate an invoice which you can access from your account.

Then our payment systems need to update your account balance to reflect the purchase.

Once all of this has happened, your balance updates.

Typically all of this happens within 60 seconds of you confirming the payment. Often instantly. But sometimes there can be a delay in the process, either due to our systems or due to your bank taking longer than expected to confirm the payment.

If this happens, you will see a 'pending' banner on your Together AI dashboard to let you know that we're aware of the transaction, but it's still in progress.

If this is the case, please don't make any further payments. Each further payment will be treated as an individual transaction, so you could end up buying more credit packs than you intended.

### Understanding Credit Types and Account Tiers

**Important:** Having credits in your balance doesn't automatically upgrade your account tier. There are two types of credits:

* **Free credits** - Promotional credits granted to your account

* **Purchased credits** - Credits you've bought with real money

Even if you have free credits showing in your balance, you may still be on the **Limited tier** and unable to access your API key. Build Tier 1 and higher tiers are unlocked only after **\$5 of actual account spend**

If you're seeing tier-related access errors despite having credits, check whether your credits are free credits or purchased credits. You may need to make an actual purchase to upgrade your tier status.

## Understanding Unexpected Charges

If you're seeing charges on your account without making API calls, you may be incurring costs from deployed resources that continue to run even when not actively used.

### Common Causes of Unexpected Charges

1. **Fine-tuned Model Hosting**: Deployed fine-tuned models incur per-minute hosting fees regardless of API usage. These charges continue until you stop the endpoint.

2. **Dedicated Endpoints**: These are charged based on hardware allocation, even without active requests. Charges accrue as long as the endpoint remains active.

3. **Serverless Model Usage**: Charged based on actual token usage and model size - you only pay for what you use.

### Managing Your Deployments

To avoid unexpected charges:

1. Visit your [models dashboard](https://api.together.xyz/models)
2. Check for deployed fine-tuned models or active dedicated endpoints
3. Stop any unused endpoints

Monitor usage and pricing at [together.ai/pricing](https://www.together.ai/pricing). Deployment charges are separate from usage charges and credit purchases.

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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt