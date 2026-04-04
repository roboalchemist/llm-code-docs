# Source: https://docs.rootly.com/api-reference/workflows/delete-a-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a workflow

> Delete a specific workflow by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json delete /v1/workflows/{id}
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
  /v1/workflows/{id}:
    parameters:
      - name: id
        in: path
        schema:
          anyOf:
            - type: string
              format: uuid
              description: Resource UUID
            - type: string
              pattern: ^[a-z0-9_-]+$
              description: Resource slug
        required: true
    delete:
      tags:
        - Workflows
      summary: Delete a workflow
      description: Delete a specific workflow by id
      operationId: deleteWorkflow
      responses:
        '200':
          description: admin can destroy locked workflow
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/workflow_response'
        '404':
          description: non-admin can't destroy locked workflow
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    workflow_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the workflow
            type:
              type: string
              enum:
                - workflows
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/workflow'
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
    workflow:
      type: object
      properties:
        name:
          type: string
          description: The title of the workflow
        slug:
          type: string
          description: The slug of the workflow
        description:
          type: string
          description: The description of the workflow
          nullable: true
        command:
          type: string
          description: Workflow command
          nullable: true
        command_feedback_enabled:
          type: boolean
          description: This will notify you back when the workflow is starting
          nullable: true
        wait:
          type: string
          description: Wait this duration before executing
          nullable: true
        repeat_every_duration:
          type: string
          description: Repeat workflow every duration
          nullable: true
        repeat_condition_duration_since_first_run:
          type: string
          description: >-
            The workflow will stop repeating if its runtime since it's first
            workflow run exceeds the duration set in this field
          nullable: true
        repeat_condition_number_of_repeats:
          type: integer
          description: >-
            The workflow will stop repeating if the number of repeats exceeds
            the value set in this field
        continuously_repeat:
          type: boolean
          description: >-
            When continuously repeat is true, repeat workflows aren't
            automatically stopped when conditions aren't met. This setting won't
            override your conditions set by
            repeat_condition_duration_since_first_run and
            repeat_condition_number_of_repeats parameters.
        repeat_on:
          type: array
          items:
            type: string
            description: Repeat on weekdays
            enum:
              - S
              - M
              - T
              - W
              - R
              - F
              - U
          nullable: true
        enabled:
          type: boolean
        locked:
          type: boolean
          description: >-
            Restricts workflow edits to admins when turned on. Only admins can
            set this field.
        position:
          type: integer
          description: The order which the workflow should run with other workflows.
        workflow_group_id:
          type: string
          description: The group this workflow belongs to.
          nullable: true
        trigger_params:
          oneOf:
            - $ref: '#/components/schemas/incident_trigger_params'
            - $ref: '#/components/schemas/action_item_trigger_params'
            - $ref: '#/components/schemas/alert_trigger_params'
            - $ref: '#/components/schemas/pulse_trigger_params'
            - $ref: '#/components/schemas/simple_trigger_params'
        environment_ids:
          type: array
          items:
            type: string
        severity_ids:
          type: array
          items:
            type: string
        incident_type_ids:
          type: array
          items:
            type: string
        incident_role_ids:
          type: array
          items:
            type: string
        service_ids:
          type: array
          items:
            type: string
        functionality_ids:
          type: array
          items:
            type: string
        group_ids:
          type: array
          items:
            type: string
        cause_ids:
          type: array
          items:
            type: string
        sub_status_ids:
          type: array
          items:
            type: string
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
    incident_trigger_params:
      type: object
      properties:
        trigger_type:
          type: string
          enum:
            - incident
        triggers:
          type: array
          items:
            type: string
            description: >-
              Actions that trigger the workflow. One of
              custom_fields.<slug>.updated, incident_in_triage,
              incident_created, incident_started, incident_updated,
              title_updated, summary_updated, status_updated, severity_updated,
              environments_added, environments_removed, environments_updated,
              incident_types_added, incident_types_removed,
              incident_types_updated, services_added, services_removed,
              services_updated, visibility_updated, functionalities_added,
              functionalities_removed, functionalities_updated, teams_added,
              teams_removed, teams_updated, causes_added, causes_removed,
              causes_updated, timeline_updated, status_page_timeline_updated,
              role_assignments_updated, role_assignments_added,
              role_assignments_removed, slack_command, slack_channel_created,
              slack_channel_converted, microsoft_teams_channel_created,
              microsoft_teams_chat_created, subscribers_updated,
              subscribers_added, subscribers_removed, user_joined_slack_channel,
              user_left_slack_channel
        incident_visibilities:
          type: array
          items:
            type: boolean
        incident_kinds:
          type: array
          items:
            type: string
            enum:
              - test
              - test_sub
              - example
              - example_sub
              - normal
              - normal_sub
              - backfilled
              - scheduled
              - scheduled_sub
        incident_statuses:
          type: array
          items:
            type: string
            enum:
              - in_triage
              - started
              - detected
              - acknowledged
              - mitigated
              - resolved
              - closed
              - cancelled
              - scheduled
              - in_progress
              - completed
        incident_inactivity_duration:
          anyOf:
            - enum:
                - null
            - type: string
              description: ex. 10 min, 1h, 3 days, 2 weeks
        incident_condition:
          type: string
          enum:
            - ALL
            - ANY
            - NONE
          default: ALL
        incident_condition_visibility:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_kind:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: IS
        incident_condition_status:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_sub_status:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_environment:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_severity:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_incident_type:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_incident_roles:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_service:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_functionality:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_group:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_cause:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_post_mortem_condition_cause:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
          description: '[DEPRECATED] Use incident_condition_cause instead'
        incident_condition_summary:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_started_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_detected_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_acknowledged_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_mitigated_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_resolved_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_conditional_inactivity:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - IS
      required:
        - trigger_type
    action_item_trigger_params:
      type: object
      properties:
        trigger_type:
          type: string
          enum:
            - action_item
        triggers:
          type: array
          items:
            type: string
            description: >-
              Actions that trigger the workflow. One of
              custom_fields.<slug>.updated, incident_updated,
              action_item_created, action_item_updated, assigned_user_updated,
              summary_updated, description_updated, status_updated,
              priority_updated, due_date_updated, teams_updated, slack_command
        incident_visibilities:
          type: array
          items:
            type: boolean
        incident_kinds:
          type: array
          items:
            type: string
            enum:
              - test
              - test_sub
              - example
              - example_sub
              - normal
              - normal_sub
              - backfilled
              - scheduled
              - scheduled_sub
        incident_statuses:
          type: array
          items:
            type: string
            enum:
              - in_triage
              - started
              - detected
              - acknowledged
              - mitigated
              - resolved
              - closed
              - cancelled
              - scheduled
              - in_progress
              - completed
        incident_inactivity_duration:
          anyOf:
            - enum:
                - null
            - type: string
              description: ex. 10 min, 1h, 3 days, 2 weeks
        incident_condition:
          type: string
          enum:
            - ALL
            - ANY
            - NONE
          default: ALL
        incident_condition_visibility:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_kind:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: IS
        incident_condition_status:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_sub_status:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_environment:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_severity:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_incident_type:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_incident_roles:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_service:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_functionality:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_group:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_condition_summary:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_started_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_detected_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_acknowledged_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_mitigated_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_condition_resolved_at:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - SET
                - UNSET
        incident_conditional_inactivity:
          anyOf:
            - enum:
                - null
            - type: string
              enum:
                - IS
        incident_action_item_condition:
          type: string
          enum:
            - ALL
            - ANY
            - NONE
        incident_action_item_condition_kind:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_action_item_kinds:
          type: array
          items:
            type: string
            enum:
              - task
              - follow_up
        incident_action_item_condition_status:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_action_item_statuses:
          type: array
          items:
            type: string
            enum:
              - open
              - in_progress
              - cancelled
              - done
        incident_action_item_condition_priority:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_action_item_priorities:
          type: array
          items:
            type: string
            enum:
              - high
              - medium
              - low
        incident_action_item_condition_group:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        incident_action_item_group_ids:
          type: array
          items:
            type: string
      required:
        - trigger_type
    alert_trigger_params:
      type: object
      properties:
        trigger_type:
          type: string
          enum:
            - alert
        triggers:
          type: array
          items:
            type: string
            description: Actions that trigger the workflow
            enum:
              - alert_created
              - alert_status_updated
        alert_condition:
          type: string
          enum:
            - ALL
            - ANY
            - NONE
        alert_condition_source:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        alert_condition_source_use_regexp:
          type: boolean
          default: false
        alert_sources:
          type: array
          items:
            type: string
        alert_condition_label:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        alert_condition_label_use_regexp:
          type: boolean
          default: false
        alert_condition_status:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        alert_condition_status_use_regexp:
          type: boolean
          default: false
        alert_statuses:
          type: array
          items:
            type: string
        alert_labels:
          type: array
          items:
            type: string
        alert_condition_payload:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        alert_condition_payload_use_regexp:
          type: boolean
          default: false
        alert_payload:
          type: array
          items:
            type: string
        alert_query_payload:
          type: string
          description: 'You can use jsonpath syntax. eg: $.incident.teams[*]'
          nullable: true
        alert_field_conditions:
          type: array
          items:
            type: object
            properties:
              alert_field_id:
                type: string
              condition_type:
                type: string
                enum:
                  - IS
                  - IS NOT
                  - ANY
                  - CONTAINS
                  - CONTAINS_ALL
                  - CONTAINS_NONE
                  - NONE
                  - SET
                  - UNSET
              values:
                type: array
                items:
                  type: string
            required:
              - alert_field_id
              - condition_type
        alert_payload_conditions:
          type: object
          properties:
            logic:
              type: string
              enum:
                - ALL
                - ANY
                - NONE
            conditions:
              type: array
              items:
                type: object
                properties:
                  query:
                    type: string
                  operator:
                    type: string
                    enum:
                      - IS
                      - IS NOT
                      - ANY
                      - CONTAINS
                      - CONTAINS_ALL
                      - CONTAINS_NONE
                      - NONE
                      - SET
                      - UNSET
                  values:
                    type: array
                    items:
                      type: string
                  use_regexp:
                    type: boolean
                required:
                  - query
                  - operator
      required:
        - trigger_type
    pulse_trigger_params:
      type: object
      properties:
        trigger_type:
          type: string
          enum:
            - pulse
        triggers:
          type: array
          items:
            type: string
            description: Actions that trigger the workflow
            enum:
              - pulse_created
        pulse_condition:
          type: string
          enum:
            - ALL
            - ANY
            - NONE
        pulse_condition_source:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        pulse_condition_source_use_regexp:
          type: boolean
          default: false
        pulse_sources:
          type: array
          items:
            type: string
        pulse_condition_label:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        pulse_condition_label_use_regexp:
          type: boolean
          default: false
        pulse_labels:
          type: array
          items:
            type: string
        pulse_condition_payload:
          type: string
          enum:
            - IS
            - IS NOT
            - ANY
            - CONTAINS
            - CONTAINS_ALL
            - CONTAINS_NONE
            - NONE
            - SET
            - UNSET
          default: ANY
        pulse_condition_payload_use_regexp:
          type: boolean
          default: false
        pulse_payload:
          type: array
          items:
            type: string
        pulse_query_payload:
          type: string
          description: 'You can use jsonpath syntax. eg: $.incident.teams[*]'
          nullable: true
      required:
        - trigger_type
    simple_trigger_params:
      type: object
      properties:
        trigger_type:
          type: string
          enum:
            - simple
        triggers:
          type: array
          items:
            type: string
            description: Actions that trigger the workflow
            enum:
              - slack_command
      required:
        - trigger_type
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).