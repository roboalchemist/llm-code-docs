# Source: https://docs.rootly.com/api-reference/alertsources/list-alert-sources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List alert sources

> List alert sources



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/alert_sources
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
  /v1/alert_sources:
    get:
      tags:
        - AlertSources
      summary: List alert sources
      description: List alert sources
      operationId: listAlertsSources
      parameters:
        - name: include
          in: query
          required: false
          schema:
            type: string
        - name: page[number]
          in: query
          required: false
          schema:
            type: integer
        - name: page[size]
          in: query
          required: false
          schema:
            type: integer
        - name: filter[search]
          in: query
          required: false
          schema:
            type: string
        - name: filter[statuses]
          in: query
          required: false
          schema:
            type: string
        - name: filter[source_types]
          in: query
          required: false
          schema:
            type: string
        - name: filter[name]
          in: query
          required: false
          schema:
            type: string
        - name: sort
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
                $ref: '#/components/schemas/alerts_source_list'
      security:
        - bearer_auth: []
components:
  schemas:
    alerts_source_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the alert source
              type:
                type: string
                enum:
                  - alert_sources
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/alerts_source'
            required:
              - id
              - type
              - attributes
        links:
          type: object
          allOf:
            - $ref: '#/components/schemas/links'
        meta:
          type: object
          allOf:
            - $ref: '#/components/schemas/meta'
      required:
        - data
        - links
        - meta
    alerts_source:
      type: object
      properties:
        name:
          type: string
          description: The name of the alert source
        source_type:
          type: string
          description: The alert source type
          enum:
            - email
            - app_dynamics
            - catchpoint
            - datadog
            - alertmanager
            - google_cloud
            - grafana
            - sentry
            - generic_webhook
            - cloud_watch
            - aws_sns
            - checkly
            - azure
            - new_relic
            - splunk
            - chronosphere
            - app_optics
            - bug_snag
            - honeycomb
            - monte_carlo
            - nagios
            - prtg
        alert_urgency_id:
          type: string
          description: ID for the default alert urgency assigned to this alert source
        deduplicate_alerts_by_key:
          type: boolean
          description: >-
            Toggle alert deduplication using deduplication key. If enabled,
            deduplication_key_kind and deduplication_key_path are required.
        deduplication_key_kind:
          type: string
          description: Kind of deduplication key.
          enum:
            - payload
        deduplication_key_path:
          type: string
          description: >-
            Path to deduplication key. This is a JSON Path to extract the
            deduplication key from the request body.
          nullable: true
        deduplication_key_regexp:
          type: string
          description: Regular expression to extract key from value found at key path.
          nullable: true
        owner_group_ids:
          type: array
          description: List of team IDs that will own the alert source
          items:
            type: string
        alert_template_attributes:
          type: object
          properties:
            title:
              type: string
              description: The alert title.
              nullable: true
            description:
              type: string
              description: The alert description.
              nullable: true
            external_url:
              type: string
              description: The alert URL.
              nullable: true
          nullable: true
        alert_source_urgency_rules_attributes:
          type: array
          description: >-
            List of rules that define the conditions under which the alert
            urgency will be set automatically based on the alert payload
          items:
            type: object
            properties:
              json_path:
                type: string
                description: >-
                  JSON path expression to extract a specific value from the
                  alert's payload for evaluation
                nullable: true
              operator:
                type: string
                description: >-
                  Comparison operator used to evaluate the extracted value
                  against the specified condition
                enum:
                  - is
                  - is_not
                  - contains
                  - does_not_contain
              value:
                type: string
                description: >-
                  Value that the extracted payload data is compared to using the
                  specified operator to determine a match
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
              kind:
                type: string
                description: The kind of the conditionable
                enum:
                  - payload
                  - alert_field
              alert_urgency_id:
                type: string
                description: The ID of the alert urgency
        sourceable_attributes:
          type: object
          description: Provide additional attributes for generic_webhook alerts source
          properties:
            auto_resolve:
              type: boolean
              description: >-
                Set this to true to auto-resolve alerts based on
                field_mappings_attributes conditions
            resolve_state:
              type: string
              description: >-
                This value is matched with the value extracted from alerts
                payload using JSON path in field_mappings_attributes
              nullable: true
            accept_threaded_emails:
              type: boolean
              description: Set this to false to reject threaded emails
            field_mappings_attributes:
              type: array
              description: Specify rules to auto resolve alerts
              items:
                type: object
                properties:
                  field:
                    type: string
                    description: Select the field on which the condition to be evaluated
                    enum:
                      - external_id
                      - state
                      - alert_title
                      - alert_description
                      - alert_external_url
                      - notification_target_type
                      - notification_target_id
                  json_path:
                    type: string
                    description: >-
                      JSON path expression to extract a specific value from the
                      alert's payload for evaluation
          nullable: true
        resolution_rule_attributes:
          type: object
          description: Provide additional attributes for email alerts source
          properties:
            enabled:
              type: boolean
              description: Set this to true to enable the auto resolution rule
            condition_type:
              type: string
              description: The type of condition to evaluate to apply auto resolution rule
              enum:
                - all
                - any
            identifier_matchable_type:
              type: string
              description: The type of the identifier matchable
              enum:
                - AlertField
              nullable: true
            identifier_matchable_id:
              type: string
              description: >-
                The ID of the identifier matchable. If identifier_matchable_type
                is AlertField, this is the ID of the alert field.
              nullable: true
            identifier_reference_kind:
              type: string
              description: The kind of the identifier reference
              enum:
                - payload
                - alert_field
            identifier_json_path:
              type: string
              description: >-
                JSON path expression to extract unique alert identifier used to
                match triggered alerts with resolving alerts
              nullable: true
            identifier_value_regex:
              type: string
              description: >-
                Regex group to further specify the part of the string used as a
                unique identifier
              nullable: true
            conditions_attributes:
              type: array
              description: List of conditions to evaluate for auto resolution
              items:
                type: object
                properties:
                  field:
                    type: string
                    description: >-
                      JSON path expression to extract a specific value from the
                      alert's payload for evaluation
                    nullable: true
                  operator:
                    type: string
                    description: >-
                      Comparison operator used to evaluate the extracted value
                      against the specified condition
                    enum:
                      - is
                      - is_not
                      - contains
                      - does_not_contain
                      - starts_with
                      - ends_with
                  value:
                    type: string
                    description: >-
                      Value that the extracted payload data is compared to using
                      the specified operator to determine a match
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
                  kind:
                    type: string
                    description: The kind of the conditionable
                    enum:
                      - payload
                      - alert_field
          nullable: true
        alert_source_fields_attributes:
          type: array
          description: >-
            List of alert fields to be added to the alert source. Note: This
            attribute requires the alert field feature to be enabled on your
            account. Contact Rootly customer support if you need assistance with
            this feature.
          items:
            type: object
            properties:
              alert_field_id:
                type: string
                description: The ID of the alert field
              template_body:
                type: string
                description: >-
                  Liquid expression to extract a specific value from the alert's
                  payload for evaluation
                nullable: true
        status:
          type: string
          description: The status of the alert source
          enum:
            - connected
            - setup_complete
            - setup_incomplete
        secret:
          type: string
          description: The secret used to authenticate non-email alert sources
        email:
          type: string
          description: The email generated for email alert sources
          nullable: true
        webhook_endpoint:
          type: string
          description: The webhook URL generated for non-email alert sources
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - name
        - status
        - secret
        - created_at
        - updated_at
    links:
      type: object
      properties:
        self:
          type: string
        first:
          type: string
        prev:
          type: string
          nullable: true
        next:
          type: string
          nullable: true
        last:
          type: string
      required:
        - self
        - first
        - prev
        - next
        - last
    meta:
      type: object
      properties:
        current_page:
          type: integer
        next_page:
          type: integer
          nullable: true
        prev_page:
          type: integer
          nullable: true
        total_count:
          type: integer
        total_pages:
          type: integer
      required:
        - current_page
        - next_page
        - prev_page
        - total_count
        - total_pages
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).