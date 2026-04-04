# Source: https://getlago.com/docs/templates/per-transaction/stripe.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone Stripe pricing

> Replicate Stripe's per-transaction pricing model with Lago.

Implement a per-transaction pricing model like Stripe, the leading payments infrastructure company, including fees based on the total amount and number of transactions.

In this article, you will learn how to build a per-transaction billing system with Lago, where a single event can trigger instant charges.
This template is suitable for companies whose pricing depends on transactions, such as fintechs and marketplaces that deduct their fees from their customers' revenue.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SBc7eB3T0rE?si=EAmRNU92Bgrh7w_B&start=62" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Pricing structure

Stripe offers "pay-as-you-go" pricing based on successful card charges processed via its platform.
Stripe's API includes many payment options. Rates and fixed fees per transaction vary depending on the payment method.

| Payment Method            | Percentage Charge (based on transaction amount) | Fixed Fee (per transaction) |
| ------------------------- | ----------------------------------------------- | --------------------------- |
| Card payments (online)    | 2.9%                                            | \$0.30                      |
| Card payments (in-person) | 2.7%                                            | \$0.05                      |

As Stripe supports more 20 payment methods in the US and most of them share the same charge model, we will focus on card payments.

## Get started

<Steps>
  <Step title="Set up Lago">
    <CodeGroup>
      ```bash cURL theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__API_KEY__"
      ```

      ```python Python theme={"dark"}
      from lago_python_client.client import Client
      from lago_python_client.exceptions import LagoApiError

      client = Client(api_key='__API_KEY__')
      ```

      ```ruby Ruby theme={"dark"}
      require 'lago-ruby-client'

      client = Lago::Api::Client.new(api_key: '__API_KEY__')
      ```

      ```javascript Javascript  theme={"dark"}
      import { Client } from 'lago-javascript-client';

      const client = Client('__API_KEY__');
      ```

      ```go Go theme={"dark"}
      package main

      import (
          "context"
          lago "github.com/getlago/lago-go-client"
      )

      client := lago.New().SetApiKey("__API_KEY__")

      ctx := context.TODO()
      ```
    </CodeGroup>
  </Step>

  <Step title="Create a billable metric">
    Create a billable metric to track transaction usage for each payment method.

    1. Set the `aggregation_type` to `sum_agg` to sum transaction amounts
    2. Set the `field_name` to `amount` to track transaction values
    3. Add a unique `code` for your billable metric
    4. Configure `filters` to distinguish between payment types

    <CodeGroup>
      ```bash cURL highlight={7,9-16} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/billable_metrics" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "billable_metric": {
            "name": "Transaction Amount",
            "code": "__BILLABLE_METRIC_CODE__",
            "description": "Total amount of transactions processed",
            "aggregation_type": "sum_agg",
            "field_name": "amount",
            "filters": [
              {
                "key": "type",
                "values": ["online", "in-person"]
              }
            ]
          }
        }'
      ```

      ```python Python highlight={3-6,10,12-14,17} theme={"dark"}
      from lago_python_client.models import BillableMetric, BillableMetricFilter

      billable_metric_filter = BillableMetricFilter(
        key='type',
        values=['online', 'in-person']
      )

      billable_metric = BillableMetric(
        name='Transaction Amount',
        code='__BILLABLE_METRIC_CODE__',
        description='Total amount of transactions processed',
        aggregation_type='sum_agg',
        field_name='amount',
        filters=[billable_metric_filter]
      )

      client.billable_metrics.create(billable_metric)
      ```

      ```ruby Ruby highlight={3,5-12} theme={"dark"}
      client.billable_metrics.create({
        name: 'Transaction Amount',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Total amount of transactions processed',
        aggregation_type: 'sum_agg',
        field_name: 'amount',
        filters: [
          {
            key: 'type',
            values: ['online', 'in-person']
          }
        ]
      })
      ```

      ```javascript Javascript highlight={3,5-12,15} theme={"dark"}
      const billableMetric = {
        name: 'Transaction Amount',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Total amount of transactions processed',
        aggregation_type: 'sum_agg',
        field_name: 'amount',
        filters: [
          {
            key: 'type',
            values: ['online', 'in-person']
          }
        ]
      };

      await client.billableMetrics.createBillableMetric({ billableMetric })
      ```

      ```go Go highlight={3,5-12,15} theme={"dark"}
      billableMetricInput := &lago.BillableMetricInput{
        Name:            "Transaction Amount",
        Code:            "__BILLABLE_METRIC_CODE__",
        Description:     "Total amount of transactions processed",
        AggregationType: "sum_agg",
        FieldName:       "amount",
        Filters: []lago.BillableMetricFilter{
          {
            Key:         "type",
            Values:      []string{"online", "in-person"},
          },
        },
      }

      billableMetric, err := client.BillableMetric().Create(ctx, billableMetricInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/billable-metrics/create) and [guide on filters](/guide/billable-metrics/filters) to learn more.
  </Step>

  <Step title="Create a plan">
    Create a plan with percentage-based charges that are paid in advance.

    1. Set the `amount_cents` to `0` since there is no subscription fee
    2. Configure `charge_model` to `percentage` for percentage-based pricing
    3. Enable `pay_in_advance` for instant charging
    4. Set `invoiceable` to `false` to avoid creating invoices for the charges
    5. Set `charges` with different rates for online vs in-person payments

    <CodeGroup>
      ```bash cURL expandable highlight={7,9,11-37} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/plans" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "plan": {
            "name": "Payment Processing Plan",
            "code": "__PLAN_CODE__",
            "description": "Per-transaction pricing for payment processing",
            "amount_cents": 0,
            "amount_currency": "USD",
            "pay_in_advance": true,
            "charges": [
              {
                "billable_metric_id": "__BILLABLE_METRIC_ID__",
                "invoice_display_name": "Online Card Payment",
                "charge_model": "percentage",
                "invoiceable": false,
                "filters": [
                  {
                    "invoice_display_name": "Online Card Payment",
                    "values": { "type": ["online"] },
                    "properties": {
                      "rate": "2.9",
                      "fixed_amount": "0.30"
                    }
                  },
                  {
                    "invoice_display_name": "In-person Card Payment",
                    "values": { "type": ["in-person"] },
                    "properties": {
                      "rate": "2.7",
                      "fixed_amount": "0.05"
                    }
                  }
                ]
              }
            ]
          }
        }'
      ```

      ```python Python expandable highlight={3-27,32,34-35,38} theme={"dark"}
      from lago_python_client.models import Plan, Charge

      online_charge_filter = ChargeFilter(
        invoice_display_name="Online Card Payment",
        values={"type": ["online"]},
        properties={
          'rate': '2.9',
          'fixed_amount': '0.30'
        }
      )

      in_person_charge_filter = ChargeFilter(
        invoice_display_name="In-person Card Payment",
        values={"type": ["in-person"]},
        properties={
          'rate': '2.7',
          'fixed_amount': '0.05'
        }
      )

      charge = Charge(
        billable_metric_code='__BILLABLE_METRIC_CODE__',
        charge_model='percentage',
        invoiceable=False,
        filters=[online_charge_filter, in_person_charge_filter]
      )

      plan = Plan(
        name='Payment Processing',
        code='__PLAN_CODE__',
        description='Per-transaction pricing for payment processing',
        amount_cents=0,
        amount_currency='USD',
        pay_in_advance=True,
        charges=[charge]
      )

      client.plans.create(plan)
      ```

      ```ruby Ruby expandable highlight={3,5,8-33} theme={"dark"}
      client.plans.create({
        name: 'Payment Processing',
        code: '__PLAN_CODE__',
        description: 'Per-transaction pricing for payment processing',
        amount_cents: 0,
        amount_currency: 'USD',
        pay_in_advance: true,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            invoice_display_name: 'Online Card Payment',
            charge_model: 'percentage',
            invoiceable: false,
            filters: [
              {
                invoice_display_name: 'Online Card Payment',
                values: { type: ['online'] },
                properties: {
                  rate: '2.9',
                  fixed_amount: '0.30'
                }
              },
              {
                invoice_display_name: 'In-person Card Payment',
                values: { type: ['in-person'] },
                properties: {
                  rate: '2.7',
                  fixed_amount: '0.05'
                }
              }
            ]
          }
        ]
      })
      ```

      ```javascript Javascript expandable highlight={3,5,7,8-33,36} theme={"dark"}
      const plan = {
        name: 'Payment Processing Plan',
        code: '__PLAN_CODE__',
        description: 'Per-transaction pricing for payment processing',
        amount_cents: 0,
        amount_currency: 'USD',
        pay_in_advance: true,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            invoice_display_name: 'Online Card Payment',
            charge_model: 'percentage',
            invoiceable: false,
            filters: [
              {
                invoice_display_name: 'Online Card Payment',
                values: { type: ['online'] },
                properties: {
                  rate: '2.9',
                  fixed_amount: '0.30'
                }
              },
              {
                invoice_display_name: 'In-person Card Payment',
                values: { type: ['in-person'] },
                properties: {
                  rate: '2.7',
                  fixed_amount: '0.05'
                }
              }
            ],
          },
        ],
      };

      await client.plans.createPlan({ plan });
      ```

      ```go Go expandable highlight={3,5,7,8-37,40} theme={"dark"}
      planInput := &lago.PlanInput{
        Name:           "Payment Processing Plan",
        Code:           "__PLAN_CODE__",
        Description:    "Per-transaction pricing for payment processing",
        AmountCents:    0,
        AmountCurrency: "USD",
        PayInAdvance:   true,
        Charges: []lago.ChargeInput{
          {
            BillableMetricID:    "__BILLABLE_METRIC_ID__",
            InvoiceDisplayName:  "Online Card Payment",
            ChargeModel:         "percentage",
            Invoiceable:         false,
            Filters: []lago.ChargeFilter{
              {
                InvoiceDisplayName: "Online Card Payment",
                Values: map[string]interface{}{
                  "type":         "online",
                },
                Properties: map[string]interface{}{
                  "rate":         "2.9",
                  "fixed_amount": "0.30",
                },
              },
              {
                InvoiceDisplayName: "In-person Card Payment",
                Values: map[string]interface{}{
                  "type":         "in-person",
                },
                Properties: map[string]interface{}{
                  "rate":         "2.7",
                  "fixed_amount": "0.05",
                },
              },
            },
          },
        },
      }

      plan, err := client.Plan().Create(ctx, planInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/plans/create) and [guide on percentage charges](/guide/plans/charges/charge-models/percentage) to learn more.
  </Step>

  <Step title="Create a customer">
    Create a customer with a unique `external_id`.

    <CodeGroup>
      ```bash cURL highlight={6} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/customers" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "customer": {
            "external_id": "__EXTERNAL_CUSTOMER_ID__",
            "name": "Acme Inc",
            "email": "john@acme.com",
            "currency": "USD",
            "timezone": "America/New_York"
          }
        }'
      ```

      ```python Python highlight={4,11} theme={"dark"}
      from lago_python_client.models import Customer

      customer = Customer(
        external_id="__EXTERNAL_CUSTOMER_ID__",
        name="Acme Inc",
        email="john@acme.com",
        currency="USD",
        timezone="America/New_York"
      )

      client.customers.create(customer)
      ```

      ```ruby Ruby highlight={2} theme={"dark"}
      client.customers.create(
        external_id: "__EXTERNAL_CUSTOMER_ID__",
        name: "Acme Inc", 
        email: "john@acme.com",
        currency: "USD",
        timezone: "America/New_York"
      )
      ```

      ```js Javascript highlight={2,9} theme={"dark"}
      const customer = {
        external_id: "__EXTERNAL_CUSTOMER_ID__",
        name: "Acme Inc",
        email: "john@acme.com",
        currency: "USD",
        timezone: "America/New_York"
      };

      await client.customers.createCustomer({ customer });
      ```

      ```go Go highlight={2,9} theme={"dark"}
      customerInput := &lago.CustomerInput{
        ExternalID: "__EXTERNAL_CUSTOMER_ID__",
        Name:       "Acme Inc",
        Email:      "john@acme.com",
        Currency:   "USD",
        Timezone:   "America/New_York",
      }

      customer, err := client.Customer().Create(ctx, customerInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/customers/create) to create a customer.
  </Step>

  <Step title="Create a subscription">
    Create a subscription for the customer with the plan's `code`.

    <CodeGroup>
      ```bash cURL highlight={6-8} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/subscriptions" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "subscription": {
            "external_customer_id": "__EXTERNAL_CUSTOMER_ID__",
            "plan_code": "__PLAN_CODE__",
            "external_id": "__EXTERNAL_SUBSCRIPTION_ID__"
          }
        }'
      ```

      ```python Python highlight={4-6,9} theme={"dark"}
      from lago_python_client.models import Subscription

      subscription = Subscription(
        external_customer_id="__EXTERNAL_CUSTOMER_ID__",
        plan_code="__PLAN_CODE__",
        external_id="__EXTERNAL_SUBSCRIPTION_ID__"
      )

      client.subscriptions.create(subscription)
      ```

      ```ruby Ruby highlight={2-4} theme={"dark"}
      client.subscriptions.create(
        external_customer_id: "__EXTERNAL_CUSTOMER_ID__",
        plan_code: "__PLAN_CODE__",
        external_id: "__EXTERNAL_SUBSCRIPTION_ID__"
      )
      ```

      ```js Javascript highlight={2-4,7} theme={"dark"}
      const subscription = {
        external_customer_id: "__EXTERNAL_CUSTOMER_ID__",
        plan_code: "__PLAN_CODE__",
        external_id: "__EXTERNAL_SUBSCRIPTION_ID__"
      };

      await client.subscriptions.createSubscription({ subscription });
      ```

      ```go Go highlight={2-4,7} theme={"dark"}
      subscriptionInput := &lago.SubscriptionInput{
        ExternalCustomerID: "__EXTERNAL_CUSTOMER_ID__",
        PlanCode:           "__PLAN_CODE__",
        ExternalID:         "__EXTERNAL_SUBSCRIPTION_ID__",
      }

      subscription, err := client.Subscription().Create(ctx, subscriptionInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/subscriptions/assign-plan) to create a subscription.

    Refer to [API reference](/api-reference/subscriptions/assign-plan) and [guide on assigning plans](/guide/subscriptions/assign-plan) in the documentation.
  </Step>

  <Step title="Ingest transactions via events">
    Send transaction events to Lago for instant processing and charging.

    1. Set the `code` to match your billable metric code
    2. Use `external_customer_id` to identify the customer
    3. Include `amount` in properties for the transaction value
    4. Add `type` property to specify online or in-person payment

    <CodeGroup>
      ```bash cURL highlight={7-12} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/events" \
       --header "Authorization: Bearer $API_KEY" \
       --header 'Content-Type: application/json' \
       --data-raw '{
         "event": {
           "transaction_id": "__TRANSACTION_ID__",
           "code": "__BILLABLE_METRIC_CODE__",
           "external_subscription_id": "__EXTERNAL_SUBSCRIPTION_ID__",
           "properties": {
             "amount": 200,
             "type": "online"
           }
         }
       }'
      ```

      ```python Python highlight={5-10,13} theme={"dark"}
      from lago_python_client.models import Event

      event = Event(
        transaction_id="__TRANSACTION_ID__",
        code="__BILLABLE_METRIC_CODE__",
        external_subscription_id="__EXTERNAL_SUBSCRIPTION_ID__",
        properties={
          "amount": 200,
          "type": "online"
        }
      )

      client.events.create(event)
      ```

      ```ruby Ruby highlight={3-8} theme={"dark"}
      client.events.create(
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          "amount": 200,
          "type": "online"
        }
      )
      ```

      ```js Javascript highlight={3-8,11} theme={"dark"}
      const event = {
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          "amount": 200,
          "type": "online"
        }
      };

      await client.events.createEvent({ event });
      ```

      ```go Go highlight={3-8,11} theme={"dark"}
      eventInput := &lago.EventInput{
        TransactionID:          "__TRANSACTION_ID__",
        Code:                   "__BILLABLE_METRIC_CODE__",
        ExternalSubscriptionID: "__EXTERNAL_SUBSCRIPTION_ID__",
        Properties: map[string]interface{}{
          "amount": 200,
          "type":   "online",
        },
      }

      event, err := client.Event().Create(ctx, eventInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/events/usage) to create an event.
  </Step>

  <Step title="Estimate fees for future transactions">
    Calculate transaction fees before processing to show users expected costs.

    1. Use `external_subscription_id` to identify the subscription
    2. Set the `code` to match your billable metric code
    3. Include `amount` for the transaction value to estimate
    4. Add `type` to get accurate rates for payment method

    <CodeGroup>
      ```bash cURL highlight={6-11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/events/estimate_fees" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "event": {
            "external_subscription_id": "__EXTERNAL_SUBSCRIPTION_ID__",
            "code": "__BILLABLE_METRIC_CODE__",
            "properties": {
              "amount": 1200,
              "type": "online"
            }
          }
        }'
      ```

      ```python Python highlight={4-9,12} theme={"dark"}
      from lago_python_client.models import Event

      event = Event(
        external_subscription_id="__EXTERNAL_SUBSCRIPTION_ID__",
        code="__BILLABLE_METRIC_CODE__",
        properties={
          "amount": 1200,
          "type": "online"
        }
      )

      client.events.estimate_fees(event)
      ```

      ```ruby Ruby highlight={2-7} theme={"dark"}
      client.events.estimate_fees(
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        properties: {
          "amount": 1200,
          "type": "online"
        }
      )
      ```

      ```javascript Javascript highlight={2-7,10} theme={"dark"}
      const event = {
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        properties: {
          "amount": 1200,
          "type": "online"
        }
      };

      await client.events.eventEstimateFees({ event });
      ```

      ```go Go highlight={2-7,10} theme={"dark"}
      eventEstimateInput := &lago.EventEstimateFeesInput{
        ExternalSubscriptionID: "__EXTERNAL_SUBSCRIPTION_ID__",
        Code:                   "__BILLABLE_METRIC_CODE__",
        Properties: map[string]string{
          "amount": 1200,
          "type": "online",
        },
      }

      estimateFees, err := client.Event().EstimateFees(ctx, eventEstimateInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/events/estimated-fee) to estimate fees.
  </Step>
</Steps>

## Wrap-up

For fintech companies like Stripe, implementing a per-transaction pricing model is a good way to **increase revenue as customers grow and capture value everytime a transaction is processed**.
With Lago, you can create your own billable metrics and use the percentage charge model paid instantly to adapt this template to your products and services.

Give it a try, click [here](https://www.getlago.com/get-started) to get started!
