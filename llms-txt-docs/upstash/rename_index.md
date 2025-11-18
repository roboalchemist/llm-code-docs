# Source: https://upstash.com/docs/devops/developer-api/vector/rename_index.md

# Rename Index

> This endpoint is used to change the name of an index.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /vector/index/{id}/rename
paths:
  path: /vector/index/{id}/rename
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
              description: The unique ID of the index to be renamed
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The new name of the index
            required: true
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Index renamed successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/vector/rename_index
components:
  schemas: {}

````