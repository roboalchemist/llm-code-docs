# Source: https://getlago.com/docs/guide/billable-metrics/aggregation-types/max.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MAX

The max aggregation type selects the highest value of a specified event property from all received events.

<Frame caption="MAX calculation method">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/max.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=bc12c9f4a6871177870bdea52b3e8e50" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="guide/images/max.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/max.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=221b977bd9576cdacaeff49fdba94f87 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/max.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=e0fdc1f64f74e578bd060cac38b8c624 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/max.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=491ddd97368f5b638870d99a8e4a5e26 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/max.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=6b7ff4aaacdbe65c3b81e58e0e0b1663 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/max.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=71bc90fad70d568aa0a0266a37af17fe 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/max.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=0048229353198be4ba816821e0088c62 2500w" />
</Frame>

## MAX billable metric

<Tabs>
  <Tab title="Dashboard">
    Here is how you can create a max aggregation from the UI:

    1. Access the **"Billable metrics"** section via the side menu;
    2. Create a new billable metric;
    3. Define a name, a code and an optional description;
    4. Select **"max"** as the aggregation type;
    5. Define the property to aggregate;
    6. Apply dimension groups if any; and
    7. Click **"Add billable metric"**.

    <Info>
      This billable metric is `metered` only, meaning it cannot be recurring, and the number of billing units resets to 0 at the end of each period.
    </Info>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash  theme={"dark"}
          LAGO_URL="https://api.getlago.com"
          API_KEY="__YOUR_API_KEY__"

          curl --location --request POST "$LAGO_URL/api/v1/billable_metrics" \
          --header "Authorization: Bearer $API_KEY" \
          --header 'Content-Type: application/json' \
          --data-raw '{
              "billable_metric": {
              "name": "API Request",
              "code": "api_requests",
              "description": "Number of API requests.",
              "aggregation_type": "max_agg",
              "field_name": "total_requests",
              "group": {}
          }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Calculation example

Lago calculates the `MAX(events.properties.property_name)` for the two following events received.

```json  theme={"dark"}
//Event received #1
{
    "transaction_id": "transaction_1",
    "external_customer_id": "1",
    "timestamp": "2022-03-16T00:00:00Z",
    "code": "api_requests",
    "properties": {
        "total_requests": 20
    }
}

//Event received #2
{
    "transaction_id": "transaction_2",
    "external_customer_id": "1",
    "timestamp": "2022-03-17T00:00:00Z",
    "code": "api_requests",
    "properties": {
        "total_requests": 10
    }
}
```

In that case, with this aggregation type, Lago takes the higest value of `total_requests` property from all events, **resulting in a billable value of 20 units.**
