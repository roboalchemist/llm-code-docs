# Source: https://docs.linkup.so/pages/documentation/development/pricing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing

> How the Linkup API pricing system works

## Billing

When you first sign up, your account is automatically credited with 5 euros. We will top up your credits back to 5 euros each month. You can add money to your account in the [Billing](https://app.linkup.so/organization/billing) section of the Linkup app.

<Tip>If you top up your account with 1,000 euros or more, we will add free credits to your account</Tip>

| Top up amount | Extra credits |
| ------------- | ------------- |
| >€1,000       | 10%           |
| >€5,000       | 15%           |
| >€10,000      | 20%           |

Please reach out to [support@linkup.so](mailto:support@linkup.so) for custom needs.

Each time you make a successful request to our API endpoints, an amount is subtracted from your account. The amount deducted per call depends on the endpoint and parameters:

## Search Endpoint

For the `/search` endpoint, the cost depends on the depth parameter:

| Call Type | Cost   |
| --------- | ------ |
| Standard  | €0.005 |
| Deep      | €0.05  |

## Fetch Endpoint

For the `/fetch` endpoint, the cost depends on the renderJS parameter:

| Call Type                    | Cost   |
| ---------------------------- | ------ |
| Without JS (renderJS: false) | €0.001 |
| With JS (renderJS: true)     | €0.005 |

If your account runs out, the API will respond with a 429 HTTP error.

<Check>
  **Important note**: No credit is subtracted when an error occurs, whether it is because of a missing parameter, an internal server error, but also when we were not able to find anything relevant to your query.
</Check>

You can view your current consumption by visiting the [Linkup App](https://app.linkup.so/consumer/dashboard).


Built with [Mintlify](https://mintlify.com).