# Source: https://docs.helicone.ai/rest/webhooks/get-v1webhooks.md

# Get Webhooks

> Get all webhooks

## OpenAPI

````yaml get /v1/webhooks
paths:
  path: /v1/webhooks
  method: get
  servers:
    - url: https://api.helicone.ai/
    - url: http://localhost:8585/
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''
          cookie: {}
    parameters:
      path: {}
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
              data:
                allOf:
                  - items:
                      properties:
                        hmac_key:
                          type: string
                        config:
                          type: string
                        version:
                          type: string
                        destination:
                          type: string
                        created_at:
                          type: string
                        id:
                          type: string
                      required:
                        - hmac_key
                        - config
                        - version
                        - destination
                        - created_at
                        - id
                      type: object
                    type: array
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: >-
              #/components/schemas/ResultSuccess__id-string--created_at-string--destination-string--version-string--config-string--hmac_key-string_-Array_
            requiredProperties:
              - data
              - error
            additionalProperties: false
          - type: object
            properties:
              data:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
              error:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/ResultError_string_'
            requiredProperties:
              - data
              - error
            additionalProperties: false
        examples:
          example:
            value:
              data:
                - hmac_key: <string>
                  config: <string>
                  version: <string>
                  destination: <string>
                  created_at: <string>
                  id: <string>
        description: Ok
  deprecated: false
  type: path
components:
  schemas: {}

````