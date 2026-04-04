# Source: https://docs.agent.ai/api-reference/get-data/find-linkedin-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Find LinkedIn Profile

> Find the LinkedIn profile slug for a person.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/find_linkedin_profile
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
  /action/find_linkedin_profile:
    post:
      tags:
        - Get Data
      summary: Find LinkedIn Profile
      description: Find the LinkedIn profile slug for a person.
      operationId: findLinkedinProfile
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: Text query to find the LinkedIn profile slug.
                  example: Dharmesh Shah
              required:
                - query
      responses:
        '200':
          description: LinkedIn profile slug
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response: dharmesh
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