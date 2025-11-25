# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-api-key.md

# Source: https://docs.fireworks.ai/api-reference/create-api-key.md

# Create API Key

## OpenAPI

````yaml post /v1/accounts/{account_id}/users/{user_id}/apiKeys
paths:
  path: /v1/accounts/{account_id}/users/{user_id}/apiKeys
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
        user_id:
          schema:
            - type: string
              required: true
              description: The User Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              apiKey:
                allOf:
                  - $ref: '#/components/schemas/gatewayApiKey'
                    description: The API key to be created.
            required: true
            refIdentifier: '#/components/schemas/GatewayCreateApiKeyBody'
            requiredProperties:
              - apiKey
        examples:
          example:
            value:
              apiKey:
                displayName: <string>
                expireTime: '2023-11-07T05:31:56Z'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              keyId:
                allOf:
                  - &ref_0
                    type: string
                    description: >-
                      Unique identifier (Key ID) for the API key, used primarily
                      for deletion.
                    readOnly: true
              displayName:
                allOf:
                  - &ref_1
                    type: string
                    description: >-
                      Display name for the API key, defaults to "default" if not
                      specified.
              key:
                allOf:
                  - &ref_2
                    type: string
                    description: >-
                      The actual API key value, only available upon creation and
                      not stored thereafter.
                    readOnly: true
              createTime:
                allOf:
                  - &ref_3
                    type: string
                    format: date-time
                    description: Timestamp indicating when the API key was created.
                    readOnly: true
              secure:
                allOf:
                  - &ref_4
                    type: boolean
                    description: >-
                      Indicates whether the plaintext value of the API key is
                      unknown to Fireworks.

                      If true, Fireworks does not know this API key's plaintext
                      value. If false, Fireworks does

                      know the plaintext value.
                    readOnly: true
              email:
                allOf:
                  - &ref_5
                    type: string
                    description: Email of the user who owns this API key.
                    readOnly: true
              prefix:
                allOf:
                  - &ref_6
                    type: string
                    title: >-
                      The first few characters of the API key to visually
                      identify it
                    readOnly: true
              expireTime:
                allOf:
                  - &ref_7
                    type: string
                    format: date-time
                    description: >-
                      Timestamp indicating when the API key will expire. If not
                      set, the key never expires.
            refIdentifier: '#/components/schemas/gatewayApiKey'
        examples:
          example:
            value:
              keyId: <string>
              displayName: <string>
              key: <string>
              createTime: '2023-11-07T05:31:56Z'
              secure: true
              email: <string>
              prefix: <string>
              expireTime: '2023-11-07T05:31:56Z'
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    gatewayApiKey:
      type: object
      properties:
        keyId: *ref_0
        displayName: *ref_1
        key: *ref_2
        createTime: *ref_3
        secure: *ref_4
        email: *ref_5
        prefix: *ref_6
        expireTime: *ref_7

````