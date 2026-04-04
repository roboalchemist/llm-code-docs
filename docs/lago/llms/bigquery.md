# Source: https://getlago.com/docs/templates/payg/bigquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone Google BigQuery pricing

> Replicate BigQuery's pay-as-you-go pricing model and offer free upfront credits with Lago.

In this article, you will learn how to offer free upfront credits for new users on a 'pay-as-you-go' pricing model.
This template is fitted for infra companies, like this BigQuery example, but is also widely used among AI companies to let new users try their products easily.
[Mistral](https://mistral.ai/news/2024-ft-hackathon/#:~:text=We%20offer%20%24100%20free%20credits%20to%20selected%20hackathon%20participants) or [Perplexity](https://docs.perplexity.ai/docs/pricing#:~:text=pplx%2Dapi%20implements%20a%20usage,of%20free%20credit%20every%20month) are other great examples.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EaRi97Q2BcQ?si=n1WP-vIdVvUzzk3v&start=67" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Pricing structure

BigQuery offers customers the possibility to subscribe for free and only pay based on usage. For new customers, the platform offers \$300 worth of credits during 90 days to try the product completely for free.

| Plan              | Cost per volume of data scanned                |
| ----------------- | ---------------------------------------------- |
| On-Demand pricing | \$6.25 per TiB (a measure of compute capacity) |

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
    Create a billable metric to track data processing volume.

    1. Set the `aggregation_type` to `sum_agg` to sum all data processed
    2. Set the `field_name` to `data_processed_volume` for tracking usage
    3. Set `recurring` to `false` for metered billing

    <CodeGroup>
      ```bash cURL highlight={7,9-11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/billable_metrics" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "billable_metric": {
            "name": "BigQuery Data Processing",
            "code": "__BILLABLE_METRIC_CODE__",
            "description": "Data processing volume in TiB",
            "aggregation_type": "sum_agg",
            "field_name": "data_processed_volume",
            "recurring": false
          }
        }'
      ```

      ```python Python highlight={5,7-9,12} theme={"dark"}
      from lago_python_client.models import BillableMetric

      billable_metric = BillableMetric(
        name='BigQuery Data Processing',
        code='__BILLABLE_METRIC_CODE__',
        description='Data processing volume in TiB',
        aggregation_type='sum_agg',
        field_name='data_processed_volume',
        recurring=False
      )

      client.billable_metrics.create(billable_metric)
      ```

      ```ruby Ruby highlight={3,5-7} theme={"dark"}
      client.billable_metrics.create({
        name: 'BigQuery Data Processing',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Data processing volume in TiB',
        aggregation_type: 'sum_agg',
        field_name: 'data_processed_volume',
        recurring: false
      })
      ```

      ```javascript JavaScript highlight={3,5-7,10} theme={"dark"}
      const billableMetric = {
        name: 'BigQuery Data Processing',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Data processing volume in TiB',
        aggregation_type: 'sum_agg',
        field_name: 'data_processed_volume',
        recurring: false
      };

      await client.billableMetrics.createBillableMetric({ billableMetric })
      ```

      ```go Go highlight={3,5-7,10} theme={"dark"}
      billableMetricInput := &lago.BillableMetricInput{
        Name:             "BigQuery Data Processing",
        Code:             "__BILLABLE_METRIC_CODE__",
        Description:      "Data processing volume in TiB",
        AggregationType:  "sum_agg",
        FieldName:        "data_processed_volume",
        Recurring:        false,
      }

      billableMetric, err := client.BillableMetric().Create(ctx, billableMetricInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/billable-metrics/create) to create a billable metric.
  </Step>

  <Step title="Create a plan">
    Create a plan with graduated pricing to include free tier usage.

    1. Set the `amount_cents` to `0` since there is no subscription fee
    2. Use `graduated` charge model with BigQuery's \$6.25 per TiB rate
    3. Configure first 10 TiB as free, then \$6.25 per TiB after that

    <CodeGroup>
      ```bash cURL highlight={7,10,13-34} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/plans" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "plan": {
            "name": "BigQuery On-Demand",
            "code": "__PLAN_CODE__",
            "interval": "monthly",
            "description": "Pay-as-you-go BigQuery pricing with free tier",
            "amount_cents": 0,
            "amount_currency": "USD",
            "pay_in_advance": false,
            "charges": [
              {
                "billable_metric_id": "__BILLABLE_METRIC_ID__",
                "charge_model": "graduated",
                "properties": {
                  "graduated_ranges": [
                    {
                      "from_value": 0,
                      "to_value": 10000,
                      "per_unit_amount": "0",
                      "flat_amount": "0"
                    },
                    {
                      "from_value": 10001,
                      "to_value": null,
                      "per_unit_amount": "6.25",
                      "flat_amount": "0"
                    }
                  ]
                }
              }
            ]
          }
        }'
      ```

      ```python Python highlight={3-22,26,29,32,35} theme={"dark"}
      from lago_python_client.models import Plan, Charge

      charge = Charge(
        billable_metric_id='__BILLABLE_METRIC_ID__',
        charge_model='graduated',
        properties={
          'graduated_ranges': [
            {
              'from_value': 0,
              'to_value': 10000,
              'per_unit_amount': '0',
              'flat_amount': '0'
            },
            {
              'from_value': 10001,
              'to_value': None,
              'per_unit_amount': '6.25',
              'flat_amount': '0'
            }
          ]
        }
      )

      plan = Plan(
        name='BigQuery On-Demand',
        code='__PLAN_CODE__',
        interval='monthly',
        description='Pay-as-you-go BigQuery pricing with free tier',
        amount_cents=0,
        amount_currency='USD',
        pay_in_advance=False,
        charges=[charge]
      )

      client.plans.create(plan)
      ```

      ```ruby Ruby highlight={3,6,9-30} theme={"dark"}
      client.plans.create({
        name: 'BigQuery On-Demand',
        code: '__PLAN_CODE__',
        interval: 'monthly',
        description: 'Pay-as-you-go BigQuery pricing with free tier',
        amount_cents: 0,
        amount_currency: 'USD',
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            charge_model: 'graduated',
            properties: {
              graduated_ranges: [
                {
                  from_value: 0,
                  to_value: 10000,
                  per_unit_amount: '0',
                  flat_amount: '0'
                },
                {
                  from_value: 10001,
                  to_value: nil,
                  per_unit_amount: '6.25',
                  flat_amount: '0'
                }
              ]
            }
          }
        ]
      })
      ```

      ```javascript JavaScript highlight={3,6,9-30,33} theme={"dark"}
      const plan = {
        name: 'BigQuery On-Demand',
        code: '__PLAN_CODE__',
        interval: 'monthly',
        description: 'Pay-as-you-go BigQuery pricing with free tier',
        amount_cents: 0,
        amount_currency: 'USD',
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            charge_model: 'graduated',
            properties: {
              graduated_ranges: [
                {
                  from_value: 0,
                  to_value: 10000,
                  per_unit_amount: '0',
                  flat_amount: '0'
                },
                {
                  from_value: 10001,
                  to_value: null,
                  per_unit_amount: '6.25',
                  flat_amount: '0'
                }
              ]
            }
          }
        ]
      };

      await client.plans.createPlan({ plan })
      ```

      ```go Go highlight={3,6,9-30,33} theme={"dark"}
      planInput := &lago.PlanInput{
        Name:           "BigQuery On-Demand",
        Code:           "__PLAN_CODE__",
        Interval:       "monthly",
        Description:    "Pay-as-you-go BigQuery pricing with free tier",
        AmountCents:    0,
        AmountCurrency: "USD",
        PayInAdvance:   false,
        Charges: []*lago.ChargeInput{
          {
            BillableMetricID: "__BILLABLE_METRIC_ID__",
            ChargeModel:        "graduated",
            Properties: map[string]interface{}{
              "graduated_ranges": []map[string]interface{}{
                {
                  "from_value":       0,
                  "to_value":         10000,
                  "per_unit_amount":  "0",
                  "flat_amount":      "0",
                },
                {
                  "from_value":       10001,
                  "to_value":         nil,
                  "per_unit_amount":  "6.25",
                  "flat_amount":      "0",
                },
              },
            },
          },
        },
      }

      plan, err := client.Plan().Create(ctx, planInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/plans/create) and [guide on graduated pricing](/guide/plans/charges/charge-models/graduated) to learn more.
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

  <Step title="Create a wallet with free credits">
    BigQuery lets new users try its product for free by offering upfront credits valid for 90 days. We can replicate this logic using Lago's wallet feature.

    1. Create a wallet with \$300 of free credits for the customer
    2. Set `expiration_at` to 90 days from now for the trial period

    <CodeGroup>
      ```bash cURL highlight={6,8-11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/wallets" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "wallet": {
            "external_customer_id": "__EXTERNAL_CUSTOMER_ID__",
            "name": "BigQuery Trial Credits",
            "rate_amount": "1.0",
            "paid_credits": "300.0",
            "granted_credits": "0.0",
            "expiration_at": "2024-12-31T23:59:59Z"
          }
        }'
      ```

      ```python Python highlight={5,7-10,13} theme={"dark"}
      from lago_python_client.models import Wallet
      from datetime import datetime, timedelta

      wallet = Wallet(
        external_customer_id='__EXTERNAL_CUSTOMER_ID__',
        name='BigQuery Trial Credits',
        rate_amount='1.0',
        paid_credits='300.0',
        granted_credits='0.0',
        expiration_at=(datetime.now() + timedelta(days=90)).isoformat() + 'Z'
      )

      client.wallets.create(wallet)
      ```

      ```ruby Ruby highlight={2,4-7} theme={"dark"}
      client.wallets.create({
        external_customer_id: '__EXTERNAL_CUSTOMER_ID__',
        name: 'BigQuery Trial Credits',
        rate_amount: '1.0',
        paid_credits: '300.0',
        granted_credits: '0.0',
        expiration_at: (Date.today + 90).strftime('%Y-%m-%dT23:59:59Z')
      })
      ```

      ```javascript JavaScript highlight={2,4-7,10} theme={"dark"}
      const wallet = {
        external_customer_id: '__EXTERNAL_CUSTOMER_ID__',
        name: 'BigQuery Trial Credits',
        rate_amount: '1.0',
        paid_credits: '300.0',
        granted_credits: '0.0',
        expiration_at: new Date(Date.now() + 90 * 24 * 60 * 60 * 1000).toISOString()
      }

      await client.wallets.createWallet({ wallet })
      ```

      ```go Go highlight={4,6-9,12} theme={"dark"}
      import "time"

      walletInput := &lago.WalletInput{
        ExternalCustomerID: "__EXTERNAL_CUSTOMER_ID__",
        Name:               "BigQuery Trial Credits",
        RateAmount:         "1.0",
        PaidCredits:        "300.0",
        GrantedCredits:     "0.0",
        ExpirationAt:       time.Now().AddDate(0, 0, 90).Format(time.RFC3339),
      }

      wallet, err := client.Wallet().Create(ctx, walletInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/wallets/create) to create a wallet.

    2. Create a subscription for the customer with the plan's `code`.

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
  </Step>

  <Step title="Ingest usage via events">
    Send usage events to Lago to track usage.

    1. Reference your billable metric with `code`
    2. Reference the customer's subscription with `external_subscription_id`
    3. Include usage and filters data in `properties`

    <CodeGroup>
      ```bash cURL highlight={7-11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/events" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "event": {
            "transaction_id": "__TRANSACTION_ID__",
            "code": "__BILLABLE_METRIC_CODE__",
            "external_subscription_id": "__EXTERNAL_SUBSCRIPTION_ID__",
            "properties": {
              "data_processed_volume": 10
            }
          }
        }'
      ```

      ```python Python highlight={5-9} theme={"dark"}
      from lago_python_client.models import Event

      event = Event(
        transaction_id="__TRANSACTION_ID__",
        code="__BILLABLE_METRIC_CODE__",
        external_subscription_id="__EXTERNAL_SUBSCRIPTION_ID__",
        properties={
          "data_processed_volume": 10
        }
      )

      client.events.create(event)
      ```

      ```ruby Ruby highlight={3-7} theme={"dark"}
      client.events.create(
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          data_processed_volume: 10
        }
      )
      ```

      ```js Javascript highlight={3-7,10} theme={"dark"}
      const event = {
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          data_processed_volume: 10
        }
      };

      await client.events.createEvent({ event });
      ```

      ```go Go highlight={3-7,10} theme={"dark"}
      eventInput := &lago.EventInput{
        TransactionID:          "__TRANSACTION_ID__",
        Code:                   "__BILLABLE_METRIC_CODE__",
        ExternalSubscriptionID: "__EXTERNAL_SUBSCRIPTION_ID__",
        Properties: map[string]interface{}{
          "data_processed_volume": 10,
        },
      }

      event, err := client.Event().Create(ctx, eventInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/events/usage) to create an event.
  </Step>

  <Step title="Monitor current usage">
    Track real-time customer usage for the current billing period.

    <CodeGroup>
      ```bash cURL highlight={1} theme={"dark"}
      curl --location --request GET "$LAGO_URL/api/v1/customers/__EXTERNAL_CUSTOMER_ID__/current_usage?external_subscription_id=__EXTERNAL_SUBSCRIPTION_ID__" \
      --header 'Authorization: Bearer __API_KEY__' \
      --header 'Content-Type: application/json'
      ```

      ```python Python highlight={1} theme={"dark"}
      customer_usage = client.customers.current_usage('__EXTERNAL_CUSTOMER_ID__', '__EXTERNAL_SUBSCRIPTION_ID__')
      ```

      ```ruby Ruby highlight={1} theme={"dark"}
      customer_usage = client.customer.current_usage('__EXTERNAL_CUSTOMER_ID__', '__EXTERNAL_SUBSCRIPTION_ID__')
      ```

      ```js Javascript highlight={1-4} theme={"dark"}
      const customerUsage = await client.customers.findCustomerCurrentUsage(
          '__EXTERNAL_CUSTOMER_ID__',
          { external_subscription_id: '__EXTERNAL_SUBSCRIPTION_ID__' }
      )
      ```

      ```go Go highlight={1} theme={"dark"}
      customerUsage, err := client.Customer().CurrentUsage(ctx, "__EXTERNAL_CUSTOMER_ID__")
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/customer-usage/get-current) to get the current usage.
  </Step>
</Steps>

## Wrap-up

Offering free upfront credits is a popular strategy among AI and infra companies with pay-as-you-go models like BigQuery.
With Lago, you can adapt this template to your products and services using:

1. Configure your pay-as-you-go pricing by aggregate using a **billable metric**;‍
2. Add this billable metric as **graduated charges** to a plan; and‍
3. Create a **wallet** and add prepaid free credits.

Give it a try, click [here](https://www.getlago.com/get-started) to get started!
