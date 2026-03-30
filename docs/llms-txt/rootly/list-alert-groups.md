# Source: https://docs.rootly.com/api-reference/alertgroups/list-alert-groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List alert groups

> List alert groups



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/alert_groups
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
  /v1/alert_groups:
    get:
      tags:
        - AlertGroups
      summary: List alert groups
      description: List alert groups
      operationId: listAlertGroups
      parameters:
        - name: include
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
                $ref: '#/components/schemas/alert_group_list'
      security:
        - bearer_auth: []
components:
  schemas:
    alert_group_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the alert group
              type:
                type: string
                enum:
                  - alert_groups
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/alert_group'
            required:
              - id
              - type
              - attributes
      required:
        - data
    alert_group:
      type: object
      properties:
        name:
          type: string
          description: The name of the alert group
        description:
          type: string
          description: The description of the alert group
          nullable: true
        slug:
          type: string
          description: The slug of the alert group
        condition_type:
          type: string
          description: Grouping condition for the alert group
        time_window:
          type: integer
          description: Time window for the alert grouping
        group_by_alert_title:
          type: boolean
          deprecated: true
          description: >-
            [DEPRECATED] Whether the alerts are grouped by title or not. This
            field is deprecated. Please use the `conditions` field with advanced
            alert grouping instead.
        group_by_alert_urgency:
          type: boolean
          deprecated: true
          description: >-
            [DEPRECATED] Whether the alerts are grouped by urgency or not. This
            field is deprecated. Please use the `conditions` field with advanced
            alert grouping instead.
        targets:
          type: array
          items:
            type: object
            properties:
              target_type:
                type: string
                description: The type of the target.
                enum:
                  - Group
                  - Service
                  - EscalationPolicy
              target_id:
                type: string
                format: uuid
                description: id for the Group, Service or EscalationPolicy
            required:
              - target_type
              - target_id
        attributes:
          deprecated: true
          description: >-
            This field is deprecated. Please use the `conditions` field instead,
            `attributes` will be removed in the future.
          type: array
          items:
            type: object
            properties:
              json_path:
                type: string
                description: The JSON path to the value to group by.
        conditions:
          type: array
          description: The conditions for the alert group
          items:
            type: object
            properties:
              property_field_type:
                type: string
                description: The type of the property field
                enum:
                  - attribute
                  - payload
                  - alert_field
              property_field_name:
                type: string
                nullable: true
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
                  - matches_existing_alert
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
              values:
                type: array
                items:
                  type: object
                  properties:
                    record_id:
                      type: string
                      description: ID of the Alert Urgency to set.
                    record_type:
                      type: string
                      description: Should be "AlertUrgency".
                  required:
                    - record_id
                    - record_type
                  nullable: true
              alert_urgency_ids:
                type: array
                description: >-
                  The Alert Urgency IDs to check in the condition. Only need to
                  be set when the property field type is 'attribute', the
                  property field name is 'alert_urgency' and the property field
                  condition type is 'is_one_of' or 'is_not_one_of'
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
                description: >-
                  The ID of the conditionable. If conditionable_type is
                  AlertField, this is the ID of the alert field.
                nullable: true
            required:
              - property_field_type
              - property_field_condition_type
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        deleted_at:
          type: string
          nullable: true
          description: Date or deletion
      required:
        - name
        - description
        - created_at
        - updated_at
        - deleted_at
        - condition_type
        - time_window
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).