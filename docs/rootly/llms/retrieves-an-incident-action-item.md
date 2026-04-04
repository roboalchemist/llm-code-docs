# Source: https://docs.rootly.com/api-reference/incidentactionitems/retrieves-an-incident-action-item.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves an incident action item

> Retrieves a specific incident_action_item by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/action_items/{id}
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
  /v1/action_items/{id}:
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
    get:
      tags:
        - IncidentActionItems
      summary: Retrieves an incident action item
      description: Retrieves a specific incident_action_item by id
      operationId: getIncidentActionItems
      responses:
        '200':
          description: incident_action_item found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/incident_action_item_response'
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
    incident_action_item_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the action item
            type:
              type: string
              enum:
                - incident_action_items
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/incident_action_item'
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
    incident_action_item:
      type: object
      properties:
        summary:
          type: string
          description: The summary of the action item
        description:
          type: string
          description: The description of incident action item
          nullable: true
        kind:
          type: string
          description: The kind of the action item
          enum:
            - task
            - follow_up
        assigned_to:
          type: object
          allOf:
            - $ref: '#/components/schemas/user_flat_response'
          description: User assigned to this action item
          nullable: true
        assigned_to_group_ids:
          type: array
          description: IDs of groups you wish to assign this action item
          items:
            type: string
          nullable: true
        priority:
          type: string
          description: The priority of the action item
          enum:
            - high
            - medium
            - low
        status:
          type: string
          description: The status of the action item
          enum:
            - open
            - in_progress
            - cancelled
            - done
        due_date:
          type: string
          description: The due date of the action item
          nullable: true
        jira_issue_id:
          type: string
          description: The Jira issue ID.
          nullable: true
        jira_issue_key:
          type: string
          description: The Jira issue key.
          nullable: true
        jira_issue_url:
          type: string
          description: The Jira issue URL.
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - summary
        - created_at
        - updated_at
    user_flat_response:
      type: object
      description: Flat user object as returned by serializer
      properties:
        id:
          type: integer
          description: User ID
        email:
          type: string
          description: User email
        first_name:
          type: string
          description: User first name
          nullable: true
        last_name:
          type: string
          description: User last name
          nullable: true
        full_name:
          type: string
          description: User full name
          nullable: true
        full_name_with_team:
          type: string
          description: User full name with team
          nullable: true
        time_zone:
          type: string
          description: User time zone
          nullable: true
        created_at:
          type: string
          description: User creation timestamp
        updated_at:
          type: string
          description: User last update timestamp
      required:
        - id
        - email
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).