# Source: https://docs.rootly.com/api-reference/statuspages/list-status-pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List status pages

> List status pages



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/status-pages
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
  /v1/status-pages:
    get:
      tags:
        - StatusPages
      summary: List status pages
      description: List status pages
      operationId: listStatusPages
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
                $ref: '#/components/schemas/status_page_list'
      security:
        - bearer_auth: []
components:
  schemas:
    status_page_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the status page
              type:
                type: string
                enum:
                  - status_pages
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/status_page'
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
    status_page:
      type: object
      properties:
        title:
          type: string
          description: The title of the status page
        slug:
          type: string
          description: The slug of the status page
        public_title:
          type: string
          description: The public title of the status page
          nullable: true
        description:
          type: string
          description: The description of the status page
          nullable: true
        public_description:
          type: string
          description: The public description of the status page
          nullable: true
        header_color:
          type: string
          description: The color of the header. Eg. "#0061F2"
          nullable: true
        footer_color:
          type: string
          description: The color of the footer. Eg. "#1F2F41"
          nullable: true
        allow_search_engine_index:
          type: boolean
          description: >-
            Allow search engines to include your public status page in search
            results
          nullable: true
        show_uptime:
          type: boolean
          description: Show uptime
          nullable: true
        show_uptime_last_days:
          type: integer
          description: Show uptime over x days
          enum:
            - 30
            - 60
            - 90
          nullable: true
        success_message:
          type: string
          description: Message showing when all components are operational
          nullable: true
        failure_message:
          type: string
          description: Message showing when at least one component is not operational
          nullable: true
        authentication_method:
          type: string
          description: Authentication method
          enum:
            - none
            - password
            - saml
          default: none
          nullable: true
        authentication_enabled:
          type: boolean
          description: >-
            Enable authentication (deprecated - use authentication_method
            instead)
          nullable: true
          default: false
          deprecated: true
        authentication_password:
          type: string
          description: Authentication password
          nullable: true
        saml_idp_sso_service_url:
          type: string
          description: SAML IdP SSO service URL
          nullable: true
        saml_idp_slo_service_url:
          type: string
          description: SAML IdP SLO service URL
          nullable: true
        saml_idp_cert:
          type: string
          description: SAML IdP certificate
          nullable: true
        saml_idp_cert_fingerprint:
          type: string
          description: SAML IdP certificate fingerprint
          nullable: true
        saml_name_identifier_format:
          type: string
          description: SAML name identifier format
          enum:
            - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
            - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
            - urn:oasis:names:tc:SAML:2.0:nameid-format:transient
            - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
          nullable: true
        section_order:
          type: array
          description: Order of sections on the status page
          items:
            type: string
            enum:
              - maintenance
              - system_status
              - incidents
          nullable: true
        website_url:
          type: string
          description: Website URL
          nullable: true
        website_privacy_url:
          type: string
          description: Website Privacy URL
          nullable: true
        website_support_url:
          type: string
          description: Website Support URL
          nullable: true
        ga_tracking_id:
          type: string
          description: Google Analytics tracking ID
          nullable: true
        time_zone:
          type: string
          description: A valid IANA time zone name.
          default: Etc/UTC
          nullable: true
        public:
          type: boolean
          description: Make the status page accessible to the public
          nullable: true
        service_ids:
          type: array
          items:
            type: string
          description: Services attached to the status page
        functionality_ids:
          type: array
          items:
            type: string
          description: Functionalities attached to the status page
        external_domain_names:
          type: array
          items:
            type: string
          description: External domain names attached to the status page
        enabled:
          type: boolean
          description: Enabled / Disable the status page
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - title
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