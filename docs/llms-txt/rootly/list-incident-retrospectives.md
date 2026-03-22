# Source: https://docs.rootly.com/api-reference/incidentretrospectives/list-incident-retrospectives.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List incident retrospectives

> List incident retrospectives



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/post_mortems
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
  /v1/post_mortems:
    get:
      tags:
        - IncidentRetrospectives
      summary: List incident retrospectives
      description: List incident retrospectives
      operationId: listIncidentPostMortems
      parameters:
        - name: include
          in: query
          required: false
          schema:
            type: string
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
        - name: filter[status]
          in: query
          required: false
          schema:
            type: string
        - name: filter[severity]
          in: query
          required: false
          schema:
            type: string
        - name: filter[type]
          in: query
          required: false
          schema:
            type: string
        - name: filter[user_id]
          in: query
          required: false
          schema:
            type: integer
        - name: filter[types]
          in: query
          required: false
          description: Filter by incident type slugs
          schema:
            type: string
        - name: filter[type_ids]
          in: query
          required: false
          description: Filter by incident type IDs (UUIDs)
          schema:
            type: string
        - name: filter[environments]
          in: query
          required: false
          description: Filter by environment slugs
          schema:
            type: string
        - name: filter[environment_ids]
          in: query
          required: false
          description: Filter by environment IDs (UUIDs)
          schema:
            type: string
        - name: filter[functionalities]
          in: query
          required: false
          description: Filter by functionality slugs
          schema:
            type: string
        - name: filter[functionality_ids]
          in: query
          required: false
          description: Filter by functionality IDs (UUIDs)
          schema:
            type: string
        - name: filter[services]
          in: query
          required: false
          description: Filter by service slugs
          schema:
            type: string
        - name: filter[service_ids]
          in: query
          required: false
          description: Filter by service IDs (UUIDs)
          schema:
            type: string
        - name: filter[teams]
          in: query
          required: false
          description: Filter by team/group slugs
          schema:
            type: string
        - name: filter[team_ids]
          in: query
          required: false
          description: Filter by team/group IDs (UUIDs)
          schema:
            type: string
        - name: filter[causes]
          in: query
          required: false
          description: Filter by cause slugs
          schema:
            type: string
        - name: filter[cause_ids]
          in: query
          required: false
          description: Filter by cause IDs (UUIDs)
          schema:
            type: string
        - name: filter[created_at][gt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[created_at][gte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[created_at][lt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[created_at][lte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[started_at][gt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[started_at][gte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[started_at][lt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[started_at][lte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[mitigated_at][gt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[mitigated_at][gte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[mitigated_at][lt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[mitigated_at][lte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[resolved_at][gt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[resolved_at][gte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[resolved_at][lt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[resolved_at][lte]
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
          description: success
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/incident_post_mortem_list'
      security:
        - bearer_auth: []
components:
  schemas:
    incident_post_mortem_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the incident retrospective
              type:
                type: string
                enum:
                  - incident_post_mortems
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/incident_post_mortem'
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
    incident_post_mortem:
      type: object
      properties:
        title:
          type: string
          description: The title of the incident retrospective
        content:
          type: string
          description: The content of the incident retrospective (Only if internal)
          nullable: true
        status:
          type: string
          description: The status of the incident retrospective
          enum:
            - draft
            - published
        started_at:
          type: string
          description: Date of started at
          nullable: true
        mitigated_at:
          type: string
          description: Date of mitigation
          nullable: true
        resolved_at:
          type: string
          description: Date of resolution
          nullable: true
        show_timeline:
          type: boolean
          description: Show events timeline of the incident retrospective
        show_timeline_trail:
          type: boolean
          description: Show trail events in the timeline of the incident retrospective
        show_timeline_genius:
          type: boolean
          description: Show workflow events in the timeline of the incident retrospective
        show_timeline_tasks:
          type: boolean
          description: Show tasks in the timeline of the incident retrospective
        show_timeline_action_items:
          type: boolean
          description: Show action items in the timeline of the incident retrospective
        show_timeline_order:
          type: string
          description: The order of the incident retrospective timeline
          enum:
            - asc
            - desc
          default: desc
        show_services_impacted:
          type: boolean
          description: Show functionalities impacted of the incident retrospective
        show_functionalities_impacted:
          type: boolean
          description: Show services impacted of the incident retrospective
        show_groups_impacted:
          type: boolean
          description: Show groups impacted of the incident retrospective
        show_alerts_attached:
          type: boolean
          description: Show alerts attached to the incident
        url:
          type: string
          description: The url to the incident retrospective
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - title
        - created_at
        - updated_at
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