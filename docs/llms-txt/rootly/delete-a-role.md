# Source: https://docs.rootly.com/api-reference/roles/delete-a-role.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a role

> Delete a specific role by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json delete /v1/roles/{id}
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
  /v1/roles/{id}:
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
        - Roles
      summary: Delete a role
      description: Delete a specific role by id
      operationId: deleteRole
      responses:
        '200':
          description: role deleted
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/role_response'
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
    role_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the role
            type:
              type: string
              enum:
                - roles
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/role'
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
    role:
      type: object
      properties:
        name:
          type: string
          description: The role name.
        slug:
          type: string
          description: The role slug.
        incident_permission_set_id:
          type: string
          description: Associated incident permissions set.
          nullable: true
        is_deletable:
          type: boolean
          description: Whether the role can be deleted.
        is_editable:
          type: boolean
          description: Whether the role can be edited.
        alerts_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
        api_keys_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        audits_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        billing_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        environments_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        form_fields_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        functionalities_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        groups_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        incident_causes_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        incident_feedbacks_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        incident_roles_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        incident_types_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        incidents_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        integrations_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        invitations_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        playbooks_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        private_incidents_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        pulses_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - update
              - read
        retrospective_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        roles_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        secrets_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        services_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        severities_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        status_pages_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        webhooks_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        workflows_permissions:
          type: array
          items:
            type: string
            enum:
              - create
              - read
              - update
              - delete
        created_at:
          type: string
        updated_at:
          type: string
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