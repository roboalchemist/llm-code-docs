# Source: https://docs.xano.com/xano-features/metadata-api/account_api/auth_me.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get authorized user

> Returns the authorized user's basic account information



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_account.json get /auth/me
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
  /auth/me:
    get:
      tags:
        - authentication
      summary: Validate the Access Token and identify the account details.
      description: |-
        Validate the Access Token and identify the account details.
        <br /><br />
        <b>Authentication:</b> required
      parameters: []
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  name:
                    type: string
                  email:
                    type: string
                  extras:
                    type: string
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