# Source: https://getlago.com/docs/guide/billable-metrics/aggregation-types/weighted-sum.md

# WEIGHTED SUM

The Weighted Sum aggregation type adds up the value of a defined event property and prorates it based on time used per period.
This is especially handy for automated GB/second calculations, for instance.

<Info>
  Currently, prorating is available **per second per period**.
  Feel free to reach out if you need additional proration options, such as hourly rates.
</Info>

<Frame caption="WEIGHTED SUM calculation method">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/weighted-sum.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=c263c2055939758c54dde6babf0fa3ca" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="guide/images/weighted-sum.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/weighted-sum.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=cb9bd9ba3dbf07d1a0cfe1d83fb6db21 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/weighted-sum.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9bc0bd7bf3a41097fe1ad98522ece211 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/weighted-sum.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=afa71c4f21767771869ddf799e2bcb31 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/weighted-sum.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=c84b35df2f18d7201adb0e6defdadc48 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/weighted-sum.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=756e88339403e56212dd35591fc5bdd1 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/weighted-sum.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=0f7d4a1b363877c94221cbfb4837c7a9 2500w" />
</Frame>

## WEIGHTED SUM billable metric

<Tabs>
  <Tab title="Dashboard">
    Here is how you can create a weighted sum aggregation from the UI:

    1. Access the **"Billable metrics"** section via the side menu;
    2. Create a new billable metric;
    3. Define a name, a code and an optional description;
    4. Select **"weighted sum"** as the aggregation type;
    5. Define it this metric is `metered` or `recurring`;
    6. Define the property to aggregate;
    7. Define the `weighted_interval` used for time proration. Currently, Lago only supports `seconds`.
    8. Apply dimension groups if any; and
    9. Click **"Add billable metric"**.

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
              "name": "GB Seconds",
              "code": "gb/s",
              "description": "Gigabytes prorated per seconds used per period",
              "aggregation_type": "weighted_sum_agg",
              "weighted_interval": "seconds",
              "field_name": "gb",
              "group": {}
          }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Calculation example

Lago calculates the `SUM(events.properties.property_name) / (DATEDIFF(SECOND, timestamp.event_1, timestamp.event_2) + 1) * (DATEDIFF(SECOND, 'period_start', 'period_end') + 1)` for the two following events received.

```json  theme={"dark"}
//Event received #1
{
    "transaction_id": "transaction_1",
    "external_customer_id": "1",
    "timestamp": "2022-03-16T00:00:00Z",
    "code": "gb/s",
    "properties": {
        "gb": 20
    }
}

//Event received #2
{
    "transaction_id": "transaction_2",
    "external_customer_id": "1",
    "timestamp": "2022-03-17T00:00:00Z",
    "code": "gb/s",
    "properties": {
        "gb": 10
    }
}
```

In that case, with this aggregation type, Lago adds up the values of the `gb` property in the event payloads, but prorates it based on time used during the current period.
Keep in mind that the entire month comprises 2,678,400 seconds. The first 20 GB has been used for a day (86,400 seconds), and the 30 GB (20 + 10) has been used for 15 days (1,296,000 seconds till the end of the month):

* (20 / 2678400) x 86400 = 0.64516129032 GB/s
* (30 / 2678400) x 1296000 = 14.5161290323 GB/s
* 0.64516129032 + 14.5161290323 = **15.1612903226 GB/s**
