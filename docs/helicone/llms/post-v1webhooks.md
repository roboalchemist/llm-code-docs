# Source: https://docs.helicone.ai/rest/webhooks/post-v1webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Webhook

> Create a new webhook

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/webhooks
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
    post:
      tags:
        - Webhooks
      operationId: NewWebhook
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WebhookData'
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/ResultSuccess_unknown_'
                  - $ref: '#/components/schemas/ResultError_unknown_'
      security:
        - api_key: []
components:
  schemas:
    WebhookData:
      properties:
        destination:
          type: string
        config:
          $ref: '#/components/schemas/Record_string.any_'
        includeData:
          type: boolean
      required:
        - destination
        - config
      type: object
      additionalProperties: false
    ResultSuccess_unknown_:
      properties:
        data: {}
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
    ResultError_unknown_:
      properties:
        data:
          type: number
          enum:
            - null
          nullable: true
        error: {}
      required:
        - data
        - error
      type: object
      additionalProperties: false
    Record_string.any_:
      properties: {}
      additionalProperties: {}
      type: object
      description: Construct a type with a set of properties K of type T
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````