# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/filter-flow-run-input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter Flow Run Input

> Filter flow run inputs by key prefix



## OpenAPI

````yaml post /flow_runs/{id}/input/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/{id}/input/filter:
    post:
      tags:
        - Flow Runs
      summary: Filter Flow Run Input
      description: Filter flow run inputs by key prefix
      operationId: filter_flow_run_input_flow_runs__id__input_filter_post
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
                #/components/schemas/Body_filter_flow_run_input_flow_runs__id__input_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/FlowRunInput'
                title: >-
                  Response Filter Flow Run Input Flow Runs  Id  Input Filter
                  Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_filter_flow_run_input_flow_runs__id__input_filter_post:
      properties:
        prefix:
          type: string
          title: Prefix
          description: The input key prefix
        limit:
          type: integer
          title: Limit
          description: The maximum number of results to return
          default: 1
        exclude_keys:
          items:
            type: string
          type: array
          title: Exclude Keys
          description: Exclude inputs with these keys
          default: []
      type: object
      required:
        - prefix
      title: Body_filter_flow_run_input_flow_runs__id__input_filter_post
    FlowRunInput:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        flow_run_id:
          type: string
          format: uuid
          title: Flow Run Id
          description: The flow run ID associated with the input.
        key:
          type: string
          title: Key
          description: The key of the input.
        value:
          type: string
          title: Value
          description: The value of the input.
        sender:
          anyOf:
            - type: string
            - type: 'null'
          title: Sender
          description: The sender of the input.
      type: object
      required:
        - flow_run_id
        - key
        - value
        - id
        - created
        - updated
      title: FlowRunInput
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