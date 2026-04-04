# Start a subscription for a future date

You can let your customers start their subscriptions on a future date. This is useful when customers want to start a new subscription after a current subscription ends, or when they wish to take advantage of a current promotion but activate their subscription on a later date.

If you start a subscription on a future date, any [setup or one-time fee](/docs/subscriptions/customize/one-time-fee/) associated with the subscription is charged immediately upon sign-up, but regular payments towards the subscription will start on the selected date.

You can update the subscription’s start date as long as it's in the future.

## Sample request

API endpoint used: [Create subscription](/docs/api/subscriptions/v1/#subscriptions_create)

```bash
curl -v -X POST https://api-m.sandbox.paypal.com/v1/billing/subscriptions
-H "Content-Type: application/json"
-H "Authorization: Bearer ACCESS-TOKEN"
-d '{
  "plan_id": "P-5ML4271244454362WXNWU5NQ",
  "start_time": "2021-11-01T00:00:00Z"
}'
```

## Modify code

- `ACCESS-TOKEN` - Your [access token](/docs/multiparty/get-started/#exchange-your-api-credentials-for-an-access-token).
- `plan_id` - The ID of the plan associated with this subscription.
- `start_time` - The desired subscription start time and date, in UTC format. This field can be updated as long as the new value is set in the future.