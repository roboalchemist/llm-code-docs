# Source: https://novita.ai/docs/api-reference/gpu-instance-update-vpc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update VPC Network

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="networkId" type="string" required={true}>
  Cluster ID. String, length limit: 1-255 characters.
</ParamField>

<ParamField body="name" type="string" required={false}>
  Custom network name. String, length limit: 1-30 characters.
</ParamField>


Built with [Mintlify](https://mintlify.com).