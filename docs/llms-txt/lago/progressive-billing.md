# Source: https://getlago.com/docs/guide/plans/progressive-billing.md

# Progressive billing

> Progressive billing, also known as threshold billing, automatically triggers an invoice when a customer's cumulative usage reaches predefined thresholds. This method ensures that customers cannot exceed certain usage limits without ensuring payment is received, reducing the risk of unpaid services or fraud.

<Info>
  **PREMIUM ADD-ON** ✨

  This progressive billing feature is available upon request only. Please [**contact us**](mailto:hello@getlago.com) to get access to this premium feature.
</Info>

## Lifetime usage

In the context of progressive billing, thresholds and invoicing behavior are **determined by the lifetime usage of a subscription**.
This approach means that Lago continuously tracks and aggregates **the total usage across all billing periods**.
By considering this cumulative usage, Lago can accurately assess whether a customer has reached predefined thresholds.

When the lifetime usage reaches a specific threshold, Lago automatically triggers the invoicing process, ensuring that usage is invoiced promptly before it exceeds the specified limits. This mechanism helps prevent overuse of services without corresponding invoice and payment, offering a safeguard against potential revenue leakage. It's important to note that lifetime usage is persistent across periods, meaning that even if a customer's usage fluctuates, Lago will account for the entire history to determine if and when an invoice should be issued.

<Info>
  The lifetime usage is calculated based on the usage amount before taxes.
</Info>

## Setting up thresholds

<Frame caption="Setting up thresholds">
    <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-setting-up-thresholds.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=262ee75ce9ebe35deb96f6fc4bf4f5c1" alt="" data-og-width="3324" width="3324" data-og-height="1366" height="1366" data-path="guide/plans/images/progressive-billing-setting-up-thresholds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-setting-up-thresholds.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=bd13dfa70744065bbdd1c76a58b1a492 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-setting-up-thresholds.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=dce9a91570daf38aeb50d2865ba16047 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-setting-up-thresholds.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=867216e054b3696fae8e050383e03990 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-setting-up-thresholds.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=6f7ec6d08facf2811bcb2ae19e42754a 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-setting-up-thresholds.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e427803b72448a1f758d97f026cfff9a 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-setting-up-thresholds.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=672e96901d6c383b736fb29cea223706 2500w" />
</Frame>

For the progressive billing feature, you can configure two types of thresholds: Step-Based Thresholds and Recurring Thresholds.

### Step-based thresholds

<Tabs>
  <Tab title="Dashboard">
    For Step-Based Thresholds, invoices are generated when the lifetime usage of a subscription reaches a defined threshold.
    You can set an unlimited number of thresholds, each with a specific amount and a unique name.

    To add progressive billing Step-Based Thresholds from the UI:

    1. Navigate to the desired plan;
    2. Access the Advanced Settings;
    3. Locate the Progressive Billing section; and
    4. Add your thresholds.

    <Frame caption="Defining step-based thresholds">
            <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-step-thresholds.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=24559ff19e41204afc4aa6e255b0dc88" alt="" data-og-width="1516" width="1516" data-og-height="1150" height="1150" data-path="guide/plans/images/progressive-billing-step-thresholds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-step-thresholds.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0297f92ef5674f76e89b274756c847c1 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-step-thresholds.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f7ab2e23c88028459bc53e98d6542305 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-step-thresholds.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=bbedbab463df384ce956ae85445d5257 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-step-thresholds.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=00a479c77840753696ac06f885fdb51c 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-step-thresholds.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=7d190a2092f3c531c5fdbac1517d502c 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-step-thresholds.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=6eeeed13ca1b984ecb1cd2450671bf10 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```json Add progressive billing thresholds {14,15,16,17,18,19,20,21,22,23,24,25,26,27} theme={"dark"}
      {
          "plan": {
              "name": "Premium",
              "invoice_display_name": null,
              "created_at": "2024-08-26T14:23:53Z",
              "code": "premium",
              "interval": "monthly",
              "description": "",
              "amount_cents": 10000,
              "amount_currency": "USD",
              "trial_period": 0.0,
              "pay_in_advance": true,
              "charges": [...],
              "usage_thresholds": [
                  {
                      "amount_cents": 500,
                      "threshold_display_name": "Step 1 "
                  },
                  {
                      "amount_cents": 5000,
                      "threshold_display_name": "Step 2"
                  },
                  {
                      "amount_cents": 10000,
                      "threshold_display_name": "Step 3"
                  }
              ]
          }
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

In the above example, Lago will issue an invoice when the specified threshold is met:

* `Invoice #1`: When the lifetime usage reaches \$5;
* `Invoice #2`: When the lifetime usage reaches \$20;
* `Invoice #3`: When the lifetime usage reaches \$50;
* `Invoice #4`: When the lifetime usage reaches \$100;
* `Invoice #5`: When the lifetime usage reaches \$1,000;
* Then, resume to 'end of the month' billing.

### Recurring threshold

<Tabs>
  <Tab title="Dashboard">
    In addition to Step-Based Thresholds, you can also set up a Recurring Threshold. This threshold determines what happens after the final step-based threshold is reached.
    If a recurring threshold is defined, Lago will continue to issue invoices each time the lifetime usage increases by the specified amount.
    For example, as shown in the image below, after the last threshold, Lago will automatically bill \$100 each time the lifetime usage increments by that amount.

    To add a recurring threshold from the UI:

    1. Navigate to the desired plan;
    2. Access the Advanced Settings;
    3. Locate the Progressive Billing section;
    4. Toggle the 'Recurring' switch; and
    5. Enter a name and define the recurring threshold amount.

    <Frame caption="Defining a recurring threshold">
            <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-recurring-threshold.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=cda9e27f64cba34635d50bd6dc52c9d6" alt="" data-og-width="1500" width="1500" data-og-height="1500" height="1500" data-path="guide/plans/images/progressive-billing-recurring-threshold.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-recurring-threshold.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c66ddb3e932669cc9d8664eb38fbee09 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-recurring-threshold.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=db61e0271477677c41931be7d454e653 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-recurring-threshold.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e0ed5bb253f5b77ff168f91277262653 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-recurring-threshold.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=517586406ff2582b9b6893c3a73db640 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-recurring-threshold.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=cee530df309e710126b4509ce8affd62 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-recurring-threshold.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=28a35ab0db4dd44c9a3224cd3413397f 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```json Add a recurring billing threshold theme={"dark"}
      {
          "plan": {
              "name": "Premium",
              "invoice_display_name": null,
              "created_at": "2024-08-26T14:23:53Z",
              "code": "premium",
              "interval": "monthly",
              "description": "",
              "amount_cents": 10000,
              "amount_currency": "USD",
              "trial_period": 0.0,
              "pay_in_advance": true,
              "charges": [...],
              "usage_thresholds": [
                  {
                      "amount_cents": 500,
                      "threshold_display_name": "Step 1 "
                  },
                  {
                      "amount_cents": 5000,
                      "threshold_display_name": "Step 2"
                  },
                  {
                      "amount_cents": 10000,
                      "threshold_display_name": "Step 3"
                  },
                  {
                  "amount_cents": 5000,
                  "threshold_display_name": "Bill every 50 dollars",
                  "recurring": true
                  }
              ]
          }
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Invoicing behaviors

For our progressive billing feature, invoices are generated whenever a threshold is crossed, regardless of when it occurs within a billing period.
However, there are a few specific behaviors and edge cases related to this feature that are important to consider.

<Frame caption="Progressive billing invoice behavior">
    <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-behavior.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=38b25d30778a9f8fc71ea7fcf9c31779" alt="" data-og-width="4438" width="4438" data-og-height="1048" height="1048" data-path="guide/plans/images/progressive-billing-invoice-behavior.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-behavior.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3d302c291ad7417b4178f3b74ae564d7 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-behavior.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3f0334569e26d13f0bca5c0e9874827e 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-behavior.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f4e191270c0d35493276c370bec59332 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-behavior.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a9a8585e28d2a372b425e2bc9d162130 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-behavior.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ecf7df1296118fdf93cdea525101287a 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-behavior.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=d6d51af6a0eb3050e22b71ff15adb784 2500w" />
</Frame>

### Invoicing during job execution

It's important to note that **threshold billing occurs when our progressive billing job runs** (every 5 minutes by default, though this interval can be adjusted on a case-by-case basis).
This means that Lago does not trigger the invoice immediately when the threshold is crossed but rather at a predefined interval.

As a result, Lago will invoice the total usage at the time the job runs, **which may slightly exceed the threshold**.
For instance, if your billing threshold is \$10 but the job runs when the customer's current usage is \$12, Lago will invoice for the full \$12.

### Charges included in the calculation

**Only charges billed in arrears (recurring or metered) are included in the lifetime usage calculation for progressive billing invoices**.
This means any charges paid in advance are excluded from this progressive billing feature.

### Excluding already billed usage

When a customer crosses a threshold for a specific subscription, Lago will invoice the total usage for the current period,
ensuring that any 'previously billed usage' is excluded.

This approach provides customers with a clear view of their current consumption while preventing them from being charged again
for usage already invoiced under previous thresholds.

It's important to note that the invoice template (as shown below) includes the following details:

* The total usage for the current period;
* An adjustment that excludes previously billed usage; and
* A footer that provides context, explaining the reason for the invoice, including lifetime usage and the threshold that was crossed.

<Frame caption="Progressive billing invoice detail">
    <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-detail.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3ee2c1215155bf28259bba27a415ced1" alt="" data-og-width="1598" width="1598" data-og-height="1806" height="1806" data-path="guide/plans/images/progressive-billing-invoice-detail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-detail.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=b68ef48de7264d1efd66c45ea7b55f38 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-detail.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=26e1723aeb4687d740ecb33258aa8371 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-detail.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ea9ffa7afbcf95656f08ae6496f74692 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-detail.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0214fae9fd5c14a4d3b337098be07549 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-detail.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2df6a15a9c59ffcfa700c8f2d850ad66 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/progressive-billing-invoice-detail.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a406abfadfd96833cdfa817292a9183f 2500w" />
</Frame>

### Grace period edge cases

It's important to note that **progressive billing invoices are not subject to a grace period** and, therefore, cannot be in a `draft` status.
The reason for this is that draft invoices are not `finalized`, and progressive billing calculations are based solely on `finalized` invoices. Including draft invoices in these calculations would significantly alter the accuracy of the progressive billing process.

### Applying discounts

Progressive billing invoices will automatically apply any available discounts, including coupons, prepaid credits, or credit notes.

### Overriding subscription thresholds

To provide maximum flexibility with the progressive billing feature, you can **override the default plan's thresholds for a specific subscription**.
This allows a particular subscription to have its own customized thresholds. You can add or remove thresholds as needed, or even disable the progressive billing feature entirely for a specific subscription.

### Modifying thresholds

You can edit, add, or remove progressive billing thresholds—or even disable this feature—at any time for a plan or subscription.
This flexibility allows you to adjust thresholds to meet your customer's needs without needing to rebuild everything from scratch.

### Being notified

Since progressive billing invoices can be triggered at any time during a billing period, it's crucial to stay informed when a customer crosses a threshold.
Lago sends a [webhook notification](/api-reference/webhooks/messages#subscription-usage-threshold-reached), `subscription.usage_threshold_reached`, providing details about the subscription and the specific threshold that was exceeded.
