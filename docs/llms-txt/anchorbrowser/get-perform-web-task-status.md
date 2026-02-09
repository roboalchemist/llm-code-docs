# Source: https://docs.anchorbrowser.io/api-reference/ai-tools/get-perform-web-task-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Perform Web Task Status

> Get the status of an asynchronous perform-web-task execution by workflow ID.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/tools/perform-web-task/{workflowId}/status
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/tools/perform-web-task/{workflowId}/status:
    get:
      tags:
        - AI Tools
      summary: Get Perform Web Task Status
      description: >-
        Get the status of an asynchronous perform-web-task execution by workflow
        ID.
      parameters:
        - in: path
          name: workflowId
          required: true
          schema:
            type: string
          description: >-
            The workflow ID returned when starting an asynchronous
            perform-web-task execution.
      responses:
        '200':
          description: The current status of the task execution.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PerformWebTaskStatusResponseSchema'
              examples:
                completed:
                  summary: Completed workflow
                  value:
                    data:
                      status: COMPLETED
                      result:
                        nodes_cpu_usage:
                          - node: pool-e1ro5g0nq-559g5
                            cluster: do-nyc1-demo-infra
                            cpu_avg_percentage: 8.29
                          - node: pool-e1ro5g0nq-559gk
                            cluster: do-nyc1-demo-infra
                            cpu_avg_percentage: 24.8
                running:
                  summary: Running workflow
                  value:
                    data:
                      status: RUNNING
                failed:
                  summary: Failed workflow
                  value:
                    data:
                      status: FAILED
                      error: Maximum number of steps exceeded
        '400':
          description: Invalid request.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    PerformWebTaskStatusResponseSchema:
      type: object
      properties:
        data:
          type: object
          oneOf:
            - $ref: '#/components/schemas/PerformWebTaskStatusSuccessResponseData'
            - $ref: '#/components/schemas/PerformWebTaskStatusRunningResponseData'
            - $ref: '#/components/schemas/PerformWebTaskStatusFailedResponseData'
      required:
        - data
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
    PerformWebTaskStatusSuccessResponseData:
      type: object
      title: success
      properties:
        status:
          type: string
          enum:
            - COMPLETED
          description: The workflow has completed successfully.
        result:
          type: object
          description: The outcome or answer produced by the autonomous task.
      required:
        - status
        - result
    PerformWebTaskStatusRunningResponseData:
      type: object
      title: running
      properties:
        status:
          type: string
          enum:
            - RUNNING
          description: The workflow is currently running.
      required:
        - status
    PerformWebTaskStatusFailedResponseData:
      type: object
      title: failed
      properties:
        status:
          type: string
          enum:
            - FAILED
          description: The workflow has failed.
        error:
          type: string
          description: Error message describing why the workflow failed.
      required:
        - status
        - error
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````