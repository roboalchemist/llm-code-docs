# Source: https://novita.ai/docs/api-reference/gpu-instance-delete-image-prewarm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Image Prewarm Tasks

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="ids" type="string[]" required={true}>
  IDs of prewarm tasks to delete.
</ParamField>


Built with [Mintlify](https://mintlify.com).