# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-integration-billing-plans.md

# List integration billing plans

> Get a list of billing plans for an integration and product.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/integration/{integrationIdOrSlug}/products/{productIdOrSlug}/plans
paths:
  path: >-
    /v1/integrations/integration/{integrationIdOrSlug}/products/{productIdOrSlug}/plans
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        integrationIdOrSlug:
          schema:
            - type: string
              required: true
        productIdOrSlug:
          schema:
            - type: string
              required: true
      query:
        metadata:
          schema:
            - type: string
              required: false
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getBillingPlans
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getBillingPlans({
              integrationIdOrSlug: "<value>",
              productIdOrSlug: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              plans:
                allOf:
                  - items:
                      properties:
                        type:
                          type: string
                          enum:
                            - prepayment
                            - subscription
                        description:
                          type: string
                        id:
                          type: string
                        name:
                          type: string
                        scope:
                          type: string
                          enum:
                            - installation
                            - resource
                        paymentMethodRequired:
                          type: boolean
                        preauthorizationAmount:
                          type: number
                        initialCharge:
                          type: string
                        minimumAmount:
                          type: string
                        maximumAmount:
                          type: string
                        maximumAmountAutoPurchasePerPeriod:
                          type: string
                        cost:
                          type: string
                        details:
                          items:
                            properties:
                              label:
                                type: string
                              value:
                                type: string
                            required:
                              - label
                            type: object
                          type: array
                        highlightedDetails:
                          items:
                            properties:
                              label:
                                type: string
                              value:
                                type: string
                            required:
                              - label
                            type: object
                          type: array
                        quote:
                          items:
                            properties:
                              line:
                                type: string
                              amount:
                                type: string
                            required:
                              - line
                              - amount
                            type: object
                          type: array
                        effectiveDate:
                          type: string
                        disabled:
                          type: boolean
                      required:
                        - type
                        - description
                        - id
                        - name
                        - scope
                        - paymentMethodRequired
                      type: object
                    type: array
            requiredProperties:
              - plans
        examples:
          example:
            value:
              plans:
                - type: prepayment
                  description: <string>
                  id: <string>
                  name: <string>
                  scope: installation
                  paymentMethodRequired: true
                  preauthorizationAmount: 123
                  initialCharge: <string>
                  minimumAmount: <string>
                  maximumAmount: <string>
                  maximumAmountAutoPurchasePerPeriod: <string>
                  cost: <string>
                  details:
                    - label: <string>
                      value: <string>
                  highlightedDetails:
                    - label: <string>
                      value: <string>
                  quote:
                    - line: <string>
                      amount: <string>
                  effectiveDate: <string>
                  disabled: true
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````