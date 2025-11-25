# Source: https://getlago.com/docs/guide/events/retrieve-usage.md

# Retrieving usage

> Learn how to retrieve usage data for both current and past billing periods.

## Retrieve current usage

<Tabs>
  <Tab title="Dashboard">
    The [current usage endpoint](../../api-reference/customer-usage/get-current) retrieves real-time usage data for the current open billing period.
    Because this billing period is still ongoing, invoice details are subject to change as new usage continues to accrue.

    Whether it's fetched from the UI or the API, the response includes:

    1. Aggregated usage data for the current period: Total units consumed and total customers' cost (so far)

    2. Detailed breakdowns per metric: Units and amounts by metric and optional sub-breakdowns by filters or groupings (e.g., per project, environment, or AI models)

    <Info>
      Note: Since the billing period is not yet finalized, the retrieved data should be treated as provisional. Final invoice values may differ.
    </Info>

    Notice that if the events were sent with timestamp in the future, they are taken into account in current usage. Yet, if you terminate the
    subscription before the timestamp of this event, it will be ignored in the termination invoice.

    <Frame caption="Retrieving current usage">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/current-usage.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=00a9984c10ab7008e26d553a48a4fbbe" data-og-width="1286" width="1286" data-og-height="892" height="892" data-path="guide/events/images/current-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/current-usage.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=aa85af7189f14c7cc1be7efb1beec819 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/current-usage.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=66f67f85c0a4eb8327827534ccf7c2f2 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/current-usage.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=5668eb756e944fa45891879ae1fb93be 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/current-usage.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=d8e16ab43a77ce456cd41e6cb1c466db 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/current-usage.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=d70447564792e39725b3bff9c62184bb 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/current-usage.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=d00a5ffb685ac661061fa4dcba4a2b1d 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Retrieve current usage theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"
      EXTERNAL_CUSTOMER_ID="__EXTERNAL_CUSTOMER_ID__"
      EXTERNAL_SUBSCRIPTION_ID="__EXTERNAL_SUBSCRIPTION_ID__"

      curl --location --request GET "$LAGO_URL/api/v1/customers/$EXTERNAL_CUSTOMER_ID/current_usage?external_subscription_id=$EXTERNAL_SUBSCRIPTION_ID" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Retrieve projected usage

<Tabs>
  <Tab title="Dashboard">
    Another endpoint provides an estimate of usage and billing amounts projected through the end of the current billing period.
    It uses current consumption trends and billing configuration to forecast the likely totals at period close. Projected usage is listed under the [projected usage endpoint](../../api-reference/customer-usage/get-projected).

    Whether it's fetched from the UI or the API, the response includes:

    1. Projected total usage units and estimated billing amount for the full billing period
    2. Per-metric projections, including: Forecasted units and amounts for each billable metric and projections broken down by optional sub-filters or groups (e.g., per project, environment, or AI models)

    <Info>
      Note: Recurring metrics, such as Seats, typically remain stable over time, unlike metered metrics which fluctuate. Therefore, the projected usage for a recurring metric is assumed to be equal to its current usage.
    </Info>

    <Frame caption="Retrieving projected usage">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/projected-usage.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=08ea89b6e97cae45e8ce61223783b3c5" data-og-width="1316" width="1316" data-og-height="898" height="898" data-path="guide/events/images/projected-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/projected-usage.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=35a7dacf674e1dceeb8bcb1656103fd8 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/projected-usage.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=42b89127f444745be380cd9dda3828a6 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/projected-usage.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=3b7152c53830adf69a3c6eb0ef6f9d77 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/projected-usage.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=7f338ab827b12a7655f5ff0019a64e57 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/projected-usage.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=9b6a565e33c0d0cc3d175218a05d1673 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/projected-usage.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=4684f6027e9485ac9052eaf1c75df3d0 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Retrieve projected usage theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"
      EXTERNAL_CUSTOMER_ID="__EXTERNAL_CUSTOMER_ID__"
      EXTERNAL_SUBSCRIPTION_ID="__EXTERNAL_SUBSCRIPTION_ID__"

      curl --location --request GET "$LAGO_URL/api/v1/customers/$EXTERNAL_CUSTOMER_ID/projected_usage?external_subscription_id=$EXTERNAL_SUBSCRIPTION_ID" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Retrieve past usage

<Tabs>
  <Tab title="Dashboard">
    The [past usage endpoint](../../api-reference/customer-usage/get-past) allows you to retrieve customer usage data for closed billing periods.
    Once a billing period has ended and is marked as closed, the associated usage data becomes final and immutable, ensuring consistency in billing and reporting.

    Modifying the price of a metric, or even deleting a metric, has no effect on past usage or previously issued invoices.
    Once a billing period is closed and its associated invoice is finalized, the past usage quantities, pricing, and resulting fees are locked.
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Retrieve current usage theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"
      EXTERNAL_CUSTOMER_ID="__EXTERNAL_CUSTOMER_ID__"
      EXTERNAL_SUBSCRIPTION_ID="__EXTERNAL_SUBSCRIPTION_ID__"

      curl --location --request GET "$LAGO_URL/api/v1/customers/$EXTERNAL_CUSTOMER_ID/past_usage?external_subscription_id=$EXTERNAL_SUBSCRIPTION_ID" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>
  </Tab>
</Tabs>
