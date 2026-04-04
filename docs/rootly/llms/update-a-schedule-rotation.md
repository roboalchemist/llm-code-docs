# Source: https://docs.rootly.com/api-reference/schedulerotations/update-a-schedule-rotation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a schedule rotation

> Update a specific schedule rotation by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json put /v1/schedule_rotations/{id}
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
  /v1/schedule_rotations/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
    put:
      tags:
        - ScheduleRotations
      summary: Update a schedule rotation
      description: Update a specific schedule rotation by id
      operationId: updateScheduleRotation
      parameters: []
      requestBody:
        content:
          application/vnd.api+json:
            schema:
              $ref: '#/components/schemas/update_schedule_rotation'
        required: true
      responses:
        '200':
          description: schedule_rotation updated
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/schedule_rotation_response'
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
    update_schedule_rotation:
      type: object
      properties:
        data:
          type: object
          properties:
            type:
              type: string
              enum:
                - schedule_rotations
            attributes:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the schedule rotation
                position:
                  type: integer
                  description: Position of the schedule rotation
                schedule_rotationable_type:
                  type: string
                  description: Schedule rotation type
                  enum:
                    - ScheduleDailyRotation
                    - ScheduleWeeklyRotation
                    - ScheduleBiweeklyRotation
                    - ScheduleMonthlyRotation
                    - ScheduleCustomRotation
                active_all_week:
                  type: boolean
                  description: Schedule rotation active all week?
                  default: true
                active_days:
                  type: array
                  items:
                    type: string
                    description: Schedule rotation active days
                    enum:
                      - S
                      - M
                      - T
                      - W
                      - R
                      - F
                      - U
                active_time_type:
                  type: string
                  items:
                    type: string
                    description: Schedule rotation active time type
                    enum:
                      - all_day
                      - same_time
                      - custom
                    default: all_day
                active_time_attributes:
                  type: array
                  description: Schedule rotation's active times
                  items:
                    type: object
                    properties:
                      start_time:
                        type: string
                        description: Start time for schedule rotation active time
                        format: time
                      end_time:
                        type: string
                        description: End time for schedule rotation active time
                        format: time
                    required:
                      - start_time
                      - end_time
                time_zone:
                  type: string
                  description: A valid IANA time zone name.
                  default: Etc/UTC
                schedule_rotationable_attributes:
                  type: object
                  oneOf:
                    - type: object
                      properties:
                        handoff_time:
                          type: string
                          description: Hand off time for daily rotation
                          format: time
                      additionalProperties: false
                      required:
                        - handoff_time
                    - type: object
                      properties:
                        handoff_time:
                          type: string
                          description: Hand off time for weekly/biweekly rotation
                          format: time
                        handoff_day:
                          type: string
                          description: Hand off day for weekly/biweekly rotation
                          enum:
                            - S
                            - M
                            - T
                            - W
                            - R
                            - F
                            - U
                      additionalProperties: false
                      required:
                        - handoff_time
                        - handoff_day
                    - type: object
                      properties:
                        handoff_time:
                          type: string
                          description: Hand off time for monthly rotation
                          format: time
                        handoff_day:
                          type: string
                          description: Hand off day for monthly rotation
                          enum:
                            - first_day_of_month
                            - last_day_of_month
                      additionalProperties: false
                      required:
                        - handoff_time
                        - handoff_day
                    - type: object
                      properties:
                        shift_length:
                          type: integer
                          description: Shift length for custom rotation
                        shift_length_unit:
                          type: string
                          description: Shift length unit for custom rotation
                          enum:
                            - hours
                            - days
                            - weeks
                        handoff_time:
                          type: string
                          description: >-
                            Hand off time for custom rotation. Use minutes for
                            hourly rotation.
                          format: time
                      additionalProperties: false
                      required:
                        - shift_length_unit
                        - shift_length
                        - handoff_time
                start_time:
                  type: string
                  format: time
                  description: >-
                    ISO8601 date and time when rotation starts. Shifts will only
                    be created after this time.
                  nullable: true
                end_time:
                  type: string
                  format: time
                  description: >-
                    ISO8601 date and time when rotation ends. Shifts will only
                    be created before this time.
                  nullable: true
                schedule_rotation_members:
                  type: array
                  description: >-
                    You can only update schedule rotation members if your
                    account has schedule nesting feature enabled
                  nullable: true
                  items:
                    type: object
                    properties:
                      member_type:
                        type: string
                        description: Type of member
                        enum:
                          - User
                          - Schedule
                      member_id:
                        type: string
                        description: ID of the member
                      position:
                        type: integer
                        description: Position of the member in rotation
                    required:
                      - member_type
                      - member_id
              additionalProperties: false
              required:
                - schedule_rotationable_type
          required:
            - type
            - attributes
      required:
        - data
    schedule_rotation_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the schedule rotation
            type:
              type: string
              enum:
                - schedule_rotations
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/schedule_rotation'
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
    schedule_rotation:
      type: object
      properties:
        schedule_id:
          type: string
          description: The ID of parent schedule
        name:
          type: string
          description: The name of the schedule rotation
        position:
          type: integer
          description: Position of the schedule rotation
        schedule_rotationable_type:
          type: string
          description: Schedule rotation type
          enum:
            - ScheduleDailyRotation
            - ScheduleWeeklyRotation
            - ScheduleBiweeklyRotation
            - ScheduleMonthlyRotation
            - ScheduleCustomRotation
        active_all_week:
          type: boolean
          description: Schedule rotation active all week?
          default: true
        active_days:
          type: array
          items:
            type: string
            description: Schedule rotation active days
            enum:
              - S
              - M
              - T
              - W
              - R
              - F
              - U
        active_time_type:
          type: string
          items:
            type: string
            description: Schedule rotation active time type
            enum:
              - all_day
              - same_time
              - custom
            default: all_day
        active_time_attributes:
          type: array
          description: Schedule rotation's active times
          items:
            type: object
            properties:
              start_time:
                type: string
                description: Start time for schedule rotation active time
                format: time
              end_time:
                type: string
                description: End time for schedule rotation active time
                format: time
            required:
              - start_time
              - end_time
        time_zone:
          type: string
          description: A valid IANA time zone name.
          default: Etc/UTC
        schedule_rotationable_attributes:
          type: object
          oneOf:
            - type: object
              properties:
                handoff_time:
                  type: string
                  description: Hand off time for daily rotation
                  format: time
              additionalProperties: false
              required:
                - handoff_time
            - type: object
              properties:
                handoff_time:
                  type: string
                  description: Hand off time for weekly/biweekly rotation
                  format: time
                handoff_day:
                  type: string
                  description: Hand off day for weekly/biweekly rotation
                  enum:
                    - S
                    - M
                    - T
                    - W
                    - R
                    - F
                    - U
              additionalProperties: false
              required:
                - handoff_time
                - handoff_day
            - type: object
              properties:
                handoff_time:
                  type: string
                  description: Hand off time for monthly rotation
                  format: time
                handoff_day:
                  type: string
                  description: Hand off day for monthly rotation
                  enum:
                    - first_day_of_month
                    - last_day_of_month
              additionalProperties: false
              required:
                - handoff_time
                - handoff_day
            - type: object
              properties:
                shift_length:
                  type: integer
                  description: Shift length for custom rotation
                shift_length_unit:
                  type: string
                  description: Shift length unit for custom rotation
                  enum:
                    - hours
                    - days
                    - weeks
                handoff_time:
                  type: string
                  description: >-
                    Hand off time for custom rotation. Use minutes for hourly
                    rotation.
                  format: time
              additionalProperties: false
              required:
                - shift_length_unit
                - shift_length
                - handoff_time
        start_time:
          type: string
          format: date
          description: >-
            ISO8601 date and time when rotation starts. Shifts will only be
            created after this time.
          nullable: true
        end_time:
          type: string
          format: date
          description: >-
            ISO8601 date and time when rotation ends. Shifts will only be
            created before this time.
          nullable: true
      required:
        - schedule_id
        - name
        - schedule_rotationable_type
        - schedule_rotationable_attributes
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).