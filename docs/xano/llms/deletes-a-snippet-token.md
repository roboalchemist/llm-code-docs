# Source: https://docs.xano.com/xano-features/metadata-api/master-metadata-api/snippet-token/deletes-a-snippet-token.md

# Source: https://docs.xano.com/xano-features/metadata-api/account_api/deletes-a-snippet-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deletes a snippet token

> Deletes a specific snippet token



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_account.json delete /snippet/{canonical}/token/{token}
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
  /snippet/{canonical}/token/{token}:
    delete:
      tags:
        - snippet / token
      summary: deletes a snippet token
      description: |-
        deletes a snippet token
        <br /><br />
        <b>Authentication:</b> required
      parameters:
        - name: canonical
          in: path
          description: ''
          required: true
          schema:
            type: string
        - name: token
          in: path
          description: ''
          required: true
          schema:
            type: string
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