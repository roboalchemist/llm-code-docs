# Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-owners.md

# Get HubSpot Owners

> Retrieve all owners (users) from a HubSpot portal.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_owners
paths:
  path: /action/get_hubspot_owners
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              hubspot_portal:
                allOf:
                  - type: string
                    description: HubSpot portal ID to retrieve owners from
                    example: '12345678'
            required: true
            requiredProperties:
              - hubspot_portal
        examples:
          example:
            value:
              hubspot_portal: '12345678'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                - id: '12345'
                  email: sarah.jones@company.com
                  firstName: Sarah
                  lastName: Jones
                  createdAt: '2022-05-10T09:30:22.123Z'
                  updatedAt: '2024-01-18T14:22:45.789Z'
                  teams:
                    - Sales
                    - Marketing
                  userRole: Super Admin
                - id: '67890'
                  email: mike.smith@company.com
                  firstName: Mike
                  lastName: Smith
                  createdAt: '2022-07-15T10:45:33.456Z'
                  updatedAt: '2023-12-05T16:18:21.345Z'
                  teams:
                    - Sales
                  userRole: Standard
        description: Retrieved HubSpot owners data
  deprecated: false
  type: path
components:
  schemas: {}

````