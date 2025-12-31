# Source: https://getlago.com/docs/guide/billable-metrics/aggregation-types/sum.md

# SUM

The sum aggregation type adds up the value of a defined event property.

<Frame caption="SUM calculation method">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/sum.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=b479a67d98f6b90a1a96e513116d8d57" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="guide/images/sum.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/sum.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=1d1c5263344b80fde7da3391f41153ee 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/sum.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=7e33fa557d288be9bc8b93146800f03c 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/sum.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=4b90c6c2d1e0251fa5cd528ff89392cc 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/sum.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=7243e47ffa7ff89ec25f01f01ae0ed95 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/sum.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=f138ab80d2ab6b4c0dc362d5b8b5f06f 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/sum.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9f9e9fb78d9e7a19a4257691ec350213 2500w" />
</Frame>

## SUM billable metric

<Tabs>
  <Tab title="Dashboard">
    Here is how you can create a sum aggregation from the UI:

    1. Access the **"Billable metrics"** section via the side menu;
    2. Create a new billable metric;
    3. Define a name, a code and an optional description;
    4. Select **"sum"** as the aggregation type;
    5. Define it this metric is `metered` or `recurring`;
    6. Define the property to aggregate;
    7. Apply dimension groups if any; and
    8. Click **"Add billable metric"**.

    <Info>
      This billable metric can be both `metered` or `recurring`.
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
              "aggregation_type": "sum_agg",
              "field_name": "total_requests",
              "group": {}
          }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Calculation example

Lago calculates the `SUM(events.properties.property_name)` for the two following events received.

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

In that case, with this aggregation type, Lago adds up the values of the `total_requests` property in the event payloads, **resulting in a billable value of 30 units.**
