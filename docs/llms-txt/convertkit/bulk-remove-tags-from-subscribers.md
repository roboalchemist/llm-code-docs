# Source: https://developers.kit.com/api-reference/tags/bulk-remove-tags-from-subscribers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk remove tags from subscribers

> See "[Bulk & async processing](#bulk-amp-async-processing)" for more information.



## OpenAPI

````yaml api-reference/v4.json delete /v4/bulk/tags/subscribers
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/bulk/tags/subscribers:
    delete:
      tags:
        - Tags
      summary: Bulk remove tags from subscribers
      description: >-
        See "[Bulk & async processing](#bulk-amp-async-processing)" for more
        information.
      parameters: []
      responses:
        '200':
          description: >-
            Deletes the taggings synchronously when 100 or less tags/subscribers
            are provided
          content:
            application/json:
              schema:
                type: object
                properties:
                  failures:
                    type: array
                    items: {}
                required:
                  - failures
              example:
                failures: []
        '202':
          description: >-
            Destroys taggings asynchronously when more than 100 tags/subscribers
            are provided
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example: {}
        '401':
          description: Returns a 401 if the token and/or account cannot be authenticated
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - The access token is invalid
        '413':
          description: >-
            Returns a 413 when the size of the request would exceed the
            account's data limit for enqueued bulk requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - >-
                    This request exceeds your queued bulk requests limit. Please
                    wait while we process your existing requests and try again
                    later.
        '422':
          description: Returns a 422 when `taggings` is empty or not an array
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - No taggings included for processing
      security:
        - OAuth2: []
components:
  securitySchemes:
    OAuth2:
      description: Authenticate API requests via an OAuth token
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://api.kit.com/v4/oauth/authorize
          tokenUrl: https://api.kit.com/v4/oauth/token
          refreshUrl: https://api.kit.com/v4/oauth/token
          scopes:
            read: Read access to Kit API v4
            write: Write access to Kit API v4

````

Built with [Mintlify](https://mintlify.com).