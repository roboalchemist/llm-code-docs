# Source: https://docs.rootly.com/api-reference/oncalls/list-on-calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List on-calls

> List who is currently on-call, with support for filtering by escalation policy, schedule, and user. Returns on-call entries grouped by escalation policy level.



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/oncalls
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
  /v1/oncalls:
    get:
      tags:
        - OnCalls
      summary: List on-calls
      description: >-
        List who is currently on-call, with support for filtering by escalation
        policy, schedule, and user. Returns on-call entries grouped by
        escalation policy level.
      operationId: listOncalls
      parameters:
        - name: include
          in: query
          description: 'comma separated if needed. eg: user,schedule'
          schema:
            type: string
            enum:
              - user
              - schedule
              - escalation_policy
          required: false
        - name: since
          in: query
          description: >-
            Start of time range in ISO-8601 format (e.g., 2025-01-01T00:00:00Z).
            Defaults to current time.
          required: false
          schema:
            type: string
        - name: until
          in: query
          description: >-
            End of time range in ISO-8601 format (e.g., 2025-01-01T00:00:00Z).
            Defaults to 'since' time.
          required: false
          schema:
            type: string
        - name: earliest
          in: query
          description: >-
            When true, returns only the first on-call user per escalation policy
            level
          required: false
          schema:
            type: boolean
        - name: time_zone
          in: query
          description: >-
            Timezone for response times (e.g., America/New_York). Defaults to
            UTC.
          required: false
          schema:
            type: string
        - name: filter[escalation_policy_ids]
          in: query
          schema:
            type: string
          description: Comma-separated escalation policy IDs
          required: false
        - name: filter[schedule_ids]
          in: query
          schema:
            type: string
          description: Comma-separated schedule IDs
          required: false
        - name: filter[user_ids]
          in: query
          schema:
            type: string
          description: Comma-separated user IDs
          required: false
        - name: filter[service_ids]
          in: query
          schema:
            type: string
          description: Comma-separated service IDs
          required: false
        - name: filter[group_ids]
          in: query
          schema:
            type: string
          description: Comma-separated group IDs (teams)
          required: false
      responses:
        '200':
          description: success
        '401':
          description: responds with unauthorized for invalid token
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
        '404':
          description: resource not found when alerting is disabled
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
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
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).