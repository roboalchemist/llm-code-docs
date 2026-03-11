# Source: https://docs.edenai.co/api-reference/files-management/delete-all-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete All Files

> Delete all uploaded files for the authenticated user.

This permanently deletes all files from storage.
This action cannot be undone.



## OpenAPI

````yaml openapi/v3-openapi.json delete /v3/upload
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
    delete:
      tags:
        - Files management
      summary: Delete All Files
      description: |-
        Delete all uploaded files for the authenticated user.

        This permanently deletes all files from storage.
        This action cannot be undone.
      operationId: delete_all_files_v3_upload_delete
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteFilesResponse'
      security:
        - AuthBearer: []
components:
  schemas:
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
  securitySchemes:
    AuthBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).