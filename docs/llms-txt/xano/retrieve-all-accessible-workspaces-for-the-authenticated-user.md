# Source: https://docs.xano.com/api-reference/workspace/retrieve-all-accessible-workspaces-for-the-authenticated-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve all accessible workspaces for the authenticated user

> Retrieve all accessible workspaces for the authenticated user
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json get /workspace
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
    get:
      tags:
        - workspace
      summary: Retrieve all accessible workspaces for the authenticated user
      description: |-
        Retrieve all accessible workspaces for the authenticated user
        <br /><br />
        <b>Authentication:</b> required
      operationId: Xano Metadata API/workspace|GET
      parameters: []
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: array
                items:
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