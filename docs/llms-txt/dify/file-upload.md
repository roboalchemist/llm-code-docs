# Source: https://docs.dify.ai/api-reference/files/file-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# File Upload

> Upload a file (currently only images are supported) for use when sending messages, enabling multimodal understanding of images and text. Supports png, jpg, jpeg, webp, gif formats. Uploaded files are for use by the current end-user only.



## OpenAPI

````yaml en/api-reference/openapi_completion.json post /files/upload
openapi: 3.0.1
info:
  title: Completion App API
  description: >-
    The text generation application offers non-session support and is ideal for
    translation, article writing, summarization AI, and more.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Completion App API. Replace {api_base_url} with the
      actual API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Completion
    description: Operations related to text generation and completion.
  - name: Files
    description: Operations related to file management.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: Operations related to user feedback.
  - name: TTS
    description: Operations related to Text-to-Speech.
  - name: Application
    description: Operations to retrieve application settings and information.
paths:
  /files/upload:
    post:
      tags:
        - Files
      summary: File Upload
      description: >-
        Upload a file (currently only images are supported) for use when sending
        messages, enabling multimodal understanding of images and text. Supports
        png, jpg, jpeg, webp, gif formats. Uploaded files are for use by the
        current end-user only.
      operationId: uploadFile
      requestBody:
        description: File upload request. Requires multipart/form-data.
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - file
                - user
              properties:
                file:
                  type: string
                  format: binary
                  description: >-
                    The file to be uploaded. Supported image types: png, jpg,
                    jpeg, webp, gif.
                user:
                  type: string
                  description: >-
                    User identifier, defined by the developer's rules, must be
                    unique within the application.
      responses:
        '200':
          description: File uploaded successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileUploadResponse'
              examples:
                success:
                  value:
                    id: 72fa9618-8f89-4a37-9b33-7e1178a24a67
                    name: example.png
                    size: 1024
                    extension: png
                    mime_type: image/png
                    created_by: 6ad1ab0a-73ff-4ac1-b9e4-cdb312f71f13
                    created_at: 1577836800
        '400':
          description: |-
            Bad Request. Possible error codes:
            - `no_file_uploaded`: A file must be provided.
            - `too_many_files`: Currently only one file is accepted.
            - `unsupported_preview`: The file does not support preview.
            - `unsupported_estimate`: The file does not support estimation.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '413':
          description: '`file_too_large`: The file is too large.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '415':
          description: >-
            `unsupported_file_type`: Unsupported extension. Currently only
            document files are accepted (Note: description says image types png,
            jpg, etc. are supported for this endpoint, but this error message
            refers to document files. Clarification might be needed from source
            documentation).
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '503':
          description: |-
            Service Unavailable. Possible error codes:
            - `s3_connection_failed`: Unable to connect to S3 service.
            - `s3_permission_denied`: No permission to upload files to S3.
            - `s3_file_too_large`: File exceeds S3 size limit.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    FileUploadResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: ID of the uploaded file.
        name:
          type: string
          description: File name.
        size:
          type: integer
          description: File size (bytes).
        extension:
          type: string
          description: File extension.
        mime_type:
          type: string
          description: File mime-type.
        created_by:
          type: string
          format: uuid
          description: End-user ID who uploaded the file.
        created_at:
          type: integer
          format: int64
          description: Creation timestamp (Unix epoch).
          example: 1577836800
    ErrorResponse:
      type: object
      properties:
        status:
          type: integer
          description: HTTP status code.
        code:
          type: string
          description: Error code specific to the application.
        message:
          type: string
          description: A human-readable error message.
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        API Key authentication. For all API requests, include your API Key in
        the `Authorization` HTTP Header, prefixed with 'Bearer '. Example:
        `Authorization: Bearer {API_KEY}`. **Strongly recommend storing your API
        Key on the server-side, not shared or stored on the client-side, to
        avoid possible API-Key leakage that can lead to serious consequences.**

````

Built with [Mintlify](https://mintlify.com).