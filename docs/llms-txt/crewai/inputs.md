# Source: https://docs.crewai.com/en/api-reference/inputs.md

# GET /inputs

> Get required inputs for your crew

## OpenAPI

````yaml enterprise-api.en.yaml get /inputs
paths:
  path: /inputs
  method: get
  servers:
    - url: https://your-actual-crew-name.crewai.com
      description: Replace with your actual deployed crew URL from the CrewAI AMP dashboard
    - url: https://my-travel-crew.crewai.com
      description: Example travel planning crew (replace with your URL)
    - url: https://content-creation-crew.crewai.com
      description: Example content creation crew (replace with your URL)
    - url: https://research-assistant-crew.crewai.com
      description: Example research assistant crew (replace with your URL)
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >
                **📋 Reference Documentation** - *The tokens shown in examples
                are placeholders for reference only.*


                Use your actual Bearer Token or User Bearer Token from the
                CrewAI AMP dashboard for real API calls.


                **Bearer Token**: Organization-level access for full crew
                operations

                **User Bearer Token**: User-scoped access with limited
                permissions
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              inputs:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: Array of required input parameter names
                    example:
                      - budget
                      - interests
                      - duration
                      - age
        examples:
          travel_crew:
            summary: Travel planning crew inputs
            value:
              inputs:
                - budget
                - interests
                - duration
                - age
          outreach_crew:
            summary: Outreach crew inputs
            value:
              inputs:
                - name
                - title
                - company
                - industry
                - our_product
                - linkedin_url
        description: Successfully retrieved required inputs
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: Error type or title
                    example: Authentication Error
              message:
                allOf:
                  - &ref_1
                    type: string
                    description: Detailed error message
                    example: Invalid bearer token provided
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error: Unauthorized
              message: Invalid or missing bearer token
        description: Authentication failed - check your bearer token
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error: Not Found
              message: The requested resource was not found
        description: Resource not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error: Internal Server Error
              message: An unexpected error occurred
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas: {}

````