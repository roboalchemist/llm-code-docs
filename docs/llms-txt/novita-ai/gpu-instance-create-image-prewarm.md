# Source: https://novita.ai/docs/api-reference/gpu-instance-create-image-prewarm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Image Prewarm Task

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="imageUrl" type="string" required={true}>
  Image address to prewarm.
</ParamField>

<ParamField body="repositoryAuth" type="string" required={false}>
  Image registry authentication ID. Required only for private registries.
</ParamField>

<ParamField body="clusterId" type="string" required={true}>
  Cluster ID where the image should be prewarmed.
</ParamField>

<ParamField body="productIds" type="string[]" required={false}>
  Product IDs to prewarm on. Leave empty to prewarm globally in the cluster.
</ParamField>

<ParamField body="note" type="string" required={false}>
  Task note or description.
</ParamField>

## Response

<ResponseField name="id" type="string" required={true}>
  Created prewarm task ID.
</ResponseField>


Built with [Mintlify](https://mintlify.com).