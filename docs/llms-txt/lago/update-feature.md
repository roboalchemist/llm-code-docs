# Source: https://getlago.com/docs/api-reference/entitlements/features/update-feature.md

# Update a feature

> This endpoint updates an existing feature representing an entitlement component of your application.

## OpenAPI

````yaml PUT /features/{code}
paths:
  path: /features/{code}
  method: put
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
      path:
        code:
          schema:
            - type: string
              required: true
              description: Code of the existing feature.
              example: seats
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              feature:
                allOf:
                  - $ref: '#/components/schemas/FeatureBaseInput'
            required: true
            refIdentifier: '#/components/schemas/FeatureUpdateInput'
            requiredProperties:
              - feature
        examples:
          example:
            value:
              feature:
                name: Number of seats
                description: Number of users of the account
                privileges:
                  - code: max
                    name: Maximum
                    value_type: integer
                  - code: max_admins
                    name: Max Admins
                    value_type: integer
                  - code: root
                    name: Allow root user
                    value_type: boolean
                  - code: provider
                    name: SSO Provider
                    value_type: select
                    config:
                      select_options:
                        - google
                        - okta
        description: Feature payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              feature:
                allOf:
                  - $ref: '#/components/schemas/FeatureObject'
            refIdentifier: '#/components/schemas/Feature'
            requiredProperties:
              - feature
        examples:
          example:
            value:
              feature:
                code: seats
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
        description: Feature updated
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 400
              error:
                allOf:
                  - type: string
                    example: Bad request
            refIdentifier: '#/components/schemas/ApiErrorBadRequest'
            requiredProperties:
              - status
              - error
        examples:
          example:
            value:
              status: 400
              error: Bad request
        description: Bad Request error
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
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 403
              error:
                allOf:
                  - type: string
                    example: Forbidden
              code:
                allOf:
                  - type: string
                    example: feature_unavailable
            refIdentifier: '#/components/schemas/ApiErrorForbidden'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 403
              error: Forbidden
              code: feature_unavailable
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 404
              error:
                allOf:
                  - type: string
                    example: Not Found
              code:
                allOf:
                  - type: string
                    example: object_not_found
            refIdentifier: '#/components/schemas/ApiErrorNotFound'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 404
              error: Not Found
              code: object_not_found
        description: Not Found error
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 422
              error:
                allOf:
                  - type: string
                    example: Unprocessable entity
              code:
                allOf:
                  - type: string
                    example: validation_errors
              error_details:
                allOf:
                  - type: object
            refIdentifier: '#/components/schemas/ApiErrorUnprocessableEntity'
            requiredProperties:
              - status
              - error
              - code
              - error_details
        examples:
          example:
            value:
              status: 422
              error: Unprocessable entity
              code: validation_errors
              error_details: {}
        description: Unprocessable entity error
  deprecated: false
  type: path
components:
  schemas:
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
    FeatureBaseInput:
      type: object
      properties:
        name:
          type:
            - string
            - 'null'
          example: Number of seats
          description: Name of the feature.
        description:
          type:
            - string
            - 'null'
          example: Number of users of the account
          description: Internal description of the feature.
        privileges:
          type: array
          items:
            type: object
            required:
              - code
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
                    description: >-
                      Array of string, required only when value_type is
                      `select`.
          example:
            - code: max
              name: Maximum
              value_type: integer
            - code: max_admins
              name: Max Admins
              value_type: integer
            - code: root
              name: Allow root user
              value_type: boolean
            - code: provider
              name: SSO Provider
              value_type: select
              config:
                select_options:
                  - google
                  - okta
          description: Privileges associated with this feature. Can be empty.

````