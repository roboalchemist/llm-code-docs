# Source: https://docs.frigade.com/api-reference/groups/groups-delete.md

# Delete a Group

## OpenAPI

````yaml delete /v1/groups
paths:
  path: /v1/groups
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
        groupId:
          schema:
            - type: string
              required: true
              description: The ID of the group
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The group has been successfully deleted.
        examples: {}
        description: The group has been successfully deleted.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The group was not found.
        examples: {}
        description: The group was not found.
  deprecated: false
  type: path
components:
  schemas: {}

````