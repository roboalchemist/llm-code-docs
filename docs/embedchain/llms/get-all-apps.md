# Source: https://docs.embedchain.ai/examples/rest-api/get-all-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all apps

> Get all applications

<RequestExample>
  ```bash Request theme={null}
  curl --request GET \
    --url http://localhost:8080/apps
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "results": [
      {
        "config": "config1.yaml",
        "id": 1,
        "app_id": "app1"
      },
      {
        "config": "config2.yaml",
        "id": 2,
        "app_id": "app2"
      }
    ]
  }
  ```
</ResponseExample>


## OpenAPI

````yaml get /apps
openapi: 3.1.0
info:
  title: Embedchain REST API
  description: This is the REST API for Embedchain.
  license:
    name: Apache 2.0
    url: https://github.com/embedchain/embedchain/blob/main/LICENSE
  version: 0.0.1
servers: []
security: []
paths:
  /apps:
    get:
      tags:
        - Apps
      summary: Get all apps
      description: Get all applications
      operationId: get_all_apps_apps_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````