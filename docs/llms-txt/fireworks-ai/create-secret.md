# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-secret.md

# Source: https://docs.fireworks.ai/api-reference/create-secret.md

# null

## OpenAPI

````yaml post /v1/accounts/{account_id}/secrets
paths:
  path: /v1/accounts/{account_id}/secrets
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
                  - &ref_0
                    type: string
                    title: |-
                      name follows the convention
                      accounts/account-id/secrets/unkey-key-id
              keyName:
                allOf:
                  - &ref_1
                    type: string
                    title: >-
                      name of the key. In this case, it can be
                      WOLFRAM_ALPHA_API_KEY
              value:
                allOf:
                  - &ref_2
                    type: string
                    example: sk-1234567890abcdef
                    description: >-
                      The secret value. This field is INPUT_ONLY and will not be
                      returned in GET or LIST responses

                      for security reasons. The value is only accepted when
                      creating or updating secrets.
            required: true
            refIdentifier: '#/components/schemas/gatewaySecret'
            requiredProperties: &ref_3
              - name
              - keyName
        examples:
          example:
            value:
              name: <string>
              keyName: <string>
              value: sk-1234567890abcdef
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - *ref_0
              keyName:
                allOf:
                  - *ref_1
              value:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/gatewaySecret'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              name: <string>
              keyName: <string>
              value: sk-1234567890abcdef
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````