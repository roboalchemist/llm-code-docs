# Source: https://www.mintlify.com/docs/optimize/feedback.md

# Source: https://www.mintlify.com/docs/api/analytics/feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user feedback

> Returns paginated user feedback with optional filtering

## Usage

Use this endpoint to export user feedback collected from your documentation. Feedback includes contextual feedback from page ratings and code snippet feedback.

Paginate through results using the `cursor` parameter returned in the response. Continue fetching while `hasMore` is `true`.

## Filtering

Filter feedback by:

* **Date range**: Use `dateFrom` and `dateTo` to limit results to a specific time period
* **Source**: Filter by `code_snippet` or `contextual` feedback types
* **Status**: Filter by status values like `pending`, `in_progress`, `resolved`, or `dismissed`

## Response types

The response contains different feedback types based on the source:

* **Contextual feedback**: Includes `helpful` boolean and optional `contact` email
* **Code snippet feedback**: Includes `code`, `filename`, and `lang` fields


## OpenAPI

````yaml analytics.openapi.json get /api/external/v1/analytics/{projectId}/feedback
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
  /api/external/v1/analytics/{projectId}/feedback:
    get:
      tags:
        - Analytics
      summary: Get user feedback
      description: Returns paginated user feedback with optional filtering
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
            type: string
            enum:
              - code_snippet
              - contextual
            description: Filter by feedback source
          required: false
          name: source
          in: query
        - schema:
            type: string
            description: Comma-separated list of statuses to filter by
          required: false
          name: status
          in: query
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 50
            description: Max results per page
          required: false
          name: limit
          in: query
        - schema:
            type: string
            description: Pagination cursor
          required: false
          name: cursor
          in: query
      responses:
        '200':
          description: Feedback data with pagination
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FeedbackResponse'
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
    FeedbackResponse:
      type: object
      properties:
        feedback:
          type: array
          description: List of feedback entries.
          items:
            anyOf:
              - type: object
                properties:
                  id:
                    type: string
                    description: Unique feedback identifier.
                  path:
                    type: string
                    description: The path or URL to the source document.
                  comment:
                    type:
                      - string
                      - 'null'
                    description: Text of the user's feedback comment.
                  createdAt:
                    type:
                      - string
                      - 'null'
                    description: Timestamp when the feedback was submitted.
                  source:
                    type: string
                    enum:
                      - code_snippet
                      - contextual
                    description: >-
                      Where the feedback originated. `code_snippet` is feedback
                      on a code block, `contextual` is page-level feedback.
                  status:
                    type: string
                    enum:
                      - pending
                      - in_progress
                      - resolved
                      - dismissed
                    description: Current review status of the feedback.
                required:
                  - id
                  - path
                  - comment
                  - createdAt
                  - source
                  - status
              - type: object
                properties:
                  id:
                    type: string
                    description: Unique feedback identifier.
                  path:
                    type: string
                    description: The path or URL to the source document.
                  comment:
                    type:
                      - string
                      - 'null'
                    description: Text of the user's feedback comment.
                  createdAt:
                    type:
                      - string
                      - 'null'
                    description: Timestamp when the feedback was submitted.
                  source:
                    type: string
                    enum:
                      - code_snippet
                      - contextual
                    description: >-
                      Where the feedback originated. `code_snippet` is feedback
                      on a code block, `contextual` is page-level feedback.
                  status:
                    type: string
                    enum:
                      - pending
                      - in_progress
                      - resolved
                      - dismissed
                    description: Current review status of the feedback.
                  helpful:
                    type: boolean
                    description: Whether the user found the content helpful.
                  contact:
                    type:
                      - string
                      - 'null'
                    description: Email address the user provided for follow-up.
                required:
                  - id
                  - path
                  - comment
                  - createdAt
                  - source
                  - status
                  - helpful
                  - contact
              - type: object
                properties:
                  id:
                    type: string
                    description: Unique feedback identifier.
                  path:
                    type: string
                    description: The path or URL to the source document.
                  comment:
                    type:
                      - string
                      - 'null'
                    description: Text of the user's feedback comment.
                  createdAt:
                    type:
                      - string
                      - 'null'
                    description: Timestamp when the feedback was submitted.
                  source:
                    type: string
                    enum:
                      - code_snippet
                      - contextual
                    description: >-
                      Where the feedback originated. `code_snippet` is feedback
                      on a code block, `contextual` is page-level feedback.
                  status:
                    type: string
                    enum:
                      - pending
                      - in_progress
                      - resolved
                      - dismissed
                    description: Current review status of the feedback.
                  code:
                    type: string
                    description: The code snippet the feedback relates to.
                  filename:
                    type:
                      - string
                      - 'null'
                    description: Filename associated with the code snippet.
                  lang:
                    type:
                      - string
                      - 'null'
                    description: Programming language of the code snippet.
                required:
                  - id
                  - path
                  - comment
                  - createdAt
                  - source
                  - status
                  - code
                  - filename
                  - lang
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
        - feedback
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