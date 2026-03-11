# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/upload_files_to_workspace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload files to workspace

> Upload files to workspace



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/file
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
  /workspace/{workspace_id}/file:
    post:
      tags:
        - file
      summary: Upload files to workspace
      description: |-
        Upload files to workspace
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace File: Create
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
          multipart/form-data:
            schema:
              type: object
              properties:
                content:
                  type: string
                  format: binary
                  description: ''
                type:
                  type: string
                  description: ''
                  enum:
                    - image
                    - video
                    - audio
                access:
                  type: string
                  description: ''
                  enum:
                    - public
                    - private
                  default: public
              required:
                - content
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                    description: ''
                    default: 10095
                  created_at:
                    type: string
                    format: timestamptz
                    description: ''
                    default: 2023-04-19 21:01:32+0000
                  name:
                    type: string
                    description: ''
                    default: file_example_MP3_1MG.mp3
                  size:
                    type: integer
                    format: int64
                    description: ''
                    default: 1087849
                  type:
                    type: string
                    description: ''
                    default: audio
                  mime:
                    type: string
                    description: ''
                    default: audio/mpeg
                  access:
                    type: string
                    description: ''
                    default: public
                  path:
                    type: string
                    description: ''
                    default: >-
                      /vault/Ramtdv50/3TA6XKsmLe-2BigGnwxSb0v00sI/qSWtbg../file_example_MP3_1MG.mp3
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