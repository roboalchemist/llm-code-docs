# Source: https://smartcar.com/docs/errors/api-errors/billing-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Billing Errors

> Thrown when limits have been reached based on your plan, or if the feature is not available.

# `VEHICLE_LIMIT`

You’ve reached the limit of vehicles in your plan. Please upgrade to unlock access to more vehicles.

```json VEHICLE_LIMIT theme={null}
{
  "type": "BILLING",
  "code": "VEHICLE_LIMIT",
  "description": "You’ve reached the limit of vehicles in your plan. Please upgrade to unlock access to more vehicles.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#vehicle-limit",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" }
}
```

### Troubleshooting Steps

To resolve this error, please [contact us](mailto:support@smartcar.com) to upgrade your plan and increase your vehicle limit.
Please note that you won’t be able to make requests to additional vehicles until the end of the current billing period or until you have upgraded your plan.

# `INVALID_PLAN`

The feature you are trying to use is not included in your current pricing plan. Please visit our pricing page to learn more about our plans and features.

```json INVALID_PLAN theme={null}
{
  "type": "BILLING",
  "code": "INVALID_PLAN",
  "description": "The feature you are trying to use is not included in your current pricing plan. Please visit our pricing page to learn more about our plans and features.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#invalid-plan",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" } 
}
```

### Troubleshooting Steps

If you have checked our pricing page and believe that the feature you are trying to use is included in your plan,
please [contact us](mailto:support@smartcar.com) and we’ll be happy to assist you.

# `VEHICLE_REQUEST_LIMIT`

You have exceeded the number of API requests that are allowed for **this** vehicle in the current billing period.
Please log in to the [Smartcar dashboard](https://dashboard.smartcar.com/login) and visit the Billing tab to learn more.

```json VEHICLE_REQUEST_LIMIT theme={null}
{
  "type": "BILLING",
  "code": "VEHICLE_REQUEST_LIMIT",
  "description": "You have exceeded the number of API requests that are allowed for this vehicle in the current billing period. Please log into the Smartcar dashboard and visit the Billing tab to learn more.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#vehicle-request-limit",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" } 
}
```

### Troubleshooting Steps

To resolve this error, please [contact us](mailto:support@smartcar.com) to upgrade your plan and increase your vehicle limit.
Please note that you won’t be able to make additional requests to this vehicle until the end of the current billing period or until you have upgraded your plan.

# `ACCOUNT_SUSPENDED`

Your Smartcar account is past due and has been suspended.
Please reach out to our finance team to resolve this issue.

```json ACCOUNT_SUSPENDED theme={null}
{
  "type": "BILLING",
  "code": "ACCOUNT_SUSPENDED",
  "description": "Your Smartcar account is past due and has been suspended. Please reach out to our finance team to resolve this issue.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#account-suspended",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20882a",
  "resolution": { "type": "FINANCE" } 
}
```

### Troubleshooting Steps

To resolve this error, please [contact us](mailto:finance@smartcar.com) to pay past due invoices.
Please note that you won’t be able to make any requests until you have resolved this issue.
