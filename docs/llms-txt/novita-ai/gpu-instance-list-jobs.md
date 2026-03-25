# Source: https://novita.ai/docs/api-reference/gpu-instance-list-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Jobs

## API Description

Retrieve a paginated list of background jobs for GPU instances. You can filter by job ID, state, type, time range, and creators.

## Request Headers

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="pageSize" type="integer" required={false}>
  Maximum number of items returned per page. Integer, value >= 0.
</ParamField>

<ParamField query="pageNum" type="integer" required={false}>
  Page number to retrieve. Integer, value >= 0.
</ParamField>

<ParamField query="jobId" type="string" required={false}>
  Filter by job ID. String, length 0–255.
</ParamField>

<ParamField query="state" type="string" required={false}>
  Filter by job state. One of: `pulling` (preparing), `running`, `fail`, `success`, `break`.
</ParamField>

<ParamField query="type" type="string" required={false}>
  Filter by job type. One of: `saveImage`, `instanceMigrate`, `autoInstanceMigrate`.
</ParamField>

<ParamField query="startTime" type="integer" required={false}>
  Start of time range (Unix timestamp in seconds). Integer, value >= 0. Default: 0.
</ParamField>

<ParamField query="endTime" type="integer" required={false}>
  End of time range (Unix timestamp in seconds). Integer, value >= 0. Default: 0.
</ParamField>

<ParamField query="creators" type="string" required={false}>
  Filter by creator user ID.
</ParamField>

## cURL Example

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/gpu-instance/openapi/v1/jobs?pageSize=5&pageNum=1&jobId=&type=&state=&startTime=&endTime=&creators=' \
--header 'Authorization: Bearer {{API_KEY}}'
```

## Response

<ResponseField name="jobs" type="object[]" required={true}>
  Job list.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="Id" type="string" required={true}>
      Job ID.
    </ResponseField>

    <ResponseField name="user" type="string" required={true}>
      The user ID who initiated the job.
    </ResponseField>

    <ResponseField name="type" type="string" required={true}>
      Job type. One of: `saveImage`, `instanceMigrate`, `autoInstanceMigrate`.
    </ResponseField>

    <ResponseField name="envs" type="object[]" required={false}>
      Environment variables for the job.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="key" type="string" required={false}>
          Environment variable name.
        </ResponseField>

        <ResponseField name="value" type="string" required={false}>
          Environment variable value.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="state" type="object" required={true}>
      Current job state information.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="state" type="string" required={true}>
          Current job state. One of: `pulling`, `running`, `fail`, `success`, `break`.
        </ResponseField>

        <ResponseField name="error" type="string" required={false}>
          Error code, if any.
        </ResponseField>

        <ResponseField name="errorMessage" type="string" required={false}>
          Error message, if any.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="logAddress" type="string" required={false}>
      Log URL for viewing job execution logs.
    </ResponseField>

    <ResponseField name="createdAt" type="string" required={true}>
      Job creation time (Unix timestamp in seconds).
    </ResponseField>

    <ResponseField name="instanceId" type="string" required={true}>
      Associated instance ID when the job was executed.
    </ResponseField>
  </Expandable>
</ResponseField>

<ParamField name="total" type="integer" required={true}>
  Total number of jobs matching the query.
</ParamField>


Built with [Mintlify](https://mintlify.com).