# Source: https://docs.rootly.com/api-reference/catalog-checklist-templates/list-catalog-checklist-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List catalog checklist templates

> List catalog checklist templates



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/catalog_checklist_templates
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
  /v1/catalog_checklist_templates:
    get:
      tags:
        - Catalog Checklist Templates
      summary: List catalog checklist templates
      description: List catalog checklist templates
      operationId: listCatalogChecklistTemplates
      parameters:
        - name: include
          in: query
          description: 'comma separated if needed. eg: template_fields,template_owners'
          schema:
            type: string
            enum:
              - template_fields
              - template_owners
          required: false
        - name: sort
          in: query
          description: 'comma separated if needed. eg: created_at,updated_at'
          schema:
            type: string
            enum:
              - created_at
              - '-created_at'
              - updated_at
              - '-updated_at'
              - name
              - '-name'
          required: false
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
        - name: filter[name]
          in: query
          required: false
          schema:
            type: string
        - name: filter[slug]
          in: query
          required: false
          schema:
            type: string
        - name: filter[catalog_type]
          in: query
          required: false
          schema:
            type: string
        - name: filter[scope_type]
          in: query
          required: false
          schema:
            type: string
        - name: filter[created_at][gt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[created_at][gte]
          in: query
          required: false
          schema:
            type: string
        - name: filter[created_at][lt]
          in: query
          required: false
          schema:
            type: string
        - name: filter[created_at][lte]
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: returns empty list for another team
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/catalog_checklist_template_list'
        '404':
          description: returns 404 when feature flag is disabled
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    catalog_checklist_template_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the checklist template
              type:
                type: string
                enum:
                  - catalog_checklist_templates
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/catalog_checklist_template'
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
    catalog_checklist_template:
      type: object
      properties:
        name:
          type: string
          description: The name of the checklist template
        slug:
          type: string
          description: The slug of the checklist template
        description:
          type: string
          description: The description of the checklist template
          nullable: true
        catalog_type:
          type: string
          description: The catalog type
          enum:
            - Service
            - Functionality
            - Environment
            - Group
            - Cause
            - IncidentType
            - Catalog
        scope_type:
          type: string
          description: The scope type
          enum:
            - Team
            - Catalog
        scope_id:
          type: string
          description: The scope ID
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        template_fields:
          type: array
          description: Template fields
          nullable: true
          items:
            type: object
            properties:
              data:
                type: object
                properties:
                  id:
                    type: string
                    description: ID of the template field
                  type:
                    type: string
                    enum:
                      - catalog_checklist_template_fields
                  attributes:
                    type: object
                    properties:
                      field_source:
                        type: string
                        description: Source of the field
                        enum:
                          - builtin
                          - custom
                      field_key:
                        type: string
                        description: Key identifying the field
                      position:
                        type: integer
                        description: Position of the field
                      catalog_field_id:
                        type: string
                        description: ID of the catalog field
                        nullable: true
                      created_at:
                        type: string
                        description: Date of creation
                      updated_at:
                        type: string
                        description: Date of last update
        template_owners:
          type: array
          description: Template owners
          nullable: true
          items:
            type: object
            properties:
              data:
                type: object
                properties:
                  id:
                    type: string
                    description: ID of the template owner
                  type:
                    type: string
                    enum:
                      - catalog_checklist_template_owners
                  attributes:
                    type: object
                    properties:
                      owner_type:
                        type: string
                        description: Type of owner
                        enum:
                          - field
                          - user
                      owner_field_key:
                        type: string
                        description: Field key for field-based owners
                        nullable: true
                      owner_user_id:
                        type: integer
                        description: User ID for user-based owners
                        nullable: true
                      created_at:
                        type: string
                        description: Date of creation
                      updated_at:
                        type: string
                        description: Date of last update
      required:
        - name
        - catalog_type
        - scope_type
        - scope_id
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