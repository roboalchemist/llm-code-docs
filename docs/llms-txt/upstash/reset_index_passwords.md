# Source: https://upstash.com/docs/devops/developer-api/vector/reset_index_passwords.md

# Reset Index Passwords

> This endpoint is used to reset regular and readonly tokens of an index.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /vector/index/{id}/reset-password
paths:
  path: /vector/index/{id}/reset-password
  method: post
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique ID of the index to reset the password for
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Index passwords reset successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/vector/reset_index_passwords
components:
  schemas: {}

````