# Source: https://docs.agent.ai/api-reference/get-data/web-page-content.md

# Web Page Content

> Extract text content from a specified web page or domain.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/grab_web_text
paths:
  path: /action/grab_web_text
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
              url:
                allOf:
                  - type: string
                    format: url
                    description: URL of the web page to extract text from.
                    example: https://agent.ai
              mode:
                allOf:
                  - type: string
                    enum:
                      - scrape
                      - crawl
                    default: scrape
                    description: >-
                      Crawler mode: 'scrape' for one page, 'crawl' for up to 100
                      pages.
                    example: scrape
            required: true
            requiredProperties:
              - url
        examples:
          example:
            value:
              url: https://agent.ai
              mode: scrape
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
              metadata:
                allOf:
                  - type: object
                    description: Web page metadata from the action
              response:
                allOf:
                  - type: string
                    description: Text content extracted from the web page
            refIdentifier: '#/components/schemas/GrabWebTextResponse'
        examples:
          example:
            value:
              status: 200
              metadata:
                description: Get things done with the help of AI agents
                favicon: https://agent.ai/agent.ai-gear/favicon/favicon.ico
                language: en
                next-head-count: '20'
                og:description: Get things done with the help of AI agents
                og:image: https://agent.ai/agent.ai-gear/for-website.jpg
                og:title: agent.ai | The Professional Network for AI Agents
                og:type: website
                og:url: https://agent.ai
                ogDescription: Get things done with the help of AI agents
                ogImage: https://agent.ai/agent.ai-gear/for-website.jpg
                ogTitle: agent.ai | The Professional Network for AI Agents
                ogUrl: https://agent.ai
                scrapeId: b189d32c-bf1d-4be4-b7a7-883c8d609d6a
                sourceURL: https://agent.ai
                statusCode: 200
                title: agent.ai | The Professional Network for AI Agents
                twitter:card: summary_large_image
                twitter:description: Get things done with the help of AI agents
                twitter:domain: agent.ai
                twitter:image: https://agent.ai/agent.ai-gear/for-website.jpg
                twitter:title: agent.ai | The Professional Network for AI Agents
                twitter:url: https://agent.ai
                url: https://agent.ai/
                viewport: width=device-width, initial-scale=1
              response: >-
                Metadata: {"twitter:title": "agent.ai | The Professional Network
                for AI Agents", "ogUrl": "https://agent.ai", "ogDescription":
                "Get things done with the help of AI agents", "og:description":
                "Get things done with the help of AI agents", "ogTitle":
                "agent.ai | The Professional Network for AI Agents", ...
        description: Text content extracted from the web page
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_0
                    type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - &ref_1
                    type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 400
              response: null
              error: >-
                Unexpected error during scrape URL: Status code 400. Bad Request
                - [{'validation': 'url', 'code': 'invalid_string', 'message':
                'Invalid url', 'path': ['url']}, {'code': 'custom', 'message':
                'URL must have a valid top-level domain or be a valid path',
                'path': ['url']}, {'code': 'custom', 'message': 'Invalid URL',
                'path': ['url']}]
        description: Text content extracted from the web page
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_0
              response:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 500
              response: null
              error: Failed to extract text from the web page.
        description: Text content extracted from the web page
  deprecated: false
  type: path
components:
  schemas: {}

````