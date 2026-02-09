# Source: https://docs.agent.ai/api-reference/get-data/web-page-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Page Content

> Extract text content from a specified web page or domain.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/grab_web_text
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
  /action/grab_web_text:
    post:
      tags:
        - Get Data
      summary: Web Page Content
      description: Extract text content from a specified web page or domain.
      operationId: grabWebText
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
                  description: URL of the web page to extract text from.
                  example: https://agent.ai
                mode:
                  type: string
                  enum:
                    - scrape
                    - crawl
                  default: scrape
                  description: >-
                    Crawler mode: 'scrape' for one page, 'crawl' for up to 100
                    pages.
                  example: scrape
              required:
                - url
      responses:
        '200':
          description: Text content extracted from the web page
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GrabWebTextResponse'
              example:
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
                  Metadata: {"twitter:title": "agent.ai | The Professional
                  Network for AI Agents", "ogUrl": "https://agent.ai",
                  "ogDescription": "Get things done with the help of AI agents",
                  "og:description": "Get things done with the help of AI
                  agents", "ogTitle": "agent.ai | The Professional Network for
                  AI Agents", ...
        '400':
          description: Text content extracted from the web page
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 400
                response: null
                error: >-
                  Unexpected error during scrape URL: Status code 400. Bad
                  Request - [{'validation': 'url', 'code': 'invalid_string',
                  'message': 'Invalid url', 'path': ['url']}, {'code': 'custom',
                  'message': 'URL must have a valid top-level domain or be a
                  valid path', 'path': ['url']}, {'code': 'custom', 'message':
                  'Invalid URL', 'path': ['url']}]
        '500':
          description: Text content extracted from the web page
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 500
                response: null
                error: Failed to extract text from the web page.
components:
  schemas:
    GrabWebTextResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        metadata:
          type: object
          description: Web page metadata from the action
        response:
          type: string
          description: Text content extracted from the web page
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