# Source: https://dev.writer.com/home/applications.md

# Source: https://dev.writer.com/api-reference/application-api/applications.md

# Generate from application

> Generate content from an existing no-code agent (formerly called no-code applications) with inputs.

## OpenAPI

````yaml post /v1/applications/{application_id}
paths:
  path: /v1/applications/{application_id}
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
              description: >-
                The unique identifier of a [no-code
                agent](/no-code/introduction) in AI Studio.
              format: uuid
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
                    items:
                      $ref: '#/components/schemas/generate_application_input'
              stream:
                allOf:
                  - type: boolean
                    description: >-
                      Indicates whether the response should be streamed.
                      Currently only supported for research assistant
                      applications.
            required: true
            title: generate_application_request
            refIdentifier: '#/components/schemas/generate_application_request'
            requiredProperties:
              - inputs
        examples:
          example:
            value:
              inputs:
                - id: <string>
                  value:
                    - <string>
              stream: true
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/applications/{application_id} \
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
            const response = await client.applications.generateContent('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
              inputs: [
                { id: 'id', value: ['string', 'string', 'string'] },
                { id: 'id', value: ['string', 'string', 'string'] },
                { id: 'id', value: ['string', 'string', 'string'] },
              ],
            });

            console.log(response.suggestion);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          response = client.applications.generate_content(
              application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              inputs=[{
                  "id": "id",
                  "value": ["string", "string", "string"],
              }, {
                  "id": "id",
                  "value": ["string", "string", "string"],
              }, {
                  "id": "id",
                  "value": ["string", "string", "string"],
              }],
          )
          print(response.suggestion)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              title:
                allOf:
                  - type: string
                    description: The name of the output field.
              suggestion:
                allOf:
                  - type: string
                    description: The response from the model specified in the application.
            title: generate_application_response
            refIdentifier: '#/components/schemas/generate_application_response'
            requiredProperties:
              - suggestion
        examples:
          example:
            value:
              title: Alt text
              suggestion: A modern dining room with a minimalist design.
        description: ''
      text/event-stream:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/generate_application_response_chunk'
        examples:
          example:
            value:
              - delta:
                  title: <string>
                  content: <string>
                  stages:
                    - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                      content: <string>
                      sources:
                        - <string>
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
    generate_application_response_chunk:
      title: generate_application_response_chunk
      required:
        - delta
      type: object
      properties:
        delta:
          $ref: '#/components/schemas/generate_application_delta'
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

````