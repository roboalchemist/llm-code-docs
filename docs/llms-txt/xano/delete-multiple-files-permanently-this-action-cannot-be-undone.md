# Source: https://docs.xano.com/api-reference/file/delete-multiple-files-permanently-this-action-cannot-be-undone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete multiple files permanently. This action cannot be undone.

> Delete multiple files permanently. This action cannot be undone.
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace File: Delete



## OpenAPI

````yaml apispec_meta_instance.json delete /workspace/{workspace_id}/file/bulk_delete
openapi: 3.0.0
info:
  title: Xano Metadata API
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a> provides support

    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://your-xano-instance.xano.io/api:meta
security: []
paths:
  /workspace/{workspace_id}/file/bulk_delete:
    delete:
      tags:
        - file
      summary: Delete multiple files permanently. This action cannot be undone.
      description: |-
        Delete multiple files permanently. This action cannot be undone.
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace File: Delete
      operationId: Xano Metadata API/workspace/{workspace_id}/file/bulk_delete|DELETE
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                ids:
                  type: array
                  items:
                    type: integer
                    format: int64
                    description: ''
              required:
                - ids
          multipart/form-data:
            schema:
              type: object
              properties:
                ids:
                  type: array
                  items:
                    type: integer
                    format: int64
                    description: ''
              required:
                - ids
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                description: ''
        '400':
          description: Input Error. Check the request payload for issues.
        '401':
          description: Unauthorized
        '403':
          description: >-
            Access denied. Additional privileges are needed access the requested
            resource.
        '404':
          description: Not Found. The requested resource does not exist.
        '429':
          description: Rate Limited. Too many requests.
        '500':
          description: Unexpected error
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).