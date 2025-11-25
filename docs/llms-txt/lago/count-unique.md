# Source: https://getlago.com/docs/guide/billable-metrics/aggregation-types/count-unique.md

# UNIQUE COUNT

The unique count aggregation type counts only the unique values of a specified event property.

<Frame caption="UNIQUE COUNT calculation method">
  <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count-unique.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=657c797f4174be09cdaba2e18cb88f29" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="guide/images/count-unique.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count-unique.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=226ad4657f7e33612b7c3bb2bf38ee8d 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count-unique.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=b2f8d1a4aa7433115e8873417480c63c 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count-unique.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=a7a27759faa647394c1a1e6dffefae13 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count-unique.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=9f626214c5e06e6bf55b4b050c2f22b6 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count-unique.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=63493aa14e5a7d3aabe4e66b3e37396c 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/count-unique.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=444c611c9fa04bfadb7ab6c0dcd2941e 2500w" />
</Frame>

## UNIQUE COUNT billable metric

<Tabs>
  <Tab title="Dashboard">
    Here is how you can create a unique count aggregation from the UI:

    1. Access the **"Billable metrics"** section via the side menu;
    2. Create a new billable metric;
    3. Define a name, a code and an optional description;
    4. Select **"count unique"** as the aggregation type;
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
              "aggregation_type": "unique_count_agg",
              "field_name": "request_id",
              "group": {}
          }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Calculation example

Lago calculates the `COUNT_DISTINCT(events.properties.property_name)` for the two following events received.

```json  theme={"dark"}
//Event received #1
{
    "transaction_id": "transaction_1",
    "external_customer_id": "1",
    "timestamp": "2022-03-16T00:00:00Z",
    "code": "api_requests",
    "properties": {
        "request_id": "id_1"
    }
}

//Event received #2
{
    "transaction_id": "transaction_2",
    "external_customer_id": "1",
    "timestamp": "2022-03-17T00:00:00Z",
    "code": "api_requests",
    "properties": {
        "request_id": "id_1"
    }
}
```

In that case, with this aggregation type, Lago only counts the unique values `request_id` property in the event payloads, **resulting in a billable value of 1 unit.**
