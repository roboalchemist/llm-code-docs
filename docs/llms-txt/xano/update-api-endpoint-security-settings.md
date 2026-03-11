# Source: https://docs.xano.com/api-reference/api-group-api/update-api-endpoint-security-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update API endpoint security settings

> Update API endpoint security configuration and access controls
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}/security
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
  /workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}/security:
    put:
      tags:
        - api group / api
      summary: Update API endpoint security settings
      description: |-
        Update API endpoint security configuration and access controls
        <br /><br />
        <b>Authentication:</b> required
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}/security|PUT
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: apigroup_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: api_id
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
                guid:
                  type: string
                  description: ''
                include_xanoscript:
                  type: boolean
                  description: ''
              required:
                - guid
          multipart/form-data:
            schema:
              type: object
              properties:
                guid:
                  type: string
                  description: ''
                include_xanoscript:
                  type: boolean
                  description: ''
              required:
                - guid
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