# Source: https://docs.dify.ai/api-reference/workflow-execution/get-workflow-run-detail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Workflow Run Detail

> Retrieve the current execution results of a workflow task based on the workflow execution ID.



## OpenAPI

````yaml en/api-reference/openapi_workflow.json get /workflows/run/{workflow_run_id}
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
  /workflows/run/{workflow_run_id}:
    get:
      tags:
        - Workflow Execution
      summary: Get Workflow Run Detail
      description: >-
        Retrieve the current execution results of a workflow task based on the
        workflow execution ID.
      operationId: getWorkflowRunDetail
      parameters:
        - name: workflow_run_id
          in: path
          required: true
          description: >-
            Workflow Run ID, can be obtained from workflow execution response or
            streaming events.
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Successfully retrieved workflow run details.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkflowRunDetailResponse'
        '404':
          description: Workflow run not found.
components:
  schemas:
    WorkflowRunDetailResponse:
      type: object
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
        inputs:
          type: string
          description: JSON string of input content.
        outputs:
          type: object
          additionalProperties: true
          nullable: true
          description: JSON object of output content.
        error:
          type: string
          nullable: true
        total_steps:
          type: integer
        total_tokens:
          type: integer
        created_at:
          type: integer
          format: int64
        finished_at:
          type: integer
          format: int64
          nullable: true
        elapsed_time:
          type: number
          format: float
          nullable: true
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).