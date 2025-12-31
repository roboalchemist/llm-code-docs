# Source: https://docs.agent.ai/api-reference/get-data/get-bluesky-posts.md

# Get Bluesky Posts

> Fetch recent posts from a specified Bluesky user handle, making it easy to monitor activity on the platform.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_bluesky_posts
paths:
  path: /action/get_bluesky_posts
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
              handle:
                allOf:
                  - type: string
                    description: Bluesky handle to fetch posts from.
                    example: mcuban.bsky.social
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
                    default: 5
                    description: Number of recent posts to fetch.
            required: true
            requiredProperties:
              - handle
              - num_posts
        examples:
          example:
            value:
              handle: mcuban.bsky.social
              num_posts: 5
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
                - cid: bafyreidfhhryjlrvausy6b75xgteie3w4jox5c4pumt5sredgpqxwxji3q
                  createdAt: '2025-02-11T20:16:41.033Z'
                  likeCount: 1043
                  replyCount: 40
                  repostCount: 113
                  text: >-
                    One year ago, we launched the Cost Plus Marketplace to help
                    healthcare businesses access affordable medications. Today,
                    we proudly supply thousands of hospitals, clinics, long-term
                    care facilities, surgery centers, and retail pharmacies.


                    ➡️ Sign up today: business.costplusdrugs.com
                  uri: >-
                    at://did:plc:h4ynx4kdeljjrfsbpk7p5xst/app.bsky.feed.post/3lhwi2fwdbs22
                - cid: bafyreihwct5awg6b25dgs3xiykcytmyqeooay6t5espe5bgbii3zvwjhwu
                  createdAt: '2025-02-11T18:51:42.838Z'
                  likeCount: 2941
                  replyCount: 131
                  repostCount: 272
                  text: >-
                    Let there be unlimited Q&A.  If the recipients are in red
                    areas, have it there.   Those local Republicans would have
                    to respond.
                  uri: >-
                    at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lhwdciahys23
                - cid: bafyreidipnc2obaikyj4poq4o7sgffysmv5gykis5mgxfodilmpaq2lpqi
                  createdAt: '2025-02-11T18:51:42.837Z'
                  likeCount: 42883
                  replyCount: 2049
                  repostCount: 9921
                  text: >-
                    Imagine if  @aoc @sanders.senate.gov , every dem,
                    SIMULTANEOUSLY held Town Halls where they allowed grant and
                    contract recipients to explain to the country what it is
                    they do and why it's important


                    Invite all media. Including RW podcasters. @spaces   Flood
                    the zone


                    Call it a Day Of Transparency
                  uri: >-
                    at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lhwdchvpbk23
                - cid: bafyreic5fbqbmcri5tmjvfygqnx4nn2akaaadpqlbhu3uv2igcidq2tmj4
                  createdAt: '2025-02-11T18:43:22.035Z'
                  likeCount: 6056
                  replyCount: 423
                  repostCount: 791
                  text: >-
                    It's not about lobbyists.   It's about the politicians on
                    this platform deciding to neuter DOGE by doing a better
                    version of what DOGE wants  to do.  Legislatively. 


                    The issue isn't the goal of efficiency and savings.  That's
                    important. 


                    The issue is the process to get there.
                  uri: >-
                    at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lhwctkcfts23
                - cid: bafyreiety4diyff3cfxrve46jtwcpwyrybmfilakc4cuip4hzo6ulxd63y
                  createdAt: '2025-02-11T17:56:59.229Z'
                  likeCount: 3
                  replyCount: 5
                  repostCount: 0
                  text: None taken.  Pretend I'm broke again.
                  uri: >-
                    at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lhwaamfxss25
        description: Retrieved Bluesky posts
  deprecated: false
  type: path
components:
  schemas: {}

````