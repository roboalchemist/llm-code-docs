# Source: https://docs.dify.ai/api-reference/workflow-execution/execute-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute Workflow

> Execute workflow. Cannot be executed without a published workflow.



## OpenAPI

````yaml en/api-reference/openapi_workflow.json post /workflows/run
openapi: 3.0.1
info:
  title: Workflow App API
  description: >-
    Workflow applications offers non-session support and is ideal for
    translation, article writing, summarization AI, and more.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Workflow App API. Replace {api_base_url} with the
      actual API base URL.
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Workflow Execution
    description: Operations related to executing and managing workflows.
  - name: Files
    description: File upload and preview operations specific to workflows.
  - name: End Users
    description: Operations related to end user information.
  - name: Application
    description: Application settings and info for workflow apps.
paths:
  /workflows/run:
    post:
      tags:
        - Workflow Execution
      summary: Execute Workflow
      description: Execute workflow. Cannot be executed without a published workflow.
      operationId: executeWorkflow
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WorkflowExecutionRequest'
            examples:
              basic_execution:
                summary: Basic workflow execution
                value:
                  inputs:
                    query: 'Summarize this text: ...'
                  response_mode: streaming
                  user: user_workflow_123
              with_file_array_variable:
                summary: Example with a file array input variable
                value:
                  inputs:
                    my_documents:
                      - type: document
                        transfer_method: local_file
                        upload_file_id: uploaded_file_id_abc
                      - type: image
                        transfer_method: remote_url
                        url: https://example.com/image.jpg
                  response_mode: blocking
                  user: user_workflow_456
      responses:
        '200':
          description: |-
            Successful workflow execution. Structure depends on `response_mode`.
            - `blocking`: `application/json` with `WorkflowCompletionResponse`.
            - `streaming`: `text/event-stream` with `ChunkWorkflowEvent` stream.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkflowCompletionResponse'
            text/event-stream:
              schema:
                type: string
                description: >-
                  A stream of Server-Sent Events. See `ChunkWorkflowEvent` for
                  structures.
        '400':
          $ref: '#/components/responses/BadRequestWorkflow'
        '500':
          $ref: '#/components/responses/InternalServerError'
components:
  schemas:
    WorkflowExecutionRequest:
      type: object
      required:
        - inputs
        - response_mode
        - user
      properties:
        inputs:
          type: object
          description: >-
            Key/value pairs for workflow variables. Value for a file array type
            variable should be a list of InputFileObjectWorkflow.
          additionalProperties:
            oneOf:
              - type: string
              - type: number
              - type: boolean
              - type: object
              - type: array
                items:
                  $ref: '#/components/schemas/InputFileObjectWorkflow'
          example:
            user_query: Translate this for me.
            target_language: French
        response_mode:
          type: string
          enum:
            - streaming
            - blocking
          description: Response mode. Cloudflare timeout is 100s for blocking.
        user:
          type: string
          description: User identifier.
    WorkflowCompletionResponse:
      type: object
      description: Response for blocking mode workflow execution.
      properties:
        workflow_run_id:
          type: string
          format: uuid
        task_id:
          type: string
          format: uuid
        data:
          $ref: '#/components/schemas/WorkflowFinishedData'
    InputFileObjectWorkflow:
      type: object
      required:
        - type
        - transfer_method
      properties:
        type:
          type: string
          enum:
            - document
            - image
            - audio
            - video
            - custom
          description: Type of file.
        transfer_method:
          type: string
          enum:
            - remote_url
            - local_file
          description: >-
            Transfer method, `remote_url` for image URL / `local_file` for file
            upload
        url:
          type: string
          format: url
          description: Image URL (when the transfer method is `remote_url`)
        upload_file_id:
          type: string
          description: >-
            Uploaded file ID, which must be obtained by uploading through the
            File Upload API in advance (when the transfer method is
            `local_file`)
      anyOf:
        - properties:
            transfer_method:
              enum:
                - remote_url
            url:
              type: string
              format: url
          required:
            - url
          not:
            required:
              - upload_file_id
        - properties:
            transfer_method:
              enum:
                - local_file
            upload_file_id:
              type: string
          required:
            - upload_file_id
          not:
            required:
              - url
    WorkflowFinishedData:
      type: object
      required:
        - id
        - workflow_id
        - status
        - created_at
        - finished_at
      properties:
        id:
          type: string
          format: uuid
        workflow_id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - running
            - succeeded
            - failed
            - stopped
        outputs:
          type: object
          additionalProperties: true
          nullable: true
        error:
          type: string
          nullable: true
        elapsed_time:
          type: number
          format: float
          nullable: true
        total_tokens:
          type: integer
          nullable: true
        total_steps:
          type: integer
          default: 0
        created_at:
          type: integer
          format: int64
        finished_at:
          type: integer
          format: int64
    ErrorResponse:
      type: object
      properties:
        status:
          type: integer
          nullable: true
        code:
          type: string
          nullable: true
        message:
          type: string
  responses:
    BadRequestWorkflow:
      description: >-
        Bad Request for workflow operation. Possible error codes: invalid_param,
        app_unavailable, provider_not_initialize, provider_quota_exceeded,
        model_currently_not_support, workflow_request_error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalServerError:
      description: Internal server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).