# Source: https://getlago.com/docs/guide/plans/charges/usage-based-charges.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage based charge

> Usage-based charges let you bill customers based on actual consumption. They are tied to billable metrics and calculated from usage events collected during the billing period.

## Overview of charges[](#overview-of-charges "Direct link to heading")

Usage-based charges allow you to add pay-as-you-go pricing to a plan.
Each charge is linked to an existing [billable metric](/guide/billable-metrics/create-billable-metrics) and calculated from the events collected during the billing period.

Common examples include API calls, active users, transactions, or compute time.
Pricing follows the charge configuration (tiers, aggregation, proration, etc.), ensuring invoices reflect real usage rather than a fixed amount.

## Charge models and billing behavior[](#charge-models "Direct link to heading")

Charges support a set of pricing options compared to the fixed charges.
They can use:

* [All charge models](/guide/plans/charges/charge-models).

They can be configured to:

* Be billed [in advance or in arrears](/guide/plans/charges/arrears-vs-advance);
* Be billed [in full or prorated](/guide/plans/charges/prorated-vs-full);
* Apply [spending minimums](/guide/plans/charges/spending-minimum) depending on the charge model;
* Support [filters](/guide/plans/charges/charges-with-filters) to control which events are included in usage calculations;
* Be grouped by [presentation keys](/guide/plans/charges/grouping) to display related usage together on invoices;
* Be marked as [invoiceable or not](/guide/plans/charges/invoiceable-vs-noninvoiceable) when billed in advance, to avoid generating too many invoices from usage events.

## Currency[](#charges-currency "Direct link to heading")

All usage-based charges use the same currency as the plan, ensuring consistency across invoices.

## Trial period[](#trial-period-exclusion "Direct link to heading")

The trial period applies only to the plan’s base amount and does not cover usage-based charges.
Usage events recorded during the trial are always considered and billed.

## Decimals precision[](#number-of-decimals "Direct link to heading")

Charges can be defined with up to 15 decimal places (for example: \$0.000123456789123).
Charges are invoiced in `amount_cents`, so Lago automatically rounds values when generating invoices (for example, USD 1102 `amount_cents` = \$11.02).

## Delete a charge[](#delete-charge "Direct link to heading")

You can delete a charge even if the plan is associated to active [subscriptions](/guide/subscriptions/assign-plan).

Once deleted and saved:

* The charge is immediately removed from all linked subscriptions
* It no longer appears in customer [current usage](/api-reference/customer-usage/customer-usage-object); and
* It is removed from all `draft` invoices.

However, the charge will still appear on invoices `finalized` before the deletion.

<Info>
  Deleting a charge does not delete the underlying events.\
  If the charge is later re-added, previously collected events may be included in billing, depending on the billing period limits.
</Info>

<Frame caption="How to delete a charge">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=74bbf2112c864a65b69f1d230bc03c92" data-og-width="1636" width="1636" data-og-height="884" height="884" data-path="guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f1e007296dc4581ad8d07c7004f16b45 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0bb99a3472f521b3ef820fdb0cd10c86 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=b446d8ef8f857cc62e47c78b2488b147 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=52a80e1e35f94b7e097259e758d2d1ae 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0885dfcd14af6496b94ecc85b3387b2b 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charges-delete-e8b82428bc7fe73f40f419fb6ee88dab.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=49202dc37f9892abf01bfa5057f1c589 2500w" />
</Frame>

## Invoice display name[](#invoice-display-names "Direct link to heading")

You can customize, during plan creation or edition, how a charge appears on invoices by setting an `invoice display name`.
This name overrides the default charge name and is shown everywhere invoices are displayed.

<Frame caption="How to modify the invoice display name">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/invoice-display-name.gif?s=7ea713a92d62bb341b2d17c543901a3a" data-og-width="1158" width="1158" data-og-height="720" height="720" data-path="guide/plans/images/invoice-display-name.gif" data-optimize="true" data-opv="3" />
</Frame>
