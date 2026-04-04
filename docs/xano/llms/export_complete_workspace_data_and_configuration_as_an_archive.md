# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/export_complete_workspace_data_and_configuration_as_an_archive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Export complete workspace data and configuration as an archive

> Leave the `branch` parameter empty to indicate the current live branch. `password` is optional. If provided, will encrypt the export and will be required when importing the file.



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/export
openapi: 3.0.0
info:
  title: Xano Metadata API (beta)
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a>

    is currently in <strong>beta</strong> and is the next
      evolution of the Developer API. It provides support
    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://x8ki-letl-twmt.n7.xano.io/api:meta
security: []
paths:
  /workspace/{workspace_id}/export:
    post:
      tags:
        - workspace
      summary: Export complete workspace data and configuration as an archive
      description: >-
        Leave the `branch` parameter empty to indicate the current live branch.
        `password` is optional. If provided, will encrypt the export and will be
        required when importing the file.

        <br /><br />

        <b>Required API Scope:</b>

        Instance Workspace: Read
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
                password:
                  type: string
                  description: ''
                branch:
                  type: string
                  description: ''
              example:
                branch: ''
                password: ''
          multipart/form-data:
            schema:
              type: object
              properties:
                password:
                  type: string
                  description: ''
                branch:
                  type: string
                  description: ''
              example:
                branch: ''
                password: ''
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties: {}
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