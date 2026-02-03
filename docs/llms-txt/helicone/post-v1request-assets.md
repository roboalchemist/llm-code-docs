# Source: https://docs.helicone.ai/rest/request/post-v1request-assets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Request Assets

> Submit assets for a specific request. - If you don't know what this is, you probably don't need this.

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>

If you don't know what this is, you probably don't need this.


## OpenAPI

````yaml post /v1/request/{requestId}/assets/{assetId}
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
  /v1/request/{requestId}/assets/{assetId}:
    post:
      tags:
        - Request
      operationId: GetRequestAssetById
      parameters:
        - in: path
          name: requestId
          required: true
          schema:
            type: string
        - in: path
          name: assetId
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_HeliconeRequestAsset.string_'
      security:
        - api_key: []
components:
  schemas:
    Result_HeliconeRequestAsset.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_HeliconeRequestAsset_'
        - $ref: '#/components/schemas/ResultError_string_'
    ResultSuccess_HeliconeRequestAsset_:
      properties:
        data:
          $ref: '#/components/schemas/HeliconeRequestAsset'
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
    HeliconeRequestAsset:
      properties:
        assetUrl:
          type: string
      required:
        - assetUrl
      type: object
      additionalProperties: false
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````