# Source: https://docs.helicone.ai/rest/webhooks/delete-v1webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Webhook

> Delete a webhook

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml delete /v1/webhooks/{webhookId}
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
  /v1/webhooks/{webhookId}:
    delete:
      tags:
        - Webhooks
      operationId: DeleteWebhook
      parameters:
        - in: path
          name: webhookId
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_null.string_'
      security:
        - api_key: []
components:
  schemas:
    Result_null.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_null_'
        - $ref: '#/components/schemas/ResultError_string_'
    ResultSuccess_null_:
      properties:
        data:
          type: number
          enum:
            - null
          nullable: true
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