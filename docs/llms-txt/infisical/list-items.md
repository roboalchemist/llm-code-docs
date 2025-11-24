# Source: https://infisical.com/docs/api-reference/endpoints/pki-collections/list-items.md

# Retrieve

> Get items in PKI collection

## OpenAPI

````yaml GET /api/v1/pki/collections/{collectionId}/items
paths:
  path: /api/v1/pki/collections/{collectionId}/items
  method: get
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
    parameters:
      path:
        collectionId:
          schema:
            - type: string
              required: true
              description: The ID of the PKI collection to list items from.
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - certificate
                - ca
              required: false
              description: The type of the PKI collection item to list.
        offset:
          schema:
            - type: number
              required: false
              description: The offset to start from.
              maximum: 100
              minimum: 0
              default: 0
        limit:
          schema:
            - type: number
              required: false
              description: The number of items to return.
              maximum: 100
              minimum: 1
              default: 25
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              collectionItems:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                        pkiCollectionId:
                          type: string
                          format: uuid
                        type:
                          type: string
                          enum:
                            - certificate
                            - ca
                        itemId:
                          type: string
                        notBefore:
                          type: string
                          format: date-time
                        notAfter:
                          type: string
                          format: date-time
                        friendlyName:
                          type: string
                      required:
                        - id
                        - createdAt
                        - updatedAt
                        - pkiCollectionId
                        - type
                        - itemId
                        - notBefore
                        - notAfter
                        - friendlyName
                      additionalProperties: false
              totalCount:
                allOf:
                  - type: number
            requiredProperties:
              - collectionItems
              - totalCount
            additionalProperties: false
        examples:
          example:
            value:
              collectionItems:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  pkiCollectionId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  type: certificate
                  itemId: <string>
                  notBefore: '2023-11-07T05:31:56Z'
                  notAfter: '2023-11-07T05:31:56Z'
                  friendlyName: <string>
              totalCount: 123
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````