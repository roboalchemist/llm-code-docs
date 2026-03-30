# Source: https://docs.perplexity.ai/api-reference/search-post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search the Web

> Search the web and retrieve relevant web page contents.



## OpenAPI

````yaml post /search
openapi: 3.1.0
info:
  title: Perplexity AI API
  description: Perplexity AI API
  version: 1.0.0
servers:
  - url: https://api.perplexity.ai
    description: Perplexity AI API
security: []
paths:
  /search:
    post:
      summary: Search the Web
      description: Search the web and retrieve relevant web page contents.
      operationId: search_search_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ApiSearchRequest'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiSearchResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
components:
  schemas:
    ApiSearchRequest:
      allOf:
        - properties:
            country:
              description: ISO 3166-1 alpha-2 country code
              maxLength: 2
              minLength: 2
              type: string
            max_results:
              default: 10
              description: Maximum number of results to return
              maximum: 20
              minimum: 1
              type: integer
            max_tokens:
              default: 10000
              description: Maximum tokens for context
              maximum: 1000000
              minimum: 1
              type: integer
            max_tokens_per_page:
              default: 4096
              description: Maximum tokens per page
              maximum: 1000000
              minimum: 1
              type: integer
            query:
              anyOf:
                - type: string
                - items:
                    type: string
                  type: array
              title: Query
              description: Search query (required)
            search_language_filter:
              description: ISO 639-1 language codes (2-character max)
              items:
                maxLength: 2
                minLength: 2
                type: string
              maxItems: 20
              type: array
          required:
            - query
          type: object
        - $ref: '#/components/schemas/SearchDomainFilter'
        - $ref: '#/components/schemas/DateFilters'
      type: object
      title: ApiSearchRequest
    ApiSearchResponse:
      properties:
        results:
          items:
            $ref: '#/components/schemas/ApiSearchPage'
          type: array
          title: Results
        id:
          type: string
          title: Id
        server_time:
          anyOf:
            - type: string
            - type: 'null'
          title: Server Time
      type: object
      required:
        - results
        - id
      title: ApiSearchResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    SearchDomainFilter:
      properties:
        search_domain_filter:
          description: Limit search results to specific domains (max 20)
          items:
            maxLength: 253
            type: string
          maxItems: 20
          type: array
      type: object
      title: SearchDomainFilter
    DateFilters:
      properties:
        last_updated_after_filter:
          $ref: '#/components/schemas/Date'
          description: Return results updated after this date (MM/DD/YYYY)
        last_updated_before_filter:
          $ref: '#/components/schemas/Date'
          description: Return results updated before this date (MM/DD/YYYY)
        search_after_date_filter:
          $ref: '#/components/schemas/Date'
          description: Return results published after this date (MM/DD/YYYY)
        search_before_date_filter:
          $ref: '#/components/schemas/Date'
          description: Return results published before this date (MM/DD/YYYY)
        search_recency_filter:
          $ref: '#/components/schemas/SearchRecencyFilter'
          description: Filter by publication recency (hour/day/week/month/year)
      type: object
      title: DateFilters
    ApiSearchPage:
      description: A single page from search results
      properties:
        title:
          type: string
          title: Title
          description: Title of the page
        url:
          type: string
          title: Url
          description: URL of the page
        snippet:
          type: string
          title: Snippet
          description: Content snippet extracted from the page
        date:
          anyOf:
            - type: string
            - type: 'null'
          title: Date
          description: Publication date of the page
        last_updated:
          anyOf:
            - type: string
            - type: 'null'
          title: Last Updated
          description: Date the page was last updated
      type: object
      required:
        - title
        - url
        - snippet
      title: ApiSearchPage
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    Date:
      description: 'Input: MM/DD/YYYY, Output: YYYY-MM-DD'
      type: string
      title: Date
    SearchRecencyFilter:
      description: Time-based recency filter for search results
      enum:
        - hour
        - day
        - week
        - month
        - year
      type: string
      title: SearchRecencyFilter
  securitySchemes:
    HTTPBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).