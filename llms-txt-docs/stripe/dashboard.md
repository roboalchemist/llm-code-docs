# Source: https://docs.stripe.com/connect/dashboard.md

# Manage connected accounts with the Dashboard

Learn about using the Stripe Dashboard to find and manage connected accounts.

You can use the Dashboard to inspect, support, and better understand your platform’s connected accounts. Some common tasks that the Dashboard supports include:

- [View all accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts.md)
- [Take action on requirement updates](https://docs.stripe.com/connect/dashboard/review-compliance-information.md#requirement-updates)
- [Create accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md#creating-accounts)
- [Find individual accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md#finding-accounts)
- [Update account information](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md#updating-accounts)
- [Send funds to accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md#sending-funds)

[View all accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts.md) at a high-level or filter and sort them to find a specific group of accounts. Use filtering to:

- View accounts that are restricted or have other issues that you can help resolve.
- View your largest accounts.
- View accounts based on their status.

[Review compliance information to take action on requirement updates](https://docs.stripe.com/connect/dashboard/review-compliance-information.md#requirement-updates). Use the instructions provided to make sure that your connected accounts remain [enabled](https://docs.stripe.com/connect/dashboard.md#enabled) when requirements change.

The other workflows, such as inspecting accounts and sending funds, are actions you can take on [individual accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md). Take these actions after you know which accounts you need to inspect or modify.

Before viewing and making changes to accounts, learn more about the Dashboard [status badges](https://docs.stripe.com/connect/dashboard.md#status-badges).

## Status badges 

Status badges provide a way to understand the status of an account. You can hover over the badges to view contextual information, and you can click the [status tabs](https://docs.stripe.com/connect/dashboard/viewing-all-accounts.md#tabs-workflows) to view accounts grouped by that status. Status badges include:

| Status                                                                          | Badge             |
| ------------------------------------------------------------------------------- | ----------------- |
| [Restricted](https://docs.stripe.com/connect/dashboard.md#restricted)           | (Restricted)      |
| [Restricted soon](https://docs.stripe.com/connect/dashboard.md#restricted-soon) | (Restricted soon) |
| [In review](https://docs.stripe.com/connect/dashboard.md#in-review)             | (In review)       |
| [Enabled](https://docs.stripe.com/connect/dashboard.md#enabled)                 | (Enabled)         |
| [Rejected](https://docs.stripe.com/connect/dashboard.md#rejected)               | (Rejected)        |

### Restricted 

**Restricted** means the account has at least one primary capability inactive. This might include *payouts* (A payout is the transfer of funds to an external account, usually a bank account, in the form of a deposit), treasury, issuing, crypto, and so on. This doesn’t include inactive payment methods. Additional information usually needs to be collected to enable these accounts. Click on an account to view details about any inactive capabilities and their requirements.

If information is required to enable the account, it appears in an **Actions required** list at the top of the Connected account details page.

### Restricted soon 

**Restricted soon** means the account has currently due requirements with an upcoming due date providing additional information.

If information is required to enable the account, it appears in an **Actions required** list at the top of the Connected account details page.

### In review 

**In review** means the account is being reviewed or verified by Stripe. This occurs when:

- Stripe is verifying the information that was provided, such as an uploaded government-issued ID document.
- Stripe is performing a watchlist check against a list of prohibited individuals and businesses.
- Stripe is reviewing the account for suspected fraudulent activity.

Review times vary depending on the requirement, but they typically last 24–48 hours.

### Enabled 

**Enabled** means the account is in good standing with all primary capabilities enabled on the account. Some accounts might require additional information when they reach a new payment volume [threshold](https://docs.stripe.com/connect/identity-verification.md#verification-requirements).

If additional information is required eventually, in the account’s [requirements](https://docs.stripe.com/api/accounts/object.md#account_object-requirements) hash, the array `eventually_due` contains at least one requirement, but payments and payouts are enabled and `current_deadline` is empty.

### Rejected 

**Rejected** means you (the platform) or Stripe rejected the connected account. Hover over the status badge to see whether you (the platform) or Stripe rejected the account.

Check the **Actions required** list at the top of the Connected account details page to see the reason the account was rejected. In general, accounts are rejected by Stripe if they’re suspected of fraudulent activity.

## Use Platform Branding for Connected Accounts

This setting only applies to new accounts created by your platform. Existing accounts aren’t affected.

As the platform, you can initialize newly created connected accounts with your platform branding settings. To do so, go to **Connect Settings** > **Branding** and enable **Copy Platform Branding**. After you enable it, all new accounts onboarding to your platform receive the same branding settings as your platform.

Use [Account Update](https://docs.stripe.com/api/accounts/update.md) to update the account’s branding after creation.

## See also

- [Viewing all accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts.md)
- [Managing individual accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md)
