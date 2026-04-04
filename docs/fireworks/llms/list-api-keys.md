# Source: https://docs.fireworks.ai/api-reference/list-api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List API Keys



## OpenAPI

````yaml get /v1/accounts/{account_id}/users/{user_id}/apiKeys
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.21.6
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/users/{user_id}/apiKeys:
    get:
      tags:
        - Gateway
      summary: List API Keys
      operationId: Gateway_ListApiKeys
      parameters:
        - name: pageSize
          description: >-
            Number of API keys to return in the response. Pagination support to
            be added.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: pageToken
          description: >-
            Token for fetching the next page of results. Pagination support to
            be added.
          in: query
          required: false
          schema:
            type: string
        - name: filter
          description: Field for filtering results.
          in: query
          required: false
          schema:
            type: string
        - name: orderBy
          description: Field for ordering results.
          in: query
          required: false
          schema:
            type: string
        - name: readMask
          description: >-
            The fields to be returned in the response. If empty or "*", all
            fields will be returned.
          in: query
          required: false
          schema:
            type: string
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: user_id
          in: path
          required: true
          description: The User Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayListApiKeysResponse'
components:
  schemas:
    gatewayListApiKeysResponse:
      type: object
      properties:
        apiKeys:
          type: array
          items:
            $ref: '#/components/schemas/gatewayApiKey'
            type: object
          description: List of API keys retrieved.
        nextPageToken:
          type: string
          title: >-
            Token for fetching the next page of results. Pagination support to
            be added.

            TODO: Implement pagination
        totalSize:
          type: integer
          format: int32
          description: The total number of API keys.
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````