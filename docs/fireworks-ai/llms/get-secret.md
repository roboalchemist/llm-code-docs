# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-secret.md

# Source: https://docs.fireworks.ai/api-reference/get-secret.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-secret.md

# Source: https://docs.fireworks.ai/api-reference/get-secret.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-secret.md

# Source: https://docs.fireworks.ai/api-reference/get-secret.md

# Get Secret

> Retrieves a secret by name. Note that the `value` field is not returned in the response for security reasons. Only the `name` and `key_name` fields are included.

## OpenAPI

````yaml get /v1/accounts/{account_id}/secrets/{secret_id}
paths:
  path: /v1/accounts/{account_id}/secrets/{secret_id}
  method: get
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
        secret_id:
          schema:
            - type: string
              required: true
              description: The Secret Id
      query:
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    title: |-
                      name follows the convention
                      accounts/account-id/secrets/unkey-key-id
              keyName:
                allOf:
                  - type: string
                    title: >-
                      name of the key. In this case, it can be
                      WOLFRAM_ALPHA_API_KEY
              value:
                allOf:
                  - type: string
                    example: sk-1234567890abcdef
                    description: >-
                      The secret value. This field is INPUT_ONLY and will not be
                      returned in GET or LIST responses

                      for security reasons. The value is only accepted when
                      creating or updating secrets.
            refIdentifier: '#/components/schemas/gatewaySecret'
            requiredProperties:
              - name
              - keyName
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