# Source: https://docs.turso.tech/api-reference/organizations/plans.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# List Plans

> Returns a list of available plans and their quotas.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/plans \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/plans
openapi: 3.0.1
info:
  title: Turso Platform API
  description: API description here
  license:
    name: MIT
  version: 0.1.0
servers:
  - url: https://api.turso.tech
    description: Turso's Platform API
security: []
paths:
  /v1/organizations/{organizationSlug}/plans:
    get:
      summary: List Plans
      description: Returns a list of available plans and their quotas.
      operationId: listOrganizationPlans
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  plans:
                    type: array
                    description: List of available plans.
                    items:
                      $ref: '#/components/schemas/OrganizationPlan'
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.
  schemas:
    OrganizationPlan:
      type: object
      properties:
        name:
          type: string
          description: The name of the plan.
          example: starter
        price:
          type: string
          description: The monthly price of the plan.
          example: '0'
        prices:
          type: array
          items:
            $ref: '#/components/schemas/PlanPrice'
        quotas:
          $ref: '#/components/schemas/PlanQuotas'
    PlanPrice:
      type: object
      properties:
        value:
          type: string
          description: Price of the available plan.
          example: '29'
        timeline:
          type: string
          description: Payment regularity.
          example: monthly
    PlanQuotas:
      type: object
      properties:
        rowsRead:
          type: integer
          description: The number of rows read allowed for the specific plan.
          example: 1000000000
        rowsWritten:
          type: integer
          description: The number of rows written allowed for the specific plan.
          example: 25000000
        databases:
          type: integer
          nullable: true
          description: The number of databases allowed for the specific plan.
          example: 500
        locations:
          type: integer
          description: The number of locations allowed for the specific plan.
          example: 3
        storage:
          type: integer
          description: The amount of storage allowed for the specific plan, in bytes.
          example: 9000000000
        groups:
          type: integer
          description: The number of groups allowed for the specific plan.
          example: 1
        bytesSynced:
          type: integer
          description: The number of bytes synced allowed for the specific plan, in bytes.
          example: 3000000000

````