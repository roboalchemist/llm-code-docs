# Source: https://getlago.com/docs/templates/payg/algolia.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone Algolia pricing

> Replicate Algolia's pay-as-you-go pricing model with Lago.

In this article, you will learn how to build a 'pay-as-you-go' billing system.
This template is suitable for companies whose pricing fully depends on usage, such as cloud service providers and API companies, that only charge their customers for the resources they consume.

## Pricing structure

For one of its products, Algolia Search, the platform offers its customers to subscribe for free and only pay based on usage.

| Model                   | Search API              |
| ----------------------- | ----------------------- |
| Monthly price           | \$1.50 / 1,000 requests |
| Free usage (each month) | 10,000 requests         |

Although users don't need to subscribe to access the platform, Algolia offers its customers **discounts** based on volume and commitment (rates available upon request).

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

  <Step title="Create billable metrics">
    Create billable metrics to track request usage for Search and Recommend APIs.

    1. Set the `aggregation_type` to `sum_agg` to sum all request volumes
    2. Set the `field_name` to `search_requests_volume` for Search API tracking
    3. Set the `recurring` to `false` for metered billing

    <CodeGroup>
      ```bash cURL highlight={7,9-11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/billable_metrics" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "billable_metric": {
            "name": "Search API Requests",
            "code": "__BILLABLE_METRIC_CODE__",
            "description": "Search API request volume",
            "aggregation_type": "sum_agg",
            "field_name": "search_requests_volume",
            "recurring": false
          }
        }'
      ```

      ```python Python highlight={5,7-9,12} theme={"dark"}
      from lago_python_client.models import BillableMetric

      billable_metric = BillableMetric(
        name='Search API Requests',
        code='__BILLABLE_METRIC_CODE__',
        description='Search API request volume',
        aggregation_type='sum_agg',
        field_name='search_requests_volume',
        recurring=False,
      )

      client.billable_metrics.create(billable_metric)
      ```

      ```ruby Ruby highlight={3,5-7} theme={"dark"}
      client.billable_metrics.create({
        name: 'Search API Requests',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Search API request volume',
        aggregation_type: 'sum_agg',
        field_name: 'search_requests_volume',
        recurring: false
      })
      ```

      ```javascript JavaScript highlight={3,5-7,10} theme={"dark"}
      const billable_metric = {
        name: 'Search API Requests',
        code: '__BILLABLE_METRIC_CODE__',
        description: 'Search API request volume',
        aggregationType: 'sum_agg', 
        fieldName: 'search_requests_volume',
        recurring: false
      };

      await client.billableMetrics.create({ billable_metric })
      ```

      ```go Go highlight={3,5-10}  theme={"dark"}
      billableMetricInput := &lago.BillableMetricInput{
        Name:           "Search API Requests",
        Code:           "__BILLABLE_METRIC_CODE__",
        Description:    "Search API request volume",
        AggregationType: "sum_agg",
        FieldName:       "search_requests_volume",
        Recurring:       false,
      }

      billableMetric, err := client.BillableMetric().Create(ctx, billableMetricInput)
      ```
    </CodeGroup>
  </Step>

  <Step title="Create a plan">
    Create a plan to price packages of requests used.

    1. Set the `amount_cents` to `0` since there is no subscription fee
    2. Set the `charges` to use `package` pricing model with Algolia's rates
    3. Configure `free_units` of 10,000 requests per month included

    <CodeGroup>
      ```bash cURL highlight={7,10,13-23} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/plans" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "plan": {
            "name": "Algolia Search",
            "code": "__PLAN_CODE__",
            "interval": "monthly",
            "description": "Pay-as-you-go pricing for Algolia Search API",
            "amount_cents": 0,
            "amount_currency": "USD",
            "pay_in_advance": false,
            "charges": [
              {
                "billable_metric_id": "__BILLABLE_METRIC_ID__",
                "charge_model": "package",
                "properties": {
                  "amount": "1.50",
                  "free_units": 10000,
                  "package_size": 1000
                }
              }
            ]
          }
        }'
      ```

      ```python Python highlight={3-11,15,18,21,24} theme={"dark"}
      from lago_python_client.models import Plan, Charge

      charge = Charge(
        billable_metric_id='__BILLABLE_METRIC_ID__',
        charge_model='package',
        properties={
          'amount': '1.50',
          'free_units': 10000,
          'package_size': 1000
        }
      )

      plan = Plan(
        name='Algolia Search PAYG',
        code='__PLAN_CODE__',
        interval='monthly',
        description='Pay-as-you-go pricing for Search API',
        amount_cents=0,
        amount_currency='USD',
        pay_in_advance=False,
        charges=[charge]
      )

      client.plans.create(plan)
      ```

      ```ruby Ruby highlight={3,6,9-19} theme={"dark"}
      client.plans.create({
        name: 'Algolia Search PAYG',
        code: '__PLAN_CODE__',
        interval: 'monthly',
        description: 'Pay-as-you-go pricing for Search API',
        amount_cents: 0,
        amount_currency: 'USD',
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            charge_model: 'package',
            properties: {
              amount: '1.50',
              free_units: 10000,
              package_size: 1000
            }
          }
        ]
      })
      ```

      ```javascript JavaScript highlight={3,6,9-19,22} theme={"dark"}
      const plan = {
        name: 'Algolia Search PAYG',
        code: '__PLAN_CODE__',
        interval: 'monthly',
        description: 'Pay-as-you-go pricing for Search API',
        amount_cents: 0,
        amount_currency: 'USD',
        pay_in_advance: false,
        charges: [
          {
            billable_metric_id: '__BILLABLE_METRIC_ID__',
            charge_model: 'package',
            properties: {
              amount: '1.50',
              free_units: 10000,
              package_size: 1000
            }
          }
        ]
      };

      await client.plans.createPlan({ plan })
      ```

      ```go Go highlight={3,6,9-19,22} theme={"dark"}
      planInput := &lago.PlanInput{
        Name:           "Algolia Search PAYG",
        Code:           "__PLAN_CODE__",
        Interval:       "monthly",
        Description:    "Pay-as-you-go pricing for Search API",
        AmountCents:    0,
        AmountCurrency: "USD",
        PayInAdvance:   false,
        Charges: []*lago.PlanChargeInput{
          {
            BillableMetricID: "__BILLABLE_METRIC_ID__",
            ChargeModel:        "package",
            Properties: map[string]interface{}{
              "amount":       "1.50",
              "free_units":   10000,
              "package_size": 1000,
            },
          },
        },
      }

      plan, err := client.Plan().Create(ctx, planInput)
      ```
    </CodeGroup>

    Refer to the [API reference](/api-reference/plans/create) and [guide on package charges](/guide/plans/charges/charge-models/package) to learn more.
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
    Send usage events to Lago to track API requests.

    1. Set the `code` to match your billable metric code
    2. Include `search_requests_volume` property with the number of requests

    <CodeGroup>
      ```bash cURL highlight={7-11} theme={"dark"}
      curl --location --request POST "$LAGO_URL/api/v1/events" \
        --header 'Authorization: Bearer __API_KEY__' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "event": {
            "transaction_id": "__TRANSACTION_ID__",
            "code": "__BILLABLE_METRIC_CODE__",
            "external_subscription_id": "__EXTERNAL_SUBSCRIPTION_ID__",
            "properties": {
              "search_requests_volume": 5000
            }
          }
        }'
      ```

      ```python Python highlight={5-9,12} theme={"dark"}
      from lago_python_client.models import Event

      event = Event(
        transaction_id="__TRANSACTION_ID__",
        code="__BILLABLE_METRIC_CODE__",
        external_subscription_id="__EXTERNAL_SUBSCRIPTION_ID__",
        properties={
          "search_requests_volume": 5000
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
          search_requests_volume: 5000
        }
      )
      ```

      ```js Javascript highlight={3-7,10} theme={"dark"}
      const event = {
        transaction_id: "__TRANSACTION_ID__",
        code: "__BILLABLE_METRIC_CODE__",
        external_subscription_id: "__EXTERNAL_SUBSCRIPTION_ID__",
        properties: {
          search_requests_volume: 5000
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
          "search_requests_volume": 5000,
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

'Pay-as-you-go' pricing strategies are popular among API companies like Algolia.
With Lago, you can adapt this template to your products and services, using some of our most popular features:

1. **Plan models**, with or without subscription;‍
2. **Billable metrics**, including the 'sum' aggregation type; and‍
3. **Charges**, including our package and graduated pricing models.

Give it a try, click [here](https://www.getlago.com/get-started) to get started!
