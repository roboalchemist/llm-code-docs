# Source: https://docs.xano.com/xano-features/metadata-api/master-metadata-api/snippet/update-settings-on-the-snippet.md

# Source: https://docs.xano.com/xano-features/metadata-api/account_api/update-settings-on-the-snippet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update settings on the snippet

> Updates the settings for a specific snippet



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_account.json post /snippet/{canonical}
openapi: 3.0.0
info:
  title: Xano Metadata API
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a>

    is currently in <strong>beta</strong> and is the next
      evolution of the Developer API. It provides support
    to programatically manage your Xano schema and content and uses Access
    Tokens to

    control access.

    <br /><br />

    This portion of the Metadata supports retrieving details on the instances
    linked to your Xano account. Additional Metadata API functionality is
    available within the <strong>meta_api</strong> key of each instance.
  version: 0.0.1
servers:
  - url: https://app.xano.com/api:meta
security: []
paths:
  /snippet/{canonical}:
    post:
      tags:
        - snippet
      summary: update settings on the snippet
      description: |-
        update settings on the snippet
        <br /><br />
        <b>Authentication:</b> required
      parameters:
        - name: canonical
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
                install_access:
                  type: string
                  description: ''
                  enum:
                    - public
                    - link
                    - token
                install_access_description:
                  type: string
                  description: ''
              required:
                - install_access
                - install_access_description
          multipart/form-data:
            schema:
              type: object
              properties:
                install_access:
                  type: string
                  description: ''
                  enum:
                    - public
                    - link
                    - token
                install_access_description:
                  type: string
                  description: ''
              required:
                - install_access
                - install_access_description
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  canonical:
                    type: string
                    description: ''
                    default: kRG3t_-i
                  created_at:
                    type: string
                    format: timestamptz
                    description: ''
                    default: 2023-03-23 23:32:56+0000
                  updated_at:
                    type: string
                    format: timestamptz
                    description: ''
                    default: 2023-03-27 17:58:48+0000
                  name:
                    type: string
                    description: ''
                    default: Token Share Test
                  review:
                    type: string
                    description: ''
                    default: pending
                  review_exception:
                    type: string
                    description: ''
                  install_access:
                    type: string
                    description: ''
                    default: public
                  install_access_description:
                    type: string
                    description: ''
                  featured:
                    type: boolean
                    description: ''
                  verified:
                    type: boolean
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