# Source: https://docs.comfy.org/api-reference/registry/get-server-feature-flags.md

# Get server feature flags

> Returns the server's feature capabilities



## OpenAPI

````yaml https://api.comfy.org/openapi get /features
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /features:
    get:
      tags:
        - Registry
      summary: Get server feature flags
      description: Returns the server's feature capabilities
      operationId: GetFeatures
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FeaturesResponse'
          description: Success
components:
  schemas:
    FeaturesResponse:
      properties:
        partner_node_conversion_rate:
          description: The conversion rate for partner nodes
          example: 0.5
          type: number
      required:
        - partner_node_conversion_rate
      type: object

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.comfy.org/llms.txt