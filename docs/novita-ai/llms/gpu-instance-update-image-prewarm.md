# Source: https://novita.ai/docs/api-reference/gpu-instance-update-image-prewarm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Image Prewarm Task

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="id" type="string" required={true}>
  Prewarm task ID.
</ParamField>

<ParamField body="note" type="string" required={false}>
  Task note.
</ParamField>


Built with [Mintlify](https://mintlify.com).