# Source: https://dev.writer.com/api-reference/application-api/post-retry-async-job.md

# Retry job execution

> Re-triggers the async execution of a single job previously created via the Async api and terminated in error.

## OpenAPI

````yaml post /v1/applications/jobs/{job_id}/retry
paths:
  path: /v1/applications/jobs/{job_id}/retry
  method: post
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
              description: The ID of the job to retry.
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/applications/jobs/{job_id}/retry \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const response = await client.applications.jobs.retry('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

            console.log(response.id);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          response = client.applications.jobs.retry(
              "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
          )
          print(response.id)
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
                    description: The unique identifier for the async job created.
              status:
                allOf:
                  - $ref: '#/components/schemas/api_job_status'
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the job was created.
            title: generate_application_async_response
            refIdentifier: '#/components/schemas/generate_application_async_response'
            requiredProperties:
              - id
              - status
              - created_at
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              status: in_progress
              created_at: '2023-11-07T05:31:56Z'
        description: Accepted
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

````