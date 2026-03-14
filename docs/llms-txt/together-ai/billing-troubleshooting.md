# Source: https://docs.together.ai/docs/billing-troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Billing Troubleshooting

> Resolving payment issues, understanding charges, and managing billing problems.

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


Built with [Mintlify](https://mintlify.com).