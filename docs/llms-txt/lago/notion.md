# Source: https://getlago.com/docs/templates/per-seat/notion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone Notion pricing

> Replicate Notion's per-seat pricing model with Lago.

Set up a per-user (or 'per-seat) pricing like [Notion](https://www.notion.so/product), the collaboration software for innovative teams, including plans based on the number of users and prepaid credits.

In this template, you will learn how to build a 'fair' billing system, with charges calculated according to the number of days of use.

This template is suitable for companies whose pricing depends on persistent metrics, such as productivity software (e.g. number of days users are active), fintechs (e.g. number of days payment cards are active) and data platforms (e.g. number of days integrations are active).

## Pricing structure

Notion offers a Personal Pro plan for individuals who want to collaborate with friends or clients, and a Team plan through which members can set up a collaborative workspace. While the Personal Pro plan is limited to one member, the Team plan allows companies to invite as many members as they need.

| Model | Team plan                    |
| ----- | ---------------------------- |
| Price | \$10 per user billed monthly |

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
    Create a recurring billable metric to track user activity over time.

    1. Add a unique `code` for your billable metric
    2. Set the `aggregation_type` to `unique_count_agg` for counting unique users
    3. Set the `field_name` to `user_id` to identify individual users
    4. Set `recurring` to `true` for persistent tracking across billing periods

    <CodeGroup>
      ```bash cURL highlight={7,9-11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/billable_metrics" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "billable_metric": {
            "name": "Active Users",
            "code": "__BILLABLE_METRIC_CODE__",
            "description": "Number of active users in the workspace",
            "aggregation_type": "unique_count_agg",
            "field_name": "user_id",
            "recurring": true
          }
        }'
      ```

      ```python Python highlight={5,7-9,12} theme={"dark"}
      from lago_python_client.models import BillableMetric

      billable_metric = BillableMetric(
        name='Active Users',
        code='__BILLABLE_METRIC_CODE__',
        description='Number of active users in the workspace',
        aggregation_type='unique_count_agg',
        field_name='user_id',
        recurring=True
      )

      client.billable_metrics.create(billable_metric)
      ```

      ```ruby Ruby highlight={3,5-7} theme={"dark"}
      client.billable_metrics.create({
        name: 'Active Users',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Number of active users in the workspace',
        aggregation_type: 'unique_count_agg',
        field_name: 'user_id',
        recurring: true
      })
      ```

      ```javascript JavaScript highlight={3,5-7,10} theme={"dark"}
      const billableMetric = {
        name: 'Active Users',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Number of active users in the workspace',
        aggregation_type: 'unique_count_agg',
        field_name: 'user_id',
        recurring: true
      };

      await client.billableMetrics.createBillableMetric({ billableMetric })
      ```

      ```go Go highlight={3,5-7,10} theme={"dark"}
      billableMetricInput := &lago.BillableMetricInput{
        Name:             "Active Users",
        Code:             "__BILLABLE_METRIC_CODE__",
        Description:      "Number of active users in the workspace",
        AggregationType:  "unique_count_agg",
        FieldName:        "user_id",
        Recurring:        true,
      }

      billableMetric, err := client.BillableMetric().Create(ctx, billableMetricInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/billable-metrics/create) and the [guide on recurring metrics](/guide/billable-metrics/recurring-vs-metered) to learn more.
  </Step>

  <Step title="Create a plan">
    Create a plan with prorated charges for fair per-seat billing.

    1. Set the `amount_cents` to `0` since there is no subscription fee
    2. Set the `charge_model` to `standard` for simple per-unit pricing
    3. Enable `prorated` billing for fair daily calculations
    4. Set the `amount` to `10` for \$10 per user per month

    <CodeGroup>
      ```bash cURL highlight={7,13-23} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/plans" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "plan": {
            "name": "Team Plan",
            "code": "__PLAN_CODE__",
            "description": "Per-seat pricing for team collaboration",
            "amount_cents": 0,
            "amount_currency": "USD",
            "interval": "monthly",
            "pay_in_advance": false,
            "charges": [
              {
                "billable_metric_id": "__BILLABLE_METRIC_ID__",
                "charge_model": "standard",
                "invoiceable": true,
                "prorated": true,
                "properties": {
                  "amount": "10"
                }
              }
            ]
          }
        }'
      ```

      ```python Python highlight={3-11,15,21,24} theme={"dark"}
      from lago_python_client.models import Plan, Charge

      charge = Charge(
        billable_metric_id='__BILLABLE_METRIC_ID__',
        charge_model='standard',
        invoiceable=True,
        prorated=True,
        properties={
          'amount': '10'
        }
      )

      plan = Plan(
        name='Team Plan',
        code='__PLAN_CODE__',
        description='Per-seat pricing for team collaboration',
        amount_cents=0,
        amount_currency='USD',
        interval='monthly',
        pay_in_advance=False,
        charges=[charge]
      )

      client.plans.create(plan)
      ```

      ```ruby Ruby highlight={3,9-19} theme={"dark"}
      client.plans.create({
        name: 'Team Plan',
        code: '__PLAN_CODE__',
        description: 'Per-seat pricing for team collaboration',
        amount_cents: 0,
        amount_currency: 'USD',
        interval: 'monthly',
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            charge_model: 'standard',
            invoiceable: true,
            prorated: true,
            properties: {
              amount: '10'
            }
          }
        ]
      })
      ```

      ```javascript Javascript highlight={3,9-19,22} theme={"dark"}
      const plan = {
        name: 'Team Plan',
        code: '__PLAN_CODE__',
        description: 'Per-seat pricing for team collaboration',
        amount_cents: 0,
        amount_currency: 'USD',
        interval: 'monthly',
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            charge_model: 'standard',
            invoiceable: true,
            prorated: true,
            properties: {
              amount: '10'
            }
          }
        ]
      };

      await client.plans.createPlan({ plan })
      ```

      ```go Go highlight={3,9-19,22} theme={"dark"}
      planInput := &lago.PlanInput{
        Name:           "Team Plan",
        Code:           "__PLAN_CODE__",
        Description:    "Per-seat pricing for team collaboration",
        AmountCents:    0,
        AmountCurrency: "USD",
        Interval:       "monthly",
        PayInAdvance:   false,
        Charges: []*lago.PlanChargeInput{
          {
            BillableMetricID: "__BILLABLE_METRIC_ID__",
            ChargeModel:        "standard",
            Invoiceable:        true,
            Prorated:           true,
            Properties: map[string]interface{}{
              "amount": "10",
            },
          },
        },
      }

      plan, err := client.Plan().Create(ctx, planInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/plans/create) and the [guide on prorated charges](/guide/plans/charges/prorated-vs-full) to learn more.
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

  <Step title="Ingest user activity events">
    Send usage events to Lago to track usage.

    1. Reference your billable metric with `code`
    2. Reference the customer's subscription with `external_subscription_id`
    3. Include `user_id` in properties to track individual users
    4. Set `operation_type` to `add` when adding users, `remove` when removing

    <CodeGroup>
      ```bash cURL highlight={7-12} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/events" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "event": {
            "transaction_id": "__TRANSACTION_ID__",
            "code": "__BILLABLE_METRIC_CODE__",
            "external_subscription_id": "__EXTERNAL_SUBSCRIPTION_ID__",
            "properties": {
              "user_id": "user_123",
              "operation_type": "add"
            }
          }
        }'
      ```

      ```python Python highlight={5-10,13} theme={"dark"}
      from lago_python_client.models import Event

      event = Event(
        transaction_id='__TRANSACTION_ID__',
        code='__BILLABLE_METRIC_CODE__',
        external_subscription_id='__EXTERNAL_SUBSCRIPTION_ID__',
        properties={
          'user_id': 'user_123',
          'operation_type': 'add'
        }
      )

      client.events.create(event)
      ```

      ```ruby Ruby highlight={3-8} theme={"dark"}
      client.events.create({
        transaction_id: '__TRANSACTION_ID__',
        code: '__BILLABLE_METRIC_CODE__',
        external_subscription_id: '__EXTERNAL_SUBSCRIPTION_ID__',
        properties: {
          user_id: 'user_123',
          operation_type: 'add'
        }
      })
      ```

      ```javascript Javascript highlight={3-8,11} theme={"dark"}
      const event = {
        transaction_id: '__TRANSACTION_ID__',
        code: '__BILLABLE_METRIC_CODE__',
        external_subscription_id: '__EXTERNAL_SUBSCRIPTION_ID__',
        properties: {
          user_id: 'user_123',
          operation_type: 'add'
        }
      };

      await client.events.createEvent({ event })
      ```

      ```go Go highlight={3-8,11} theme={"dark"}
      eventInput := &lago.EventInput{
        TransactionID:        "__TRANSACTION_ID__",
        Code:                 "__BILLABLE_METRIC_CODE__",
        ExternalSubscriptionID: "__EXTERNAL_SUBSCRIPTION_ID__",
        Properties: map[string]interface{}{
          "user_id":        "user_123",
          "operation_type": "add",
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

For software companies like Notion, implementing a 'fair' per-user pricing model is a good way to **increase transparency and customer satisfaction**.
With Lago, you can create your own persistent metrics to adapt this template to your products and services.

Give it a try, click [here](https://www.getlago.com/get-started) to get started!
