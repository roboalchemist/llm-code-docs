# Source: https://docs.agent.ai/api-reference/get-data/find-linkedin-profile.md

# Find LinkedIn Profile

> Find the LinkedIn profile slug for a person.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/find_linkedin_profile
paths:
  path: /action/find_linkedin_profile
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
                    description: Text query to find the LinkedIn profile slug.
                    example: Dharmesh Shah
            required: true
            requiredProperties:
              - query
        examples:
          example:
            value:
              query: Dharmesh Shah
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
              response: dharmesh
        description: LinkedIn profile slug
  deprecated: false
  type: path
components:
  schemas: {}

````