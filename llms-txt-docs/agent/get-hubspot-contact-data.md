# Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-contact-data.md

# Get HubSpot Contact Data

> Retrieve contact data from HubSpot based on a query or get the most recent contact.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_contact_object
paths:
  path: /action/get_hubspot_contact_object
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
                      Search query to find specific contact. Defaults to
                      '_most_recent_contact' if not provided or too short.
                    example: john.doe@example.com
            required: true
            requiredProperties:
              - query
        examples:
          example:
            value:
              query: john.doe@example.com
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
                  firstname: John
                  lastname: Doe
                  email: john.doe@example.com
                  phone: +1-123-456-7890
                  jobtitle: Product Manager
                  company: Acme Corporation
                  createdate: '2023-05-20T13:45:22.123Z'
                  hs_lastmodifieddate: '2024-02-15T11:24:36.789Z'
                createdAt: '2023-05-20T13:45:22.123Z'
                updatedAt: '2024-02-15T11:24:36.789Z'
                archived: false
        description: Retrieved HubSpot contact data
  deprecated: false
  type: path
components:
  schemas: {}

````