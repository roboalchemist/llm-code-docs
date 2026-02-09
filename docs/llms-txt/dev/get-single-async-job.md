# Source: https://dev.writer.com/api-reference/application-api/get-single-async-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a single job

> Retrieves a single job created via the Async API.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml get /v1/applications/jobs/{job_id}
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/applications/jobs/{job_id}:
    get:
      tags:
        - template
      summary: Retrieve a single job
      description: Retrieves a single job created via the Async API.
      parameters:
        - name: job_id
          description: The ID of the job to retrieve.
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get_async_application_job_response'
      security:
        - bearerAuth: []
components:
  schemas:
    get_async_application_job_response:
      title: get_async_application_job_response
      required:
        - id
        - status
        - application_id
        - created_at
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: The unique identifier for the job.
        status:
          $ref: '#/components/schemas/api_job_status'
        application_id:
          type: string
          description: The ID of the application associated with this job.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the job was created.
        updated_at:
          type: string
          format: date-time
          description: The timestamp when the job was last updated.
        completed_at:
          type: string
          format: date-time
          description: The timestamp when the job was completed.
        data:
          $ref: '#/components/schemas/generate_application_response'
          type: object
          description: The result of the completed job, if applicable.
        error:
          type: string
          description: The error message if the job failed.
    api_job_status:
      title: api_job_status
      description: The status of the job.
      type: string
      enum:
        - in_progress
        - failed
        - completed
    generate_application_response:
      title: generate_application_response
      required:
        - suggestion
      type: object
      properties:
        title:
          type: string
          description: The name of the output field.
        suggestion:
          type: string
          description: The response from the model specified in the application.
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