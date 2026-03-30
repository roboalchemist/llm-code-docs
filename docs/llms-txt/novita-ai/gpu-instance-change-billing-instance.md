# Source: https://novita.ai/docs/api-reference/gpu-instance-change-billing-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Convert Pay-As-You-Go Instance to Subscription

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  The ID of the pay-as-you-go instance to be converted to a subscription instance.
</ParamField>

<ParamField body="month" type="integer" required={true}>
  Subscription period after conversion, in months.
</ParamField>


Built with [Mintlify](https://mintlify.com).