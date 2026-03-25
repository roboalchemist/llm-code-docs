# Source: https://docs.rootly.com/api-reference/dashboardpanels/update-a-dashboard-panel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a dashboard panel

> Update a specific dashboard panel by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json put /v1/dashboard_panels/{id}
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
  /v1/dashboard_panels/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
    put:
      tags:
        - DashboardPanels
      summary: Update a dashboard panel
      description: Update a specific dashboard panel by id
      operationId: updateDashboardPanel
      parameters: []
      requestBody:
        content:
          application/vnd.api+json:
            schema:
              $ref: '#/components/schemas/update_dashboard_panel'
        required: true
      responses:
        '200':
          description: dashboard panel updated
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/dashboard_panel_response'
      security:
        - bearer_auth: []
components:
  schemas:
    update_dashboard_panel:
      type: object
      properties:
        data:
          type: object
          properties:
            type:
              type: string
              enum:
                - dashboard_panels
            attributes:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the dashboard_panel
                  nullable: true
                params:
                  type: object
                  properties:
                    display:
                      type: string
                      enum:
                        - line_chart
                        - line_stepped_chart
                        - column_chart
                        - stacked_column_chart
                        - monitoring_chart
                        - pie_chart
                        - table
                        - aggregate_value
                    description:
                      type: string
                    table_fields:
                      type: array
                      items:
                        type: string
                    legend:
                      type: object
                      properties:
                        groups:
                          type: string
                          enum:
                            - all
                            - charted
                          default: all
                    datalabels:
                      type: object
                      properties:
                        enabled:
                          type: boolean
                    datasets:
                      type: array
                      items:
                        type: object
                        properties:
                          name:
                            type: string
                            nullable: true
                          collection:
                            type: string
                            enum:
                              - alerts
                              - incidents
                              - incident_post_mortems
                              - incident_action_items
                              - users
                          filter:
                            type: array
                            items:
                              type: object
                              properties:
                                operation:
                                  type: string
                                  enum:
                                    - and
                                    - or
                                rules:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      operation:
                                        type: string
                                        enum:
                                          - and
                                          - or
                                      condition:
                                        type: string
                                        enum:
                                          - '='
                                          - '!='
                                          - '>='
                                          - <=
                                          - exists
                                          - not_exists
                                          - contains
                                          - not_contains
                                          - assigned
                                          - unassigned
                                      key:
                                        type: string
                                      value:
                                        type: string
                          group_by:
                            oneOf:
                              - type: string
                                nullable: true
                              - type: object
                                properties:
                                  key:
                                    type: string
                                    enum:
                                      - custom_field
                                      - incident_role
                                  value:
                                    type: string
                                required:
                                  - key
                                  - value
                                nullable: true
                          aggregate:
                            type: object
                            properties:
                              operation:
                                type: string
                                enum:
                                  - count
                                  - sum
                                  - average
                              key:
                                type: string
                                nullable: true
                              cumulative:
                                type: boolean
                                nullable: true
                            nullable: true
                position:
                  type: object
                  properties:
                    x:
                      type: number
                    'y':
                      type: number
                    w:
                      type: number
                    h:
                      type: number
                  required:
                    - x
                    - 'y'
                    - w
                    - h
                  nullable: true
              additionalProperties: false
      required:
        - data
    dashboard_panel_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the dashboard_panel
            type:
              type: string
              enum:
                - dashboard_panels
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/dashboard_panel'
          required:
            - id
            - type
            - attributes
      required:
        - data
    dashboard_panel:
      type: object
      properties:
        dashboard_id:
          type: string
          description: The panel dashboard
        name:
          type: string
          description: The name of the dashboard_panel
          nullable: true
        params:
          type: object
          properties:
            display:
              type: string
              enum:
                - line_chart
                - line_stepped_chart
                - column_chart
                - stacked_column_chart
                - monitoring_chart
                - pie_chart
                - table
                - aggregate_value
            description:
              type: string
            table_fields:
              type: array
              items:
                type: string
            legend:
              type: object
              properties:
                groups:
                  type: string
                  enum:
                    - all
                    - charted
                  default: all
            datalabels:
              type: object
              properties:
                enabled:
                  type: boolean
            datasets:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    nullable: true
                  collection:
                    type: string
                    enum:
                      - alerts
                      - incidents
                      - incident_post_mortems
                      - incident_action_items
                      - users
                  filter:
                    type: array
                    items:
                      type: object
                      properties:
                        operation:
                          type: string
                          enum:
                            - and
                            - or
                        rules:
                          type: array
                          items:
                            type: object
                            properties:
                              operation:
                                type: string
                                enum:
                                  - and
                                  - or
                              condition:
                                type: string
                                enum:
                                  - '='
                                  - '!='
                                  - '>='
                                  - <=
                                  - exists
                                  - not_exists
                                  - contains
                                  - not_contains
                                  - assigned
                                  - unassigned
                              key:
                                type: string
                              value:
                                type: string
                  group_by:
                    oneOf:
                      - type: string
                        nullable: true
                      - type: object
                        properties:
                          key:
                            type: string
                            enum:
                              - custom_field
                              - incident_role
                          value:
                            type: string
                        required:
                          - key
                          - value
                        nullable: true
                  aggregate:
                    type: object
                    properties:
                      operation:
                        type: string
                        enum:
                          - count
                          - sum
                          - average
                      key:
                        type: string
                        nullable: true
                      cumulative:
                        type: boolean
                        nullable: true
                    nullable: true
        position:
          type: object
          properties:
            x:
              type: number
            'y':
              type: number
            w:
              type: number
            h:
              type: number
          required:
            - x
            - 'y'
            - w
            - h
          nullable: true
        data:
          type: array
          items:
            type: object
      required:
        - params
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).