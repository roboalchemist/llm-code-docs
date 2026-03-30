# Source: https://novita.ai/docs/api-reference/gpu-instance-break-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Break Job

## API Description

Forcefully interrupt a running job.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="jobId" type="string" required={true}>
  The job ID to be interrupted. String, length 0–255.
</ParamField>

## cURL Example

```bash  theme={"system"}
curl --location --request POST 'https://api.novita.ai/gpu-instance/openapi/v1/job/break' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_KEY}}' \
--data-raw '{
  "jobId": "10wi9visv0rqt57w"
}'
```

## Response

<ResponseField name="jobId" type="string" required={true}>
  The job ID.
</ResponseField>


Built with [Mintlify](https://mintlify.com).