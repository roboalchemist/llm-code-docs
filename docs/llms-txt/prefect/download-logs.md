# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/download-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Download Logs

> Download all flow run logs as a CSV file, collecting all logs until there are no more logs to retrieve.



## OpenAPI

````yaml get /flow_runs/{id}/logs/download
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/{id}/logs/download:
    get:
      tags:
        - Flow Runs
      summary: Download Logs
      description: >-
        Download all flow run logs as a CSV file, collecting all logs until
        there are no more logs to retrieve.
      operationId: download_logs_flow_runs__id__logs_download_get
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