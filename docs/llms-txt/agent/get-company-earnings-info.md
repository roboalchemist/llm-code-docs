# Source: https://docs.agent.ai/api-reference/get-data/get-company-earnings-info.md

# Get Company Earnings Info

> Retrieve company earnings information for a given stock symbol over time.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/company_financial_info
paths:
  path: /action/company_financial_info
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
              company:
                allOf:
                  - type: string
                    description: Stock symbol of the company.
                    example: HUBS, NKE, AAPL
              quarter:
                allOf:
                  - type: integer
                    format: int64
                    enum:
                      - 1
                      - 2
                      - 3
                      - 4
                    default: 1
                    description: Quarter of the year to retrieve earnings info.
              year:
                allOf:
                  - type: integer
                    description: Year of the earnings info to retrieve.
                    example: '2025'
            required: true
            requiredProperties:
              - company
              - quarter
              - year
        examples:
          example:
            value:
              company: HUBS, NKE, AAPL
              quarter: 1
              year: '2025'
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
              response: >-
                Operator: Good afternoon and welcome to the HubSpot Q2 2024
                Earnings Call. My name is Harry and I will be your operator
                today.
        description: >-
          Retrieve company earnings information for a given stock symbol over
          time
  deprecated: false
  type: path
components:
  schemas: {}

````