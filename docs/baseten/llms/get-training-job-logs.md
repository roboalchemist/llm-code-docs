# Source: https://docs.baseten.co/reference/training-api/get-training-job-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get training job logs

> Get the logs for a training job with the provided filters.



## OpenAPI

````yaml post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    post:
      summary: Get the logs for a training job.
      description: Get the logs for a training job with the provided filters.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetTrainingJobLogsRequestV1'
        required: true
      responses:
        '200':
          description: A response to querying logs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLogsResponseV1'
components:
  parameters:
    training_project_id:
      schema:
        type: string
      name: training_project_id
      in: path
      required: true
    training_job_id:
      schema:
        type: string
      name: training_job_id
      in: path
      required: true
  schemas:
    GetTrainingJobLogsRequestV1:
      description: A request to fetch training logs.
      properties:
        start_epoch_millis:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Epoch millis timestamp to start fetching logs
          title: Start Epoch Millis
        end_epoch_millis:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Epoch millis timestamp to end fetching logs
          title: End Epoch Millis
        direction:
          anyOf:
            - $ref: '#/components/schemas/SortOrderV1'
            - type: 'null'
          default: null
          description: Sort order for logs
        limit:
          anyOf:
            - maximum: 1000
              minimum: 1
              type: integer
            - type: 'null'
          default: 500
          description: Limit of logs to fetch in a single request
          title: Limit
      title: GetTrainingJobLogsRequestV1
      type: object
    GetLogsResponseV1:
      description: A response to querying logs.
      properties:
        logs:
          description: Logs for a specific entity.
          items:
            $ref: '#/components/schemas/LogV1'
          title: Logs
          type: array
      required:
        - logs
      title: GetLogsResponseV1
      type: object
    SortOrderV1:
      enum:
        - asc
        - desc
      title: SortOrderV1
      type: string
    LogV1:
      properties:
        timestamp:
          description: Epoch nanosecond timestamp of the log message.
          title: Timestamp
          type: string
        message:
          description: The contents of the log message.
          title: Message
          type: string
        replica:
          anyOf:
            - type: string
            - type: 'null'
          description: The replica the log line was emitted from.
          title: Replica
      required:
        - timestamp
        - message
        - replica
      title: LogV1
      type: object
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````