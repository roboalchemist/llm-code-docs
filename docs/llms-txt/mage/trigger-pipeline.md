# Source: https://docs.mage.ai/orchestration/triggers/trigger-pipeline.md

# Source: https://docs.mage.ai/getting-started/trigger-pipeline.md

# Source: https://docs.mage.ai/extensibility/api-reference/pipeline-runs/trigger-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger pipeline

`POST /api/pipeline_schedules/:pipeline_schedule_id/pipeline_runs/:token`

Run a pipeline using an API request. For more information,
read this [guide](/orchestration/triggers/trigger-pipeline-api).

<ParamField path="pipeline_schedule_id" type="integer" required>
  Pipeline schedule ID that pipeline runs should all belong to.
</ParamField>

<ParamField path="token" type="string" required>
  Unique token of the pipeline schedule that you want to trigger.
</ParamField>

<RequestExample>
  ```curl cURL theme={"system"}
  curl --request POST \
    --url 'http://localhost:6789/api/pipeline_schedules/71/pipeline_runs/4506463a01944ef492f70005996dac1a' \
    --data '{
    "env": "dev",
    "test": 1
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"system"}
  {
    "pipeline_run": {
      "id": 1249,
      "created_at": "2023-04-01 00:36:23.507282+00:00",
      "updated_at": "2023-04-01 00:36:39.962084+00:00",
      "pipeline_schedule_id": 71,
      "pipeline_uuid": "example_pipeline",
      "execution_date": "2023-04-01 00:36:39.904371+00:00",
      "status": "running",
      "completed_at": null,
      "variables": {},
      "passed_sla": false,
      "event_variables": {
        "env": "dev",
        "test": 1
      },
      "metrics": null,
      "backfill_id": null
    }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).