# Source: https://docs.pinata.cloud/api-reference/endpoint/v3-list-api-keys.md

# List API Keys

> `org:write`


## OpenAPI

````yaml get /api_keys
paths:
  path: /api_keys
  method: get
  servers:
    - url: https://api.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        revoked:
          schema:
            - type: boolean
              description: Returns only API keys that have been revoked
        limitedUse:
          schema:
            - type: boolean
              description: Returns only API keys with a max_uses value set
        exhausted:
          schema:
            - type: boolean
              description: >-
                Can only be used in conjunction with limitedUse query set to
                true. Returns only API keys with max_uses that have hit their
                use limit.
        name:
          schema:
            - type: string
              description: Returns API keys that match ilike on the API keys name column
        offset:
          schema:
            - type: number
              description: Paginate through list of keys by offsetting number of results
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value:
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
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````