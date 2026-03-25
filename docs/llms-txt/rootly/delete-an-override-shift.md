# Source: https://docs.rootly.com/api-reference/overrideshifts/delete-an-override-shift.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an override shift

> Delete a specific override shift by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json delete /v1/override_shifts/{id}
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
  /v1/override_shifts/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
    delete:
      tags:
        - OverrideShifts
      summary: Delete an override shift
      description: Delete a specific override shift by id
      operationId: deleteOverrideShift
      responses:
        '200':
          description: override shift deleted
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/override_shift_response'
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
    override_shift_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the shift
            type:
              type: string
              enum:
                - shifts
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/override_shift'
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
    override_shift:
      type: object
      properties:
        schedule_id:
          type: string
          description: ID of schedule
          nullable: false
        rotation_id:
          type: string
          description: ID of rotation
          nullable: true
        starts_at:
          type: string
          description: Start datetime of shift
          nullable: false
        ends_at:
          type: string
          description: End datetime of shift
          nullable: false
        is_override:
          type: boolean
          description: Denotes shift is an override shift
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        shift_override:
          type: object
          allOf:
            - $ref: '#/components/schemas/shift_override_response'
          description: Override metadata
          nullable: true
        user_id:
          type: integer
          description: Override shift user
          nullable: false
        user:
          type: object
          allOf:
            - $ref: '#/components/schemas/user_response'
          description: User metadata
          nullable: false
      required:
        - schedule_id
        - rotation_id
        - starts_at
        - ends_at
        - is_override
    shift_override_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the shift override
            type:
              type: string
              enum:
                - shift_override
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/shift_override'
          required:
            - id
            - type
            - attributes
      required:
        - data
    user_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the user
            type:
              type: string
              enum:
                - users
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/user'
            relationships:
              $ref: '#/components/schemas/user_relationships'
          required:
            - id
            - type
            - attributes
      required:
        - data
    shift_override:
      type: object
      properties:
        shift_id:
          type: string
          description: ID of shift
          nullable: false
        created_by_user_id:
          type: integer
          description: User who created the override
          nullable: false
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - shift_id
        - created_by_user_id
    user:
      type: object
      properties:
        email:
          type: string
          description: The email of the user
        first_name:
          type: string
          description: First name of the user
          nullable: true
        last_name:
          type: string
          description: Last name of the user
          nullable: true
        full_name:
          type: string
          description: The full name of the user
          nullable: true
        full_name_with_team:
          type: string
          description: The full name with team of the user
          nullable: true
        time_zone:
          type: string
          description: Configured time zone
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - email
        - created_at
        - updated_at
    user_relationships:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/role_relationship'
        on_call_role:
          $ref: '#/components/schemas/on_call_role_relationship'
    role_relationship:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
            type:
              type: string
              enum:
                - roles
          nullable: true
    on_call_role_relationship:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
            type:
              type: string
              enum:
                - on_call_roles
          nullable: true
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).