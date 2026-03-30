# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/update_security_settings_for_an_api_group_configure_access_permissions_and_authentication_requirements.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update security settings for an API group. Configure access permissions and authentication requirements.

> Update security settings for an API group. Configure access permissions and authentication requirements.



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json put /workspace/{workspace_id}/apigroup/{apigroup_id}/security
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
  /workspace/{workspace_id}/apigroup/{apigroup_id}/security:
    put:
      tags:
        - api group
      summary: >-
        Update security settings for an API group. Configure access permissions
        and authentication requirements.
      description: >-
        Update security settings for an API group. Configure access permissions
        and authentication requirements.

        <br /><br />

        <b>Authentication:</b> required

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Api: Update
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                guid:
                  type: string
                  description: ''
                canonical:
                  type: string
                  description: ''
              required:
                - guid
                - canonical
          multipart/form-data:
            schema:
              type: object
              properties:
                guid:
                  type: string
                  description: ''
                canonical:
                  type: string
                  description: ''
              required:
                - guid
                - canonical
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
                  created_at:
                    type: string
                    format: timestamptz
                    description: ''
                    default: 2023-04-19 21:01:32+0000
                  updated_at:
                    type: string
                    format: timestamptz
                    description: ''
                    default: 2023-04-19 21:01:32+0000
                  name:
                    type: string
                    description: ''
                    default: API Group Test
                  description:
                    type: string
                    description: ''
                    default: My API groups description
                  docs:
                    type: string
                    description: ''
                    default: Documentation
                  guid:
                    type: string
                    description: ''
                    default: YE1fwVhQ-enRlc6Sb42Gqru58-0
                  canonical:
                    type: string
                    description: ''
                    default: FRzyRdY0
                  branch:
                    type: string
                    description: ''
                    default: v1
                  tag:
                    type: array
                    items:
                      type: string
                      description: ''
                    default:
                      - example tag
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