# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/create-flow-run-input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Flow Run Input

> Create a key/value input for a flow run.



## OpenAPI

````yaml post /flow_runs/{id}/input
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/{id}/input:
    post:
      tags:
        - Flow Runs
      summary: Create Flow Run Input
      description: Create a key/value input for a flow run.
      operationId: create_flow_run_input_flow_runs__id__input_post
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The flow run id
            title: Id
          description: The flow run id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_create_flow_run_input_flow_runs__id__input_post
      responses:
        '201':
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
    Body_create_flow_run_input_flow_runs__id__input_post:
      properties:
        key:
          type: string
          title: Key
          description: The input key
        value:
          type: string
          contentMediaType: application/octet-stream
          title: Value
          description: The value of the input
        sender:
          anyOf:
            - type: string
            - type: 'null'
          title: Sender
          description: The sender of the input
      type: object
      required:
        - key
        - value
      title: Body_create_flow_run_input_flow_runs__id__input_post
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
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).