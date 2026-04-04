# Source: https://docs.agent.ai/api-reference/get-data/get-company-earnings-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Company Earnings Info

> Retrieve company earnings information for a given stock symbol over time.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/company_financial_info
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
  /action/company_financial_info:
    post:
      tags:
        - Get Data
      summary: Get Company Earnings Info
      description: >-
        Retrieve company earnings information for a given stock symbol over
        time.
      operationId: companyFinancialInfo
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                company:
                  type: string
                  description: Stock symbol of the company.
                  example: HUBS, NKE, AAPL
                quarter:
                  type: integer
                  format: int64
                  enum:
                    - 1
                    - 2
                    - 3
                    - 4
                  default: 1
                  description: Quarter of the year to retrieve earnings info.
                year:
                  type: integer
                  description: Year of the earnings info to retrieve.
                  example: '2025'
              required:
                - company
                - quarter
                - year
      responses:
        '200':
          description: >-
            Retrieve company earnings information for a given stock symbol over
            time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response: >-
                  Operator: Good afternoon and welcome to the HubSpot Q2 2024
                  Earnings Call. My name is Harry and I will be your operator
                  today.
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