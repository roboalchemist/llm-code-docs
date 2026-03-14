# Source: https://docs.edenai.co/api-reference/files-management/upload-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload File

> Upload a file for persistent storage.

Returns a file_id that can be used in subsequent API calls to /v3/universal-ai.

Files are stored securely and only accessible by the file owner.
Default expiration is 30 days, maximum 30 days.



## OpenAPI

````yaml openapi/v3-openapi.json post /v3/upload
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/upload:
    post:
      tags:
        - Files management
      summary: Upload File
      description: >-
        Upload a file for persistent storage.


        Returns a file_id that can be used in subsequent API calls to
        /v3/universal-ai.


        Files are stored securely and only accessible by the file owner.

        Default expiration is 30 days, maximum 30 days.
      operationId: upload_file_v3_upload_post
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Body_upload_file_v3_upload_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UploadResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - AuthBearer: []
components:
  schemas:
    Body_upload_file_v3_upload_post:
      properties:
        file:
          type: string
          format: binary
          title: File
          description: File to upload
        expires_in_days:
          type: integer
          maximum: 30
          minimum: 1
          title: Expires In Days
          description: Expiration in days (1-30)
          default: 30
        purpose:
          type: string
          maxLength: 50
          minLength: 1
          title: Purpose
          description: Purpose of the file
          default: general
      type: object
      required:
        - file
      title: Body_upload_file_v3_upload_post
    UploadResponse:
      properties:
        file_id:
          type: string
          format: uuid
          title: File Id
          description: Unique file identifier for use in API calls
        file_name:
          type: string
          title: File Name
          description: Original filename
        file_size:
          type: integer
          title: File Size
          description: File size in bytes
        file_mimetype:
          type: string
          title: File Mimetype
          description: Detected MIME type
        purpose:
          type: string
          title: Purpose
          description: Purpose of the file (e.g., 'general', 'assistants')
        metadata:
          additionalProperties: true
          type: object
          title: Metadata
          description: File metadata (e.g., page_count for PDFs/documents)
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Upload timestamp
        expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expires At
          description: Expiration timestamp
      type: object
      required:
        - file_id
        - file_name
        - file_size
        - file_mimetype
        - purpose
        - created_at
      title: UploadResponse
      description: Response for a successful file upload.
      example:
        created_at: '2025-12-08T10:30:00Z'
        expires_at: '2026-01-07T10:30:00Z'
        file_id: 550e8400-e29b-41d4-a716-446655440000
        file_mimetype: application/pdf
        file_name: invoice.pdf
        file_size: 1048576
        metadata:
          page_count: 5
        purpose: general
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    AuthBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).