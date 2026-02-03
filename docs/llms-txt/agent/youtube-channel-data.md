# Source: https://docs.agent.ai/api-reference/get-data/youtube-channel-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# YouTube Channel Data

> Retrieve detailed information about a YouTube channel, including its videos and statistics.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_youtube_channel
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
  /action/get_youtube_channel:
    post:
      tags:
        - Get Data
      summary: YouTube Channel Data
      description: >-
        Retrieve detailed information about a YouTube channel, including its
        videos and statistics.
      operationId: getYoutubeChannel
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  format: url
                  description: URL of the YouTube channel.
                  example: https://youtube.com/watch?v=example
              required:
                - url
      responses:
        '200':
          description: Data about the YouTube channel
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  about:
                    description: >-
                      We help the daring build legendary companies – from idea
                      to IPO and beyond.
                    joined_date: '2008-10-21'
                    joined_date_text: Joined Oct 21, 2008
                    links:
                      - link: http://www.sequoiacap.com
                        title: Sequoia Capital
                    subscribers: 49100
                    videos: 64
                    views: 1280815
                  channel:
                    avatar: >-
                      https://yt3.googleusercontent.com/uCN-D7KzMQY-Ti-xTsNAwilXVFFMYjEBRju_mXrR22HUYxJZjVZgP_SnamO9KbPo2XN-nE3O-A=s900-c-k-c0x00ffffff-no-rj
                    banner: >-
                      https://yt3.googleusercontent.com/mGnQSToNn5cN4iKUglTb8BdiuqSfpR-LHrv2KNDzsUqTDr3I5JS77pzQp8hleQqXI3AgM0alJA=w2560-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj
                    description: >-
                      We help the daring build legendary companies – from idea
                      to IPO and beyond.
                    first_link: http://www.sequoiacap.com
                    handle: '@sequoiacapital'
                    id: UCWrF0oN6unbXrWsTN7RctTw
                    is_family_safe: true
                    keywords: >-
                      "venture capital" technology sequoia "sequoia capital" vc
                      start-up funding "silicon valley"
                    subscribers: 49100
                    tags:
                      - venture capital
                      - technology
                      - sequoia
                      - sequoia capital
                      - vc
                      - start-up
                      - funding
                      - silicon valley
                    title: Sequoia Capital
                    videos: 64
                  highlighted_video:
                    description: >-
                      When ChatGPT ushered in a new paradigm of AI in everyday
                      use, many companies attempted to adapt to the new paradigm
                      by rushing to add chat interfaces to their products. Eric
                      has a different take—he doesn’t think chatbots are the
                      right form factor for everything. He thinks “zero-touch”
                      automation that works invisibly in the background can be
                      more valuable in many cases. He cites self-driving cars as
                      an analogy—or in this case, “self-driving money.” Ramp is
                      a new kind of finance management company for businesses,
                      offering AI-powered financial tools to help companies
                      handle spending and expense processes. We’ll hear why Eric
                      thinks AI that you never see is one of the most powerful
                      instruments for reducing time spent on drudgery and
                      unlocking more time for meaningful work.  


                      Hosted by: Ravi Gupta and Sonya Huang, Sequoia Capital
                    id: gFWwB3z8ags
                    link: https://www.youtube.com/watch?v=gFWwB3z8ags
                    published_time: 2 months ago
                    title: >-
                      Ramp CEO Eric Glyman: Using AI to Build “Self-Driving
                      Money”
                    views: 3624
                  search_metadata:
                    created_at: '2025-02-11T22:16:29Z'
                    html_url: >-
                      https://www.searchapi.io/api/v1/searches/search_ZW75dANvqloTO6aPX4blrDJ3.html
                    id: search_ZW75dANvqloTO6aPX4blrDJ3
                    json_url: >-
                      https://www.searchapi.io/api/v1/searches/search_ZW75dANvqloTO6aPX4blrDJ3
                    parsing_time_taken: 0.03
                    request_time_taken: 2.08
                    request_url: https://www.youtube.com/@sequoiacapital
                    status: Success
                    total_time_taken: 2.1
                  search_parameters:
                    channel_id: '@sequoiacapital'
                    engine: youtube_channel
                    gl: US
                    hl: en
                  videos_sections:
                    - section_title: Training Data
                      videos:
                        - id: xMrBgC-bKUU
                          length: '54:47'
                          link: https://www.youtube.com/watch?v=xMrBgC-bKUU
                          position: 1
                          published_time: 7 days ago
                          thumbnail: >-
                            https://i.ytimg.com/vi/xMrBgC-bKUU/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDym1dDc0DXHsgKHCRvR3qTl03eSQ
                          title: >-
                            Roblox Studio Head Stef Corazza: Using AI to Empower
                            Creators
                          views: 540
        '400':
          description: Data about the YouTube channel
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 400
                response: null
                error: >-
                  The requested page doesn't exist or there are no translations
                  available for the video.
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