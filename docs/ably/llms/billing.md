# Source: https://ably.com/docs/liveobjects/concepts/billing.md

# Source: https://ably.com/docs/platform/pricing/billing.md

# Billing

Your monthly bills are calculated based on the base package fee, plus your usage for that month.

Usage is calculated on the last day of the month and invoices are issued in arrears on the 1st of the following month.

Note that minutes are the smallest units that we bill against, and they are rounded up. So if a connection was open for 10.01 minutes then this will be billed as 11 minutes of usage.

## Upgrades and downgrades

For package upgrades, the base package price will be charged pro-rata from the point in the month that you upgraded. This is true for both base package prices if you are upgrading from a paid package.

Package downgrades take effect on the 1st of the following month.

<Aside data-type='note'>
If you have an [Enterprise package](https://ably.com/docs/platform/pricing/enterprise.md) with Ably, then contact your Customer Success Manager to discuss any details or queries you may have regarding your package.
</Aside>

## Billing details and invoices

The following details will appear on your credit card or bank statement when payments are processed by Ably:

* Name: *Ably Real-Time Ltd London*
* Processor: *Stripe*
* Currency: *$USD*

To update your billing details:

1. Ensure you are the account owner or have the billing [role](https://ably.com/docs/platform/account/users.md).
2. Log in to your [account](https://ably.com/login) and select *Billing* from the *Account* menu.

You can update your payment details and view your invoices in this screen.

It's also possible to have your invoices sent to an accounts department by filling in the *Optional billing email address*.

## Billing alerts

Billing alerts notify you by email when your monthly spending exceeds a set amount if you're on a Standard or Pro package. This feature helps you monitor costs and avoid unexpected charges.

The following steps guide you through setting up billing alerts:

* Log in to your Ably [account.](https://ably.com/login)
* In the [Create new alert](https://ably.com/accounts/any/package#billing-alerts-section) section, select the email address from the dropdown list where you want to receive the alert. The available choices depend on your [user role](https://ably.com/docs/platform/account/users.md#roles).
  * If you are an owner: Yourself and billing users associated with the account.
  * If you are a user with a billing role: Yourself only.
* Enter a value greater than your base package fee in the *Amount* field. This amount sets the threshold at which you will receive a notification.
* Click *Create alert* to save your changes.

## Related Topics

* [Overview](https://ably.com/docs/platform/pricing.md): Understand the pricing models available to you, and understand the benefits of each package type.
* [Limits](https://ably.com/docs/platform/pricing/limits.md): The limits associated with each Ably package.
* [Pricing FAQs](https://ably.com/docs/platform/pricing/faqs.md): A list of the most commonly asked questions related to Ably pricing.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
