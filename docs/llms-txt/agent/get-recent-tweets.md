# Source: https://docs.agent.ai/api-reference/get-data/get-recent-tweets.md

# Get Recent Tweets

> This action fetches recent tweets from a specified Twitter handle.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_recent_tweets
paths:
  path: /action/get_recent_tweets
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
              profile_handle:
                allOf:
                  - type: string
                    description: Twitter handle to fetch recent tweets from.
                    example: dharmesh
              recent_tweets_count:
                allOf:
                  - type: string
                    description: Number of recent tweets to fetch.
                    example: '10'
            required: true
            requiredProperties:
              - profile_handle
              - recent_tweets_count
        examples:
          example:
            value:
              profile_handle: dharmesh
              recent_tweets_count: '10'
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
                - created_at: '2025-02-11T20:26:06.000Z'
                  edit_history_tweet_ids:
                    - '1889410607004123312'
                  id: '1889410607004123312'
                  public_metrics:
                    bookmark_count: 2
                    impression_count: 3037
                    like_count: 23
                    quote_count: 0
                    reply_count: 2
                    retweet_count: 1
                  text: |-
                    "Photos or it didn't happen" ~someone

                    "APIs or the LLM didn't launch" ~me
                - created_at: '2025-02-11T19:38:21.000Z'
                  edit_history_tweet_ids:
                    - '1889398586820948045'
                  id: '1889398586820948045'
                  public_metrics:
                    bookmark_count: 0
                    impression_count: 111
                    like_count: 0
                    quote_count: 0
                    reply_count: 1
                    retweet_count: 0
                  text: >-
                    @akbarhshah I think we'll see standardization within
                    platforms, but I think establishing open standards *across*
                    platforms will take longer.


                    Standards are hard even when things are moving at a normal
                    pace.


                    In the world of A.I. it's going to be tricky.
                - created_at: '2025-02-11T18:46:17.000Z'
                  edit_history_tweet_ids:
                    - '1889385484868313291'
                  id: '1889385484868313291'
                  public_metrics:
                    bookmark_count: 0
                    impression_count: 0
                    like_count: 0
                    quote_count: 0
                    reply_count: 0
                    retweet_count: 243
                  text: >-
                    RT @readswithravi: “If it costs you your peace, it's too
                    expensive.”


                    — Paulo Coelho
                - created_at: '2025-02-11T18:43:43.000Z'
                  edit_history_tweet_ids:
                    - '1889384838353780917'
                  id: '1889384838353780917'
                  public_metrics:
                    bookmark_count: 77
                    impression_count: 8970
                    like_count: 85
                    quote_count: 3
                    reply_count: 13
                    retweet_count: 5
                  text: >-
                    Many seem to still be hung up on the debate of what is or
                    isn't an agent. Do they need to be autonomous? Do they have
                    to have full "agency"?


                    Here's my simple take:


                    This is not a binary thing, it's a spectrum. Software (which
                    is what agents are) can be less agentic or more…
                    https://t.co/epbmUT8VT3
                - created_at: '2025-02-11T16:05:27.000Z'
                  edit_history_tweet_ids:
                    - '1889345008676814883'
                  id: '1889345008676814883'
                  public_metrics:
                    bookmark_count: 0
                    impression_count: 0
                    like_count: 0
                    quote_count: 0
                    reply_count: 0
                    retweet_count: 1
                  text: >-
                    RT @leveragedupside: @dharmesh Women possess this skill
                    innately—that’s why we have more than 1 kid…


                    And the brain does actually change to…
                - created_at: '2025-02-10T22:27:00.000Z'
                  edit_history_tweet_ids:
                    - '1889078644364169703'
                  id: '1889078644364169703'
                  public_metrics:
                    bookmark_count: 108
                    impression_count: 35552
                    like_count: 441
                    quote_count: 2
                    reply_count: 18
                    retweet_count: 44
                  text: >-
                    And the remaining 1% is forgetting past pain and just going
                    at it again and again and again. https://t.co/sAwuDdfTx4
                - created_at: '2025-02-08T17:44:13.000Z'
                  edit_history_tweet_ids:
                    - '1888282700504498593'
                  id: '1888282700504498593'
                  public_metrics:
                    bookmark_count: 86
                    impression_count: 16778
                    like_count: 247
                    quote_count: 8
                    reply_count: 32
                    retweet_count: 29
                  text: >-
                    Today: SMB = Small Medium Business


                    Tomorrow: SMB = Small Mighty Business


                    With the power of A.I. agents, and digitally-hybrid teams a
                    5 person company will be able to do what previously needed a
                    50-person company to do.


                    A 50 person company will do what used to take 500 or 5,000…
                    https://t.co/17Lt6ceEmP https://t.co/1dgI04wtiY
                - created_at: '2025-02-07T19:16:27.000Z'
                  edit_history_tweet_ids:
                    - '1887943523930095638'
                  id: '1887943523930095638'
                  public_metrics:
                    bookmark_count: 0
                    impression_count: 0
                    like_count: 0
                    quote_count: 0
                    reply_count: 0
                    retweet_count: 4
                  text: >-
                    RT @AIAgentNews: 🚨Dharmesh's AI Agent Marketplace Just Hit
                    500,000 Users


                    Agent .ai was started by @dharmesh, founder &amp; CTO of

                    @HubSpot, 5…
                - created_at: '2025-02-06T19:34:21.000Z'
                  edit_history_tweet_ids:
                    - '1887585641262948669'
                  id: '1887585641262948669'
                  public_metrics:
                    bookmark_count: 27
                    impression_count: 6478
                    like_count: 23
                    quote_count: 0
                    reply_count: 6
                    retweet_count: 2
                  text: >-
                    This is just the kind of agent-building I had hoped would
                    happen on https://t.co/t8qEJJUqJQ. https://t.co/ZQ6l3dgqJ5
                - created_at: '2025-02-06T18:14:05.000Z'
                  edit_history_tweet_ids:
                    - '1887565444548333876'
                  id: '1887565444548333876'
                  public_metrics:
                    bookmark_count: 0
                    impression_count: 0
                    like_count: 0
                    quote_count: 0
                    reply_count: 0
                    retweet_count: 16
                  text: >-
                    RT @ShaneMac: Launching testnet is a huge milestone for
                    XMTP. This is real progress toward our long-term goal of
                    building a truly decentral…
        description: Recent tweets from the specified handle
  deprecated: false
  type: path
components:
  schemas: {}

````