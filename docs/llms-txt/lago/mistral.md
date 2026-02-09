# Source: https://getlago.com/docs/templates/per-token/mistral.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone Mistral pricing

> Replicate Mistral's per-token pricing model with Lago.

In this article, you will learn how Mistral is using Lago to build a billing system based on AI tokens.
This template is suitable for Large Language Model (LLM) and Generative AI companies whose pricing can vary based on the application or model used.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qZLRsVOk-MY?si=xZN856Dod8YNRoob&start=176" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Pricing structure

For Mistral, pricing depends on the language model used. Here are several price points they offer:
Prices are per 1M tokens used. You can think of tokens as pieces of words (learn more [here](https://mistral.ai/technology/#models))."

| Models         | Input             | Output            |
| -------------- | ----------------- | ----------------- |
| mistral-small  | \$1 / 1M tokens   | \$3 / 1M tokens   |
| mistral-medium | \$2.7 / 1M tokens | \$8.1 / 1M tokens |
| mistral-large  | \$4 / 1M tokens   | \$12 / 1M tokens  |

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
    Create a single billable metric to track token usage across different models and input/output types.

    1. Add a unique `code` for your billable metric
    2. Set `aggregation_type` to `sum_agg`
    3. Set `field_name` to `tokens`
    4. Set `recurring` to `false`
    5. Set `filters` to distinguish between models and token types

    <CodeGroup>
      ```bash cURL highlight={7,9-21} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/billable_metrics" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "billable_metric": {
            "name": "AI Tokens",
            "code": "__BILLABLE_METRIC_CODE__",
            "description": "Token usage across Mistral AI models",
            "aggregation_type": "sum_agg",
            "field_name": "tokens",
            "recurring": false,
            "filters": [
              {
                "key": "model",
                "values": ["mistral-small", "mistral-medium", "mistral-large"]
              },
              {
                "key": "type", 
                "values": ["input", "output"]
              }
            ]
          }
        }'
      ```

      ```python Python highlight={3-6,8-11,15,17-20,23} theme={"dark"}
      from lago_python_client.models import BillableMetric, BillableMetricFilter

      model_filter = BillableMetricFilter(
        key='model',
        values=['mistral-small', 'mistral-medium', 'mistral-large']
      )

      type_filter = BillableMetricFilter(
        key='type',
        values=['input', 'output']
      )

      billable_metric = BillableMetric(
        name='Tokens',
        code='__BILLABLE_METRIC_CODE__',
        description='Token usage across Mistral AI models',
        aggregation_type='sum_agg',
        field_name='tokens',
        recurring=False,
        filters=[model_filter, type_filter]
      )

      client.billable_metrics.create(billable_metric)
      ```

      ```ruby Ruby highlight={3,5-17} theme={"dark"}
      client.billable_metrics.create({
        name: 'Tokens',
        code: '__BILLABLE_METRIC_CODE__', 
        description: 'Token usage across Mistral AI models',
        aggregation_type: 'sum_agg',
        field_name: 'tokens',
        recurring: false,
        filters: [
          {
            key: 'model',
            values: ['mistral-small', 'mistral-medium', 'mistral-large']
          },
          {
            key: 'type',
            values: ['input', 'output']
          }
        ]
      })
      ```

      ```js Javascript highlight={3,5-7,8-17,20} theme={"dark"}
      const billableMetric = {
        name: "Tokens",
        code: "__BILLABLE_METRIC_CODE__",
        description: "Token usage across Mistral AI models", 
        aggregation_type: "sum_agg",
        field_name: "tokens",
        recurring: false,
        filters: [
          {
            key: "model",
            values: ["mistral-small", "mistral-medium", "mistral-large"]
          },
          {
            key: "type",
            values: ["input", "output"]
          }
        ]
      };

      await client.billableMetrics.createBillableMetric({ billableMetric });
      ```

      ```go Go highlight={3,5-17,20} theme={"dark"}
      bmInput := &lago.BillableMetricInput{
        Name:            "Tokens",
        Code:            "__BILLABLE_METRIC_CODE__",
        Description:     "Token usage across Mistral AI models",
        AggregationType: lago.SumAggregation,
        FieldName:       "tokens",
        Recurring:       false,
        Filters:         []lago.BillableMetricFilter{
          {
            Key:    "model",
            Values: []string{"mistral-small", "mistral-medium", "mistral-large"},
          },
          {
            Key:    "type", 
            Values: []string{"input", "output"},
          },
        },
      }

      billableMetric, err := client.BillableMetric().Create(ctx, bmInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/billable-metrics/create) and [guide on filters](/guide/billable-metrics/filters) to learn more.
  </Step>

  <Step title="Create a plan">
    Create a plan to price packages of tokens used with Mistral's specific pricing tiers.

    1. Add a unique `code` for your plan
    2. Under `charges`, configure pricing tiers for different models and token types

    <CodeGroup>
      ```bash cURL expandable highlight={7,12-66} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/plans" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "plan": {
            "name": "Mistral AI Pricing",
            "code": "__PLAN_CODE__",
            "amount_cents": 0,
            "amount_currency": "USD",
            "interval": "monthly",
            "pay_in_advance": false,
            "charges": [
              {
                "billable_metric_id": "__BILLABLE_METRIC_ID__",
                "charge_model": "package",
                "filters": [
                  {
                    "invoice_display_name": "mistral-small-input",
                    "properties": {
                      "amount": "1",
                      "free_units": 0,
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["mistral-small"],
                      "type": ["input"]
                    }
                  },
                  {
                    "invoice_display_name": "mistral-small-output", 
                    "properties": {
                      "amount": "3",
                      "free_units": 0,
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["mistral-small"],
                      "type": ["output"]
                    }
                  },
                  {
                    "invoice_display_name": "mistral-large-input",
                    "properties": {
                      "amount": "4", 
                      "free_units": 0,
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["mistral-large"],
                      "type": ["input"]
                    }
                  },
                  {
                    "invoice_display_name": "mistral-large-output",
                    "properties": {
                      "amount": "12",
                      "free_units": 0, 
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["mistral-large"],
                      "type": ["output"]
                    }
                  } 
                ]
              }
            ]
          }
        }'
      ```

      ```python Python expandable highlight={4-8,10-14,16-20,22-26,29-33,37,42,45} theme={"dark"}
      from lago_python_client.models import Plan, Charge, ChargeFilter

      # Filters for different models and token types
      small_input_filter = ChargeFilter(
        invoice_display_name="mistral-small-input",
        properties={"amount": "1", "free_units": 0, "package_size": 1000000},
        values={"model": ["mistral-small"], "type": ["input"]}
      )

      small_output_filter = ChargeFilter(
        invoice_display_name="mistral-small-output", 
        properties={"amount": "3", "free_units": 0, "package_size": 1000000},
        values={"model": ["mistral-small"], "type": ["output"]}
      )

      large_input_filter = ChargeFilter(
        invoice_display_name="mistral-large-input",
        properties={"amount": "4", "free_units": 0, "package_size": 1000000},
        values={"model": ["mistral-large"], "type": ["input"]}
      )

      large_output_filter = ChargeFilter(
        invoice_display_name="mistral-large-output",
        properties={"amount": "12", "free_units": 0, "package_size": 1000000},
        values={"model": ["mistral-large"], "type": ["output"]}
      )

      # Charge for all filters
      charge = Charge(
        billable_metric_id="__BILLABLE_METRIC_ID__",
        charge_model="package",
        filters=[small_input_filter, small_output_filter, large_input_filter, large_output_filter]
      )

      plan = Plan(
        name="Mistral Plan",
        code="__PLAN_CODE__",
        amount_cents=0,
        amount_currency="USD", 
        interval="monthly",
        pay_in_advance=False,
        charges=[charge]
      )

      client.plans.create(plan)
      ```

      ```ruby Ruby expandable highlight={3,8-35} theme={"dark"}
      client.plans.create({
        name: "Mistral AI Pricing",
        code: "__PLAN_CODE__",
        amount_cents: 0,
        amount_currency: "USD",
        interval: "monthly",
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: "__BILLABLE_METRIC_ID__",
            charge_model: "package",
            filters: [
              {
                invoice_display_name: "mistral-small-input",
                properties: { amount: "1", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-small"], type: ["input"] }
              },
              {
                invoice_display_name: "mistral-small-output",
                properties: { amount: "3", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-small"], type: ["output"] }
              },
              {
                invoice_display_name: "mistral-large-input", 
                properties: { amount: "4", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-large"], type: ["input"] }
              },
              {
                invoice_display_name: "mistral-large-output",
                properties: { amount: "12", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-large"], type: ["output"] }
              }
            ]
          }
        ]
      })
      ```

      ```js Javascript expandable highlight={3,8-35,38} theme={"dark"}
      const plan = {
        name: "Mistral AI Pricing",
        code: "__PLAN_CODE__",
        amount_cents: 0,
        amount_currency: "USD",
        interval: "monthly",
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: "__BILLABLE_METRIC_ID__",
            charge_model: "package",
            filters: [
              {
                invoice_display_name: "mistral-small-input",
                properties: { amount: "1", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-small"], type: ["input"] }
              },
              {
                invoice_display_name: "mistral-small-output",
                properties: { amount: "3", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-small"], type: ["output"] }
              },
              {
                invoice_display_name: "mistral-large-input",
                properties: { amount: "4", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-large"], type: ["input"] }
              },
              {
                invoice_display_name: "mistral-large-output", 
                properties: { amount: "12", free_units: 0, package_size: 1000000 },
                values: { model: ["mistral-large"], type: ["output"] }
              }
            ]
          }
        ]
      };

      await client.plans.createPlan({ plan });
      ```

      ```go Go expandable highlight={3,8-51,54} theme={"dark"}
      planInput := &lago.PlanInput{
        Name:           "Mistral AI Pricing",
        Code:           "__PLAN_CODE__", 
        AmountCents:    0,
        AmountCurrency: "USD",
        Interval:       "monthly",
        PayInAdvance:   false,
        Charges:        []lago.PlanChargeInput{
          {
            BillableMetricID: "__BILLABLE_METRIC_ID__",
            ChargeModel:        "package",
            Filters: []lago.ChargeFilter{
              {
                InvoiceDisplayName: "mistral-small-input",
                Properties: map[string]interface{}{
                  "amount": "1", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"mistral-small"}, "type": []string{"input"},
                },
              },
              {
                InvoiceDisplayName: "mistral-small-output",
                Properties: map[string]interface{}{
                  "amount": "3", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"mistral-small"}, "type": []string{"output"},
                },
              },
              {
                InvoiceDisplayName: "mistral-large-input",
                Properties: map[string]interface{}{
                  "amount": "4", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"mistral-large"}, "type": []string{"input"},
                },
              },
              {
                InvoiceDisplayName: "mistral-large-output",
                Properties: map[string]interface{}{
                  "amount": "12", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"mistral-large"}, "type": []string{"output"},
                },
              },
            },
          },
        },
      }

      plan, err := client.Plan().Create(ctx, planInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/plans/create) and [guide on charges with filters](/guide/plans/charges/charges-with-filters) to learn more.
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

  <Step title="Prepay usage with credits">
    1. Create a wallet with the customer's `external_customer_id`,
       set the wallet `currency` and `rate_amount` for credit conversion

    <CodeGroup>
      ```bash cURL highlight={7,11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/wallets" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "wallet": {
            "name": "AI Credits",
            "external_customer_id": "__EXTERNAL_CUSTOMER_ID__",
            "currency": "USD",
            "paid_credits": "100.0",
            "granted_credits": "25.0",
            "rate_amount": "1.0"
          }
        }'
      ```

      ```python Python highlight={5,9} theme={"dark"}
      from lago_python_client.models import Wallet

      wallet = Wallet(
        name="AI Credits",
        external_customer_id="__EXTERNAL_CUSTOMER_ID__",
        currency="USD",
        paid_credits="100.0",
        granted_credits="25.0",
        rate_amount="1.0"
      )

      client.wallets.create(wallet)
      ```

      ```ruby Ruby highlight={3,7} theme={"dark"}
      client.wallets.create({
        name: "AI Credits",
        external_customer_id: "__EXTERNAL_CUSTOMER_ID__",
        currency: "USD",
        paid_credits: "100.0",
        granted_credits: "25.0",
        rate_amount: "1.0"
      })
      ```

      ```js Javascript highlight={3,7,10} theme={"dark"}
      const wallet = {
        name: "AI Credits",
        external_customer_id: "__EXTERNAL_CUSTOMER_ID__",
        currency: "USD",
        paid_credits: 100.0,
        granted_credits: 25.0,
        rate_amount: 1.0
      };

      await client.wallets.createWallet({ wallet });
      ```

      ```go Go highlight={3,7,10} theme={"dark"}
        walletInput := &lago.WalletInput{
          Name:               "AI Credits",
          ExternalCustomerID: "__EXTERNAL_CUSTOMER_ID__",
          Currency:           "USD",
          PaidCredits:        "100.0",
          GrantedCredits:     "25.0",
          RateAmount:         "1.0",
        }

        wallet, err := lagoClient.Wallet().Create(walletInput)
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
      ```bash cURL highlight={7-13} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/events" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "event": {
            "transaction_id": "__TRANSACTION_ID__",
            "code": "__BILLABLE_METRIC_CODE__",
            "external_subscription_id": "__EXTERNAL_SUBSCRIPTION_ID__",
            "properties": {
              "tokens": 2000000,
              "model": "mistral-small",
              "type": "input"
            }
          }
        }'
      ```

      ```python Python highlight={5-11} theme={"dark"}
      from lago_python_client.models import Event

      event = Event(
        transaction_id="__TRANSACTION_ID__",
        code="__BILLABLE_METRIC_CODE__",
        external_subscription_id="__EXTERNAL_SUBSCRIPTION_ID__",
        properties={
          "tokens": 2000000,
          "model": "mistral-small",
          "type": "input"
        }
      )

      client.events.create(event)
      ```

      ```ruby Ruby highlight={3-9} theme={"dark"}
      client.events.create(
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          tokens: 2000000,
          model: "mistral-small",
          type: "input"
        }
      )
      ```

      ```js Javascript highlight={3-9,12} theme={"dark"}
      const event = {
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          tokens: 2000000,
          model: "mistral-small",
          type: "input"
        }
      };

      await client.events.createEvent({ event });
      ```

      ```go Go highlight={3-9,12} theme={"dark"}
      eventInput := &lago.EventInput{
        TransactionID:          "__TRANSACTION_ID__",
        Code:                   "__BILLABLE_METRIC_CODE__",
        ExternalSubscriptionID: "__EXTERNAL_SUBSCRIPTION_ID__",
        Properties: map[string]interface{}{
          "tokens": 2000000,
          "model":  "mistral-small",
          "type":   "input",
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

Per-token pricing offers flexibility and visibility, and allows LLM and Generative AI companies like Mistral to attract more customers.
With Lago, you can create your own metric dimensions to adapt this template to your products and services.

Give it a try, click [here](https://www.getlago.com/get-started) to get started!
