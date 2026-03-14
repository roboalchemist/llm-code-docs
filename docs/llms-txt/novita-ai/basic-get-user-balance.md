# Source: https://novita.ai/docs/api-reference/basic-get-user-balance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Balance Info

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseField name="availableBalance" type="string" required={false}>
  The user's credit balance, unit is 0.0001 USD.
</ResponseField>

<ResponseField name="cashBalance" type="string" required={false}>
  The remaining balance of your top-up. The Unit is 0.0001 USD.
</ResponseField>

<ResponseField name="creditLimit" type="string" required={false}>
  Your credit limit (i.e., the maximum amount you can owe), unit is 0.0001 USD.
</ResponseField>

<ResponseField name="outstandingInvoices" type="string" required={false}>
  The amount you currently owe, unit is 0.0001 USD.
</ResponseField>


Built with [Mintlify](https://mintlify.com).