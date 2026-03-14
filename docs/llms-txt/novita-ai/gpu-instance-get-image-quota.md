# Source: https://novita.ai/docs/api-reference/gpu-instance-get-image-quota.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Image Prewarm Quota

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseField name="total" type="integer" required={true}>
  Number of created prewarm tasks.
</ResponseField>

<ResponseField name="limit" type="integer" required={true}>
  Maximum number of prewarm tasks that can be created.
</ResponseField>

<ResponseField name="perImageSize" type="integer" required={true}>
  Maximum image size per prewarm task (GB).
</ResponseField>


Built with [Mintlify](https://mintlify.com).