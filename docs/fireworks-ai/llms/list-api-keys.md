# Source: https://docs.fireworks.ai/api-reference/list-api-keys.md

# List API Keys

## OpenAPI

````yaml get /v1/accounts/{account_id}/users/{user_id}/apiKeys
paths:
  path: /v1/accounts/{account_id}/users/{user_id}/apiKeys
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
        user_id:
          schema:
            - type: string
              required: true
              description: The User Id
      query:
        pageSize:
          schema:
            - type: integer
              required: false
              description: >-
                Number of API keys to return in the response. Pagination support
                to be added.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                Token for fetching the next page of results. Pagination support
                to be added.
        filter:
          schema:
            - type: string
              required: false
              description: Field for filtering results.
        orderBy:
          schema:
            - type: string
              required: false
              description: Field for ordering results.
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
              apiKeys:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayApiKey'
                    description: List of API keys retrieved.
              nextPageToken:
                allOf:
                  - type: string
                    title: >-
                      Token for fetching the next page of results. Pagination
                      support to be added.

                      TODO: Implement pagination
              totalSize:
                allOf:
                  - type: integer
                    format: int32
                    description: The total number of API keys.
            refIdentifier: '#/components/schemas/gatewayListApiKeysResponse'
        examples:
          example:
            value:
              apiKeys:
                - keyId: <string>
                  displayName: <string>
                  key: <string>
                  createTime: '2023-11-07T05:31:56Z'
                  secure: true
                  email: <string>
                  prefix: <string>
                  expireTime: '2023-11-07T05:31:56Z'
              nextPageToken: <string>
              totalSize: 123
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    gatewayApiKey:
      type: object
      properties:
        keyId:
          type: string
          description: >-
            Unique identifier (Key ID) for the API key, used primarily for
            deletion.
          readOnly: true
        displayName:
          type: string
          description: >-
            Display name for the API key, defaults to "default" if not
            specified.
        key:
          type: string
          description: >-
            The actual API key value, only available upon creation and not
            stored thereafter.
          readOnly: true
        createTime:
          type: string
          format: date-time
          description: Timestamp indicating when the API key was created.
          readOnly: true
        secure:
          type: boolean
          description: >-
            Indicates whether the plaintext value of the API key is unknown to
            Fireworks.

            If true, Fireworks does not know this API key's plaintext value. If
            false, Fireworks does

            know the plaintext value.
          readOnly: true
        email:
          type: string
          description: Email of the user who owns this API key.
          readOnly: true
        prefix:
          type: string
          title: The first few characters of the API key to visually identify it
          readOnly: true
        expireTime:
          type: string
          format: date-time
          description: >-
            Timestamp indicating when the API key will expire. If not set, the
            key never expires.

````