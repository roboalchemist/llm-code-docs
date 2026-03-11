# Source: https://docs.edenai.co/api-reference/files-management/delete-files-by-ids.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Files By Ids

> Delete specific files by their IDs.

Only files owned by the authenticated user will be deleted.
Files that don't exist or aren't owned by the user are silently ignored.
This action cannot be undone.



## OpenAPI

````yaml openapi/v3-openapi.json post /v3/upload/delete
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/upload/delete:
    post:
      tags:
        - Files management
      summary: Delete Files By Ids
      description: |-
        Delete specific files by their IDs.

        Only files owned by the authenticated user will be deleted.
        Files that don't exist or aren't owned by the user are silently ignored.
        This action cannot be undone.
      operationId: delete_files_by_ids_v3_upload_delete_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeleteFilesRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteFilesResponse'
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
    DeleteFilesRequest:
      properties:
        file_ids:
          items:
            type: string
            format: uuid
          type: array
          maxItems: 100
          minItems: 1
          title: File Ids
          description: List of file IDs to delete (1-100)
      type: object
      required:
        - file_ids
      title: DeleteFilesRequest
      description: Request body for deleting multiple files.
      example:
        file_ids:
          - 550e8400-e29b-41d4-a716-446655440000
          - 550e8400-e29b-41d4-a716-446655440001
    DeleteFilesResponse:
      properties:
        deleted_count:
          type: integer
          title: Deleted Count
          description: Number of files deleted
      type: object
      required:
        - deleted_count
      title: DeleteFilesResponse
      description: Response for file deletion.
      example:
        deleted_count: 5
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