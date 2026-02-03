# Source: https://dev.writer.com/api-reference/application-api/post-retry-async-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retry job execution

> Re-triggers the async execution of a single job previously created via the Async api and terminated in error.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml post /v1/applications/jobs/{job_id}/retry
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/applications/jobs/{job_id}/retry:
    post:
      tags:
        - template
      summary: Retry job execution
      description: >-
        Re-triggers the async execution of a single job previously created via
        the Async api and terminated in error.
      parameters:
        - name: job_id
          description: The ID of the job to retry.
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '202':
          description: Accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/generate_application_async_response'
      security:
        - bearerAuth: []
components:
  schemas:
    generate_application_async_response:
      title: generate_application_async_response
      required:
        - id
        - status
        - created_at
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: The unique identifier for the async job created.
        status:
          $ref: '#/components/schemas/api_job_status'
        created_at:
          type: string
          format: date-time
          description: The timestamp when the job was created.
    api_job_status:
      title: api_job_status
      description: The status of the job.
      type: string
      enum:
        - in_progress
        - failed
        - completed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````