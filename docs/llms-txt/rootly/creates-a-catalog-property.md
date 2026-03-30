# Source: https://docs.rootly.com/api-reference/teams/creates-a-catalog-property.md

# Source: https://docs.rootly.com/api-reference/services/creates-a-catalog-property.md

# Source: https://docs.rootly.com/api-reference/incidenttypes/creates-a-catalog-property.md

# Source: https://docs.rootly.com/api-reference/functionalities/creates-a-catalog-property.md

# Source: https://docs.rootly.com/api-reference/environments/creates-a-catalog-property.md

# Source: https://docs.rootly.com/api-reference/causes/creates-a-catalog-property.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creates a Catalog Property

> Creates a new Catalog Property from provided data



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json post /v1/causes/properties
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
  /v1/causes/properties:
    post:
      tags:
        - Causes
      summary: Creates a Catalog Property
      description: Creates a new Catalog Property from provided data
      operationId: createCauseCatalogProperty
      parameters: []
      requestBody:
        content:
          application/vnd.api+json:
            schema:
              $ref: '#/components/schemas/new_catalog_property'
        required: true
      responses:
        '201':
          description: catalog_property created ignores wrong catalog_type attribute
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/catalog_property_response'
        '401':
          description: responds with unauthorized for invalid token
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
        '422':
          description: exceeds max fields per catalog
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    new_catalog_property:
      type: object
      description: A catalog can have a maximum of 50 properties.
      properties:
        data:
          type: object
          properties:
            type:
              type: string
              enum:
                - catalog_properties
            attributes:
              type: object
              properties:
                name:
                  type: string
                kind:
                  type: string
                  enum:
                    - text
                    - reference
                    - boolean
                    - reference
                    - service
                    - functionality
                    - environment
                    - group
                    - cause
                    - incident_type
                    - user
                kind_catalog_id:
                  type: string
                  description: Restricts values to items of specified catalog.
                  nullable: true
                multiple:
                  type: boolean
                  description: Whether the attribute accepts multiple values.
                position:
                  type: integer
                  description: Default position of the item when displayed in a list.
                  nullable: true
                required:
                  type: boolean
                  description: Whether the property is required.
                catalog_type:
                  type: string
                  description: The type of catalog the property belongs to.
                  enum:
                    - catalog
                    - cause
                    - environment
                    - functionality
                    - incident_type
                    - service
                    - team
              additionalProperties: false
              required:
                - name
                - kind
          required:
            - type
            - attributes
      required:
        - data
    catalog_property_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the catalog_property
            type:
              type: string
              enum:
                - catalog_properties
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/catalog_property'
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
    catalog_property:
      type: object
      properties:
        catalog_id:
          type: string
          nullable: true
        name:
          type: string
        slug:
          type: string
        kind:
          type: string
          enum:
            - text
            - reference
        kind_catalog_id:
          type: string
          description: Restricts values to items of specified catalog.
          nullable: true
        multiple:
          type: boolean
          description: Whether the attribute accepts multiple values.
        position:
          type: integer
          description: Default position of the item when displayed in a list.
          nullable: true
        created_at:
          type: string
        updated_at:
          type: string
        required:
          type: boolean
          description: Whether the property is required.
        catalog_type:
          type: string
          description: The type of catalog the property belongs to.
          enum:
            - catalog
            - cause
            - environment
            - functionality
            - incident_type
            - service
            - team
      required:
        - catalog_id
        - name
        - kind
        - multiple
        - position
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).