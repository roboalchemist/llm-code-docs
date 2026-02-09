# Source: https://getlago.com/docs/guide/billable-metrics/aggregation-types/count.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# COUNT

The count aggregation type is straightforward. It tallies the exact number of events received during a period.

<Frame caption="COUNT calculation method">
  <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=4a9878963e1f6d8c628cd34b09f40d7e" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="guide/images/count.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=ee6ed5716b08391a9391f8443d7fad82 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=a0792d8321cb48939ddd9a3aac2c4b84 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=9c49a8b13203441e0e0a946a837c2045 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=f204d63d7151abfa83dbbd02b912a0dc 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=01d31c43342b9d83ecb01e0407a7d133 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=7acc969d0c90c3e6e63771f1522ff3df 2500w" />
</Frame>

## COUNT billable metric

<Tabs>
  <Tab title="Dashboard">
    Here is how you can create a count aggregation from the UI:

    1. Access the **"Billable metrics"** section via the side menu;
    2. Create a new billable metric;
    3. Define a name, a code and an optional description;
    4. Select **"count"** as the aggregation type;
    5. Apply dimension groups if any; and
    6. Click **"Add billable metric"**.

    <Info>
      This billable metric is `metered` only, meaning it cannot be recurring, and the number
      of billing units resets to 0 at the end of each period.
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
              "aggregation_type": "count_agg",
              "group": {}
          }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Calculation example

Lago calculates the `COUNT(events.code)` for the two following events received.

```json  theme={"dark"}
//Event received #1
{
    "transaction_id": "transaction_1",
    "external_customer_id": "1",
    "timestamp": "2022-03-16T00:00:00Z",
    "code": "api_requests",
    "properties": {}
}

//Event received #2
{
    "transaction_id": "transaction_2",
    "external_customer_id": "1",
    "timestamp": "2022-03-17T00:00:00Z",
    "code": "api_requests",
    "properties": {}
}
```

In that case, with this aggregation type, Lago simply counts the number events received, **resulting in a billable value of 2 units.**
