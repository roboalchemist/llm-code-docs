# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/prepare-model.md

# Source: https://docs.fireworks.ai/api-reference/prepare-model.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/prepare-model.md

# Source: https://docs.fireworks.ai/api-reference/prepare-model.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/prepare-model.md

# Source: https://docs.fireworks.ai/api-reference/prepare-model.md

# Prepare Model for different precisions

## OpenAPI

````yaml post /v1/accounts/{account_id}/models/{model_id}:prepare
paths:
  path: /v1/accounts/{account_id}/models/{model_id}:prepare
  method: post
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
        model_id:
          schema:
            - type: string
              required: true
              description: The Model Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              precision:
                allOf:
                  - $ref: '#/components/schemas/DeploymentPrecision'
                    title: the precision with which the model will be prepared
              readMask:
                allOf:
                  - type: string
                    title: >-
                      The fields to be returned in the response. If empty or
                      "*", all fields will be returned.

                      This is added as is used in getResource()
            required: true
            refIdentifier: '#/components/schemas/GatewayPrepareModelBody'
        examples:
          example:
            value:
              precision: PRECISION_UNSPECIFIED
              readMask: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    DeploymentPrecision:
      type: string
      enum:
        - PRECISION_UNSPECIFIED
        - FP16
        - FP8
        - FP8_MM
        - FP8_AR
        - FP8_MM_KV_ATTN
        - FP8_KV
        - FP8_MM_V2
        - FP8_V2
        - FP8_MM_KV_ATTN_V2
        - NF4
        - FP4
        - BF16
        - FP4_BLOCKSCALED_MM
        - FP4_MX_MOE
      default: PRECISION_UNSPECIFIED
      title: >-
        - PRECISION_UNSPECIFIED: if left unspecified we will treat this as a
        legacy model created before

        self serve

````