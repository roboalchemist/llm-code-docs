# Source: https://docs.rootly.com/api-reference/teams/list-catalog-properties.md

# Source: https://docs.rootly.com/api-reference/services/list-catalog-properties.md

# Source: https://docs.rootly.com/api-reference/incidenttypes/list-catalog-properties.md

# Source: https://docs.rootly.com/api-reference/functionalities/list-catalog-properties.md

# Source: https://docs.rootly.com/api-reference/environments/list-catalog-properties.md

# Source: https://docs.rootly.com/api-reference/causes/list-catalog-properties.md

# Source: https://docs.rootly.com/api-reference/catalogentityproperties/list-catalog-properties.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List catalog properties

> **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to retrieve field values instead.

List Catalog Entity Properties.



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/catalog_entities/{catalog_entity_id}/properties
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
  /v1/catalog_entities/{catalog_entity_id}/properties:
    parameters:
      - name: catalog_entity_id
        in: path
        required: true
        schema:
          type: string
    get:
      tags:
        - CatalogEntityProperties
      summary: List catalog properties
      description: >-
        **Deprecated:** This endpoint is deprecated, please use `include=fields`
        on catalog entities or native catalog endpoints (teams, services,
        functionalities, incident_types, causes, environments) to retrieve field
        values instead.


        List Catalog Entity Properties.
      operationId: listCatalogEntityProperties
      parameters:
        - name: include
          in: query
          description: 'comma separated if needed. eg: catalog_entity,catalog_field'
          schema:
            type: string
            enum:
              - catalog_entity
              - catalog_field
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
        - name: filter[catalog_field_id]
          in: query
          required: false
          schema:
            type: string
        - name: filter[key]
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
          description: success
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/catalog_entity_property_list'
      deprecated: true
      security:
        - bearer_auth: []
components:
  schemas:
    catalog_entity_property_list:
      type: object
      description: >-
        **Deprecated:** This endpoint is deprecated, please use `include=fields`
        on catalog entities or native catalog endpoints (teams, services,
        functionalities, incident_types, causes, environments) to retrieve field
        values instead.
      deprecated: true
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the catalog_entity_property
              type:
                type: string
                enum:
                  - catalog_entity_properties
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/catalog_entity_property'
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
    catalog_entity_property:
      type: object
      description: >-
        **Deprecated:** This endpoint is deprecated, please use `include=fields`
        on catalog entities or native catalog endpoints (teams, services,
        functionalities, incident_types, causes, environments) to retrieve field
        values instead.
      deprecated: true
      properties:
        catalog_entity_id:
          type: string
        catalog_field_id:
          type: string
        key:
          type: string
          enum:
            - text
            - catalog_entity
        value:
          type: string
        created_at:
          type: string
        updated_at:
          type: string
      required:
        - catalog_entity_id
        - catalog_field_id
        - key
        - value
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