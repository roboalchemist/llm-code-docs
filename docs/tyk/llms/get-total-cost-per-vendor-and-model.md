# Source: https://tyk.io/docs/api-reference/analytics/get-total-cost-per-vendor-and-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get total cost per vendor and model

> Get the total cost per vendor and model for a given time period, including currency



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /analytics/total-cost-per-vendor-and-model
openapi: 3.0.1
info:
  title: AI Studio API
  description: This is the API for the AI Studio user and group management system.
  termsOfService: http://swagger.io/terms/
  contact:
    name: API Support
    url: http://www.swagger.io/support
    email: support@tyk.io
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
  version: '1.0'
servers:
  - url: //localhost:8080/api/v1
security:
  - BearerAuth: []
paths:
  /analytics/total-cost-per-vendor-and-model:
    get:
      tags:
        - Analytics
      summary: Get total cost per vendor and model
      description: >-
        Get the total cost per vendor and model for a given time period,
        including currency
      parameters:
        - name: start_date
          in: query
          description: Start date (YYYY-MM-DD)
          required: true
          schema:
            type: string
        - name: end_date
          in: query
          description: End date (YYYY-MM-DD)
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/analytics.VendorModelCost'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
components:
  schemas:
    analytics.VendorModelCost:
      type: object
      properties:
        currency:
          type: string
        model:
          type: string
        totalCost:
          type: number
        vendor:
          type: string
    api.ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              detail:
                type: string
              title:
                type: string
      description: Error response model
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).