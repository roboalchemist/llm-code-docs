# Source: https://docs.mage.ai/extensibility/api-reference/pipelines/create-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create pipeline

`POST /api/pipelines`

<ParamField query="name" type="string" required>
  Human readable name of the pipeline.
</ParamField>

<ResponseField name="type" type="string" required>
  The type of the pipeline:
  `integration`, `pyspark`, `python`, `streaming`
  Note that `python` is a standard (batch) pipeline with a python backend, while `pyspark` is a batch pipeline with a spark backend.
</ResponseField>

<ParamField query="clone_pipeline_uuid" type="string">
  If supplied, the uuid of a pipeline to clone.
</ParamField>

<ParamField query="extensions" type="array of objects">
  Array of [extension](/design/blocks/extension) block objects. Same shape as `blocks`.
</ParamField>

<ParamField query="callbacks" type="array of objects">
  Array of [callback](/development/blocks/callbacks) block objects.  Same shape as `blocks`.
</ParamField>

<ParamField query="conditionals" type="array of objects">
  Array of [conditional](/development/blocks/conditionals/) block objects.  Same shape as `blocks`.
</ParamField>

<RequestExample>
  ```bash Request theme={"system"}
    curl --request POST 
    -H 'Content-Type: application/json' 
    -H 'Cookie: oauth_token=some_really_long_string'
    -H 'X-API-KEY: zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2'
    -d '{"pipeline": {"name": "arwen-starlight", "type": "python"}}' 
    --url http://localhost:6789/api/pipelines
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
      "widgets": []
    }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).