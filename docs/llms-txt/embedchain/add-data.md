# Source: https://docs.embedchain.ai/examples/rest-api/add-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add data

> Add a data source to an app.

<RequestExample>
  ```bash Request theme={null}
  curl --request POST \
    --url http://localhost:8080/{app_id}/add \
    -d "source=https://www.forbes.com/profile/elon-musk" \
    -d "data_type=web_page"
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  { "response": "fec7fe91e6b2d732938a2ec2e32bfe3f" }
  ```
</ResponseExample>


## OpenAPI

````yaml post /{app_id}/add
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
  /{app_id}/add:
    post:
      tags:
        - Apps
      summary: Add data
      description: Add a data source to an app.
      operationId: add_datasource_to_an_app__app_id__add_post
      parameters:
        - name: app_id
          in: path
          required: true
          schema:
            type: string
            title: App Id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SourceApp'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DefaultResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    SourceApp:
      properties:
        source:
          type: string
          title: Source
          description: The source that you want to add to the App.
          default: ''
        data_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Data Type
          description: >-
            The type of data to add, remove it if you want Embedchain to detect
            it automatically.
          default: ''
      type: object
      title: SourceApp
      example:
        source: https://en.wikipedia.org/wiki/Elon_Musk
    DefaultResponse:
      properties:
        response:
          type: string
          title: Response
      type: object
      required:
        - response
      title: DefaultResponse
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