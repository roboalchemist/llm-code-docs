# Source: https://docs.rootly.com/api-reference/incidentretrospectives/retrieves-an-incident-retrospective.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves an incident retrospective

> List incidents retrospectives



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/post_mortems/{id}
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
  /v1/post_mortems/{id}:
    parameters:
      - name: id
        in: path
        schema:
          anyOf:
            - type: string
              format: uuid
              description: Resource UUID
            - type: string
              pattern: ^[a-z0-9_-]+$
              description: Resource slug
        required: true
    get:
      tags:
        - IncidentRetrospectives
      summary: Retrieves an incident retrospective
      description: List incidents retrospectives
      operationId: ListIncidentPostmortem
      responses:
        '200':
          description: incident_post_mortem found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/incident_post_mortem_response'
        '404':
          description: resource not found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    incident_post_mortem_response:
      type: object
      properties:
        data:
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
      required:
        - data
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
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).