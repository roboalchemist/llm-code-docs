# Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-owners.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get HubSpot Owners

> Retrieve all owners (users) from a HubSpot portal.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_owners
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/get_hubspot_owners:
    post:
      tags:
        - HubSpot
      summary: Get HubSpot Owners
      description: Retrieve all owners (users) from a HubSpot portal.
      operationId: getHubspotOwners
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                hubspot_portal:
                  type: string
                  description: HubSpot portal ID to retrieve owners from
                  example: '12345678'
              required:
                - hubspot_portal
      responses:
        '200':
          description: Retrieved HubSpot owners data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
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
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````