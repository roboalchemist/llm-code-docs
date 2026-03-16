# Source: https://docs.rootly.com/api-reference/alertroutes/list-alert-routes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List alert routes

> List all alert routes for the current team with filtering and pagination. **Note: This endpoint requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly customer support.**



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/alert_routes
openapi: 3.0.1
info:
  title: Rootly API v1
  version: v1
  description: >+
    # How to generate an API Key?

    - **Organization dropdown** > **Organization Settings** > **API Keys**


    # JSON:API Specification

    Rootly is using **JSON:API** (https://jsonapi.org) specification:

    - JSON:API is a specification for how a client should request that resources
    be fetched or modified, and how a server should respond to those requests.

    - JSON:API is designed to minimize both the number of requests and the
    amount of data transmitted between clients and servers. This efficiency is
    achieved without compromising readability, flexibility, or discoverability.

    - JSON:API requires use of the JSON:API media type
    (**application/vnd.api+json**) for exchanging data.


    # Authentication and Requests

    We use standard HTTP Authentication over HTTPS to authorize your requests.

    ```
      curl --request GET \
    --header 'Content-Type: application/vnd.api+json' \

    --header 'Authorization: Bearer YOUR-TOKEN' \

    --url https://api.rootly.com/v1/incidents

    ```


    <br/>


    # Rate limiting

    - There is a default limit of **5** **GET**, **HEAD**, and **OPTIONS** calls
    **per API key** every **60 seconds** (0 hours). The limit is calculated over
    a **0-hour sliding window** looking back from the current time. While the
    limit can be configured to support higher thresholds, you must first contact
    your **Rootly Customer Success Manager** to make any adjustments.

    - There is a default limit of **3** **POST**, **PUT**, **PATCH** or
    **DELETE** calls **per API key** every **60 seconds** (0 hours). The limit
    is calculated over a **0-hour sliding window** looking back from the current
    time. While the limit can be configured to support higher thresholds, you
    must first contact your **Rootly Customer Success Manager** to make any
    adjustments.

    - When rate limits are exceeded, the API will return a **429 Too Many
    Requests** HTTP status code with the response: `{"error": "Rate limit
    exceeded. Try again later."}`

    - **X-RateLimit headers** are included in every API response, providing
    real-time rate limit information:
      - **X-RateLimit-Limit** - The maximum number of requests permitted and the time window (e.g., "1000, 1000;window=3600" for 1000 requests per hour)
      - **X-RateLimit-Remaining** - The number of requests remaining in the current rate limit window
      - **X-RateLimit-Used** - The number of requests already made in the current window
      - **X-RateLimit-Reset** - The time at which the current rate limit window resets, in UTC epoch seconds

    # Pagination

    - Pagination is supported for all endpoints that return a collection of
    items.

    - Pagination is controlled by the **page** query parameter


    ## Example

    ```
      curl --request GET \
    --header 'Content-Type: application/vnd.api+json' \

    --header 'Authorization: Bearer YOUR-TOKEN' \

    --url https://api.rootly.com/v1/incidents?page[number]=1&page[size]=10

    ```

  x-logo:
    url: https://rootly-heroku.s3.us-east-1.amazonaws.com/swagger/v1/logo.png
servers:
  - url: https://api.rootly.com
security: []
paths:
  /v1/alert_routes:
    get:
      tags:
        - AlertRoutes
      summary: List alert routes
      description: >-
        List all alert routes for the current team with filtering and
        pagination. **Note: This endpoint requires access to Advanced Alert
        Routing. If you're unsure whether you have access to this feature,
        please contact Rootly customer support.**
      operationId: listAlertRoutes
      parameters:
        - name: page[number]
          in: query
          required: false
          schema:
            type: integer
        - name: page[size]
          in: query
          required: false
          schema:
            type: integer
        - name: filter[search]
          in: query
          required: false
          schema:
            type: string
        - name: filter[name]
          in: query
          required: false
          schema:
            type: string
        - name: sort
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: alert routes filtered by search
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/alert_route_list'
        '401':
          description: unauthorized
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    alert_route_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the alert route
              type:
                type: string
                enum:
                  - alert_routes
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/alert_route'
            required:
              - id
              - type
              - attributes
        links:
          type: object
          allOf:
            - $ref: '#/components/schemas/links'
        meta:
          type: object
          allOf:
            - $ref: '#/components/schemas/meta'
      required:
        - data
        - links
        - meta
    errors_list:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              title:
                type: string
              status:
                type: string
              code:
                type: string
                nullable: true
              detail:
                type: string
                nullable: true
            required:
              - title
              - status
    alert_route:
      type: object
      properties:
        name:
          type: string
          description: The name of the alert route
        enabled:
          type: boolean
          description: Whether the alert route is enabled
        alerts_source_ids:
          type: array
          items:
            type: string
            format: uuid
            description: The ID of the alerts source
        owning_team_ids:
          type: array
          items:
            type: string
            format: uuid
            description: The ID of the owning team
        rules:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the alert routing rule
              position:
                type: integer
                description: The position of the alert routing rule for ordering evaluation
              fallback_rule:
                type: boolean
                description: Whether this is a fallback rule
                default: false
              destinations:
                type: array
                items:
                  type: object
                  properties:
                    target_type:
                      type: string
                      enum:
                        - Service
                        - Group
                        - Functionality
                        - EscalationPolicy
                      description: The type of the target
                    target_id:
                      type: string
                      format: uuid
                      description: The ID of the target
                  required:
                    - target_type
                    - target_id
              condition_groups:
                type: array
                items:
                  type: object
                  properties:
                    position:
                      type: integer
                      description: The position of the condition group
                    conditions:
                      type: array
                      items:
                        type: object
                        properties:
                          property_field_condition_type:
                            type: string
                            enum:
                              - is_one_of
                              - is_not_one_of
                              - contains
                              - does_not_contain
                              - starts_with
                              - ends_with
                              - matches_regex
                              - is_empty
                          property_field_name:
                            type: string
                            description: The name of the property field
                          property_field_type:
                            type: string
                            enum:
                              - attribute
                              - payload
                              - alert_field
                          property_field_value:
                            type: string
                            description: The value of the property field
                            nullable: true
                          property_field_values:
                            type: array
                            items:
                              type: string
                            nullable: true
                          alert_urgency_ids:
                            type: array
                            description: The Alert Urgency IDs to check in the condition
                            items:
                              type: string
                            nullable: true
                          conditionable_type:
                            type: string
                            description: The type of the conditionable
                            enum:
                              - AlertField
                            nullable: true
                          conditionable_id:
                            type: string
                            format: uuid
                            description: The ID of the conditionable
                            nullable: true
                        required:
                          - property_field_condition_type
                          - property_field_type
                  required:
                    - conditions
            required:
              - name
              - destinations
              - condition_groups
      required:
        - name
        - alerts_source_ids
    links:
      type: object
      properties:
        self:
          type: string
        first:
          type: string
        prev:
          type: string
          nullable: true
        next:
          type: string
          nullable: true
        last:
          type: string
      required:
        - self
        - first
        - prev
        - next
        - last
    meta:
      type: object
      properties:
        current_page:
          type: integer
        next_page:
          type: integer
          nullable: true
        prev_page:
          type: integer
          nullable: true
        total_count:
          type: integer
        total_pages:
          type: integer
      required:
        - current_page
        - next_page
        - prev_page
        - total_count
        - total_pages
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).