# Source: https://dev.writer.com/home/api-reference-link.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate from application

> Generate content from an existing no-code agent (formerly called no-code applications) with inputs.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml post /v1/applications/{application_id}
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/applications/{application_id}:
    post:
      tags:
        - Generation API
      summary: Generate from application
      description: >-
        Generate content from an existing no-code agent (formerly called no-code
        applications) with inputs.
      operationId: generateContent
      parameters:
        - name: application_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
          description: >-
            The unique identifier of a [no-code agent](/no-code/introduction) in
            AI Studio.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/generate_application_request'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/generate_application_response'
              example:
                title: Alt text
                suggestion: A modern dining room with a minimalist design.
            text/event-stream:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/generate_application_response_chunk'
      security:
        - bearerAuth: []
components:
  schemas:
    generate_application_request:
      title: generate_application_request
      required:
        - inputs
      type: object
      properties:
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/generate_application_input'
        stream:
          type: boolean
          description: >-
            Indicates whether the response should be streamed. Currently only
            supported for research assistant applications.
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
    generate_application_response_chunk:
      title: generate_application_response_chunk
      required:
        - delta
      type: object
      properties:
        delta:
          $ref: '#/components/schemas/generate_application_delta'
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
    generate_application_delta:
      title: generate_application_delta
      type: object
      properties:
        title:
          type: string
          description: The name of the output.
        content:
          type: string
          description: The main text output.
        stages:
          type: array
          nullable: true
          description: A list of stages that show the 'thinking process'.
          items:
            $ref: '#/components/schemas/generate_application_chunk_stage'
          minItems: 1
    generate_application_chunk_stage:
      title: generate_application_chunk_stage
      required:
        - id
        - content
      type: object
      properties:
        id:
          type: string
          description: The unique identifier for the stage.
          format: uuid
        content:
          type: string
          description: The text content of the stage.
        sources:
          type: array
          nullable: true
          description: >-
            A list of sources (URLs) that that stage used to process that
            particular step.
          items:
            type: string
          minItems: 1
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