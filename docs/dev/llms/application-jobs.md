# Source: https://dev.writer.com/api-reference/application-api/application-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve all jobs

> Retrieve all jobs created via the async API, linked to the provided application ID (or alias).

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml get /v1/applications/{application_id}/jobs
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/applications/{application_id}/jobs:
    get:
      tags:
        - template
      summary: Retrieve all jobs
      description: >-
        Retrieve all jobs created via the async API, linked to the provided
        application ID (or alias).
      parameters:
        - name: application_id
          in: path
          description: The ID of the no-code app for which to retrieve jobs.
          required: true
          schema:
            type: string
        - name: status
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/api_job_status'
        - name: offset
          in: query
          description: The pagination offset for retrieving the jobs.
          required: false
          schema:
            type: integer
            format: int64
        - name: limit
          in: query
          description: The pagination limit for retrieving the jobs.
          required: false
          schema:
            type: integer
            format: int32
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get_async_application_jobs_response'
      security:
        - bearerAuth: []
components:
  schemas:
    api_job_status:
      title: api_job_status
      description: The status of the job.
      type: string
      enum:
        - in_progress
        - failed
        - completed
    get_async_application_jobs_response:
      title: get_async_application_jobs_response
      required:
        - result
      type: object
      properties:
        result:
          type: array
          items:
            $ref: '#/components/schemas/get_async_application_job_response'
        totalCount:
          type: integer
          format: int64
          description: The total number of jobs associated with the application.
        pagination:
          type: object
          properties:
            offset:
              type: integer
              format: int64
              description: The pagination offset for retrieving the jobs.
            limit:
              type: integer
              format: int32
              description: The pagination limit for retrieving the jobs.
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