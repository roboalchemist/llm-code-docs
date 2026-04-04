# Source: https://docs.helicone.ai/rest/property/post-v1propertyquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Properties

> Query properties for a specific user

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/property/query
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
  /v1/property/query:
    post:
      tags:
        - Property
      operationId: GetProperties
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties: {}
              type: object
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_Property-Array.string_'
      security:
        - api_key: []
components:
  schemas:
    Result_Property-Array.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_Property-Array_'
        - $ref: '#/components/schemas/ResultError_string_'
    ResultSuccess_Property-Array_:
      properties:
        data:
          items:
            $ref: '#/components/schemas/Property'
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
    Property:
      properties:
        property:
          type: string
      required:
        - property
      type: object
      additionalProperties: false
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````