# Source: https://docs.helicone.ai/rest/webhooks/get-v1webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Webhooks

> Get all webhooks

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml get /v1/webhooks
openapi: 3.0.0
info:
  title: helicone-api
  version: 1.0.0
  license:
    name: MIT
  contact: {}
servers:
  - url: https://api.helicone.ai/
  - url: http://localhost:8585/
security: []
paths:
  /v1/webhooks:
    get:
      tags:
        - Webhooks
      operationId: GetWebhooks
      parameters: []
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Result__id-string--created_at-string--destination-string--version-string--config-string--hmac_key-string_-Array.string_
      security:
        - api_key: []
components:
  schemas:
    Result__id-string--created_at-string--destination-string--version-string--config-string--hmac_key-string_-Array.string_:
      anyOf:
        - $ref: >-
            #/components/schemas/ResultSuccess__id-string--created_at-string--destination-string--version-string--config-string--hmac_key-string_-Array_
        - $ref: '#/components/schemas/ResultError_string_'
    ResultSuccess__id-string--created_at-string--destination-string--version-string--config-string--hmac_key-string_-Array_:
      properties:
        data:
          items:
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
          type: number
          enum:
            - null
          nullable: true
      required:
        - data
        - error
      type: object
      additionalProperties: false
    ResultError_string_:
      properties:
        data:
          type: number
          enum:
            - null
          nullable: true
        error:
          type: string
      required:
        - data
        - error
      type: object
      additionalProperties: false
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````