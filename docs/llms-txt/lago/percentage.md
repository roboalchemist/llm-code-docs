# Source: https://getlago.com/docs/guide/plans/charges/charge-models/percentage.md

# Percentage

Select the percentage charge model if you want to apply a **percentage and a
fixed fee on transactions** (e.g. bank transfers, ATM withdrawals, etc.).

This charge model is generally used with billable metrics that allow users to
calculate the total amount of transactions (e.g. `sum` aggregation type and
`amount` defined as the event property -
[learn more](/guide/billable-metrics/aggregation-types)).

You can define several parameters for the percentage charge model, including:

* **Percentage rate**: charge rate that applies to the total amount (e.g. 1.2%
  on transactions);
* **Fixed fee (optional)**: fee that applies to each event ingested during the
  billing period (e.g. \$0.10 per transaction);
* **Free units (per event - optional)**: number of events that are not subject to
  the fixed fee;
* **Free units (total amount - optional)**: amount that is not subject to the
  charge rate;
* **Per-transaction spending minimum (per event - optional)**: sets the minimum amount of spending required for each individual transaction; and
* **Per-transaction spending maximum (per event - optional)**: sets the maximum amount of spending required for each individual transaction.

When free units are defined for both the total amount and number of events, Lago
performs checks each time a new event is ingested to determine whether the free
units still apply. In the illustration below for instance, the first 3 events or
\$500 are free.

<Info>**Premium feature ✨**: only users with a premium license can define a per-transaction spending minimum and maximum for the percentage pricing model.
Please **[contact us](mailto:hello@getlago.com)** to get access to Lago Cloud and Lago Self-Hosted Premium.</Info>

<Frame caption="Configuration of the percentage charge model">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f88d747a5cfbf0dd3865507908d083d1" data-og-width="2380" width="2380" data-og-height="1616" height="1616" data-path="guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=345e1e6d121a4587f8681f0ba2c74e0d 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=31c810fa90986722985c252298dbd713 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=453887e828e7bacab8b220bbf7cb547e 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0b5865ea99ff6b4a7114c4365a5ce6b0 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=6f57fcdf334d0094d234c8632c8ef7a8 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/percentage-model-b2657bc04ac57c27cfe3bc3b830fd8dc.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=99782516dee5156893a52ffd89e7ff24 2500w" />
</Frame>

Consider the following list of events:

| Event         | Amount | Total number of events         | Total amount       | Result     |
| ------------- | ------ | ------------------------------ | ------------------ | ---------- |
| Transaction 1 | \$200  | 1 free event (out of 3)        | \$200 (\$500 free) | No charges |
| Transaction 2 | \$100  | 2 free events (out of 3)       | \$300 (\$500 free) | No charges |
| Transaction 3 | \$100  | 3 free events (out of 3)       | \$400 (\$500 free) | No charges |
| Transaction 4 | \$50   | 4 events (free units exceeded) | \$450 (\$500 free) | Charge     |

Therefore, for the fourth transaction, the charge will be \$0.10 x 1 event + 1.2%
of \$50 = \$0.70.
