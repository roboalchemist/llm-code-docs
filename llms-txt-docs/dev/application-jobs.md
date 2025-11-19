# Source: https://dev.writer.com/api-reference/application-api/application-jobs.md

# Retrieve all jobs

> Retrieve all jobs created via the async API, linked to the provided application ID (or alias).

## OpenAPI

````yaml get /v1/applications/{application_id}/jobs
paths:
  path: /v1/applications/{application_id}/jobs
  method: get
  servers:
    - url: https://api.writer.com
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
          cookie: {}
    parameters:
      path:
        application_id:
          schema:
            - type: string
              required: true
              description: The ID of the no-code app for which to retrieve jobs.
      query:
        status:
          schema:
            - type: enum<string>
              enum:
                - in_progress
                - failed
                - completed
              required: false
              title: api_job_status
              description: The status of the job.
        offset:
          schema:
            - type: integer
              required: false
              description: The pagination offset for retrieving the jobs.
        limit:
          schema:
            - type: integer
              required: false
              description: The pagination limit for retrieving the jobs.
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request GET
          https://api.writer.com/v1/applications/{application_id}/jobs \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            // Automatically fetches more pages as needed.
            for await (const applicationGenerateAsyncResponse of client.applications.jobs.list('application_id')) {
              console.log(applicationGenerateAsyncResponse.id);
            }
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          page = client.applications.jobs.list(
              application_id="application_id",
          )
          page = page.result[0]
          print(page.id)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              result:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/get_async_application_job_response'
              totalCount:
                allOf:
                  - type: integer
                    format: int64
                    description: The total number of jobs associated with the application.
              pagination:
                allOf:
                  - type: object
                    properties:
                      offset:
                        type: integer
                        format: int64
                        description: The pagination offset for retrieving the jobs.
                      limit:
                        type: integer
                        format: int32
                        description: The pagination limit for retrieving the jobs.
            title: get_async_application_jobs_response
            refIdentifier: '#/components/schemas/get_async_application_jobs_response'
            requiredProperties:
              - result
        examples:
          example:
            value:
              result:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  status: in_progress
                  application_id: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  updated_at: '2023-11-07T05:31:56Z'
                  completed_at: '2023-11-07T05:31:56Z'
                  data:
                    title: <string>
                    suggestion: <string>
                  error: <string>
              totalCount: 123
              pagination:
                offset: 123
                limit: 123
        description: Successful response
  deprecated: false
  type: path
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
          type: object
          description: The result of the completed job, if applicable.
          $ref: '#/components/schemas/generate_application_response'
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

````