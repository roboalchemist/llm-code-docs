# Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-contact-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get HubSpot Contact Data

> Retrieve contact data from HubSpot based on a query or get the most recent contact.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_contact_object
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
  /action/get_hubspot_contact_object:
    post:
      tags:
        - HubSpot
      summary: Get HubSpot Contact Data
      description: >-
        Retrieve contact data from HubSpot based on a query or get the most
        recent contact.
      operationId: getHubspotContactObject
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: >-
                    Search query to find specific contact. Defaults to
                    '_most_recent_contact' if not provided or too short.
                  example: john.doe@example.com
              required:
                - query
      responses:
        '200':
          description: Retrieved HubSpot contact data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
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