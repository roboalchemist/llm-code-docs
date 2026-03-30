# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/reference-i-ds.mdx

***

## stoplight-id: 0b87c98d87c36

# Reference IDs

The Cash App Pay API provides a `reference_id` field on all create, update, and upsert endpoints which can be used by an API client to set its own identifier for the resource. This allows API clients to establish a "link" between their systems and the Cash App Pay API.

All resources support querying by `reference_id` using "list" endpoints. If you lose the Cash App Pay-provided ID of a resource but have the `reference_id` from your systems, you can use this functionality to look up the Cash App Pay IDs of each resource.

## Requirements

Reference IDs must:

* Not contain any PII (personally identifiable information)
* Have between 1 and 1024 characters.

Reference IDs are required for brands and merchants. This prevents duplicate brands and merchants from being onboarded to Cash App Pay.
