# Source: https://docs.fireworks.ai/api-reference/get-evaluation-job-log-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Evaluation Job execution logs (stream log endpoint + tracing IDs).



## OpenAPI

````yaml get /v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}:getExecutionLogEndpoint
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.21.6
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}:getExecutionLogEndpoint:
    get:
      tags:
        - Gateway
      summary: Get Evaluation Job execution logs (stream log endpoint + tracing IDs).
      operationId: Gateway_GetEvaluationJobExecutionLogEndpoint
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: evaluation_job_id
          in: path
          required: true
          description: The Evaluation Job Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/gatewayGetEvaluationJobExecutionLogEndpointResponse
components:
  schemas:
    gatewayGetEvaluationJobExecutionLogEndpointResponse:
      type: object
      properties:
        executionLogSignedUri:
          type: string
          description: >-
            Short-lived signed URL for the execution log file.

            Empty if the log file has not been created yet (e.g. job not started
            or still initializing).
        contentType:
          type: string
          description: |-
            Content type for the log file (e.g. "text/plain").
            Only set when execution_log_signed_uri is present.
        expireTime:
          type: string
          format: date-time
          description: |-
            Expiration time of the signed URL.
            Only set when execution_log_signed_uri is present.
      description: |-
        Response carries the stream log URL (for VirtualizedLogViewer).

        Next ID: 4
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````