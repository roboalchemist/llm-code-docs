# Source: https://docs.agent.ai/api-reference/get-data/google-news-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Google News Data

> Fetch news articles based on queries and date ranges to stay updated on relevant topics or trends.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_google_news
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
  /action/get_google_news:
    post:
      tags:
        - Get Data
      summary: Google News Data
      description: >-
        Fetch news articles based on queries and date ranges to stay updated on
        relevant topics or trends.
      operationId: getGoogleNews
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: Search terms to find news articles.
                  example: AI advancements
                date_range:
                  type: string
                  enum:
                    - 24h
                    - 7d
                    - 30d
                  default: 24h
                  description: Timeframe for news articles.
              required:
                - query
                - date_range
      responses:
        '200':
          description: Retrieved Twitter user profiles
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  organic_results:
                    - date: 3 hours ago
                      favicon: >-
                        data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAA21BMVEVHcEzs5uv12rr09uTh0d2w4cDx+PmJ1J7H3Z3////uoaOS06TQ467yxaXH3aTz/fzEs9byzc3d5sZ50pL258fC2pj52JP546rzyrH1w6r//f/0wZyGxE37vSHzhiMHsEHtLimaTqIbsUmaRp2xicBwyYrrQ0Y3wV7sOTei0Xj00oXuWlmsu8L6wTH47vL9yEz12sXzgRHthIj3vH+z1oulZ6zqcHbGn8+lvLinVKydzGaAwkf/y2XP2ZHbj5/Be6rz36f2lU6opaPvqav3x6TzqHe5foPYt7j5tWsGVJ14AAAAHHRSTlMAVJGkdYw6paQQs72ZpdhFnLeBpIGkwpOn4WTlS2+lhgAAAJdJREFUGJWdj8UOwkAABZeWli3u2rW6K67F+f8vohAS7p3bzOElD4CCcA1JrJb/PsZ4tqRG6af90QTj1LBop/1NHEIOxjfXcjV10crDEPn+PY4SemRM/exM9wilcXSlGlNXEgDdre2g8Hx5JGyzNnURzGVZPoQv73nSdKKQGmjmYWdnQeCZRFGIAKQ6hHAAeb5XyRGK3HoDPCIQ0lJQeO8AAAAASUVORK5CYII=
                      link: >-
                        https://pune.news/market/ibm-positioned-for-growth-amid-ai-advancements-oppenheimer-reports-304984/
                      position: 1
                      snippet: >-
                        Oppenheimer Predicts Significant Upside for IBM Stock.
                        Oppenheimer analysts believe that International Business
                        Machines (IBM) may be...
                      source: pune.news
                      thumbnail: >-
                        data:image/jpeg;base64,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
                      title: >-
                        IBM Positioned for Growth Amid AI Advancements,
                        Oppenheimer Reports
                    - date: 1 day ago
                      favicon: >-
                        data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAA21BMVEVHcEzs5uv12rr09uTh0d2w4cDx+PmJ1J7H3Z3////uoaOS06TQ467yxaXH3aTz/fzEs9byzc3d5sZ50pL258fC2pj52JP546rzyrH1w6r//f/0wZyGxE37vSHzhiMHsEHtLimaTqIbsUmaRp2xicBwyYrrQ0Y3wV7sOTei0Xj00oXuWlmsu8L6wTH47vL9yEz12sXzgRHthIj3vH+z1oulZ6zqcHbGn8+lvLinVKydzGaAwkf/y2XP2ZHbj5/Be6rz36f2lU6opaPvqav3x6TzqHe5foPYt7j5tWsGVJ14AAAAHHRSTlMAVJGkdYw6paQQs72ZpdhFnLeBpIGkwpOn4WTlS2+lhgAAAJdJREFUGJWdj8UOwkAABZeWli3u2rW6K67F+f8vohAS7p3bzOElD4CCcA1JrJb/PsZ4tqRG6af90QTj1LBop/1NHEIOxjfXcjV10crDEPn+PY4SemRM/exM9wilcXSlGlNXEgDdre2g8Hx5JGyzNnURzGVZPoQv73nSdKKQGmjmYWdnQeCZRFGIAKQ6hHAAeb5XyRGK3HoDPCIQ0lJQeO8AAAAASUVORK5CYII=
                      link: >-
                        https://pune.news/apps-and-software/one-ui-and-android-experts-discuss-ai-advancements-in-samsung-galaxy-s25-303920/
                      position: 2
                      snippet: >-
                        One UI, Android Experts Discuss S25's Galaxy AI and
                        Gemini Upgrades. At the Galaxy AI Future Lab in the
                        Philippines, One UI and Android...
                      source: pune.news
                      thumbnail: >-
                        data:image/jpeg;base64,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
                      title: >-
                        One UI and Android Experts Discuss AI Advancements in
                        Samsung Galaxy S25
                    - date: 3 weeks ago
                      favicon: >-
                        data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACLUlEQVQ4jYVSS2hTURA9d1760lfFgJuqqPEbcKO1YqupiFKR+lmIIsVKBV2I0oXdia6t6ErxU82iO5eiUEHqp6JBF1mUuCg1saltKiimaonQT146My5MYppGc2C4F+7MmXvmDFACEaln5hAzDzOzm4uPzHxfVetK8wtQ1Rpm7tEKYOaQiDj5OpMvFpFnRLRLXRezTx5itr8PnByFssDjXwNvcwucI60wtg0RCRtjWohoxgAAM/cQ0RmZ+Ib0pU7MjY2U/aW9rRG+67fzUkOWZZ0zIlJvjBlQ18Xk+XZwchTGtuEca4PdEASI4EbeIfPmJXxdN2CtXF3MuRXMHFJVzUZv6fejjZrav0PdwfflxJebRzeYeVhVdS6yXTO9NTr9oKPSHIsJYh4AfgDQqSFQTRZVwUPzdDdfnVowi50bLVw5Xg0Aa6nIx/nnf+DO/b0TgDEAmPauwy8sRu+X2Lzk/suLCrFnkwcAsMxn8s+fCMArAEgsbcfJn0Fci0cQnRha0DX+VfA2/qd1w3pPgd/k1jPqchanXlzESHocNlWhNXAQTcvrQYYwkBrE4+gkZj63IlBr495pB8YAqrolv0ghIjqbmv6BC+EuJNLjZbVv8Dbh5t5O1PoMRKTbsqwOAwAi4qhqHxHtdiWLR4nneJoMYyQ9DijgX7IC+1YFcSJwGI7HCxF5TUQHjDGzBXYRcfJLVcH7u6pa/U+LVLWOmbuZOcbMmVx8YOY7IrK5NP83npmzQvMZEV8AAAAASUVORK5CYII=
                      link: >-
                        https://blog.google/technology/ai/2024-ai-extraordinary-progress-advancement/
                      position: 3
                      snippet: >-
                        As we move into 2025, we're looking back at the
                        astonishing progress in AI in 2024.
                      source: Google Blog
                      thumbnail: >-
                        data:image/jpeg;base64,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
                      title: >-
                        2024: A year of extraordinary progress and advancement
                        in AI
                  pagination:
                    current: 1
                    next: >-
                      https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=10&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8NMDegQIBBAW
                    other_pages:
                      '2': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=10&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAE
                      '3': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=20&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAG
                      '4': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=30&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAI
                      '5': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=40&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAK
                      '6': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=50&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAM
                      '7': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=60&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAO
                      '8': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=70&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAQ
                      '9': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=80&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAS
                      '10': >-
                        https://www.google.com/search?q=AI+advancements&sca_esv=98cf8f3b668dc52c&gl=us&hl=en&tbm=nws&ei=UdqrZ4u0CejH4-EP9Lyf8Qo&start=90&sa=N&ved=2ahUKEwjLoIOg4LyLAxXo4zgGHXTeJ64Q8tMDegQIBBAU
                  search_information:
                    detected_location: Boston, Massachusetts
                    query_displayed: AI advancements
                    time_taken_displayed: 0.34
                    total_results: 102000
                  search_parameters:
                    device: desktop
                    engine: google_news
                    gl: us
                    google_domain: google.com
                    hl: en
                    location: Boston
                    location_used: Boston,Massachusetts,United States
                    q: AI advancements
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