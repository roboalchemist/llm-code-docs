# Source: https://www.mintlify.com/docs/api/analytics/assistant-conversations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get assistant conversations

> Returns paginated AI assistant conversation history

## Usage

Use this endpoint to export AI assistant conversation history from your documentation. Each conversation includes the user query, assistant response, sources cited, and query category.

Paginate through results using the `cursor` parameter returned in the response. Continue fetching while `hasMore` is `true`.

## Filtering

Filter conversations by date range using `dateFrom` and `dateTo` parameters.

## Conversation data

Each conversation includes:

* **query**: The user's question
* **response**: The assistant's answer
* **sources**: Pages referenced in the response, with title and URL
* **queryCategory**: Classification of the query type (if available)


## OpenAPI

````yaml analytics.openapi.json get /api/external/v1/analytics/{projectId}/assistant
openapi: 3.1.0
info:
  title: Mintlify Analytics Export API
  version: 1.0.0
  description: API for exporting documentation analytics data
servers:
  - url: https://api.mintlify.com
    description: Production
security: []
paths:
  /api/external/v1/analytics/{projectId}/assistant:
    get:
      tags:
        - Analytics
      summary: Get assistant conversations
      description: Returns paginated AI assistant conversation history
      parameters:
        - $ref: '#/components/parameters/projectId'
        - schema:
            type: string
            description: Date in ISO 8601 or YYYY-MM-DD format
            example: '2024-01-01'
          required: false
          name: dateFrom
          in: query
        - schema:
            type: string
            description: Date in ISO 8601 or YYYY-MM-DD format
            example: '2024-01-01'
          required: false
          name: dateTo
          in: query
        - schema:
            type: number
            minimum: 1
            maximum: 1000
            default: 100
            description: Max results per page
          required: false
          name: limit
          in: query
        - schema:
            type: string
            format: ulid
            description: Pagination cursor (ULID format)
          required: false
          name: cursor
          in: query
      responses:
        '200':
          description: Conversation data with pagination
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssistantConversationsResponse'
        '400':
          description: Invalid query parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnalyticsErrorResponse'
        '500':
          description: Server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnalyticsErrorResponse'
      security:
        - bearerAuth: []
components:
  parameters:
    projectId:
      schema:
        $ref: '#/components/schemas/projectId'
      required: true
      name: projectId
      in: path
  schemas:
    AssistantConversationsResponse:
      type: object
      properties:
        conversations:
          type: array
          description: List of assistant conversations.
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique conversation identifier.
              timestamp:
                type: string
                description: Timestamp when the conversation occurred.
              query:
                type: string
                description: The user's question to the assistant.
              response:
                type: string
                description: The assistant's response.
              sources:
                type: array
                description: Documentation pages referenced in the response.
                items:
                  type: object
                  properties:
                    title:
                      type: string
                      description: Title of the referenced documentation page.
                    url:
                      type: string
                      description: URL of the referenced documentation page.
                  required:
                    - title
                    - url
              queryCategory:
                type:
                  - string
                  - 'null'
                description: >-
                  Auto-assigned category grouping for the conversation, if
                  applicable.
            required:
              - id
              - timestamp
              - query
              - response
              - sources
              - queryCategory
        nextCursor:
          type:
            - string
            - 'null'
          description: >-
            Cursor to retrieve the next page of results. Null if no more
            results.
        hasMore:
          type: boolean
          description: Whether additional results are available beyond this page.
      required:
        - conversations
        - nextCursor
        - hasMore
    AnalyticsErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Error message describing what went wrong.
        details:
          type: array
          description: Additional details about the error.
          items:
            type: object
            properties:
              message:
                type: string
                description: Description of a specific validation or processing error.
            required:
              - message
      required:
        - error
    projectId:
      type: string
      description: >-
        Your project ID. Can be copied from the [API
        keys](https://dashboard.mintlify.com/settings/organization/api-keys)
        page in your dashboard.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        The Authorization header expects a Bearer token. Use an admin API key
        (prefixed with `mint_`). This is a server-side secret key. Generate one
        on the [API keys
        page](https://dashboard.mintlify.com/settings/organization/api-keys) in
        your dashboard.

````