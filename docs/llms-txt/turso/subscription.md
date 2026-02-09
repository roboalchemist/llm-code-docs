# Source: https://docs.turso.tech/api-reference/organizations/subscription.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Current Subscription

> Returns the current subscription details for the organization.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/subscription \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/subscription
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
  /v1/organizations/{organizationSlug}/subscription:
    get:
      summary: Current Subscription
      description: Returns the current subscription details for the organization.
      operationId: getOrganizationSubscription
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
                  subscription:
                    type: object
                    properties:
                      name:
                        type: string
                        description: The name of the plan for the current subscription.
                        example: scaler
                      overages:
                        type: boolean
                        description: Whether overages are enabled for the organization.
                      plan:
                        type: string
                        description: The name of the plan for the current subscription.
                        example: scaler
                      timeline:
                        type: string
                        description: Whether the plan is billed monthly or yearly.
                        example: monthly
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.

````