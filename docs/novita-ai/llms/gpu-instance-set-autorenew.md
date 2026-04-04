# Source: https://novita.ai/docs/api-reference/gpu-instance-set-autorenew.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Auto Renew

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="instanceIds" type="string[]" required={true}>
  Instance ID list.
</ParamField>

<ParamField body="autoRenew" type="boolean" required={true}>
  Whether to enable automatic renewal.
</ParamField>

<ParamField body="autoRenewMonth" type="integer" required={true}>
  Automatic renewal period, in months.
</ParamField>


Built with [Mintlify](https://mintlify.com).