# Source: https://docs.rootly.com/api-reference/escalationpolicies/retrieves-an-escalation-policy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves an escalation policy

> Retrieves a specific escalation policy by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/escalation_policies/{id}
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
  /v1/escalation_policies/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
    get:
      tags:
        - EscalationPolicies
      summary: Retrieves an escalation policy
      description: Retrieves a specific escalation policy by id
      operationId: getEscalationPolicy
      parameters:
        - name: include
          in: query
          description: >-
            comma separated if needed. eg:
            escalation_policy_levels,escalation_policy_paths
          schema:
            type: string
            enum:
              - escalation_policy_levels
              - escalation_policy_paths
              - groups
              - services
          required: false
      responses:
        '200':
          description: escalation policy found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/escalation_policy_response'
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
    escalation_policy_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the escalation policy
            type:
              type: string
              enum:
                - escalation_policies
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/escalation_policy'
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
    escalation_policy:
      type: object
      properties:
        name:
          type: string
          description: The name of the escalation policy
        description:
          type: string
          description: The description of the escalation policy
          nullable: true
        repeat_count:
          type: integer
          description: >-
            The number of times this policy will be executed until someone
            acknowledges the alert
        created_by_user_id:
          type: integer
          description: User who created the escalation policy
        last_updated_by_user_id:
          type: integer
          description: User who updated the escalation policy
        group_ids:
          type: array
          items:
            type: string
          description: >-
            Associated groups (alerting the group will trigger escalation
            policy)
        service_ids:
          type: array
          items:
            type: string
          description: >-
            Associated services (alerting the service will trigger escalation
            policy)
        business_hours:
          type: object
          properties:
            time_zone:
              type: string
              description: Time zone for business hours
              enum:
                - International Date Line West
                - Etc/GMT+12
                - American Samoa
                - Pacific/Pago_Pago
                - Midway Island
                - Pacific/Midway
                - Hawaii
                - Pacific/Honolulu
                - Alaska
                - America/Juneau
                - Pacific Time (US & Canada)
                - America/Los_Angeles
                - Tijuana
                - America/Tijuana
                - Arizona
                - America/Phoenix
                - Mazatlan
                - America/Mazatlan
                - Mountain Time (US & Canada)
                - America/Denver
                - Central America
                - America/Guatemala
                - Central Time (US & Canada)
                - America/Chicago
                - Chihuahua
                - America/Chihuahua
                - Guadalajara
                - America/Mexico_City
                - Mexico City
                - America/Mexico_City
                - Monterrey
                - America/Monterrey
                - Saskatchewan
                - America/Regina
                - Bogota
                - America/Bogota
                - Eastern Time (US & Canada)
                - America/New_York
                - Indiana (East)
                - America/Indiana/Indianapolis
                - Lima
                - America/Lima
                - Quito
                - America/Lima
                - Atlantic Time (Canada)
                - America/Halifax
                - Caracas
                - America/Caracas
                - Georgetown
                - America/Guyana
                - La Paz
                - America/La_Paz
                - Puerto Rico
                - America/Puerto_Rico
                - Santiago
                - America/Santiago
                - Newfoundland
                - America/St_Johns
                - Asuncion
                - America/Asuncion
                - Brasilia
                - America/Sao_Paulo
                - Buenos Aires
                - America/Argentina/Buenos_Aires
                - Montevideo
                - America/Montevideo
                - Greenland
                - America/Nuuk
                - Mid-Atlantic
                - Atlantic/South_Georgia
                - Azores
                - Atlantic/Azores
                - Cape Verde Is.
                - Atlantic/Cape_Verde
                - Casablanca
                - Africa/Casablanca
                - Dublin
                - Europe/Dublin
                - Edinburgh
                - Europe/London
                - Lisbon
                - Europe/Lisbon
                - London
                - Europe/London
                - Monrovia
                - Africa/Monrovia
                - UTC
                - Etc/UTC
                - Amsterdam
                - Europe/Amsterdam
                - Belgrade
                - Europe/Belgrade
                - Berlin
                - Europe/Berlin
                - Bern
                - Europe/Zurich
                - Bratislava
                - Europe/Bratislava
                - Brussels
                - Europe/Brussels
                - Budapest
                - Europe/Budapest
                - Copenhagen
                - Europe/Copenhagen
                - Ljubljana
                - Europe/Ljubljana
                - Madrid
                - Europe/Madrid
                - Paris
                - Europe/Paris
                - Prague
                - Europe/Prague
                - Rome
                - Europe/Rome
                - Sarajevo
                - Europe/Sarajevo
                - Skopje
                - Europe/Skopje
                - Stockholm
                - Europe/Stockholm
                - Vienna
                - Europe/Vienna
                - Warsaw
                - Europe/Warsaw
                - West Central Africa
                - Africa/Algiers
                - Zagreb
                - Europe/Zagreb
                - Zurich
                - Europe/Zurich
                - Athens
                - Europe/Athens
                - Bucharest
                - Europe/Bucharest
                - Cairo
                - Africa/Cairo
                - Harare
                - Africa/Harare
                - Helsinki
                - Europe/Helsinki
                - Jerusalem
                - Asia/Jerusalem
                - Kaliningrad
                - Europe/Kaliningrad
                - Pretoria
                - Africa/Johannesburg
                - Riga
                - Europe/Riga
                - Sofia
                - Europe/Sofia
                - Tallinn
                - Europe/Tallinn
                - Vilnius
                - Europe/Vilnius
                - Baghdad
                - Asia/Baghdad
                - Istanbul
                - Europe/Istanbul
                - Kuwait
                - Asia/Kuwait
                - Minsk
                - Europe/Minsk
                - Moscow
                - Europe/Moscow
                - Nairobi
                - Africa/Nairobi
                - Riyadh
                - Asia/Riyadh
                - St. Petersburg
                - Europe/Moscow
                - Volgograd
                - Europe/Volgograd
                - Tehran
                - Asia/Tehran
                - Abu Dhabi
                - Asia/Muscat
                - Baku
                - Asia/Baku
                - Muscat
                - Asia/Muscat
                - Samara
                - Europe/Samara
                - Tbilisi
                - Asia/Tbilisi
                - Yerevan
                - Asia/Yerevan
                - Kabul
                - Asia/Kabul
                - Almaty
                - Asia/Almaty
                - Astana
                - Asia/Almaty
                - Ekaterinburg
                - Asia/Yekaterinburg
                - Islamabad
                - Asia/Karachi
                - Karachi
                - Asia/Karachi
                - Tashkent
                - Asia/Tashkent
                - Chennai
                - Asia/Kolkata
                - Kolkata
                - Asia/Kolkata
                - Mumbai
                - Asia/Kolkata
                - New Delhi
                - Asia/Kolkata
                - Sri Jayawardenepura
                - Asia/Colombo
                - Kathmandu
                - Asia/Kathmandu
                - Dhaka
                - Asia/Dhaka
                - Urumqi
                - Asia/Urumqi
                - Bangkok
                - Asia/Bangkok
                - Hanoi
                - Asia/Bangkok
                - Jakarta
                - Asia/Jakarta
                - Krasnoyarsk
                - Asia/Krasnoyarsk
                - Novosibirsk
                - Asia/Novosibirsk
                - Beijing
                - Asia/Shanghai
                - Chongqing
                - Asia/Chongqing
                - Hong Kong
                - Asia/Hong_Kong
                - Irkutsk
                - Asia/Irkutsk
                - Kuala Lumpur
                - Asia/Kuala_Lumpur
                - Perth
                - Australia/Perth
                - Singapore
                - Asia/Singapore
                - Taipei
                - Asia/Taipei
                - Ulaanbaatar
                - Asia/Ulaanbaatar
                - Osaka
                - Asia/Tokyo
                - Sapporo
                - Asia/Tokyo
                - Seoul
                - Asia/Seoul
                - Tokyo
                - Asia/Tokyo
                - Yakutsk
                - Asia/Yakutsk
                - Adelaide
                - Australia/Adelaide
                - Darwin
                - Australia/Darwin
                - Brisbane
                - Australia/Brisbane
                - Canberra
                - Australia/Canberra
                - Guam
                - Pacific/Guam
                - Hobart
                - Australia/Hobart
                - Melbourne
                - Australia/Melbourne
                - Port Moresby
                - Pacific/Port_Moresby
                - Sydney
                - Australia/Sydney
                - Vladivostok
                - Asia/Vladivostok
                - Magadan
                - Asia/Magadan
                - New Caledonia
                - Pacific/Noumea
                - Solomon Is.
                - Pacific/Guadalcanal
                - Srednekolymsk
                - Asia/Srednekolymsk
                - Auckland
                - Pacific/Auckland
                - Fiji
                - Pacific/Fiji
                - Kamchatka
                - Asia/Kamchatka
                - Marshall Is.
                - Pacific/Majuro
                - Wellington
                - Pacific/Auckland
                - Chatham Is.
                - Pacific/Chatham
                - Nuku'alofa
                - Pacific/Tongatapu
                - Samoa
                - Pacific/Apia
                - Tokelau Is.
                - Pacific/Fakaofo
              nullable: true
            days:
              type: array
              items:
                type: string
                enum:
                  - M
                  - T
                  - W
                  - R
                  - F
                  - U
                  - S
              description: Business days
              nullable: true
            start_time:
              type: string
              description: Start time for business hours (HH:MM)
              nullable: true
            end_time:
              type: string
              description: End time for business hours (HH:MM)
              nullable: true
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - name
        - repeat_count
        - created_by_user_id
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).