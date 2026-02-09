# Source: https://getlago.com/docs/guide/plans/commitment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Commitments

<Info>
  **Premium feature ✨**:

  This feature is only available to users with a premium license. Please **[contact us](mailto:hello@getlago.com)** to get access to Lago Cloud and Lago Self-Hosted Premium.
</Info>

In your plan configuration, Lago provides the flexibility to define specific spending commitments tailored to your business needs.
These commitments serve as a financial baseline for the services you offer. However, understanding the unique requirements of each customer,
Lago offers the capability to customize these commitments on a per-customer basis at the time of creating a subscription.

## Minimum commitment

### Guidelines

Besides setting [spending minimums per charge](/guide/plans/charges/spending-minimum), Lago also allows you to define minimum invoice totals.
This ensures customers meet a minimum spend per billing period, securing a steady revenue flow and aiding in accurate financial forecasting.
The minimum commitment per invoice set in Lago applies to the total spending in the billing period including -if applicable- the subscription fee and all usage-based fees.

* **Commitment interval:** The minimum commitment is aligned with the billing interval of the plan. For instance, if the plan is billed monthly, the minimum commitment is also established on a monthly basis;
* **Customizable commitments:** When assigning a plan to a customer, you have the option to override the default commitment. This allows for customized minimum commitments per customer, accommodating negotiated contract terms; and
* **Arrears calculation:** The commitment is calculated in arrears, meaning Lago waits until the end of the billing period to assess whether users have met their minimum spending commitment. This approach ensures accurate billing based on actual usage.

### True-up fee

If the total spending falls below the minimum commitment at the end of the billing period, Lago will **apply a true-up fee to adjust the invoice and meet the minimum spending requirement**.
Conversely, if spending exceeds the minimum commitment, Lago will generate an invoice for the actual consumption, without issuing a true-up fee.

<Info>
  The minimum commitment is calculated based on the pre-tax amount and before any discounts (such as coupons or credits) are applied.
</Info>

### Defining a minimum commitment

<Tabs>
  <Tab title="Dashboard">
    To create or update a minimum commitment from the user interface:

    1. Access an existing or a new plan **"Plan"**;
    2. Navigate below usage based charges;
    3. Define a **minimum commitment**; and
    4. Click **"Add plan"** to confirm.

    <Frame caption="Define a minimum commitment">
      <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/minimum-commitment-on-plan.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=7c4d75015b62584cea23adf8fb51c4f0" data-og-width="1702" width="1702" data-og-height="1408" height="1408" data-path="guide/payments/images/minimum-commitment-on-plan.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/minimum-commitment-on-plan.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=35bda87f1ea6af29729f7fe975f0af9d 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/minimum-commitment-on-plan.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=29b48e8f7da42bff66fd32efeae9071f 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/minimum-commitment-on-plan.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=a9d5612f2503bb65a63f2f375d69144e 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/minimum-commitment-on-plan.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=627421fb9618453e1bf232e8a6877e5d 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/minimum-commitment-on-plan.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=e3805690b2b5212615ff368994e11294 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/minimum-commitment-on-plan.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=fb4089f730a6a97a9af524127726df27 2500w" />
    </Frame>

    <Info>
      The minimum commitment must follow the plan's interval. You can add a specific tax rate for this minimum commitment.
    </Info>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```json Define a minimum commitment {16-22} theme={"dark"}
      {
          "plan": {
            "name": "Basic",
            "invoice_display_name": null,
            "created_at": "2024-02-23T16:01:04Z",
            "code": "basic",
            "interval": "monthly",
            "description": "",           
            "amount_cents": 10000,
            "pay_in_advance": true,
            "bill_charges_monthly": null,
            "customers_count": 2,
            "active_subscriptions_count": 2,
            "draft_invoices_count": 0,
            "parent_id": null,
            "minimum_commitment": {
              "plan_code": "basic",
              "invoice_display_name": "Minimum Contract Commitment",
              "amount_cents": 50000,
              "interval": "monthly",
              "taxes": []
              },
            "charges": [
                {
                  "id": "ca205886-cf09-4e42-aed6-34cb2afd0c29",
                  "billable_metric_id": "5b320600-715b-4ef5-88c1-4f88c0ec5c50",
                  "invoice_display_name": "",
                  "billable_metric_code": "storage",
                  "created_at": "2024-02-23T16:01:04Z",
                  "charge_model": "standard",
                  "invoiceable": true,
                  "pay_in_advance": false,
                  "prorated": false,
                  "properties": {
                      "amount": "1"
                  },
                  "group_properties": [],
                  "taxes": []
                },
                {
                  "id": "1d5c78c6-0e22-424f-af8d-6784f6ff44ec",
                  "billable_metric_id": "4cbc5940-32fb-48a8-aa39-ad664b34a062",
                  "invoice_display_name": null,
                  "billable_metric_code": "seats",
                  "created_at": "2024-02-23T16:04:09Z",
                  "charge_model": "standard",
                  "invoiceable": true,
                  "pay_in_advance": true,
                  "prorated": false,
                  "min_amount_cents": 0,
                  "properties": {
                      "amount": "7"
                  },
                  "group_properties": [],
                  "taxes": []
                }
              ],
            "taxes": []
          }
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Overwriting a minimum commitment

<Tabs>
  <Tab title="Dashboard">
    To overwrite the minimum commitment for a specific customer, follow these instructions:

    1. Access a specific customer;
    2. Choose to assign a new plan or edit an existing subscription; and
    3. Override the default plan's minimum commitment with a new value.

    <Frame caption="Overwriting a minimum commitment">
      <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/overwriting-minimum-commitment.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=bd591710ee82e36b1cd1c95a7988360b" data-og-width="2914" width="2914" data-og-height="1338" height="1338" data-path="guide/payments/images/overwriting-minimum-commitment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/overwriting-minimum-commitment.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9b793845b05bbb8f457aba41528a83a2 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/overwriting-minimum-commitment.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=47e9b7992a2302e56ce9a3b8b4538441 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/overwriting-minimum-commitment.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=d47a5dc39679571621a1bdaac53f8838 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/overwriting-minimum-commitment.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=d47de28e5292730eba32eab0df197339 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/overwriting-minimum-commitment.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=73384b4647de667caa61cbfd5bead370 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/overwriting-minimum-commitment.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=407115f985ddef2d0f65ea0d9a3f041f 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```json Define a minimum commitment theme={"dark"}
          {
          "subscription": {
            "external_customer_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
            "plan_code": "premium",
            "name": "Repository A",
            "external_id": "my_sub_1234567890",
            "billing_time": "anniversary",
            "subscription_at": "2022-08-08T00:00:00Z",
            "plan_overrides": {
              "amount_cents": 10000,
              "amount_currency": "USD",
              "description": "Plan for early stage startups.",
              "invoice_display_name": "Startup plan",
              "name": "Startup",
              "tax_codes": [],
              "minimum_commitment": {
                "plan_code": "basic",
                "invoice_display_name": "Minimum Contract Commitment",
                "amount_cents": 50000,
                "interval": "monthly",
                "taxes": []
              }
              "charges": []
            }
          }
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>
