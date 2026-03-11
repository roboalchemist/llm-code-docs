# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/retrieve_information_about_the_authenticated_user_including_id_name_and_email_address.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve information about the authenticated user including ID, name, and email address.

> Retrieve information about the authenticated user including ID, name, and email address.



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json get /auth/me
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
  /auth/me:
    get:
      tags:
        - authentication
      summary: >-
        Retrieve information about the authenticated user including ID, name,
        and email address.
      description: >-
        Retrieve information about the authenticated user including ID, name,
        and email address.

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