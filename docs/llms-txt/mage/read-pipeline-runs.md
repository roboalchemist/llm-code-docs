# Source: https://docs.mage.ai/extensibility/api-reference/pipeline-runs/read-pipeline-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Read pipeline runs

`GET /api/pipeline_schedules/:pipeline_schedule_id/pipeline_runs`

<ParamField path="pipeline_schedule_id" type="integer" required>
  Pipeline schedule ID that pipeline runs should all belong to.
</ParamField>

<ParamField query="_limit" type="integer">
  Maximum number of logs to be returned in the API response.

  Example: `20`
</ParamField>

<ParamField query="_offset" type="integer">
  Read logs after N number of logs, where N equals `_offset`.

  Example: `10`
</ParamField>

<RequestExample>
  ```curl cURL theme={"system"}
  curl --request GET \
    --url 'http://localhost:6789/api/pipeline_schedules/1/pipeline_runs?api_key=zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2' \
    --header 'OAUTH-TOKEN=some_really_long_string' \
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"system"}
  {
    "pipeline_runs": [
      ...
    ],
    "metadata": {
      "count": 22,
      "next": false
    }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).