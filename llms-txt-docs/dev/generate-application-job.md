# Source: https://dev.writer.com/api-reference/application-api/generate-application-job.md

# Generate from application (async)

> Generate content asynchronously from an existing no-code agent (formerly called no-code applications) with inputs.

## OpenAPI

````yaml post /v1/applications/{application_id}/jobs
paths:
  path: /v1/applications/{application_id}/jobs
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
        application_id:
          schema:
            - type: string
              required: true
              description: The ID of the no-code app for which to create a job.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              inputs:
                allOf:
                  - type: array
                    description: A list of input objects to generate content for.
                    items:
                      $ref: '#/components/schemas/generate_application_input'
            required: true
            title: generate_application_async_request
            refIdentifier: '#/components/schemas/generate_application_async_request'
            requiredProperties:
              - inputs
        examples:
          example:
            value:
              inputs:
                - id: <string>
                  value:
                    - <string>
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/applications/{application_id}/jobs \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"inputs":[{"id": "Image ID", "value": ["12345"]}]}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const job = await client.applications.jobs.create('application_id', {
              inputs: [{ id: 'id', value: ['string'] }],
            });

            console.log(job.id);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          job = client.applications.jobs.create(
              application_id="application_id",
              inputs=[{
                  "id": "id",
                  "value": ["string"],
              }],
          )
          print(job.id)
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
        description: ''
  deprecated: false
  type: path
components:
  schemas:
    generate_application_input:
      title: generate_application_input
      required:
        - id
        - value
      type: object
      properties:
        id:
          type: string
          description: >-
            The unique identifier for the input field from the application. All
            input types from the No-code application are supported (i.e. Text
            input, Dropdown, File upload, Image input). The identifier should be
            the name of the input type.
        value:
          type: array
          items:
            type: string
          description: >-
            The value for the input field. 


            If the input type is "File upload", you must pass the `file_id` of
            an uploaded file. You cannot pass a file object directly. See the
            [file upload
            endpoint](https://dev.writer.com/api-reference/file-api/upload-files)
            for instructions on uploading files or the [list files
            endpoint](https://dev.writer.com/api-reference/file-api/get-all-files)
            for how to see a list of uploaded files and their IDs.
    api_job_status:
      title: api_job_status
      description: The status of the job.
      type: string
      enum:
        - in_progress
        - failed
        - completed

````