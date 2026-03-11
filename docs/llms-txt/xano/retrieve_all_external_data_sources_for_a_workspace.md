# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/retrieve_all_external_data_sources_for_a_workspace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve all external data sources for a workspace

> Retrieve all external data sources for a workspace



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json get /workspace/{workspace_id}/datasource
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
  /workspace/{workspace_id}/datasource:
    get:
      tags:
        - workspace / datasource
      summary: Retrieve all external data sources for a workspace
      description: |-
        Retrieve all external data sources for a workspace
        <br /><br />
        <b>Authentication:</b> required
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
                    color:
                      type: string
                      description: ''
                      default: '#008000'
                    label:
                      type: string
                      description: ''
                      default: live
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