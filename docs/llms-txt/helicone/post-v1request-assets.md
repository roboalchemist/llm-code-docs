# Source: https://docs.helicone.ai/rest/request/post-v1request-assets.md

# Submit Request Assets

> Submit assets for a specific request. - If you don't know what this is, you probably don't need this.

## OpenAPI

````yaml post /v1/request/{requestId}/assets/{assetId}
paths:
  path: /v1/request/{requestId}/assets/{assetId}
  method: post
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
      path:
        requestId:
          schema:
            - type: string
              required: true
        assetId:
          schema:
            - type: string
              required: true
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
                  - $ref: '#/components/schemas/HeliconeRequestAsset'
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_HeliconeRequestAsset_'
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
                assetUrl: <string>
        description: Ok
  deprecated: false
  type: path
components:
  schemas:
    HeliconeRequestAsset:
      properties:
        assetUrl:
          type: string
      required:
        - assetUrl
      type: object
      additionalProperties: false

````