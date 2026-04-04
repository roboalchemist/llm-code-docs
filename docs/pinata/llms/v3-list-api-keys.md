# Source: https://docs.pinata.cloud/api-reference/endpoint/v3-list-api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List API Keys

> `org:write`




## OpenAPI

````yaml get /api_keys
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /api_keys:
    get:
      tags:
        - default
      summary: List API Keys
      description: |
        `org:write`
      parameters:
        - name: revoked
          in: query
          schema:
            type: boolean
          description: Returns only API keys that have been revoked
          example: 'true'
        - name: limitedUse
          in: query
          schema:
            type: boolean
          description: Returns only API keys with a max_uses value set
          example: 'true'
        - name: exhausted
          in: query
          schema:
            type: boolean
          description: >-
            Can only be used in conjunction with limitedUse query set to true.
            Returns only API keys with max_uses that have hit their use limit.
          example: 'true'
        - name: name
          in: query
          schema:
            type: string
          description: Returns API keys that match ilike on the API keys name column
          example: 70707d38-d683-4cc5-9e46-162d6f57d320
        - name: offset
          in: query
          schema:
            type: number
          description: Paginate through list of keys by offsetting number of results
          example: 10
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Wed, 12 Jun 2024 15:57:42 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '571'
            Connection:
              schema:
                type: string
                example: keep-alive
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
              example:
                keys:
                  - id: d4ea5a38-4e0a-4126-8fd4-7534d258a995
                    name: 5d945010-d9f0-4ef5-a7a9-4eb487dcdf53
                    key: 6270c5f4ed520756d498effbb6eb4b5f
                    max_uses: 2
                    uses: 2
                    user_id: 32bd7147-51d5-4df2-8771-7aeb9dcac7a2
                    scopes:
                      endpoints:
                        pinning:
                          pinFileToIPFS: true
                          pinJSONToIPFS: true
                      admin: false
                    revoked: true
                    createdAt: '2024-06-12T15:34:50.324Z'
                    updatedAt: '2024-06-12T15:34:51.204Z'
                count: 1
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````