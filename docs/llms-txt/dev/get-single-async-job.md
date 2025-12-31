# Source: https://dev.writer.com/api-reference/application-api/get-single-async-job.md

# Retrieve a single job

> Retrieves a single job created via the Async API.

## OpenAPI

````yaml get /v1/applications/jobs/{job_id}
paths:
  path: /v1/applications/jobs/{job_id}
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
        job_id:
          schema:
            - type: string
              required: true
              description: The ID of the job to retrieve.
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request GET
          https://api.writer.com/v1/applications/jobs/{job_id} \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const applicationGenerateAsyncResponse = await client.applications.jobs.retrieve(
              '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
            );

            console.log(applicationGenerateAsyncResponse.id);
          }

          main();
      - lang: Python
        source: >-
          import os

          from writerai import Writer


          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )

          application_generate_async_response =
          client.applications.jobs.retrieve(
              "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
          )

          print(application_generate_async_response.id)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
                    description: The unique identifier for the job.
              status:
                allOf:
                  - $ref: '#/components/schemas/api_job_status'
              application_id:
                allOf:
                  - type: string
                    description: The ID of the application associated with this job.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the job was created.
              updated_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the job was last updated.
              completed_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the job was completed.
              data:
                allOf:
                  - type: object
                    description: The result of the completed job, if applicable.
                    $ref: '#/components/schemas/generate_application_response'
              error:
                allOf:
                  - type: string
                    description: The error message if the job failed.
            title: get_async_application_job_response
            refIdentifier: '#/components/schemas/get_async_application_job_response'
            requiredProperties:
              - id
              - status
              - application_id
              - created_at
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              status: in_progress
              application_id: <string>
              created_at: '2023-11-07T05:31:56Z'
              updated_at: '2023-11-07T05:31:56Z'
              completed_at: '2023-11-07T05:31:56Z'
              data:
                title: <string>
                suggestion: <string>
              error: <string>
        description: Successful response
  deprecated: false
  type: path
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