# Source: https://docs.rootly.com/api-reference/livecallrouters/update-a-live-call-router.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Live Call Router

> Update a specific Live Call Router by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json put /v1/live_call_routers/{id}
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
  /v1/live_call_routers/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
    put:
      tags:
        - LiveCallRouters
      summary: Update a Live Call Router
      description: Update a specific Live Call Router by id
      operationId: updateLiveCallRouter
      parameters: []
      requestBody:
        content:
          application/vnd.api+json:
            schema:
              $ref: '#/components/schemas/update_live_call_router'
        required: true
      responses:
        '200':
          description: live_call_router updated
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/live_call_router_response'
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
    update_live_call_router:
      type: object
      properties:
        data:
          type: object
          properties:
            type:
              type: string
              enum:
                - live_call_routers
            attributes:
              type: object
              properties:
                kind:
                  type: string
                  description: The kind of the live_call_router
                  enum:
                    - voicemail
                    - live
                enabled:
                  type: boolean
                  description: Whether the live_call_router is enabled
                name:
                  type: string
                  description: The name of the live_call_router
                country_code:
                  type: string
                  description: The country code of the live_call_router
                  enum:
                    - AU
                    - CA
                    - DE
                    - NL
                    - NZ
                    - GB
                    - US
                phone_type:
                  type: string
                  description: The phone type of the live_call_router
                  enum:
                    - local
                    - toll_free
                    - mobile
                voicemail_greeting:
                  type: string
                  description: The voicemail greeting of the live_call_router
                caller_greeting:
                  type: string
                  description: The caller greeting message of the live_call_router
                waiting_music_url:
                  type: string
                  description: The waiting music URL of the live_call_router
                  enum:
                    - >-
                      https://storage.rootly.com/twilio/voicemail/ClockworkWaltz.mp3
                    - >-
                      https://storage.rootly.com/twilio/voicemail/ith_brahms-116-4.mp3
                    - >-
                      https://storage.rootly.com/twilio/voicemail/Mellotroniac_-_Flight_Of_Young_Hearts_Flute.mp3
                    - >-
                      https://storage.rootly.com/twilio/voicemail/BusyStrings.mp3
                    - >-
                      https://storage.rootly.com/twilio/voicemail/oldDog_-_endless_goodbye_%28instr.%29.mp3
                    - >-
                      https://storage.rootly.com/twilio/voicemail/MARKOVICHAMP-Borghestral.mp3
                    - >-
                      https://storage.rootly.com/twilio/voicemail/ith_chopin-15-2.mp3
                sent_to_voicemail_delay:
                  type: integer
                  description: >-
                    The delay (seconds) after which the caller in redirected to
                    voicemail
                should_redirect_to_voicemail_on_no_answer:
                  type: boolean
                  description: This prompts the caller to choose voicemail or connect live
                escalation_level_delay_in_seconds:
                  type: integer
                  description: This overrides the delay (seconds) in escalation levels
                should_auto_resolve_alert_on_call_end:
                  type: boolean
                  description: This overrides the delay (seconds) in escalation levels
                alert_urgency_id:
                  type: string
                  description: This is used in escalation paths to determine who to page
                calling_tree_prompt:
                  type: string
                  description: >-
                    The audio instructions callers will hear when they call this
                    number, prompting them to select from available options to
                    route their call
                paging_targets:
                  type: array
                  description: >-
                    Paging targets that callers can select from when this live
                    call router is configured as a phone tree.
                  items:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The ID of paging target
                      type:
                        type: string
                        description: The type of the paging target
                        enum:
                          - service
                          - team
                          - escalation_policy
                      alert_urgency_id:
                        type: string
                        description: >-
                          This is used in escalation paths to determine who to
                          page
                    required:
                      - id
                      - type
                      - alert_urgency_id
                    nullable: false
                escalation_policy_trigger_params:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The ID of notification target
                    type:
                      type: string
                      description: The type of the notification target
                      enum:
                        - Service
                        - Group
                        - EscalationPolicy
                  required:
                    - id
                    - type
              additionalProperties: false
          required:
            - type
            - attributes
      required:
        - data
    live_call_router_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the live_call_router
            type:
              type: string
              enum:
                - live_call_routers
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/live_call_router'
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
    live_call_router:
      type: object
      properties:
        kind:
          type: string
          description: The kind of the live_call_router
          enum:
            - voicemail
            - live
        enabled:
          type: boolean
          description: Whether the live_call_router is enabled
        name:
          type: string
          description: The name of the live_call_router
        country_code:
          type: string
          description: The country code of the live_call_router
          enum:
            - AU
            - CA
            - DE
            - NL
            - NZ
            - GB
            - US
        phone_type:
          type: string
          description: The phone type of the live_call_router
          enum:
            - local
            - toll_free
            - mobile
        phone_number:
          type: string
          description: >-
            You can select a phone number using
            [generate_phone_number](#//api/v1/live_call_routers/generate_phone_number)
            API and pass that phone number here to register
        voicemail_greeting:
          type: string
          description: The voicemail greeting of the live_call_router
        caller_greeting:
          type: string
          description: The caller greeting message of the live_call_router
        waiting_music_url:
          type: string
          description: The waiting music URL of the live_call_router
          enum:
            - https://storage.rootly.com/twilio/voicemail/ClockworkWaltz.mp3
            - https://storage.rootly.com/twilio/voicemail/ith_brahms-116-4.mp3
            - >-
              https://storage.rootly.com/twilio/voicemail/Mellotroniac_-_Flight_Of_Young_Hearts_Flute.mp3
            - https://storage.rootly.com/twilio/voicemail/BusyStrings.mp3
            - >-
              https://storage.rootly.com/twilio/voicemail/oldDog_-_endless_goodbye_%28instr.%29.mp3
            - >-
              https://storage.rootly.com/twilio/voicemail/MARKOVICHAMP-Borghestral.mp3
            - https://storage.rootly.com/twilio/voicemail/ith_chopin-15-2.mp3
        sent_to_voicemail_delay:
          type: integer
          description: >-
            The delay (seconds) after which the caller in redirected to
            voicemail
        should_redirect_to_voicemail_on_no_answer:
          type: boolean
          description: This prompts the caller to choose voicemail or connect live
        escalation_level_delay_in_seconds:
          type: integer
          description: This overrides the delay (seconds) in escalation levels
        should_auto_resolve_alert_on_call_end:
          type: boolean
          description: This overrides the delay (seconds) in escalation levels
        alert_urgency_id:
          type: string
          description: This is used in escalation paths to determine who to page
        calling_tree_prompt:
          type: string
          description: >-
            The audio instructions callers will hear when they call this number,
            prompting them to select from available options to route their call
        paging_targets:
          type: array
          description: >-
            Paging targets that callers can select from when this live call
            router is configured as a phone tree.
          items:
            type: object
            properties:
              id:
                type: string
                description: The ID of paging target
              type:
                type: string
                description: The type of the paging target
                enum:
                  - service
                  - team
                  - escalation_policy
              alert_urgency_id:
                type: string
                description: This is used in escalation paths to determine who to page
            required:
              - id
              - type
              - alert_urgency_id
            nullable: false
        escalation_policy_trigger_params:
          type: object
          properties:
            id:
              type: string
              description: The ID of notification target
            type:
              type: string
              description: The type of the notification target
              enum:
                - Service
                - Group
                - EscalationPolicy
          required:
            - id
            - type
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - name
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).