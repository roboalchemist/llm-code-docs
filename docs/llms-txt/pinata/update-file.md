# Source: https://docs.pinata.cloud/api-reference/endpoint/update-file.md

# Update File

> `org:files:write`


## OpenAPI

````yaml put /files/{network}/{id}
paths:
  path: /files/{network}/{id}
  method: put
  servers:
    - url: https://api.pinata.cloud/v3
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
        network:
          schema:
            - type: enum<string>
              enum:
                - public
                - private
              required: true
              description: Target a file on either the public or private IPFS network
        id:
          schema:
            - type: string
              required: true
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
                    description: The updated name for a file
              keyvalues:
                allOf:
                  - type: object
                    additionalProperties: true
                    description: Stringified key/values metadata
            example:
              name: Hello Files API
        examples:
          example:
            value:
              name: Hello Files API
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
                      id:
                        type: string
                      name:
                        type: string
                      cid:
                        type: string
                      size:
                        type: number
                      number_of_files:
                        type: number
                      keyvalues:
                        type: object
                      mime_type:
                        type: string
                      group_id:
                        type: string
                      created_at:
                        type: string
        examples:
          example:
            value:
              data:
                id: e5323ea7-8a02-4486-9b6f-63c788810aeb
                name: e093dbd3-f276-4bb3-a43e-60437725f410.txt
                cid: bafkreicnu2aqjkoglrlrd65giwo4l64pdajxffk6jtq2vb7yaiopc3yu7m
                size: 36
                number_of_files: 1
                mime_type: text/plain
                group_id: 18893556-de8e-4229-8a9a-27b95468dd3e
                keyvalues:
                  whimsey: 'true'
                created_at: '2024-08-27T14:57:51.485934Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````