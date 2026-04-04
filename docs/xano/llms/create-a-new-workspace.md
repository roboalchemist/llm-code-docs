# Source: https://docs.xano.com/api-reference/workspace/create-a-new-workspace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new workspace

> Create a new workspace
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Instance Workspace: Create



## OpenAPI

````yaml apispec_meta_instance.json post /workspace
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
  /workspace:
    post:
      tags:
        - workspace
      summary: Create a new workspace
      description: |-
        Create a new workspace
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Instance Workspace: Create
      operationId: Xano Metadata API/workspace|POST
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
              required:
                - name
              example:
                name: My New Workspace
                description: A new workspace for my project
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
              required:
                - name
              example:
                name: My New Workspace
                description: A new workspace for my project
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
                    default: 1
                  name:
                    type: string
                    description: ''
                    default: My Workspace
                  description:
                    type: string
                    description: ''
                    default: My Workspace Description
                  branch:
                    type: string
                    description: ''
                    default: v1
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