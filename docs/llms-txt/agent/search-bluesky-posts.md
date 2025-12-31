# Source: https://docs.agent.ai/api-reference/get-data/search-bluesky-posts.md

# Search Bluesky Posts

> Search for Bluesky posts matching specific keywords or criteria to gather social media insights.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/search_bluesky_posts
paths:
  path: /action/search_bluesky_posts
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              query:
                allOf:
                  - type: string
                    description: Search terms to find relevant Bluesky posts.
                    example: artificial intelligence
              num_posts:
                allOf:
                  - type: integer
                    format: int64
                    enum:
                      - 1
                      - 5
                      - 10
                      - 25
                      - 50
                      - 100
                    default: 1
                    description: Number of matching posts to fetch.
            required: true
            requiredProperties:
              - query
              - num_posts
        examples:
          example:
            value:
              query: artificial intelligence
              num_posts: 1
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                - author:
                    displayName: ''
                    handle: insurencecompanie.bsky.social
                  cid: bafyreigh6t7gf2opl5sl72ej6zi46y6mnvff7lncpju7jv2uzphqno5muu
                  createdAt: '2025-02-12T00:14:58.952Z'
                  likeCount: 0
                  replyCount: 0
                  repostCount: 0
                  text: "Tariff, trade with Visa to dominate\_talks\n\nMichael Balman An foreign policy analyst Afp Narendra Modi in artificial intelligence action in Paris on Tuesday When the Prime Minister of India Narendra is a modicer of Washington and meets Donald DLing President Week, there will be some warm hugs and…"
                  uri: >-
                    at://did:plc:bvuaxil7a2fpcnxkgpgzbois/app.bsky.feed.post/3lhwveizrl62o
        description: Bluesky posts search results
  deprecated: false
  type: path
components:
  schemas: {}

````