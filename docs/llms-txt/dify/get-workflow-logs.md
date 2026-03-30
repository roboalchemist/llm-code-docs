# Source: https://docs.dify.ai/api-reference/workflow-execution/get-workflow-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Workflow Logs

> Returns workflow logs, with the first page returning the latest `{limit}` messages, i.e., in reverse order.



## OpenAPI

````yaml en/api-reference/openapi_workflow.json get /workflows/logs
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
  /workflows/logs:
    get:
      tags:
        - Workflow Execution
      summary: Get Workflow Logs
      description: >-
        Returns workflow logs, with the first page returning the latest
        `{limit}` messages, i.e., in reverse order.
      operationId: getWorkflowLogs
      parameters:
        - name: keyword
          in: query
          description: Keyword to search.
          schema:
            type: string
        - name: status
          in: query
          description: Filter by status.
          schema:
            type: string
            enum:
              - succeeded
              - failed
              - stopped
              - running
        - name: page
          in: query
          description: Current page.
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          description: Number of items per page.
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Successfully retrieved workflow logs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkflowLogsResponse'
components:
  schemas:
    WorkflowLogsResponse:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer
        has_more:
          type: boolean
        data:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowLogItem'
    WorkflowLogItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        workflow_run:
          $ref: '#/components/schemas/WorkflowRunSummary'
        created_from:
          type: string
        created_by_role:
          type: string
        created_by_account:
          type: string
          format: uuid
          nullable: true
        created_by_end_user:
          $ref: '#/components/schemas/EndUserSummary'
        created_at:
          type: integer
          format: int64
    WorkflowRunSummary:
      type: object
      properties:
        id:
          type: string
          format: uuid
        version:
          type: string
        status:
          type: string
          enum:
            - running
            - succeeded
            - failed
            - stopped
        error:
          type: string
          nullable: true
        elapsed_time:
          type: number
          format: float
        total_tokens:
          type: integer
        total_steps:
          type: integer
        created_at:
          type: integer
          format: int64
        finished_at:
          type: integer
          format: int64
          nullable: true
    EndUserSummary:
      type: object
      properties:
        id:
          type: string
          format: uuid
        type:
          type: string
        is_anonymous:
          type: boolean
        session_id:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).