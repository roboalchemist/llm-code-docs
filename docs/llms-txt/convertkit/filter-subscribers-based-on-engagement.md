# Source: https://developers.kit.com/api-reference/subscribers/filter-subscribers-based-on-engagement.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter subscribers based on engagement



## OpenAPI

````yaml api-reference/v4.json post /v4/subscribers/filter
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/subscribers/filter:
    post:
      tags:
        - Subscribers
      summary: Filter subscribers based on engagement
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SubscriberFilterRequest'
            example:
              all:
                - type: opens
                  count_greater_than: 5
                  after: '2024-01-01'
                  before: '2024-12-31'
                - type: clicks
                  count_greater_than: 2
                  after: '2024-01-01'
                  before: '2024-12-31'
                  any:
                    - type: urls
                      urls:
                        - kit.com
                        - amazon.com
                      matching: contains
                    - type: broadcasts
                      ids:
                        - 1
                        - 2
                        - 3
      responses:
        '200':
          description: Returns a list of subscribers matching the filters
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscribers:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        first_name:
                          type: string
                          nullable: true
                        email_address:
                          type: string
                        created_at:
                          type: string
                        tag_names:
                          type: array
                          items:
                            type: string
                        tag_ids:
                          type: array
                          items:
                            type: string
                      required:
                        - id
                        - first_name
                        - email_address
                        - created_at
                  pagination:
                    type: object
                    properties:
                      has_previous_page:
                        type: boolean
                      has_next_page:
                        type: boolean
                      start_cursor:
                        type: string
                      end_cursor:
                        type: string
                      per_page:
                        type: integer
                      total_count:
                        type: integer
                    required:
                      - has_previous_page
                      - has_next_page
                      - start_cursor
                      - end_cursor
                      - per_page
                required:
                  - subscribers
                  - pagination
              example:
                subscribers:
                  - id: '456'
                    first_name: Jane
                    email_address: jane@example.com
                    created_at: '2024-12-01T15:45:00Z'
                    tag_names:
                      - newsletter
                      - engaged
                    tag_ids:
                      - '123'
                      - '456'
                  - id: '789'
                    first_name: null
                    email_address: anonymous@example.com
                    created_at: '2024-11-15T10:00:00Z'
                    tag_names: []
                    tag_ids: []
                pagination:
                  has_previous_page: false
                  has_next_page: true
                  start_cursor: WzQ1Nl0=
                  end_cursor: Wzc4OV0=
                  per_page: 10
                  total_count: 42
        '401':
          description: Returns a 401 if the token and/or account cannot be authenticated
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - The access token is invalid
      security:
        - API Key: []
        - OAuth2: []
components:
  schemas:
    SubscriberFilterRequest:
      type: object
      description: >-
        Filter subscribers based on engagement and subscription criteria using
        the 'all' array with filter conditions that must all be met (AND logic).
      properties:
        all:
          type: array
          description: Array of filter conditions where ALL must be met (AND logic)
          items:
            $ref: '#/components/schemas/FilterCondition'
      required:
        - all
    FilterCondition:
      type: object
      description: >-
        A filter condition with type and optional parameters. Used within the
        'all' array for complex filtering where multiple conditions must be met.
      properties:
        type:
          type: string
          enum:
            - opens
            - clicks
            - sent
            - delivered
            - subscribed
          description: Type of filter condition
        count_greater_than:
          type: integer
          description: Minimum count (exclusive). Not applicable for 'subscribed' type.
        count_less_than:
          type: integer
          description: Maximum count (exclusive). Not applicable for 'subscribed' type.
        after:
          type: string
          format: date
          description: >-
            Start date (YYYY-MM-DD). For 'subscribed' type, filters by
            subscriber_created_at. For other types, filters by event date.
        before:
          type: string
          format: date
          description: >-
            End date (YYYY-MM-DD). For 'subscribed' type, filters by
            subscriber_created_at. For other types, filters by event date.
        any:
          type: array
          description: >-
            Array of OR conditions for filtering by specific broadcasts or URLs.
            Subscriber activity must match ANY of these conditions. Not
            applicable for 'subscribed' type.
          items:
            oneOf:
              - $ref: '#/components/schemas/BroadcastAnyCondition'
                title: Broadcasts
              - $ref: '#/components/schemas/UrlAnyCondition'
                title: URLs (clicks only)
      required:
        - type
    BroadcastAnyCondition:
      type: object
      description: >-
        Filter by specific broadcast IDs. Subscriber must have interacted with
        ANY of the specified broadcasts.
      properties:
        type:
          type: string
          enum:
            - broadcasts
          description: Must be 'broadcasts'
        ids:
          type: array
          items:
            type: integer
          description: Array of broadcast IDs. Subscriber must match ANY of these.
      required:
        - type
        - ids
    UrlAnyCondition:
      type: object
      description: >-
        Filter by URL patterns. Only applicable for 'clicks' type. Subscriber
        must have clicked ANY of the specified URLs.
      properties:
        type:
          type: string
          enum:
            - urls
          description: Must be 'urls'
        ids:
          type: array
          items:
            type: integer
          description: Array of URL IDs. Subscriber must have clicked ANY of these.
        urls:
          type: array
          items:
            type: string
          description: Array of URL patterns. Subscriber must have clicked ANY of these.
        matching:
          type: string
          enum:
            - exact
            - contains
            - starts_with
            - ends_with
          description: URL matching strategy
          default: exact
      required:
        - type
  securitySchemes:
    API Key:
      description: Authenticate API requests via an API Key
      type: apiKey
      in: header
      name: X-Kit-Api-Key
    OAuth2:
      description: Authenticate API requests via an OAuth token
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://api.kit.com/v4/oauth/authorize
          tokenUrl: https://api.kit.com/v4/oauth/token
          refreshUrl: https://api.kit.com/v4/oauth/token
          scopes:
            read: Read access to Kit API v4
            write: Write access to Kit API v4

````

Built with [Mintlify](https://mintlify.com).