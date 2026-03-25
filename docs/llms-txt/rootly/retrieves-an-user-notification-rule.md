# Source: https://docs.rootly.com/api-reference/usernotificationrules/retrieves-an-user-notification-rule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves an user notification rule

> Retrieves a specific user notification rule by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/notification_rules/{id}
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
  /v1/notification_rules/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
    get:
      tags:
        - UserNotificationRules
      summary: Retrieves an user notification rule
      description: Retrieves a specific user notification rule by id
      operationId: getUserNotificationRule
      responses:
        '200':
          description: user_notification_rule found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/user_notification_rule_response'
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
    user_notification_rule_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the rule
            type:
              type: string
              enum:
                - user_notification_rules
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/user_notification_rule'
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
    user_notification_rule:
      type: object
      properties:
        user_id:
          type: integer
        delay:
          type: integer
          description: Delay after which rule gets triggered
          nullable: true
        position:
          type: integer
          description: Position of the rule
          nullable: true
        user_email_address_id:
          type: string
          description: User email address to which notification to be sent
          nullable: true
        user_call_number_id:
          type: string
          description: User phone number to which notification to be sent
          nullable: true
        user_sms_number_id:
          type: string
          description: User sms number to which notification to be sent
          nullable: true
        user_device_id:
          type: string
          description: User device to which notification to be sent
          nullable: true
        enabled_contact_types:
          type: array
          description: Contact types for which notification needs to be enabled
          items:
            type: string
            enum:
              - email
              - sms
              - call
              - device
              - non_critical_device
              - slack
          nullable: false
        notification_type:
          type: string
          description: >-
            Type of notification rule (audible or quiet). Audible notifications
            use sound/vibration to alert users, while quiet notifications are
            silent.
          enum:
            - audible
            - quiet
          nullable: false
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).