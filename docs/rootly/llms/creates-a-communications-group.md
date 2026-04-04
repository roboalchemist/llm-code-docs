# Source: https://docs.rootly.com/api-reference/communications-groups/creates-a-communications-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creates a communications group

> Creates a new communications group from provided data



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json post /v1/communications/groups
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
  /v1/communications/groups:
    post:
      tags:
        - Communications Groups
      summary: Creates a communications group
      description: Creates a new communications group from provided data
      operationId: createCommunicationsGroup
      parameters: []
      requestBody:
        content:
          application/vnd.api+json:
            schema:
              $ref: '#/components/schemas/new_communications_group'
        required: true
      responses:
        '201':
          description: communications group created
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/communications_group_response'
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
    new_communications_group:
      type: object
      properties:
        data:
          type: object
          properties:
            type:
              type: string
              enum:
                - communications_groups
            attributes:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the communications group
                description:
                  type: string
                  description: The description of the communications group
                  nullable: true
                communication_type_id:
                  type: string
                  description: The communication type ID
                is_private:
                  type: boolean
                  description: Whether the group is private
                  nullable: true
                condition_type:
                  type: string
                  description: Condition type
                  enum:
                    - any
                    - all
                  nullable: true
                sms_channel:
                  type: boolean
                  description: SMS channel enabled
                  nullable: true
                email_channel:
                  type: boolean
                  description: Email channel enabled
                  nullable: true
                member_ids:
                  type: array
                  description: Array of member user IDs
                  nullable: true
                  items:
                    type: integer
                slack_channel_ids:
                  type: array
                  description: Array of Slack channel IDs
                  nullable: true
                  items:
                    type: string
                communication_group_conditions:
                  type: array
                  description: Group conditions attributes
                  nullable: true
                  items:
                    type: object
                    properties:
                      property_type:
                        type: string
                        description: Property type
                        enum:
                          - service
                          - severity
                          - functionality
                          - group
                          - incident_type
                      service_ids:
                        type: array
                        description: Array of service IDs
                        nullable: true
                        items:
                          type: string
                      severity_ids:
                        type: array
                        description: Array of severity IDs
                        nullable: true
                        items:
                          type: string
                      functionality_ids:
                        type: array
                        description: Array of functionality IDs
                        nullable: true
                        items:
                          type: string
                      group_ids:
                        type: array
                        description: Array of group IDs
                        nullable: true
                        items:
                          type: string
                      incident_type_ids:
                        type: array
                        description: Array of incident type IDs
                        nullable: true
                        items:
                          type: string
                communication_external_group_members:
                  type: array
                  description: External group members attributes
                  nullable: true
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: Name of the external member
                      email:
                        type: string
                        description: Email of the external member
                      phone_number:
                        type: string
                        description: Phone number of the external member
              additionalProperties: false
              required:
                - name
                - communication_type_id
          required:
            - type
            - attributes
      required:
        - data
    communications_group_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the communications group
            type:
              type: string
              enum:
                - communications_groups
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/communications_group'
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
    communications_group:
      type: object
      properties:
        name:
          type: string
          description: The name of the communications group
        slug:
          type: string
          description: The slug of the communications group
        description:
          type: string
          description: The description of the communications group
          nullable: true
        communication_type_id:
          type: string
          description: The communication type ID
        is_private:
          type: boolean
          description: Whether the group is private
        condition_type:
          type: string
          description: Condition type
          enum:
            - any
            - all
        sms_channel:
          type: boolean
          description: SMS channel enabled
        email_channel:
          type: boolean
          description: Email channel enabled
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        communication_group_conditions:
          type: array
          description: Group conditions attributes
          nullable: true
          items:
            type: object
            properties:
              property_type:
                type: string
                description: Property type
                enum:
                  - service
                  - severity
                  - functionality
                  - group
                  - incident_type
              service_ids:
                type: array
                description: Array of service IDs
                nullable: true
                items:
                  type: string
              severity_ids:
                type: array
                description: Array of severity IDs
                nullable: true
                items:
                  type: string
              functionality_ids:
                type: array
                description: Array of functionality IDs
                nullable: true
                items:
                  type: string
              group_ids:
                type: array
                description: Array of group IDs
                nullable: true
                items:
                  type: string
              incident_type_ids:
                type: array
                description: Array of incident type IDs
                nullable: true
                items:
                  type: string
        member_ids:
          type: array
          description: Array of member user IDs
          nullable: true
          items:
            type: integer
        slack_channel_ids:
          type: array
          description: Array of Slack channel IDs
          nullable: true
          items:
            type: string
        communication_external_group_members:
          type: array
          description: External group members
          nullable: true
          items:
            type: object
            properties:
              id:
                type: string
                description: ID of the external group member
              name:
                type: string
                description: Name of the external member
              email:
                type: string
                description: Email of the external member
              phone_number:
                type: string
                description: Phone number of the external member
      required:
        - name
        - communication_type_id
        - is_private
        - condition_type
        - sms_channel
        - email_channel
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).