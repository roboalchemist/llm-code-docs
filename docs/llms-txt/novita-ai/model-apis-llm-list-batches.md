# Source: https://novita.ai/docs/api-reference/model-apis-llm-list-batches.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List batch

Displays a list of all available batch jobs.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseField name="data" type="array" required={true}>
  An array of batch job objects.

  <Expandable title="Batch Object Properties" defaultOpen={false}>
    <ResponseField name="id" type="string" required={true}>
      A unique identifier for the batch job.
    </ResponseField>

    <ResponseField name="object" type="string" required={true}>
      The object type, which is always `batch`.
    </ResponseField>

    <ResponseField name="endpoint" type="string" required={true}>
      The API endpoint that the batch job is using for processing requests.
    </ResponseField>

    <ResponseField name="input_file_id" type="string" required={true}>
      The ID of the input file containing the batch requests.
    </ResponseField>

    <ResponseField name="output_file_id" type="string" required={true}>
      The ID of the output file containing the batch results. Empty until the batch is completed.
    </ResponseField>

    <ResponseField name="error_file_id" type="string" required={true}>
      The ID of the error file containing any errors that occurred during batch processing. Empty until errors occur.
    </ResponseField>

    <ResponseField name="completion_window" type="string" required={true}>
      The time window for batch completion. Currently fixed at `48h`.
    </ResponseField>

    <ResponseField name="in_progress_at" type="string | null" required={false}>
      The timestamp when the batch started processing. Null if not yet started.
    </ResponseField>

    <ResponseField name="expires_at" type="string | null" required={false}>
      The timestamp when the batch will expire. Null if not set.
    </ResponseField>

    <ResponseField name="finalizing_at" type="string | null" required={false}>
      The timestamp when the batch started finalizing. Null if not yet finalizing.
    </ResponseField>

    <ResponseField name="completed_at" type="string | null" required={false}>
      The timestamp when the batch was completed. Null if not yet completed.
    </ResponseField>

    <ResponseField name="failed_at" type="string | null" required={false}>
      The timestamp when the batch failed. Null if not failed.
    </ResponseField>

    <ResponseField name="expired_at" type="string | null" required={false}>
      The timestamp when the batch expired. Null if not expired.
    </ResponseField>

    <ResponseField name="cancelling_at" type="string | null" required={false}>
      The timestamp when the batch started cancelling. Null if not cancelling.
    </ResponseField>

    <ResponseField name="cancelled_at" type="string | null" required={false}>
      The timestamp when the batch was cancelled. Null if not cancelled.
    </ResponseField>

    <ResponseField name="status" type="string" required={true}>
      The current status of the batch job.

      Available statuses:

      * `VALIDATING` - The input file is being validated before the batch can begin
      * `PROGRESS` - Batch is in progress
      * `COMPLETED` - Batch processing completed successfully
      * `FAILED` - Batch processing failed
      * `EXPIRED` - Batch exceeded deadline
      * `CANCELLING` - Batch is being cancelled
      * `CANCELLED` - Batch was cancelled
    </ResponseField>

    <ResponseField name="errors" type="string" required={false}>
      Error messages if any errors occurred during batch processing.
    </ResponseField>

    <ResponseField name="version" type="integer" required={true}>
      The version number of the batch job.
    </ResponseField>

    <ResponseField name="created_at" type="string" required={true}>
      The timestamp when the batch job was created.
    </ResponseField>

    <ResponseField name="updated_at" type="string | null" required={false}>
      The timestamp when the batch job was last updated. Null if never updated.
    </ResponseField>

    <ResponseField name="created_by" type="string" required={true}>
      The unique identifier of the user who created the batch job.
    </ResponseField>

    <ResponseField name="created_by_key_id" type="string" required={true}>
      The API key ID used to create the batch job.
    </ResponseField>

    <ResponseField name="remark" type="string" required={false}>
      Optional remark or note for the batch job.
    </ResponseField>

    <ResponseField name="total" type="integer" required={true}>
      The total number of requests in the batch.
    </ResponseField>

    <ResponseField name="completed" type="integer" required={true}>
      The number of completed requests in the batch.
    </ResponseField>

    <ResponseField name="failed" type="integer" required={true}>
      The number of failed requests in the batch.
    </ResponseField>

    <ResponseField name="metadata" type="object | null" required={false}>
      Additional metadata associated with the batch job. Null if no metadata is provided.
    </ResponseField>

    <ResponseField name="request_counts" type="object" required={true}>
      Detailed request count information.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="total" type="integer" required={true}>
          The total number of requests in the batch.
        </ResponseField>

        <ResponseField name="completed" type="integer" required={true}>
          The number of successfully completed requests.
        </ResponseField>

        <ResponseField name="failed" type="integer" required={true}>
          The number of failed requests.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="first_id" type="string" required={true}>
  The ID of the first batch in the list.
</ResponseField>

<ResponseField name="has_more" type="boolean" required={true}>
  Indicates whether there are more batches available beyond this list.
</ResponseField>

<ResponseField name="last_id" type="string" required={true}>
  The ID of the last batch in the list.
</ResponseField>

<ResponseField name="object" type="string" required={true}>
  The object type, which is always `list`.
</ResponseField>


Built with [Mintlify](https://mintlify.com).