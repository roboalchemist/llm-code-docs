# Source: https://docs.edenai.co/api-reference/files-management/list-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List Files

> List uploaded files for the authenticated user.

Optionally filter by purpose. Only returns non-expired files.
Results are ordered by creation date (newest first).



## OpenAPI

````yaml openapi/v3-openapi.json get /v3/upload
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
    get:
      tags:
        - Files management
      summary: List Files
      description: |-
        List uploaded files for the authenticated user.

        Optionally filter by purpose. Only returns non-expired files.
        Results are ordered by creation date (newest first).
      operationId: list_files_v3_upload_get
      parameters:
        - name: purpose
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                maxLength: 50
              - type: 'null'
            description: Filter by purpose
            title: Purpose
          description: Filter by purpose
        - name: page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            description: Page number (1-indexed)
            default: 1
            title: Page
          description: Page number (1-indexed)
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            maximum: 1000
            minimum: 1
            description: Maximum number of items per page
            default: 100
            title: Limit
          description: Maximum number of items per page
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListFilesResponse'
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
    ListFilesResponse:
      properties:
        items:
          items:
            $ref: '#/components/schemas/FileResponse'
          type: array
          title: Items
          description: List of items
        total:
          type: integer
          title: Total
          description: Total number of items
        page:
          type: integer
          title: Page
          description: Current page number
        limit:
          type: integer
          title: Limit
          description: Items per page
        total_pages:
          type: integer
          title: Total Pages
          description: Total number of pages
      type: object
      required:
        - items
        - total
        - page
        - limit
        - total_pages
      title: ListFilesResponse
      description: Response for listing files with pagination.
      example:
        items:
          - created_at: '2025-12-08T10:30:00Z'
            expires_at: '2026-01-07T10:30:00Z'
            file_id: 550e8400-e29b-41d4-a716-446655440000
            file_mimetype: application/pdf
            file_name: invoice.pdf
            file_size: 1048576
            metadata:
              page_count: 5
            purpose: general
        limit: 100
        page: 1
        total: 25
        total_pages: 1
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    FileResponse:
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
      title: FileResponse
      description: Response for a file.
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