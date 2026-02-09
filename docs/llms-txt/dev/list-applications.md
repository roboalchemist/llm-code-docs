# Source: https://dev.writer.com/api-reference/application-api/list-applications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List applications

> Retrieves a paginated list of no-code agents (formerly called no-code applications) with optional filtering and sorting capabilities.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml get /v1/applications
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/applications:
    get:
      tags:
        - Generation API
      summary: List applications
      description: >-
        Retrieves a paginated list of no-code agents (formerly called no-code
        applications) with optional filtering and sorting capabilities.
      parameters:
        - name: order
          in: query
          required: false
          description: Sort order for the results based on creation time.
          schema:
            type: string
            default: desc
            enum:
              - asc
              - desc
        - name: before
          in: query
          required: false
          description: Return results before this application ID for pagination.
          schema:
            type: string
            format: uuid
        - name: after
          in: query
          required: false
          description: Return results after this application ID for pagination.
          schema:
            type: string
            format: uuid
        - name: limit
          in: query
          required: false
          description: Maximum number of applications to return in the response.
          schema:
            type: integer
            format: int32
            default: 50
        - name: type
          in: query
          required: false
          description: Filter applications by their type.
          schema:
            $ref: '#/components/schemas/application_type'
            default: generation
      responses:
        '200':
          description: Successfully retrieved list of applications.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get_applications_response'
      security:
        - bearerAuth: []
components:
  schemas:
    application_type:
      title: application_type
      description: The type of no-code application.
      type: string
      enum:
        - generation
    get_applications_response:
      title: get_applications_response
      description: Response object containing a paginated list of applications.
      required:
        - data
        - has_more
      type: object
      properties:
        data:
          type: array
          description: List of application objects with their configurations.
          items:
            $ref: '#/components/schemas/application_with_inputs'
        first_id:
          type: string
          format: uuid
          description: UUID of the first application in the current page.
        last_id:
          type: string
          format: uuid
          description: UUID of the last application in the current page.
        has_more:
          type: boolean
          description: Indicates if there are more results available in subsequent pages.
    application_with_inputs:
      title: application_with_inputs
      description: Detailed application object including its input configuration.
      required:
        - id
        - name
        - type
        - status
        - inputs
        - created_at
        - updated_at
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the application.
        name:
          type: string
          description: Display name of the application.
        type:
          $ref: '#/components/schemas/application_type'
        status:
          $ref: '#/components/schemas/application_status'
        inputs:
          type: array
          description: List of input configurations for the application.
          items:
            $ref: '#/components/schemas/application_input'
        created_at:
          type: string
          format: date-time
          description: Timestamp when the application was created.
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the application was last updated.
        last_deployed_at:
          type: string
          format: date-time
          description: Timestamp when the application was last deployed.
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