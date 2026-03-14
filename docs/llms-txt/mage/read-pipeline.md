# Source: https://docs.mage.ai/extensibility/api-reference/pipelines/read-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Read pipelines

To retrieve all pipelines:

`GET /api/pipelines`

To fetch a single pipeline:

`GET /api/pipelines/:uuid`

<ParamField query="include_schedules" type="integer">
  If `1`, the pipeline object will include associated triggers.
</ParamField>

<RequestExample>
  ```bash Request theme={"system"}
  curl --request GET \
    --url 'http://localhost:6789/api/pipelines/arwen_starlight?api_key=zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2' \
    --header 'OAUTH-TOKEN=some_really_long_string'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"system"}
  {
    "pipeline": {
      "data_integration": null,
      "description": null,
      "executor_config": {},
      "executor_count": 1,
      "executor_type": null,
      "name": "arwen-starlight",
      "notification_config": {},
      "type": "python",
      "updated_at": null,
      "uuid": "arwen_starlight",
      "spark_config": {},
      "blocks": [],
      "callbacks": [],
      "conditionals": [],
      "widgets": [],
      "extensions": {}
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).