# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-integration-billing-plans.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List integration billing plans

> Get a list of billing plans for an integration and product.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/integration/{integrationIdOrSlug}/products/{productIdOrSlug}/plans
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/integrations/integration/{integrationIdOrSlug}/products/{productIdOrSlug}/plans:
    get:
      tags:
        - integrations
      summary: List integration billing plans
      description: Get a list of billing plans for an integration and product.
      operationId: getBillingPlans
      parameters:
        - name: integrationIdOrSlug
          in: path
          required: true
          schema:
            type: string
        - name: integrationConfigurationId
          in: query
          required: false
          schema:
            type: string
        - name: productIdOrSlug
          in: path
          required: true
          schema:
            type: string
        - name: metadata
          in: query
          required: false
          schema:
            type: string
        - name: source
          in: query
          required: false
          schema:
            type: string
            enum:
              - marketplace
              - deploy-button
              - external
              - v0
              - resource-claims
              - cli
              - oauth
              - backoffice
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  plans:
                    items:
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
                          enum:
                            - false
                            - true
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
                              - amount
                              - line
                            type: object
                          type: array
                        effectiveDate:
                          type: string
                        disabled:
                          type: boolean
                          enum:
                            - false
                            - true
                      required:
                        - description
                        - id
                        - name
                        - paymentMethodRequired
                        - scope
                        - type
                      type: object
                    type: array
                required:
                  - plans
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````