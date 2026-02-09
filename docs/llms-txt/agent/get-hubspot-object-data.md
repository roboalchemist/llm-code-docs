# Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-object-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get HubSpot Object Data

> Retrieve data for any supported HubSpot object type based on a query or get the most recent object.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_object
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
  /action/get_hubspot_object:
    post:
      tags:
        - HubSpot
      summary: Get HubSpot Object Data
      description: >-
        Retrieve data for any supported HubSpot object type based on a query or
        get the most recent object.
      operationId: getHubspotObject
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                object_type:
                  type: string
                  description: >-
                    Type of HubSpot object to retrieve (e.g., company, contact,
                    deal).
                  example: company
                  enum:
                    - company
                    - contact
                    - deal
                    - ticket
                query:
                  type: string
                  description: >-
                    Search query to find specific object. Defaults to
                    '_most_recent_company' if not provided or too short (or
                    '_most_recent_contact' if object_type is 'contact').
                  example: Acme Corporation
              required:
                - object_type
                - query
      responses:
        '200':
          description: Retrieved HubSpot object data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
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