# Source: https://novita.ai/docs/api-reference/gpu-instance-renewal-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Renew Subscription Instance

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceId" type="string" required={true}>
  The ID of the subscription instance to be renewed.
</ParamField>

<ParamField body="month" type="integer" required={true}>
  Renewal period, in months.
</ParamField>


Built with [Mintlify](https://mintlify.com).