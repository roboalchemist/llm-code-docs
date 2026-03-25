# Source: https://novita.ai/docs/api-reference/gpu-instance-list-cpu-products.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List CPU Products

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="clusterId" type="string" required={false}>
  Filter by specified cluster ID. String, length limit: 0-255 characters.
</ParamField>

<ParamField query="productName" type="string" required={false}>
  Filter by product name (fuzzy match). String, length limit: 0-255 characters.
</ParamField>

## Response

<ResponseField name="id" type="string" required={true}>
  CPU product ID.
</ResponseField>

<ResponseField name="name" type="string" required={true}>
  CPU product name.
</ResponseField>

<ResponseField name="cpuNum" type="integer" required={false}>
  Number of CPU cores.
</ResponseField>

<ResponseField name="memorySize" type="integer" required={false}>
  Memory size (GB).
</ResponseField>

<ResponseField name="rootfsSize" type="integer" required={false}>
  Root filesystem size (GB).
</ResponseField>

<ResponseField name="localVolumeSize" type="integer" required={false}>
  Local disk size (GB).
</ResponseField>

<ResponseField name="availableDeploy" type="boolean" required={false}>
  Whether this product can be used to create an instance. Values:

  * true: This product can be used to create an instance.
  * false: Insufficient resources, cannot create an instance.
</ResponseField>

<ResponseField name="price" type="integer" required={false}>
  Unit price of the product.
</ResponseField>


Built with [Mintlify](https://mintlify.com).