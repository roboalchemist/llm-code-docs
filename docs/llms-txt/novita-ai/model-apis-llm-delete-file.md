# Source: https://novita.ai/docs/api-reference/model-apis-llm-delete-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete file

Deletes a specific file using its file ID.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Path Parameters

<ParamField path="file_id" type="string" required={true}>
  The unique identifier of the file to delete.
</ParamField>

## Response

<ResponseField name="deleted" type="boolean" required={true}>
  Indicates whether the file was successfully deleted. Returns `true` if the deletion was successful.
</ResponseField>

<ResponseField name="id" type="string" required={true}>
  The unique identifier of the deleted file.
</ResponseField>

<ResponseField name="object" type="string" required={true}>
  The object type, which is always `file`.
</ResponseField>


Built with [Mintlify](https://mintlify.com).