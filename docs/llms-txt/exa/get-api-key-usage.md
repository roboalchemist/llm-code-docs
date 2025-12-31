# Source: https://docs.exa.ai/reference/team-management/get-api-key-usage.md

# Get API Key Usage

> Retrieve usage analytics and billing data for a specific API key.

## OpenAPI

````yaml get /api-keys/{id}/usage
paths:
  path: /api-keys/{id}/usage
  method: get
  servers:
    - url: https://admin-api.exa.ai/team-management
  request:
    security:
      - title: apikey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: Service API key for team authentication
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the API key
              format: uuid
      query:
        start_date:
          schema:
            - type: string
              required: false
              description: >-
                Start date for the usage period (ISO 8601 format). Defaults to
                30 days ago. Must be within the last 100 days.
              format: date-time
        end_date:
          schema:
            - type: string
              required: false
              description: >-
                End date for the usage period (ISO 8601 format). Defaults to
                current time.
              format: date-time
        group_by:
          schema:
            - type: enum<string>
              enum:
                - hour
                - day
                - month
              required: false
              description: >-
                Time granularity for grouping results. Currently reserved for
                future enhancements and does not change the response shape.
                Defaults to 'day'.
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Get usage for the last 30 days (default)
        lang: bash
        source: >
          curl -X GET
          'https://admin-api.exa.ai/team-management/api-keys/{id}/usage' \
            -H 'x-api-key: YOUR-SERVICE-KEY'
      - label: Get usage for a specific date range
        lang: bash
        source: >
          curl -X GET
          'https://admin-api.exa.ai/team-management/api-keys/{id}/usage?start_date=2025-01-01&end_date=2025-01-31'
          \
            -H 'x-api-key: YOUR-SERVICE-KEY'
      - label: Get usage for a specific date range
        lang: python
        source: |
          import requests
          from datetime import datetime, timedelta

          headers = {
              'x-api-key': 'YOUR-SERVICE-KEY'
          }

          params = {
              'start_date': '2025-01-01T00:00:00Z',
              'end_date': '2025-01-31T23:59:59Z'
          }

          response = requests.get(
              'https://admin-api.exa.ai/team-management/api-keys/{id}/usage',
              headers=headers,
              params=params
          )

          print(response.json())
      - label: Get usage for a specific date range
        lang: javascript
        source: |
          const params = new URLSearchParams({
            start_date: '2025-01-01T00:00:00Z',
            end_date: '2025-01-31T23:59:59Z'
          });

          const response = await fetch(
            `https://admin-api.exa.ai/team-management/api-keys/{id}/usage?${params}`,
            {
              method: 'GET',
              headers: {
                'x-api-key': 'YOUR-SERVICE-KEY'
              }
            }
          );

          const result = await response.json();
          console.log(result);
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              api_key_id:
                allOf:
                  - type: string
                    format: uuid
                    description: The API key ID
              api_key_name:
                allOf:
                  - type: string
                    nullable: true
                    description: The name of the API key
              team_id:
                allOf:
                  - type: string
                    format: uuid
                    description: The team ID this key belongs to
              period:
                allOf:
                  - type: object
                    properties:
                      start:
                        type: string
                        format: date-time
                        description: Start of the usage period
                      end:
                        type: string
                        format: date-time
                        description: End of the usage period
              total_cost_usd:
                allOf:
                  - type: number
                    description: Total cost in USD for the period
                    example: 45.67
              cost_breakdown:
                allOf:
                  - type: array
                    description: Breakdown of costs by price type
                    items:
                      type: object
                      properties:
                        price_id:
                          type: string
                          description: Unique identifier for the price
                        price_name:
                          type: string
                          description: >-
                            Name of the price (e.g., "Neural Search", "Content
                            Retrieval")
                        quantity:
                          type: number
                          description: Total quantity consumed
                        amount_usd:
                          type: number
                          description: Cost in USD for this price type
              metadata:
                allOf:
                  - type: object
                    properties:
                      generated_at:
                        type: string
                        format: date-time
                        description: When this report was generated
        examples:
          example:
            value:
              api_key_id: 550e8400-e29b-41d4-a716-446655440000
              api_key_name: Production API Key
              team_id: 660e8400-e29b-41d4-a716-446655440000
              period:
                start: '2025-01-01T00:00:00Z'
                end: '2025-01-31T23:59:59Z'
              total_cost_usd: 45.67
              cost_breakdown:
                - price_id: price_neural_search
                  price_name: Neural Search
                  quantity: 1000
                  amount_usd: 30
                - price_id: price_content_retrieval
                  price_name: Content Retrieval
                  quantity: 500
                  amount_usd: 15.67
              metadata:
                generated_at: '2025-02-01T10:30:00Z'
        description: Usage data retrieved successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    examples:
                      - Invalid API key ID format. Must be a valid UUID.
                      - >-
                        Invalid date format. Use ISO 8601 format (YYYY-MM-DD or
                        YYYY-MM-DDTHH:mm:ss)
                      - start_date must be before end_date
                      - >-
                        Date range too far in the past. start_date must be
                        within the last 100 days.
                      - >-
                        Invalid group_by parameter. Must be one of: hour, day,
                        month
        examples:
          example:
            value:
              error: Invalid API key ID format. Must be a valid UUID.
        description: Bad Request - Invalid parameters
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: Unauthorized
        examples:
          example:
            value:
              error: Unauthorized
        description: Unauthorized - Invalid or missing service key
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: API key not found
        examples:
          example:
            value:
              error: API key not found
        description: Not Found - API key does not exist
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: Failed to fetch usage data. Please try again later.
        examples:
          example:
            value:
              error: Failed to fetch usage data. Please try again later.
        description: Internal Server Error - Failed to fetch usage data
  deprecated: false
  type: path
components:
  schemas: {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt