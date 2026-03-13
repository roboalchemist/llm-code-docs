# Source: https://docs.dify.ai/api-reference/workflow-execution/stop-workflow-task-generation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Stop Workflow Task Generation

> Stops a workflow task generation. Only supported in streaming mode.



## OpenAPI

````yaml en/api-reference/openapi_workflow.json post /workflows/tasks/{task_id}/stop
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
  /workflows/tasks/{task_id}/stop:
    post:
      tags:
        - Workflow Execution
      summary: Stop Workflow Task Generation
      description: Stops a workflow task generation. Only supported in streaming mode.
      operationId: stopWorkflowTaskGeneration
      parameters:
        - name: task_id
          in: path
          required: true
          description: Task ID from the streaming chunk.
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - user
              properties:
                user:
                  type: string
                  description: User identifier.
      responses:
        '200':
          $ref: '#/components/responses/SuccessResult'
components:
  responses:
    SuccessResult:
      description: Operation successful.
      content:
        application/json:
          schema:
            type: object
            properties:
              result:
                type: string
                example: success
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).