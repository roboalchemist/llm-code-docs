# Source: https://docs.embedchain.ai/examples/rest-api/check-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Check status

> Endpoint to check the status of the API

<RequestExample>
  ```bash Request theme={null}
    curl --request GET \
      --url http://localhost:8080/ping
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  { "ping": "pong" }
  ```
</ResponseExample>


## OpenAPI

````yaml get /ping
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
  /ping:
    get:
      tags:
        - Utility
      summary: Check status
      description: Endpoint to check the status of the API
      operationId: check_status_ping_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````