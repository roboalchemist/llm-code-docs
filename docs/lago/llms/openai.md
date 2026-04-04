# Source: https://getlago.com/docs/templates/per-token/openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone OpenAI pricing

> Replicate OpenAI's per-token pricing model with Lago.

In this article, you will learn how to build a billing system with Lago based on tokens.
This template is suitable for Large Language Model (LLM) and Generative AI companies whose pricing can vary based on the application or model used.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ulLpAn8_P9o?si=18NXjL8pITlrVuZ7&start=35" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Pricing structure

For OpenAI, pricing depends on the language model used. Here are several price points they offer:
*"Prices are per 1,000 tokens. You can think of tokens as pieces of words, where 1,000 tokens is about 750 words (learn more [here](https://platform.openai.com/tokenizer))."*

| Model       | Input                 | Output                |
| ----------- | --------------------- | --------------------- |
| 8K context  | \$0.03 / 1,000 tokens | \$0.06 / 1,000 tokens |
| 32K context | \$0.06 / 1,000 tokens | \$0.12 / 1,000 tokens |

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
            "description": "Token usage across OpenAI models",
            "aggregation_type": "sum_agg",
            "field_name": "tokens",
            "recurring": false,
            "filters": [
              {
                "key": "model",
                "values": ["8k", "32k"]
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
        values=['8k', '32k']
      )

      type_filter = BillableMetricFilter(
        key='type',
        values=['input', 'output']
      )

      billable_metric = BillableMetric(
        name='Tokens',
        code='__BILLABLE_METRIC_CODE__',
        description='Token usage across OpenAI models',
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
        description: 'Token usage across OpenAI models',
        aggregation_type: 'sum_agg',
        field_name: 'tokens',
        recurring: false,
        filters: [
          {
            key: 'model',
            values: ['8k', '32k']
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
        description: "Token usage across OpenAI models", 
        aggregation_type: "sum_agg",
        field_name: "tokens",
        recurring: false,
        filters: [
          {
            key: "model",
            values: ["8k", "32k"]
          },
          {
            key: "type",
            values: ["input", "output"]
          }
        ]
      };

      await client.billableMetrics.createBillableMetric(billableMetric);
      ```

      ```go Go highlight={3,5-17,20} theme={"dark"}
      bmInput := &lago.BillableMetricInput{
        Name:            "Tokens",
        Code:            "__BILLABLE_METRIC_CODE__",
        Description:     "Token usage across OpenAI models",
        AggregationType: lago.SumAggregation,
        FieldName:       "tokens",
        Recurring:       false,
        Filters:         []lago.BillableMetricFilter{
          {
            Key:    "type",
            Values: []string{"input", "output"},
          },
          {
            Key:    "model",
            Values: []string{"8k", "32k"},
          },
        },
      }

      billableMetric, err := lagoClient.BillableMetric().Create(bmInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/billable-metrics/create) and [guide on filters](/guide/billable-metrics/filters) to learn more.
  </Step>

  <Step title="Create a plan">
    Create a plan to price packages of tokens used with OpenAI's specific pricing tiers.

    1. Add a unique `code` for your plan
    2. Under `charges`, configure pricing tiers for different models and token types

    <CodeGroup>
      ```bash cURL expandable highlight={7,12-67} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/plans" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "plan": {
            "name": "OpenAI Pricing",
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
                    "invoice_display_name": "8k-input",
                    "properties": {
                      "amount": "0.03",
                      "free_units": 0,
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["8k"],
                      "type": ["input"]
                    }
                  },
                  {
                    "invoice_display_name": "8k-output", 
                    "properties": {
                      "amount": "0.06",
                      "free_units": 0,
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["8k"],
                      "type": ["output"]
                    }
                  },
                  {
                    "invoice_display_name": "32k-input",
                    "properties": {
                      "amount": "0.06", 
                      "free_units": 0,
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["32k"],
                      "type": ["input"]
                    }
                  },
                  {
                    "invoice_display_name": "32k-output",
                    "properties": {
                      "amount": "0.12",
                      "free_units": 0, 
                      "package_size": 1000000
                    },
                    "values": {
                      "model": ["32k"],
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
        invoice_display_name="8k-input",
        properties={"amount": "0.03", "free_units": 0, "package_size": 1000000},
        values={"model": ["8k"], "type": ["input"]}
      )

      small_output_filter = ChargeFilter(
        invoice_display_name="8k-output", 
        properties={"amount": "0.06", "free_units": 0, "package_size": 1000000},
        values={"model": ["8k"], "type": ["output"]}
      )

      large_input_filter = ChargeFilter(
        invoice_display_name="32k-input",
        properties={"amount": "0.06", "free_units": 0, "package_size": 1000000},
        values={"model": ["32k"], "type": ["input"]}
      )

      large_output_filter = ChargeFilter(
        invoice_display_name="32k-output",
        properties={"amount": "0.12", "free_units": 0, "package_size": 1000000},
        values={"model": ["32k"], "type": ["output"]}
      )

      # Charge for all filters
      charge = Charge(
        billable_metric_id="__BILLABLE_METRIC_ID__",
        charge_model="package",
        filters=[small_input_filter, small_output_filter, large_input_filter, large_output_filter]
      )

      plan = Plan(
        name="OpenAI Plan",
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
        name: "OpenAI Pricing",
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
                invoice_display_name: "8k-input",
                properties: { amount: "0.03", free_units: 0, package_size: 1000000 },
                values: { model: ["8k"], type: ["input"] }
              },
              {
                invoice_display_name: "8k-output",
                properties: { amount: "0.06", free_units: 0, package_size: 1000000 },
                values: { model: ["8k"], type: ["output"] }
              },
              {
                invoice_display_name: "32k-input", 
                properties: { amount: "0.06", free_units: 0, package_size: 1000000 },
                values: { model: ["32k"], type: ["input"] }
              },
              {
                invoice_display_name: "32k-output",
                properties: { amount: "0.12", free_units: 0, package_size: 1000000 },
                values: { model: ["32k"], type: ["output"] }
              }
            ]
          }
        ]
      })
      ```

      ```js Javascript expandable highlight={3,8-35,38} theme={"dark"}
      const plan = {
        name: "OpenAI Pricing",
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
                invoice_display_name: "8k-input",
                properties: { amount: "0.03", free_units: 0, package_size: 1000000 },
                values: { model: ["8k"], type: ["input"] }
              },
              {
                invoice_display_name: "8k-output",
                properties: { amount: "0.06", free_units: 0, package_size: 1000000 },
                values: { model: ["8k"], type: ["output"] }
              },
              {
                invoice_display_name: "32k-input",
                properties: { amount: "0.06", free_units: 0, package_size: 1000000 },
                values: { model: ["32k"], type: ["input"] }
              },
              {
                invoice_display_name: "32k-output", 
                properties: { amount: "0.12", free_units: 0, package_size: 1000000 },
                values: { model: ["32k"], type: ["output"] }
              }
            ]
          }
        ]
      };

      await client.plans.createPlan({ plan });
      ```

      ```go Go expandable highlight={3,8-51,54} theme={"dark"}
      planInput := &lago.PlanInput{
        Name:           "OpenAI Pricing",
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
                InvoiceDisplayName: "8k-input",
                Properties: map[string]interface{}{
                  "amount": "0.03", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"8k"}, "type": []string{"input"},
                },
              },
              {
                InvoiceDisplayName: "8k-output",
                Properties: map[string]interface{}{
                  "amount": "0.06", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"8k"}, "type": []string{"output"},
                },
              },
              {
                InvoiceDisplayName: "32k-input",
                Properties: map[string]interface{}{
                  "amount": "0.06", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"32k"}, "type": []string{"input"},
                },
              },
              {
                InvoiceDisplayName: "32k-output",
                Properties: map[string]interface{}{
                  "amount": "0.12", "free_units": 0, "package_size": 1000000,
                },
                Values: map[string]string{
                  "model": []string{"32k"}, "type": []string{"output"},
                },
              },
            },
          },
        },
      }

      plan, err := lagoClient.Plan().Create(planInput)
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
  </Step>

  <Step title="Ingest usage via events">
    Send usage events to Lago to track usage.

    1. Reference your billable metric with `code`
    2. Reference the customer's subscription with `external_subscription_id`
    3. Include usage and filters data in `properties`

    <CodeGroup>
      ```bash cURL highlight={10,11,12-16} theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__API_KEY__"

      curl --location --request POST "$LAGO_URL/api/v1/events" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "event": {
            "transaction_id": "__TRANSACTION_ID__",
            "code": "__BILLABLE_METRIC_CODE__",
            "external_subscription_id": "__EXTERNAL_SUBSCRIPTION_ID__",
            "properties": {
              "total": 5000,
              "model": "8k",
              "type": "input"
            }
          }
        }'
      ```

      ```python Python highlight={9,10-15} theme={"dark"}
      from lago_python_client.client import Client
      from lago_python_client.exceptions import LagoApiError
      from lago_python_client.models import Event

      client = Client(api_key='__API_KEY__')

      event = Event(
        transaction_id="__TRANSACTION_ID__",
        code="__BILLABLE_METRIC_CODE__",
        external_subscription_id="__EXTERNAL_SUBSCRIPTION_ID__",
        properties={
          "total": 5000,
          "model": "8k",
          "type": "input"
        }
      )

      try:
          client.events.create(event)
      except LagoApiError as e:
          repair_broken_state(e)  # do something on error or raise your own exception
      ```

      ```ruby Ruby highlight={7,8-13} theme={"dark"}
      require 'lago-ruby-client'

      client = Lago::Api::Client.new(api_key: '__API_KEY__')

      client.events.create(
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          total: 5000,
          model: "8k",
          type: "input"
        }
      )
      ```

      ```js Javascript highlight={4,5-10} theme={"dark"}
      await client.events.createEvent({
        event: {
          transaction_id: "__TRANSACTION_ID__",
          code: "__BILLABLE_METRIC_CODE__",
          external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
          properties: {
            total: 5000,
            model: "8k",
            type: "input"
          }
        }
      });
      ```

      ```go Go highlight={10-16} theme={"dark"}
      eventInput := &lago.EventInput{
        TransactionID:          "__TRANSACTION_ID__",
        Code:                   "__BILLABLE_METRIC_CODE__",
        ExternalSubscriptionID: "__EXTERNAL_SUBSCRIPTION_ID__",
        Properties: map[string]interface{}{
          "total": 5000,
          "model": "8k",
          "type":  "input",
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

Per-token pricing offers flexibility and visibility, and allows LLM and Generative AI companies like OpenAI to attract more customers.
With Lago, you can create your own metric dimensions to adapt this template to your products and services.

Give it a try, click [here](https://www.getlago.com/get-started) to get started!
