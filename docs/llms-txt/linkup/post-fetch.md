# Source: https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-fetch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# /fetch

> The `/fetch` endpoint allows you to fetch a single webpage from a given URL.

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

The **`/fetch`** endpoint retrieves a markdown representation of a webpage at the given URL, with the ability to render the Javascript or not.


## OpenAPI

````yaml https://api.linkup.so/v1/openapi.json post /v1/fetch
openapi: 3.0.0
info:
  title: Linkup API
  description: >-
    Search the web in real time to get trustworthy, source-backed answers. Find
    the latest news and comprehensive results from the most relevant sources.
    Use natural language queries to quickly gather facts, citations, and
    context.
  version: '1.0'
  contact: {}
servers:
  - url: https://api.linkup.so
security: []
tags: []
paths:
  /v1/fetch:
    post:
      tags:
        - Fetch
      summary: /fetch
      description: >-
        The `/fetch` endpoint allows you to fetch a single webpage from a given
        URL.
      operationId: fetch
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FetchDto'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FetchResponseDto'
        '400':
          description: Bad Request - Invalid parameters
        '401':
          description: Unauthorized - Invalid or missing API key
        '429':
          description: Too Many Requests - Rate limit exceeded or insufficient credits
      security:
        - bearer: []
components:
  schemas:
    FetchDto:
      type: object
      properties:
        url:
          type: string
          description: The URL of the webpage you want to fetch.
          example: https://docs.linkup.so
          format: uri
        renderJs:
          type: boolean
          default: false
          description: Defines whether the API should render the JavaScript of the webpage.
          example: false
        includeRawHtml:
          type: boolean
          default: false
          description: >-
            Defines whether the API should include the raw HTML of the webpage
            in its response.
          example: false
        extractImages:
          type: boolean
          default: false
          description: >-
            Defines whether the API should extract the images from the webpage
            in its response.
          example: false
      required:
        - url
    FetchResponseDto:
      type: object
      properties:
        markdown:
          type: string
          description: The clean markdown version of the webpage.
          example: Get started for free, no credit card required...
        rawHtml:
          type: string
          description: The raw HTML version of the webpage.
          example: >-
            <!DOCTYPE html><html
            lang="en"><head>...</head><body>...</body></html>
        images:
          description: List of images extracted from the webpage.
          example:
            - alt: Image 1
              url: https://example.com/image.jpg
            - alt: Image 2
              url: https://example.com/image2.jpg
          type: array
          items:
            $ref: '#/components/schemas/FetchImageDto'
      required:
        - markdown
    FetchImageDto:
      type: object
      properties:
        url:
          type: string
          description: The URL of the image.
          example: https://example.com/image.jpg
        alt:
          type: string
          description: The alt text of the image.
          example: Image description
      required:
        - url
  securitySchemes:
    bearer:
      scheme: bearer
      bearerFormat: JWT
      type: http

````

Built with [Mintlify](https://mintlify.com).