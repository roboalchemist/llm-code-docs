# Source: https://dev.writer.com/api-reference/application-api/application-details.md

# Application details

> Retrieves detailed information for a specific no-code agent (formerly called no-code applications), including its configuration and current status.

## OpenAPI

````yaml get /v1/applications/{application_id}
paths:
  path: /v1/applications/{application_id}
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
              description: Unique identifier of the application to retrieve.
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request GET
          https://api.writer.com/v1/applications/{application_id} \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const application = await client.applications.retrieve('application_id');

            console.log(application.id);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          application = client.applications.retrieve(
              "application_id",
          )
          print(application.id)
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
                    description: Unique identifier for the application.
              name:
                allOf:
                  - type: string
                    description: Display name of the application.
              type:
                allOf:
                  - $ref: '#/components/schemas/application_type'
              status:
                allOf:
                  - $ref: '#/components/schemas/application_status'
              inputs:
                allOf:
                  - type: array
                    description: List of input configurations for the application.
                    items:
                      $ref: '#/components/schemas/application_input'
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: Timestamp when the application was created.
              updated_at:
                allOf:
                  - type: string
                    format: date-time
                    description: Timestamp when the application was last updated.
              last_deployed_at:
                allOf:
                  - type: string
                    format: date-time
                    description: Timestamp when the application was last deployed.
            title: application_with_inputs
            description: Detailed application object including its input configuration.
            refIdentifier: '#/components/schemas/application_with_inputs'
            requiredProperties:
              - id
              - name
              - type
              - status
              - inputs
              - created_at
              - updated_at
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              name: <string>
              type: generation
              status: deployed
              inputs:
                - name: <string>
                  input_type: text
                  description: <string>
                  required: true
                  options:
                    list:
                      - <string>
              created_at: '2023-11-07T05:31:56Z'
              updated_at: '2023-11-07T05:31:56Z'
              last_deployed_at: '2023-11-07T05:31:56Z'
        description: Successfully retrieved application details.
  deprecated: false
  type: path
components:
  schemas:
    application_type:
      title: application_type
      description: The type of no-code application.
      type: string
      enum:
        - generation
    application_status:
      title: application_status
      description: >-
        Current deployment status of the application. Note: currently only
        `deployed` applications are returned.
      type: string
      enum:
        - deployed
        - draft
    application_input:
      title: application_input
      description: Configuration for an individual input field in the application.
      required:
        - name
        - input_type
        - required
      type: object
      properties:
        name:
          type: string
          description: Identifier for the input field.
        input_type:
          $ref: '#/components/schemas/application_input_type'
        description:
          type: string
          description: Human-readable description of the input field's purpose.
        required:
          type: boolean
          description: Indicates if this input field is mandatory.
        options:
          $ref: '#/components/schemas/application_input_options'
    application_input_type:
      title: application_input_type
      description: Type of input field determining its behavior and validation rules.
      type: string
      enum:
        - text
        - dropdown
        - file
        - media
    application_input_options:
      description: Type-specific configuration options for input fields.
      oneOf:
        - $ref: '#/components/schemas/application_input_dropdown_options'
        - $ref: '#/components/schemas/application_input_file_options'
        - $ref: '#/components/schemas/application_input_media_options'
        - $ref: '#/components/schemas/application_input_text_options'
    application_input_dropdown_options:
      title: Dropdown
      description: Configuration options specific to dropdown-type input fields.
      required:
        - list
      type: object
      properties:
        list:
          type: array
          description: List of available options in the dropdown menu.
          items:
            type: string
    application_input_file_options:
      title: File
      description: Configuration options specific to file upload input fields.
      required:
        - max_files
        - file_types
        - max_word_count
        - max_file_size_mb
        - upload_types
      type: object
      properties:
        max_files:
          type: integer
          format: int32
          description: Maximum number of files that can be uploaded.
        file_types:
          type: array
          description: List of allowed file extensions.
          items:
            type: string
        max_word_count:
          type: integer
          format: int32
          description: Maximum number of words allowed in text files.
        max_file_size_mb:
          type: integer
          format: int32
          description: Maximum file size allowed in megabytes.
        upload_types:
          type: array
          description: List of allowed upload types for file inputs.
          items:
            $ref: '#/components/schemas/file_upload_type'
    application_input_media_options:
      title: Media
      description: Configuration options specific to media upload input fields.
      required:
        - file_types
        - max_image_size_mb
      type: object
      properties:
        file_types:
          type: array
          description: List of allowed media file types.
          items:
            type: string
        max_image_size_mb:
          type: integer
          format: int32
          description: Maximum media file size allowed in megabytes.
    application_input_text_options:
      title: Text
      description: Configuration options specific to text input fields.
      required:
        - max_fields
        - min_fields
      type: object
      properties:
        max_fields:
          type: integer
          format: int32
          description: Maximum number of text fields allowed.
        min_fields:
          type: integer
          format: int32
          description: Minimum number of text fields required.
    file_upload_type:
      title: file_upload_type
      description: Type of file upload method supported by the application.
      type: string
      enum:
        - url
        - file_id

````