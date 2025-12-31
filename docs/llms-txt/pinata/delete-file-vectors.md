# Source: https://docs.pinata.cloud/api-reference/endpoint/delete-file-vectors.md

# Delete File Vectors

> `org:write`


## OpenAPI

````yaml delete /vectorize/files/{file_id}
paths:
  path: /vectorize/files/{file_id}
  method: delete
  servers:
    - url: https://uploads.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        file_id:
          schema:
            - type: string
              required: true
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              success:
                allOf:
                  - type: boolean
            requiredProperties:
              - success
        examples:
          example:
            value:
              success: true
        description: Vectorize File Response
  deprecated: false
  type: path
components:
  schemas: {}

````