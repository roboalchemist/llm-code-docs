# Source: https://docs.frigade.com/api-reference/users/users-delete.md

# Delete a User

## OpenAPI

````yaml delete /v1/users
paths:
  path: /v1/users
  method: delete
  request:
    security:
      - title: bearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Authentication header of the form `Bearer: <token>`, where
                `<token>` is either your public or private API key. [See when to
                use which](/v2/api-reference/authorization)
          cookie: {}
    parameters:
      path: {}
      query:
        foreignId:
          schema:
            - type: string
              required: false
              description: Deprecated. Use userId instead.
              deprecated: true
        userId:
          schema:
            - type: string
              required: true
              description: The ID of the user
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The user has been successfully deleted.
        examples: {}
        description: The user has been successfully deleted.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The user was not found.
        examples: {}
        description: The user was not found.
  deprecated: false
  type: path
components:
  schemas: {}

````