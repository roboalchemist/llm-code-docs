# Source: https://docs.mage.ai/extensibility/api-reference/pipeline-schedules/create-pipeline-schedule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create pipeline schedule

`POST /api/pipelines/:pipeline_uuid/pipeline_schedules`

<ParamField path="pipeline_uuid" type="string" required>
  Pipeline UUID that the pipeline schedule should all belong to.
</ParamField>

<ParamField body="pipeline_schedule" type="object" required>
  <Expandable title="payload" defaultOpen="true">
    <ParamField body="name" type="string" required />

    <ParamField body="description" type="string" />

    <ParamField body="schedule_interval" type="string" />

    <ParamField body="schedule_type" type="string" />

    <ParamField body="settings" type="object" />

    <ParamField body="sla" type="integer" />

    <ParamField body="start_time" type="datetime" />

    <ParamField body="status" type="string" />

    <ParamField body="variables" type="object" />
  </Expandable>
</ParamField>

<RequestExample>
  ```bash Request theme={"system"}
    curl --request POST 
    -H 'Content-Type: application/json' 
    -H 'Cookie: oauth_token=some_really_long_string'
    -H 'X-API-KEY: zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2'
    -d '{
      "pipeline_schedule": {
        "name": "Example Pipeline Schedule Name",
        "schedule_type": "time",
        "event_matchers": [],
        "schedule_interval": "@once",
        "start_time": "2023-03-06 04:53:00",
        "variables": {
          "env": "dev112222",
          "test": 11111
        },
        "sla": 1000,
        "settings": {
          "allow_blocks_to_fail": true,
          "create_initial_pipeline_run": false,
          "skip_if_previous_running": true
        }
      }
    }'
    --url http://localhost:6789/api/pipelines/example_pipeline/pipeline_schedules
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"system"}
  {
    "pipeline_schedule": {
      "id": 55,
      "created_at": "2023-03-08 04:52:54.268096+00:00",
      "updated_at": "2023-04-01 00:52:11.753497+00:00",
      "name": "Example Pipeline Schedule Name",
      "pipeline_uuid": "example_pipeline",
      "schedule_type": "time",
      "start_time": "2023-03-06 04:53:00+00:00",
      "schedule_interval": "@once",
      "status": "inactive",
      "variables": {
        "env": "dev112222",
        "test": 11111
      },
      "sla": 1000,
      "token": "67d62ed3e66143839f58945bb7d16387",
      "settings": {
        "allow_blocks_to_fail": true,
        "create_initial_pipeline_run": false,
        "skip_if_previous_running": true
      },
      "event_matchers": []
    }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).