# Source: https://getlago.com/docs/api-reference/entitlements/plan-entitlements/create-plan-entitlement.md

# Create plan entitlements

> This endpoint creates new entitlements by adding features to a plan. Note that all existing entitlements will be deleted and replaced by the ones provided. To add a new entitlement without removing the existing ones, use PATCH. The feature must exist and all privileges must be valid for the feature.

## OpenAPI

````yaml POST /plans/{code}/entitlements
paths:
  path: /plans/{code}/entitlements
  method: post
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
              description: Code of the existing plan.
              example: startup
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              entitlements:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      additionalProperties:
                        oneOf:
                          - type: integer
                          - type: boolean
                          - type: string
                      description: >-
                        Privilege values for this feature. All privileges must
                        exist on the feature.
                    example:
                      seats:
                        max: 20
                        max_admins: 10
                        root: false
                      sso:
                        provider: okta
                    description: >-
                      Feature entitlements with their privilege values. Each key
                      is a feature code, and the value is an object containing
                      privilege codes with their associated values.
            required: true
            refIdentifier: '#/components/schemas/EntitlementUpdateInput'
            requiredProperties:
              - entitlements
        examples:
          example:
            value:
              entitlements:
                seats:
                  max: 20
                  max_admins: 10
                  root: false
                sso:
                  provider: okta
        description: Entitlement payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              entitlements:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/PlanEntitlementObject'
            refIdentifier: '#/components/schemas/PlanEntitlements'
            requiredProperties:
              - entitlements
        examples:
          example:
            value:
              entitlements:
                - code: seats
                  name: Number of seats
                  description: Number of users of the account
                  privileges:
                    - code: max
                      name: Maximum
                      value_type: integer
                      config: {}
                      value: 10
                    - code: max_admins
                      name: Max Admins
                      value_type: integer
                      config: {}
                      value: 5
                    - code: root
                      name: Allow root user
                      value_type: boolean
                      config: {}
                      value: true
                    - code: provider
                      name: SSO Provider
                      value_type: select
                      value: google
                      config:
                        select_options:
                          - google
                          - okta
        description: Entitlement created
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
    PlanEntitlementPrivilegeObject:
      allOf:
        - $ref: '#/components/schemas/FeaturePrivilegeObject'
        - type: object
          required:
            - value
          properties:
            value:
              oneOf:
                - type: integer
                  description: Value for integer type privileges
                - type: boolean
                  description: Value for boolean type privileges
                - type: string
                  description: Value for string or select type privileges
              example: 10
              description: >-
                Value assigned to this privilege in the entitlement. Type
                depends on the privilege's value_type.
    PlanEntitlementObject:
      type: object
      required:
        - code
        - name
        - description
        - privileges
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
            $ref: '#/components/schemas/PlanEntitlementPrivilegeObject'
          example:
            - code: max
              name: Maximum
              value_type: integer
              config: {}
              value: 10
            - code: max_admins
              name: Max Admins
              value_type: integer
              config: {}
              value: 5
            - code: root
              name: Allow root user
              value_type: boolean
              config: {}
              value: true
            - code: provider
              name: SSO Provider
              value_type: select
              value: google
              config:
                select_options:
                  - google
                  - okta
          description: >-
            Privileges associated with this feature. Each privilege must have a
            value assigned.

````