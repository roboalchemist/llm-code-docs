# Source: https://getlago.com/docs/guide/billable-metrics/aggregation-types/latest.md

# LATEST

The latest aggregation type selects the most recent value of a specified event property from all received events.

<Frame caption="LATEST calculation method">
  <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/latest.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=881b2357be5ea1f21d6d24f9896b28bb" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="guide/images/latest.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/latest.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=8d93a27405897b16cbaf4be6a78e4671 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/latest.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=c13816ac4eeea97ee46836e26dabc0aa 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/latest.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=4890cd600d5690a6afd2ffbae48a182a 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/latest.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=55eae77ac032c46489625e131b5a2f1b 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/latest.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=08d574189f9ac2ce99bda89b87119e22 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/latest.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=2a2c5015686b862a4a915daf38550e9b 2500w" />
</Frame>

## LATEST billable metric

<Tabs>
  <Tab title="Dashboard">
    Here is how you can create a max aggregation from the UI:

    1. Access the **"Billable metrics"** section via the side menu;
    2. Create a new billable metric;
    3. Define a name, a code and an optional description;
    4. Select **"latest"** as the aggregation type;
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
              "aggregation_type": "latest_agg",
              "field_name": "total_requests",
              "group": {}
          }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Calculation example

Lago calculates the `LAST_VALUE(events.properties.property_name) OVER ([PARTITION BY events.timestamp])` for the two following events received.

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

In that case, with this aggregation type, Lago takes the latest value of `total_requests` property from all events, **resulting in a billable value of 10 units.**
