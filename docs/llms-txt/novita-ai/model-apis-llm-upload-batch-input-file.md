# Source: https://novita.ai/docs/api-reference/model-apis-llm-upload-batch-input-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload file

Upload the batch input file so that it can be correctly referenced when creating a batch.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="file" type="file" required={true}>
  The batch input file to be uploaded should be in `.jsonl` format, with each line detailing an API inference request.

  Each request must have a unique `custom_id` to identify inference results in the output file after batch processing. The parameters within the `body` field of each line are used as the actual inference request parameters for the endpoint.

  <Warning>
    All requests within a single batch JSONL file must target the same model. Do not mix requests for different models in one batch.
  </Warning>

  Here is an example of an input file containing two requests:

  ```JSON  theme={"system"}
  {"custom_id": "request-1", "body": {"model": "deepseek/deepseek-v3-0324", "messages": [{"role": "user", "content": "Hello, world!"}], "max_tokens": 400}}
  {"custom_id": "request-2", "body": {"model": "deepseek/deepseek-v3-0324", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 1000}}
  ```
</ParamField>

<ParamField body="purpose" type="string" required={true}>
  The purpose of the uploaded file. For batch processing, this should be set to `batch`.

  Enum: `batch`
</ParamField>

## Response

<ResponseField name="id" type="string" required={true}>
  The unique identifier of the uploaded file.
</ResponseField>

<ResponseField name="object" type="string" required={true}>
  The object type, which is always `file`.
</ResponseField>

<ResponseField name="bytes" type="integer" required={true}>
  The size of the uploaded file in bytes.
</ResponseField>

<ResponseField name="created_at" type="integer" required={true}>
  The Unix timestamp (in seconds) when the file was created.
</ResponseField>

<ResponseField name="filename" type="string" required={true}>
  The name of the uploaded file.
</ResponseField>

<ResponseField name="purpose" type="string" required={true}>
  The purpose of the uploaded file.
</ResponseField>

<ResponseField name="metadata" type="object" required={false}>
  Additional metadata about the uploaded file.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="total_requests" type="integer" required={true}>
      The total number of requests contained in the batch input file.
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).