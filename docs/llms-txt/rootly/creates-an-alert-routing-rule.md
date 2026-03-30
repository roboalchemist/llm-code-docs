# Source: https://docs.rootly.com/api-reference/alertroutingrules/creates-an-alert-routing-rule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creates an alert routing rule

> Creates a new alert routing rule from provided data. **Note: If you are an advanced alert routing user, you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are an advanced user, please contact Rootly customer support.**



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json post /v1/alert_routing_rules
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
  /v1/alert_routing_rules:
    post:
      tags:
        - AlertRoutingRules
      summary: Creates an alert routing rule
      description: >-
        Creates a new alert routing rule from provided data. **Note: If you are
        an advanced alert routing user, you should use the Alert Routes endpoint
        instead of this endpoint. If you don't know whether you are an advanced
        user, please contact Rootly customer support.**
      operationId: createAlertRoutingRule
      parameters: []
      requestBody:
        content:
          application/vnd.api+json:
            schema:
              $ref: '#/components/schemas/new_alert_routing_rule'
        required: true
      responses:
        '201':
          description: alert routing rule created
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/alert_routing_rule_response'
        '401':
          description: responds with unauthorized for invalid token
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
        '422':
          description: invalid request
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    new_alert_routing_rule:
      type: object
      properties:
        data:
          type: object
          properties:
            type:
              type: string
              enum:
                - alert_routing_rules
            attributes:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the alert routing rule
                enabled:
                  type: boolean
                  description: Whether the alert routing rule is enabled
                owning_team_ids:
                  type: array
                  description: >-
                    The IDs of the teams which own the alert routing rule. If
                    the user doesn't have Alert Routing Create Permission in
                    On-Call Roles, then this field is required and can contain
                    Team IDs the user is an admin of.
                  items:
                    type: string
                    format: uuid
                alerts_source_id:
                  type: string
                  format: uuid
                  description: The ID of the alerts source
                position:
                  type: integer
                  description: >-
                    The position of the alert routing rule for ordering
                    evaluation
                condition_type:
                  type: string
                  description: The type of condition for the alert routing rule
                  enum:
                    - all
                    - any
                conditions:
                  type: array
                  items:
                    type: object
                    properties:
                      property_field_type:
                        type: string
                        description: The type of the property field
                        enum:
                          - attribute
                          - payload
                      property_field_name:
                        type: string
                        description: >-
                          The name of the property field. If the property field
                          type is selected as 'attribute', then the allowed
                          property field names are 'summary' (for Title),
                          'description', 'alert_urgency' and 'external_url' (for
                          Alert Source URL). If the property field type is
                          selected as 'payload', then the property field name
                          should be supplied in JSON Path syntax.
                      property_field_condition_type:
                        type: string
                        description: The condition type of the property field
                        enum:
                          - is_one_of
                          - is_not_one_of
                          - contains
                          - does_not_contain
                          - starts_with
                          - ends_with
                          - matches_regex
                          - is_empty
                      property_field_value:
                        type: string
                        description: >-
                          The value of the property field. Can be null if the
                          property field condition type is 'is_one_of' or
                          'is_not_one_of'
                      property_field_values:
                        type: array
                        description: >-
                          The values of the property field. Need to be passed if
                          the property field condition type is 'is_one_of' or
                          'is_not_one_of' except for when property field name is
                          'alert_urgency'
                        items:
                          type: string
                    required:
                      - property_field_type
                      - property_field_name
                      - property_field_condition_type
                destination:
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
              additionalProperties: false
              required:
                - name
                - alerts_source_id
                - destination
          required:
            - type
            - attributes
      required:
        - data
    alert_routing_rule_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the alert_routing_rule
            type:
              type: string
              enum:
                - alert_routing_rules
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/alert_routing_rule'
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
    alert_routing_rule:
      type: object
      properties:
        name:
          type: string
          description: The name of the alert routing rule
        enabled:
          type: boolean
          description: Whether the alert routing rule is enabled
        alerts_source_id:
          type: string
          format: uuid
          description: The ID of the alerts source
        position:
          type: integer
          description: The position of the alert routing rule for ordering evaluation
        condition_type:
          type: string
          description: The type of condition for the alert routing rule
          enum:
            - all
            - any
        conditions:
          type: array
          description: The conditions for the alert routing rule
          items:
            type: object
            properties:
              property_field_type:
                type: string
                description: The type of the property field
                enum:
                  - attribute
                  - payload
              property_field_name:
                type: string
                description: >-
                  The name of the property field. If the property field type is
                  selected as 'attribute', then the allowed property field names
                  are 'summary' (for Title), 'description', 'alert_urgency' and
                  'external_url' (for Alert Source URL). If the property field
                  type is selected as 'payload', then the property field name
                  should be supplied in JSON Path syntax.
              property_field_condition_type:
                type: string
                description: The condition type of the property field
                enum:
                  - is_one_of
                  - is_not_one_of
                  - contains
                  - does_not_contain
                  - starts_with
                  - ends_with
                  - matches_regex
                  - is_empty
              property_field_value:
                type: string
                description: >-
                  The value of the property field. Can be null if the property
                  field condition type is 'is_one_of' or 'is_not_one_of'
                nullable: true
              property_field_values:
                type: array
                description: >-
                  The values of the property field. Used if the property field
                  condition type is 'is_one_of' or 'is_not_one_of' except for
                  when property field name is 'alert_urgency'
                items:
                  type: string
            required:
              - property_field_type
              - property_field_name
              - property_field_condition_type
        destination:
          type: object
          description: The destinations for the alert routing rule
          nullable: true
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
          description: The condition groups for the alert routing rule
          items:
            type: object
            properties:
              id:
                type: string
                format: uuid
                description: Unique ID of the condition group
              position:
                type: integer
                description: The position of the condition group for ordering
              conditions:
                type: array
                description: The conditions within this group
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      format: uuid
                      description: Unique ID of the condition
                    property_field_type:
                      type: string
                      description: The type of the property field
                      enum:
                        - attribute
                        - payload
                    property_field_name:
                      type: string
                      description: The name of the property field
                    property_field_condition_type:
                      type: string
                      description: The condition type of the property field
                      enum:
                        - is_one_of
                        - is_not_one_of
                        - contains
                        - does_not_contain
                        - starts_with
                        - ends_with
                        - matches_regex
                        - is_empty
                    property_field_value:
                      type: string
                      description: The value of the property field
                      nullable: true
                    property_field_values:
                      type: array
                      description: The values of the property field
                      items:
                        type: string
                      nullable: true
                    conditionable_id:
                      type: string
                      format: uuid
                      description: The ID of the conditionable object
                      nullable: true
                    conditionable_type:
                      type: string
                      description: The type of the conditionable object
                      nullable: true
                    created_at:
                      type: string
                      description: Date of creation
                    updated_at:
                      type: string
                      description: Date of last update
                  required:
                    - property_field_type
                    - property_field_name
                    - property_field_condition_type
              created_at:
                type: string
                description: Date of creation
              updated_at:
                type: string
                description: Date of last update
            required:
              - position
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - name
        - enabled
        - alerts_source_id
        - position
        - condition_type
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).