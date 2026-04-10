# Source: https://dev.writer.com/api-reference/application-api/generate-application-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate from application (async)

> Generate content asynchronously from an existing no-code agent (formerly called no-code applications) with inputs.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml post /v1/applications/{application_id}/jobs
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
    post:
      tags:
        - template
      summary: Generate from application (async)
      description: >-
        Generate content asynchronously from an existing no-code agent (formerly
        called no-code applications) with inputs.
      parameters:
        - name: application_id
          description: The ID of the no-code app for which to create a job.
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/generate_application_async_request'
        required: true
      responses:
        '202':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/generate_application_async_response'
      security:
        - bearerAuth: []
components:
  schemas:
    generate_application_async_request:
      title: generate_application_async_request
      required:
        - inputs
      type: object
      properties:
        inputs:
          type: array
          description: A list of input objects to generate content for.
          items:
            $ref: '#/components/schemas/generate_application_input'
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