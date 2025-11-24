# Source: https://docs.agent.ai/api-reference/get-data/search-results.md

# Search Results

> Fetch search results from Google or YouTube for specific queries, providing valuable insights and content.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_search_results
paths:
  path: /action/get_search_results
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
              search_engine:
                allOf:
                  - type: string
                    enum:
                      - google
                      - youtube
                      - youtube_channel
                    default: google
                    description: Search engine to use.
              query:
                allOf:
                  - type: string
                    description: Search terms to find specific results.
                    example: best AI tools
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
                    description: Number of results to return.
            required: true
            requiredProperties:
              - search_engine
              - query
              - num_posts
        examples:
          example:
            value:
              search_engine: google
              query: best AI tools
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
                organic_results:
                  - date: Oct 2, 2024
                    displayed_link: https://zapier.com › App picks › Best apps
                    domain: zapier.com
                    favicon: >-
                      data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAclBMVEX/TwD/SQD/RQD/oon/xrX/SwD/PQD/QgD/hWP/Yiv/9/H/8en/uaT/iGj///r/nIH/yrz/0cP/ppD/6eD/28//NgD/rZX/Ug3/cUj/lHb/////gmD/elH/mHv/sZ7/wrH/39X/jm7/az3/KgD/z8D/ZzdopBX/AAAAp0lEQVR4Ae3LhQ3EMBBE0fWanTjMjP2XGBIdpoJ8aURPAz96InhjlL0pF0IgOSelkIqikBIE4mXaOI5rPc+3QeipKIDYS9I4Cy7Ni7JSddN6tipY3CX9AGY0oSUnYu1N8zIkxnpzabpkGbps8pQ8jU/VsNCKLcdzMUs3WC8yuhrJhZrSaCxc3ZamcaEZhepH4a8cLkVEwpHLmgnknADBYxze4xKevtoBMjsJ9axv3/4AAAAASUVORK5CYII=
                    link: https://zapier.com/blog/best-ai-productivity-tools/
                    position: 1
                    sitelinks:
                      inline:
                        - link: https://zapier.com/blog/free-ai-tools/
                          title: The best free AI tools
                        - link: https://zapier.com/blog/best-ai-chatbot/
                          title: The best AI chatbots
                        - link: https://zapier.com/blog/best-ai-search-engine/
                          title: The best AI search engines
                        - link: https://zapier.com/blog/all-articles/best-apps/
                          title: Best apps
                    snippet: >-
                      The best AI productivity tools by category · Chatbots
                      (ChatGPT, Claude, Meta AI, Zapier Agents) · Search engines
                      (Perplexity, Google AI ...
                    snippet_highlighted_words:
                      - best AI
                      - tools
                      - AI
                      - AI
                    source: Zapier
                    title: The best AI productivity tools in 2025
                pagination:
                  current: 1
                  next: >-
                    https://www.google.com/search?q=best+AI+tools&oq=best+AI+tools&gl=us&hl=en&start=1&num=1&ie=UTF-8
                related_searches:
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Best+AI+tools+free&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgbEAE
                    query: Best AI tools free
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Chatgpt&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgaEAE
                    query: Chatgpt
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Best+AI+tools+for+students&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgYEAE
                    query: Best AI tools for students
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Best+AI+tools+like+ChatGPT&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgZEAE
                    query: Best AI tools like ChatGPT
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Free+AI+tools+list&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgXEAE
                    query: Free AI tools list
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Best+AI+tools+for+business&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgWEAE
                    query: Best AI tools for business
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Free+AI+tools+online&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgVEAE
                    query: Free AI tools online
                  - link: >-
                      https://www.google.com/search?num=1&sca_esv=98cf8f3b668dc52c&hl=en&gl=us&q=Perplexity+AI&sa=X&ved=2ahUKEwi37IWr4ryLAxUNJNAFHXkRHdkQ1QJ6BAgcEAE
                    query: Perplexity AI
                search_information:
                  detected_location: United States
                  query_displayed: best AI tools
                  time_taken_displayed: 0.28
                  total_results: 4070000000
                search_parameters:
                  device: desktop
                  engine: google
                  gl: us
                  google_domain: google.com
                  hl: en
                  num: '1'
                  q: best AI tools
        description: Search results
  deprecated: false
  type: path
components:
  schemas: {}

````