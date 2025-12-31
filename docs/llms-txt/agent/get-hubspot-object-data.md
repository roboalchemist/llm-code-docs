# Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-object-data.md

# Get HubSpot Object Data

> Retrieve data for any supported HubSpot object type based on a query or get the most recent object.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_object
paths:
  path: /action/get_hubspot_object
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
              object_type:
                allOf:
                  - type: string
                    description: >-
                      Type of HubSpot object to retrieve (e.g., company,
                      contact, deal).
                    example: company
                    enum:
                      - company
                      - contact
                      - deal
                      - ticket
              query:
                allOf:
                  - type: string
                    description: >-
                      Search query to find specific object. Defaults to
                      '_most_recent_company' if not provided or too short (or
                      '_most_recent_contact' if object_type is 'contact').
                    example: Acme Corporation
            required: true
            requiredProperties:
              - object_type
              - query
        examples:
          example:
            value:
              object_type: company
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
                  createdate: '2023-01-15T15:30:45.123Z'
                  hs_lastmodifieddate: '2024-03-10T09:12:34.567Z'
                createdAt: '2023-01-15T15:30:45.123Z'
                updatedAt: '2024-03-10T09:12:34.567Z'
                archived: false
        description: Retrieved HubSpot object data
  deprecated: false
  type: path
components:
  schemas: {}

````