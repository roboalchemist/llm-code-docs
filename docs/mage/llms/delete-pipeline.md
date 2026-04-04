# Source: https://docs.mage.ai/extensibility/api-reference/pipelines/delete-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete pipeline

`DELETE /api/pipelines/:uuid`

<RequestExample>
  ```bash Request theme={"system"}
    curl -X DELETE 
    --url http://localhost:6789/api/pipelines/arwen_starlight
    -H 'Content-Type: application/json' 
    -H 'Cookie: oauth_token=some_really_long_string' 
    -H 'X-API-KEY: zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2' 
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
      "type": "integration",
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