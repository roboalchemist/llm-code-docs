# Source: https://docs.rootly.com/api-reference/formfields/delete-a-form-field.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Form Field

> Delete a specific form_field by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json delete /v1/form_fields/{id}
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
  /v1/form_fields/{id}:
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
        - FormFields
      summary: Delete a Form Field
      description: Delete a specific form_field by id
      operationId: deleteFormField
      responses:
        '200':
          description: form_field deleted
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/form_field_response'
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
    form_field_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the form field
            type:
              type: string
              enum:
                - form_fields
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/form_field'
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
    form_field:
      type: object
      properties:
        kind:
          type: string
          description: The kind of the form field
          enum:
            - custom
            - title
            - summary
            - mitigation_message
            - resolution_message
            - severity
            - environments
            - types
            - services
            - causes
            - functionalities
            - teams
            - visibility
            - mark_as_test
            - mark_as_backfilled
            - labels
            - notify_emails
            - trigger_manual_workflows
            - show_ongoing_incidents
            - attach_alerts
            - mark_as_in_triage
            - in_triage_at
            - started_at
            - detected_at
            - acknowledged_at
            - mitigated_at
            - resolved_at
            - closed_at
            - custom_sub_status
            - manual_starting_datetime_field
        input_kind:
          type: string
          description: The input kind of the form field
          enum:
            - text
            - textarea
            - select
            - multi_select
            - date
            - datetime
            - number
            - checkbox
            - tags
            - rich_text
        value_kind:
          type: string
          description: The value kind of the form field
          enum:
            - inherit
            - group
            - service
            - functionality
            - user
            - catalog_entity
            - environment
            - cause
            - incident_type
        value_kind_catalog_id:
          type: string
          description: The ID of the catalog used when value_kind is `catalog_entity`
          nullable: true
        name:
          type: string
          description: The name of the form field
        slug:
          type: string
          description: The slug of the form field
        description:
          type: string
          description: The description of the form field
          nullable: true
        shown:
          type: array
          items:
            type: string
            description: >-
              Where the form field is shown. Add custom forms using the custom
              form's `slug` field. Or choose a built-in form:
              `web_new_incident_form`, `web_update_incident_form`,
              `web_incident_post_mortem_form`, `web_incident_mitigation_form`,
              `web_incident_resolution_form`, `web_incident_cancellation_form`,
              `web_scheduled_incident_form`,
              `web_update_scheduled_incident_form`, `incident_post_mortem`,
              `slack_new_incident_form`, `slack_update_incident_form`,
              `slack_update_incident_status_form`,
              `slack_incident_mitigation_form`,
              `slack_incident_resolution_form`,
              `slack_incident_cancellation_form`,
              `slack_scheduled_incident_form`,
              `slack_update_scheduled_incident_form`
        required:
          type: array
          items:
            type: string
            description: >-
              Where the form field is required. Add custom forms using the
              custom form's `slug` field. Or choose a built-in form:
              `web_new_incident_form`, `web_update_incident_form`,
              `web_incident_post_mortem_form`, `web_incident_mitigation_form`,
              `web_incident_resolution_form`, `web_incident_cancellation_form`,
              `web_scheduled_incident_form`,
              `web_update_scheduled_incident_form`, `slack_new_incident_form`,
              `slack_update_incident_form`, `slack_update_incident_status_form`,
              `slack_incident_mitigation_form`,
              `slack_incident_resolution_form`,
              `slack_incident_cancellation_form`,
              `slack_scheduled_incident_form`,
              `slack_update_scheduled_incident_form`
        show_on_incident_details:
          type: boolean
          description: Whether the form field is shown on the incident details panel
        enabled:
          type: boolean
          description: Whether the form field is enabled
        default_values:
          type: array
          items:
            type: string
            description: The default values.
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        auto_set_by_catalog_property_id:
          type: string
          description: Catalog property ID to auto-set this form field.
          nullable: true
      required:
        - kind
        - input_kind
        - value_kind
        - name
        - shown
        - required
        - default_values
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).