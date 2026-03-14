# Source: https://docs.together.ai/docs/billing-payment-methods.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Payment Methods & Invoices

> Managing payment cards, ACH transfers, viewing invoices, and updating billing details.

## Supported Payment Methods

Together AI supports two payment methods to fund your account:

* **Credit and debit cards** — accepted from all major networks (Visa, Mastercard, American Express). Available to all customers.
* **ACH bank transfers** — pay directly from a U.S. bank account. Available to customers with an enterprise contract only (early access).

***

## Credit and Debit Cards

Together AI accepts all major credit and debit cards on networks including Visa, Mastercard, and American Express. Prepaid cards are not supported.

<Note>
  In some territories, banks require authorization for every transaction. We send an authorization link to your account's registered email. Monitor your inbox at the start of the month to approve outstanding balance payments and avoid service interruption.
</Note>

### Updating Your Payment Card

Together AI allows you to link only one payment card at a time. You can update it at any time through your [billing settings](https://api.together.ai/settings/billing).

1. In your billing settings, click the "Update Card" button in the **Payment Info** panel
2. Enter your new card details in the popup window
3. Save and complete any verification steps requested by your card provider

You can follow this flow even if you're updating billing information for the same card, for example if you have a new Tax ID. However, **billing addresses must match your card details due to fraud prevention measures** - you cannot update to a different billing address while keeping the same payment card.

Please note that the Tax ID field won't appear until you have entered your address information.

**Note:** If you need to add your organization name, add a different email address to receive invoices, or add a non-standard Tax ID format, contact Support for assistance. These changes cannot be made through the billing settings interface.

### Removing Payment Cards

When you link a card to Together's systems, it enables updates to your account that allow negative balances, with charges on the 3rd of each month. Due to these account changes, you can only update the linked payment card. You cannot delete the card linked to the account without providing replacement details.

***

## ACH Bank Transfers (Early Access)

<Note>
  ACH bank transfers are currently in early access and available to customers with an enterprise contract only. [Contact Support](https://portal.usepylon.com/together-ai/forms/support-request) to request access.
</Note>

ACH (Automated Clearing House) payments allow you to pay for Together AI credits and end of month invoice balances directly from your U.S. bank account. It's a good fit if you're making large purchases or running into credit card limits. You can purchase up to \$100,000 per transaction.

### Adding a bank account

We support most U.S. financial institutions with instant verification. Once your account has been enabled for ACH as a payment method, you can link your bank by following these steps:

1. Go to your [Billing settings](https://api.together.ai/settings/billing)
2. Scroll down to the **Payment Method** block and click the edit icon
3. Select **US Bank Account** at the top of the form that appears
4. Enter your email and full name
5. Search for or select your bank and follow the on-screen steps to authorize your account
6. Enter your billing address
7. Click **Save Payment Method**

<Note>
  Only U.S. financial institutions that support instant verification are available right now. Manual entry of routing and account numbers is not supported.
</Note>

### Purchasing credits

Once your bank account is linked, purchasing credits works the same way as with a credit card.

1. Go to your [Billing settings](https://api.together.ai/settings/billing)
2. Click **Add Credits** in the Credits Balance block
3. Enter an amount (up to \$100,000) and confirm

Because ACH is in early access, credits are deposited into your account immediately — you don't need to wait for the payment to settle. If the payment ultimately fails, your credit balance will be adjusted and your account suspended until the outstanding balance is resolved.

### Things to know

* **One payment method at a time.** Using ACH as a payment method replaces a saved credit card. If you want to switch back to a card, you can add new card details at any time, which will replace the bank account.
* **Auto-recharge is not available with ACH.** If you have auto-recharge enabled, it will be turned off when you switch to bank transfer.
* **Failed payments.** If a payment fails, your credit balance will be adjusted. Contact [Support](https://portal.usepylon.com/together-ai/forms/support-request) if you have questions about a failed transaction.

### Troubleshooting

**My bank isn't showing up in the list.**
Only U.S. banks that support instant verification are currently available. If your institution isn't listed, try searching by name or contact [Support](https://portal.usepylon.com/together-ai/forms/support-request).

**I got an error during bank selection.**
This can happen if your bank is temporarily unable to verify the account link. Contact [Support](https://portal.usepylon.com/together-ai/forms/support-request) and we'll help investigate.

**I got an error after clicking Save.**
Try refreshing the page and attempting again. If the issue persists, reach out to [Support](https://portal.usepylon.com/together-ai/forms/support-request) with any error details.

***

## Viewing Previous Invoices

All of your previous invoices (and current usage) can be viewed and downloaded in your [billing settings](https://api.together.ai/settings/billing).

Just scroll down to billing history.

Note that you may receive \$0 invoices even when using free or pre-purchased credits. These provide a record of your usage, including tokens used and models accessed. You can download the invoice PDF for details.

## Adding Business Details to Invoices

You can add your business name or other details to your invoices. Unfortunately this can't be done through your billing settings at the moment, so reach out to Support and they'll get it sorted for you!


Built with [Mintlify](https://mintlify.com).