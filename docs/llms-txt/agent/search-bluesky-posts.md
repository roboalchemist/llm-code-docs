# Source: https://docs.agent.ai/api-reference/get-data/search-bluesky-posts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Bluesky Posts

> Search for Bluesky posts matching specific keywords or criteria to gather social media insights.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/search_bluesky_posts
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/search_bluesky_posts:
    post:
      tags:
        - Get Data
      summary: Search Bluesky Posts
      description: >-
        Search for Bluesky posts matching specific keywords or criteria to
        gather social media insights.
      operationId: searchBlueskyPosts
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: Search terms to find relevant Bluesky posts.
                  example: artificial intelligence
                num_posts:
                  type: integer
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
              required:
                - query
                - num_posts
      responses:
        '200':
          description: Bluesky posts search results
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  - author:
                      displayName: ''
                      handle: insurencecompanie.bsky.social
                    cid: >-
                      bafyreigh6t7gf2opl5sl72ej6zi46y6mnvff7lncpju7jv2uzphqno5muu
                    createdAt: '2025-02-12T00:14:58.952Z'
                    likeCount: 0
                    replyCount: 0
                    repostCount: 0
                    text: "Tariff, trade with Visa to dominate\_talks\n\nMichael Balman An foreign policy analyst Afp Narendra Modi in artificial intelligence action in Paris on Tuesday When the Prime Minister of India Narendra is a modicer of Washington and meets Donald DLing President Week, there will be some warm hugs and…"
                    uri: >-
                      at://did:plc:bvuaxil7a2fpcnxkgpgzbois/app.bsky.feed.post/3lhwveizrl62o
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````