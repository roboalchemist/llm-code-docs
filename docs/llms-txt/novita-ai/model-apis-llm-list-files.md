# Source: https://novita.ai/docs/api-reference/model-apis-llm-list-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List files

Displays a list of all available files.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseField name="code" type="string" required={true}>
  HTTP status code indicating the result of the request.
</ResponseField>

<ResponseField name="message" type="string" required={true}>
  A descriptive message about the request result.
</ResponseField>

<ResponseField name="data" type="array" required={true}>
  An array of file objects.

  <Expandable title="File Object Properties" defaultOpen={false}>
    <ResponseField name="id" type="string" required={true}>
      The unique identifier of the file.
    </ResponseField>

    <ResponseField name="object" type="string" required={true}>
      The object type, which is always `file`.
    </ResponseField>

    <ResponseField name="bytes" type="integer" required={true}>
      The size of the file in bytes.
    </ResponseField>

    <ResponseField name="filename" type="string" required={true}>
      The name of the file.
    </ResponseField>

    <ResponseField name="created_at" type="integer" required={true}>
      The Unix timestamp (in seconds) when the file was created.
    </ResponseField>

    <ResponseField name="expires_at" type="integer" required={false}>
      The Unix timestamp (in seconds) when the file will expire. Only present for output files.
    </ResponseField>

    <ResponseField name="purpose" type="string" required={true}>
      The purpose of the file.

      Available purposes:

      * `batch` - Input file for batch processing
      * `batch_output` - Output file from batch processing
    </ResponseField>

    <ResponseField name="metadata" type="object" required={true}>
      Additional metadata about the file.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="total_requests" type="integer" required={false}>
          The total number of requests in the batch input file. Only present for batch input files.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).