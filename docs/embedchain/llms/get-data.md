# Source: https://docs.embedchain.ai/examples/rest-api/get-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data

> Get all data sources for an app

<RequestExample>
  ```bash Request theme={null}
  curl --request GET \
    --url http://localhost:8080/{app_id}/data
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "results": [
      {
        "data_type": "web_page",
        "data_value": "https://www.forbes.com/profile/elon-musk/",
        "metadata": "null"
      }
    ]
  }
  ```
</ResponseExample>


## OpenAPI

````yaml get /{app_id}/data
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
  /{app_id}/data:
    get:
      tags:
        - Apps
      summary: Get data
      description: Get all data sources for an app
      operationId: get_datasources_associated_with_app_id__app_id__data_get
      parameters:
        - name: app_id
          in: path
          required: true
          schema:
            type: string
            title: App Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````