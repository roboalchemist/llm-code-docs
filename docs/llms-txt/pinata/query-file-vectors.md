# Source: https://docs.pinata.cloud/api-reference/endpoint/query-file-vectors.md

# Query File Vectors

> `org:write`


## OpenAPI

````yaml post /vectorize/groups/{group_id}/query
paths:
  path: /vectorize/groups/{group_id}/query
  method: post
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
        group_id:
          schema:
            - type: string
              required: true
              description: ID of the target group
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              text:
                allOf:
                  - type: string
                    description: Query string
        examples:
          example:
            value:
              text: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      count:
                        type: number
                      matches:
                        type: array
                        items:
                          type: object
                          properties:
                            file_id:
                              type: string
                            cid:
                              type: string
                            score:
                              type: number
        examples:
          example:
            value:
              data:
                count: 123
                matches:
                  - file_id: <string>
                    cid: <string>
                    score: 123
        description: Vectorize File Response
  deprecated: false
  type: path
components:
  schemas: {}

````