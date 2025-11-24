# Source: https://docs.fireworks.ai/api-reference/list-secrets.md

# List Secrets

> Lists all secrets for an account. Note that the `value` field is not returned in the response for security reasons. Only the `name` and `key_name` fields are included for each secret.

## OpenAPI

````yaml get /v1/accounts/{account_id}/secrets
paths:
  path: /v1/accounts/{account_id}/secrets
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
      query:
        pageSize:
          schema:
            - type: integer
              required: false
        pageToken:
          schema:
            - type: string
              required: false
        filter:
          schema:
            - type: string
              required: false
              description: Unused but required to use existing ListRequest functionality.
        orderBy:
          schema:
            - type: string
              required: false
              description: Unused but required to use existing ListRequest functionality.
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
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewaySecret'
              nextPageToken:
                allOf:
                  - type: string
              totalSize:
                allOf:
                  - type: integer
                    format: int32
                    description: The total number of secrets.
            refIdentifier: '#/components/schemas/gatewayListSecretsResponse'
        examples:
          example:
            value:
              secrets:
                - name: <string>
                  keyName: <string>
                  value: sk-1234567890abcdef
              nextPageToken: <string>
              totalSize: 123
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    gatewaySecret:
      type: object
      properties:
        name:
          type: string
          title: |-
            name follows the convention
            accounts/account-id/secrets/unkey-key-id
        keyName:
          type: string
          title: name of the key. In this case, it can be WOLFRAM_ALPHA_API_KEY
        value:
          type: string
          example: sk-1234567890abcdef
          description: >-
            The secret value. This field is INPUT_ONLY and will not be returned
            in GET or LIST responses

            for security reasons. The value is only accepted when creating or
            updating secrets.
      required:
        - name
        - keyName

````