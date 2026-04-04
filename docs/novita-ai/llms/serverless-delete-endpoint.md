# Source: https://novita.ai/docs/api-reference/serverless-delete-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Endpoint

## Description

After deleting an endpoint, all worker processes associated with this endpoint will be automatically removed. Please proceed with caution.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="name" type="string" required={true}>
  The ID of the endpoint to delete.
</ParamField>


Built with [Mintlify](https://mintlify.com).