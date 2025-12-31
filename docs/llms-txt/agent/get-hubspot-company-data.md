# Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-company-data.md

# Get HubSpot Company Data

> Retrieve company data from HubSpot based on a query or get the most recent company.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_company_object
paths:
  path: /action/get_hubspot_company_object
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
              query:
                allOf:
                  - type: string
                    description: >-
                      Search query to find specific company. Defaults to
                      '_most_recent_company' if not provided or too short.
                    example: Acme Corporation
            required: true
            requiredProperties:
              - query
        examples:
          example:
            value:
              query: Acme Corporation
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
                id: '12345678'
                properties:
                  name: Acme Corporation
                  domain: acme.com
                  industry: Technology
                  phone: +1-123-456-7890
                  address: 123 Main St, Anytown, USA
                  createdate: '2023-01-15T15:30:45.123Z'
                  hs_lastmodifieddate: '2024-03-10T09:12:34.567Z'
                createdAt: '2023-01-15T15:30:45.123Z'
                updatedAt: '2024-03-10T09:12:34.567Z'
                archived: false
        description: Retrieved HubSpot company data
  deprecated: false
  type: path
components:
  schemas: {}

````