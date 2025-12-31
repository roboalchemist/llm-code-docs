# Source: https://getlago.com/docs/api-reference/entitlements/features/get-all-features.md

# List all features

> This endpoint retrieves all existing features that represent entitlement components of your application.

## OpenAPI

````yaml GET /features
paths:
  path: /features
  method: get
  servers:
    - url: https://api.getlago.com/api/v1
      description: US Lago cluster
    - url: https://api.eu.getlago.com/api/v1
      description: EU Lago cluster
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        page:
          schema:
            - type: integer
              required: false
              description: Page number.
              example: 1
          explode: true
        per_page:
          schema:
            - type: integer
              required: false
              description: Number of records per page.
              example: 20
          explode: true
        search_term:
          schema:
            - type: string
              required: false
              description: Search in name, code and description.
          explode: true
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              features:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/FeatureObject'
              meta:
                allOf:
                  - $ref: '#/components/schemas/PaginationMeta'
            refIdentifier: '#/components/schemas/FeaturesPaginated'
            requiredProperties:
              - features
              - meta
        examples:
          example:
            value:
              features:
                - code: seats
                  name: Number of seats
                  description: Number of users of the account
                  privileges:
                    - code: max
                      name: Maximum
                      value_type: integer
                      config: {}
                    - code: max_admins
                      name: Max Admins
                      value_type: integer
                      config: {}
                    - code: root
                      name: Allow root user
                      value_type: boolean
                      config: {}
                    - code: provider
                      name: SSO Provider
                      value_type: select
                      config:
                        select_options:
                          - google
                          - okta
                  created_at: '2025-07-17T12:34:35Z'
              meta:
                current_page: 2
                next_page: 3
                prev_page: 1
                total_pages: 4
                total_count: 70
        description: List of features
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 401
              error:
                allOf:
                  - type: string
                    example: Unauthorized
            refIdentifier: '#/components/schemas/ApiErrorUnauthorized'
            requiredProperties:
              - status
              - error
        examples:
          example:
            value:
              status: 401
              error: Unauthorized
        description: Unauthorized error
  deprecated: false
  type: path
components:
  schemas:
    PaginationMeta:
      type: object
      required:
        - current_page
        - total_pages
        - total_count
      properties:
        current_page:
          type: integer
          description: Current page.
          example: 2
        next_page:
          type:
            - integer
            - 'null'
          description: Next page.
          example: 3
        prev_page:
          type:
            - integer
            - 'null'
          description: Previous page.
          example: 1
        total_pages:
          type: integer
          description: Total number of pages.
          example: 4
        total_count:
          type: integer
          description: Total number of records.
          example: 70
    FeaturePrivilegeObject:
      type: object
      required:
        - code
        - name
        - value_type
        - config
      properties:
        code:
          type: string
          example: max
          description: Unique code for the privilege.
        name:
          type:
            - string
            - 'null'
          example: Maximum
          description: Display name for the privilege.
        value_type:
          type: string
          enum:
            - integer
            - boolean
            - string
            - select
          example: integer
          description: 'Data type of the privilege value. Default: string'
        config:
          type: object
          properties:
            select_options:
              type: array
              items:
                type: string
              example:
                - google
                - okta
              description: Array of string, required only when value_type is `select`.
    FeatureObject:
      type: object
      required:
        - code
        - name
        - description
        - privileges
        - created_at
      properties:
        code:
          type: string
          example: seats
          description: Unique code used to identify the feature. Max 255 characters.
        name:
          type:
            - string
            - 'null'
          example: Number of seats
          description: Name of the feature. Max 255 characters.
        description:
          type:
            - string
            - 'null'
          example: Number of users of the account
          description: Description of the feature. Max 600 characters.
        privileges:
          type: array
          items:
            $ref: '#/components/schemas/FeaturePrivilegeObject'
          example:
            - code: max
              name: Maximum
              value_type: integer
              config: {}
            - code: max_admins
              name: Max Admins
              value_type: integer
              config: {}
            - code: root
              name: Allow root user
              value_type: boolean
              config: {}
            - code: provider
              name: SSO Provider
              value_type: select
              config:
                select_options:
                  - google
                  - okta
          description: Privileges associated with this feature. Can be empty.
        created_at:
          type: string
          format: date-time
          example: '2025-07-17T12:34:35Z'
          description: Creation date of the feature.

````