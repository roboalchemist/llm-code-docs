# Source: https://www.thundercompute.com/docs/api-reference/utilities/get-current-pricing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get current pricing

> Retrieve current hourly pricing information for compute resources



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json get /pricing
openapi: 3.1.0
info:
  contact:
    email: support@thundercompute.com
    name: Thunder Compute API Support
    url: https://thundercompute.com/support
  description: >-
    This is the Thunder Compute API server for managing compute resources and
    GPU workloads.
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
  termsOfService: http://swagger.io/terms/
  title: Thunder Compute API
  version: '1.0'
servers:
  - description: Production server
    url: https://api.thundercompute.com:8443/v1
security: []
externalDocs:
  description: ''
  url: ''
paths:
  /pricing:
    get:
      tags:
        - utilities
      summary: Get current pricing
      description: Retrieve current hourly pricing information for compute resources
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.PricingResponse'
          description: OK
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.ErrorResponse'
          description: Internal Server Error
components:
  schemas:
    thundertypes.PricingResponse:
      properties:
        pricing:
          $ref: '#/components/schemas/thundertypes.PricingMap'
      type: object
    thundertypes.ErrorResponse:
      properties:
        code:
          example: 400
          type: integer
        error:
          example: invalid_request
          type: string
        message:
          example: The request is malformed
          type: string
      type: object
    thundertypes.PricingMap:
      additionalProperties:
        type: number
      type: object

````