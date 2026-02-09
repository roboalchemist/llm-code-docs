# Source: https://docs.agent.ai/api-reference/get-data/youtube-search-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# YouTube Search Results

> Perform a YouTube search and retrieve results for specified queries.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/run_youtube_search
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
  /action/run_youtube_search:
    post:
      tags:
        - Get Data
      summary: YouTube Search Results
      description: Perform a YouTube search and retrieve results for specified queries.
      operationId: runYoutubeSearch
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: Search terms for YouTube.
                  example: machine learning tutorials
              required:
                - query
      responses:
        '200':
          description: YouTube search results
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  search_information:
                    total_results: 3383350
                  search_parameters:
                    engine: youtube
                    gl: US
                    hl: en
                    q: AI advancements
                  shorts:
                    - items:
                        - id: OI1vPRfnN2o
                          link: https://www.youtube.com/shorts/OI1vPRfnN2o
                          position: 1
                          thumbnail: >-
                            https://i.ytimg.com/vi/OI1vPRfnN2o/oar2.jpg?sqp=-oaymwEdCJUDENAFSFWQAgHyq4qpAwwIARUAAIhCcAHAAQY=&rs=AOn4CLBcsaGmJ8EwCfjCpatPL462tFR1UQ
                          title: >-
                            The world is changing — HUGE AI advancements in
                            robotics just happened  🤯 #autonomousrobotics
                          views: 8700
                        - id: OK0YhF3NMpQ
                          link: https://www.youtube.com/shorts/OK0YhF3NMpQ
                          position: 2
                          thumbnail: >-
                            https://i.ytimg.com/vi/OK0YhF3NMpQ/hq720.jpg?sqp=-oaymwEdCJUDENAFSFXyq4qpAw8IARUAAIhCcAHAAQbQAQE=&rs=AOn4CLCHSrIC86zUTlRystaI2t8wQzYveA
                          title: OpenAI's CEO on What Kids Should Be Studying
                          views: 4200000
                        - id: hB0pqmq9IKg
                          link: https://www.youtube.com/shorts/hB0pqmq9IKg
                          position: 3
                          thumbnail: >-
                            https://i.ytimg.com/vi/hB0pqmq9IKg/oardefault.jpg?sqp=-oaymwEdCJUDENAFSFWQAgHyq4qpAwwIARUAAIhCcAHAAQY=&rs=AOn4CLDfwABwpUhMCmgy00FviHPciFNmBQ
                          title: >-
                            Using AI, they can automatically identify and
                            categorize what their satellites see.
                          views: 2800000
                      position: 9
                      section_title: Shorts
                    - items:
                        - id: DqH_4uJ2BOI
                          link: https://www.youtube.com/shorts/DqH_4uJ2BOI
                          position: 1
                          thumbnail: >-
                            https://i.ytimg.com/vi/DqH_4uJ2BOI/hq720_2.jpg?sqp=-oaymwEdCJYDENAFSFXyq4qpAw8IARUAAIhCcAHAAQbQAQE=&rs=AOn4CLBo5_OSidSf_dIUG-HAlHkGk4hLDg
                          title: Elon Musk's Prediction for AI Future
                          views: 571000
                        - id: wQCRZlbLgY4
                          link: https://www.youtube.com/shorts/wQCRZlbLgY4
                          position: 2
                          thumbnail: >-
                            https://i.ytimg.com/vi/wQCRZlbLgY4/oardefault.jpg?sqp=-oaymwEdCJUDENAFSFWQAgHyq4qpAwwIARUAAIhCcAHAAQY=&rs=AOn4CLDG1izH6eaT9peuefHHxb10oE5y2w
                          title: The future of AI
                          views: 2300000
                        - id: ItvWg1duv_k
                          link: https://www.youtube.com/shorts/ItvWg1duv_k
                          position: 3
                          thumbnail: >-
                            https://i.ytimg.com/vi/ItvWg1duv_k/oar2.jpg?sqp=-oaymwEdCJUDENAFSFWQAgHyq4qpAwwIARUAAIhCcAHAAQY=&rs=AOn4CLCqNnmpYosU6J_Q5SNgbm9RMS8ncg
                          title: Why AI Is More Important Than We Thought
                          views: 5200
                      position: 13
                      section_title: Shorts
                  suggestions:
                    - ai tutorial
                    - ai news
                    - ai future
                    - artificial intelligence news
                    - artificial intelligence robot
                    - artificial intelligence documentary
                    - how does ai work
                    - what is ai
                    - artificial intelligence podcast
                    - ai advantage
                    - mustafa suleyman
                    - ai learning
                    - two minute papers
                    - artificial intelligence explained
                    - what is artificial intelligence
                  videos:
                    - badges:
                        - New
                      channel:
                        id: UC5l7RouTQ60oUjLjt1Nh-UQ
                        is_verified: true
                        link: https://www.youtube.com/@airevolutionx
                        thumbnail: >-
                          https://yt3.ggpht.com/XRZC_XqZoSUtB_Zo9R0w2vDRqGqVv0lKZTRYI6b-7DPKi32MtByVhxgIokLAguhf7fw__K8o3g=s68-c-k-c0x00ffffff-no-rj
                        title: AI Revolution
                      description: "AI-powered humanoid robots are rapidly advancing, with the Phantom MK1 making its first public appearance in a nightclub\_..."
                      id: yrGKgdxnsHA
                      length: '9:48'
                      link: https://www.youtube.com/watch?v=yrGKgdxnsHA
                      position: 1
                      published_time: 2 days ago
                      thumbnail:
                        rich: >-
                          https://i.ytimg.com/vi/yrGKgdxnsHA/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLALbhxknt2JnWP6RkVAPkmhcsaMgg
                        static: >-
                          https://i.ytimg.com/vi/yrGKgdxnsHA/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCWOsAcglqmbAjzlT2L0rzUmJ6w8Q
                      title: The First AI Humanoid Soldier SHOCKED The Internet!
                      views: 35861
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