# Source: https://docs.rootly.com/api-reference/workflowformfieldconditions/list-workflow-form-field-conditions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List workflow form field conditions

> List workflow form field conditions



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/workflows/{workflow_id}/form_field_conditions
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
  /v1/workflows/{workflow_id}/form_field_conditions:
    parameters:
      - name: workflow_id
        in: path
        required: true
        schema:
          type: string
    get:
      tags:
        - WorkflowFormFieldConditions
      summary: List workflow form field conditions
      description: List workflow form field conditions
      operationId: listWorkflowFormFieldConditions
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
      responses:
        '200':
          description: success
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/workflow_form_field_condition_list'
      security:
        - bearer_auth: []
components:
  schemas:
    workflow_form_field_condition_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the workflow_form_field_condition
              type:
                type: string
                enum:
                  - workflow_form_field_conditions
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/workflow_form_field_condition'
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
    workflow_form_field_condition:
      type: object
      properties:
        workflow_id:
          type: string
          description: The workflow for this condition
        form_field_id:
          type: string
          description: The custom field for this condition
        incident_condition:
          type: string
          description: The trigger condition
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
        values:
          type: array
          items:
            type: string
            description: The value to associate with the custom field trigger
        selected_catalog_entity_ids:
          type: array
          items:
            type: string
            description: The selected catalog entities for select and multi_select kinds
        selected_functionality_ids:
          type: array
          items:
            type: string
            description: The selected functionalities for select and multi_select kinds
        selected_group_ids:
          type: array
          items:
            type: string
            description: The selected groups (teams) for select and multi_select kinds
        selected_option_ids:
          type: array
          items:
            type: string
            description: The selected option id for select and multi_select kinds
        selected_service_ids:
          type: array
          items:
            type: string
            description: The selected services for select and multi_select kinds
        selected_user_ids:
          type: array
          items:
            type: integer
            description: The selected user id for select and multi_select kinds
        selected_cause_ids:
          type: array
          items:
            type: string
            description: The selected causes for select and multi_select kinds
        selected_environment_ids:
          type: array
          items:
            type: string
            description: The selected environments for select and multi_select kinds
        selected_incident_type_ids:
          type: array
          items:
            type: string
            description: The selected incident types for select and multi_select kinds
      required:
        - workflow_id
        - form_field_id
        - incident_condition
        - selected_catalog_entity_ids
        - selected_option_ids
        - selected_user_ids
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