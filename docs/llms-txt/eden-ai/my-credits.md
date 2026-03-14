# Source: https://docs.edenai.co/api-reference/cost-monitoring/my-credits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# My Credits

> Get you current credits



## OpenAPI

````yaml openapi/v3-cost-management.json get /cost_management/credits/
openapi: 3.0.3
info:
  title: Cost Monitoring
  version: '2.0'
  description: Your project description
servers:
  - url: https://api.edenai.run/v2
security: []
paths:
  /cost_management/credits/:
    get:
      tags:
        - Cost Monitoring
      summary: My Credits
      description: Get you current credits
      operationId: cost_management_<Display Name of your Subfeature>
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/credits_serializer'
          description: ''
      security:
        - FeatureApiAuth: []
components:
  schemas:
    credits_serializer:
      type: object
      properties:
        credits:
          type: number
          format: double
      required:
        - credits
  securitySchemes:
    FeatureApiAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).