# Source: https://docs.xano.com/api-reference/branch/update-a-workspace-branch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a workspace branch

> Update an existing branch's label, description, or color.
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Instance Workspace: Update



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/branch/{branch_label}
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
  /workspace/{workspace_id}/branch/{branch_label}:
    put:
      tags:
        - branch
      summary: Update a workspace branch
      description: |-
        Update an existing branch's label, description, or color.
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Instance Workspace: Update
      operationId: Xano Metadata API/workspace/{workspace_id}/branch/{branch_label}|PUT
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: branch_label
          in: path
          description: ''
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                label:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                color:
                  type: string
                  description: ''
              example:
                label: updated-branch
                description: Updated description
                color: '#ff5733'
          multipart/form-data:
            schema:
              type: object
              properties:
                label:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                color:
                  type: string
                  description: ''
              example:
                label: updated-branch
                description: Updated description
                color: '#ff5733'
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  created_at:
                    type: string
                    description: ''
                    default: 2023-06-22 22:59:11+0000
                  label:
                    type: string
                    description: ''
                    default: v1
                  live:
                    type: boolean
                    description: ''
                    default: true
                  backup:
                    type: boolean
                    description: ''
                    default: 'false'
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