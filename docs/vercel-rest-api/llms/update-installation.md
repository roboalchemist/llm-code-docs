# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Installation

> This endpoint updates an integration installation.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}
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
  /v1/installations/{integrationConfigurationId}:
    patch:
      tags:
        - marketplace
      summary: Update Installation
      description: This endpoint updates an integration installation.
      operationId: update-installation
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  enum:
                    - ready
                    - pending
                    - onboarding
                    - suspended
                    - resumed
                    - uninstalled
                    - error
                externalId:
                  type: string
                billingPlan:
                  type: object
                  required:
                    - id
                    - type
                    - name
                  properties:
                    id:
                      type: string
                    type:
                      type: string
                      enum:
                        - prepayment
                        - subscription
                    name:
                      type: string
                    description:
                      type: string
                    paymentMethodRequired:
                      type: boolean
                    cost:
                      type: string
                    details:
                      type: array
                      items:
                        type: object
                        properties:
                          label:
                            type: string
                          value:
                            type: string
                        required:
                          - label
                        additionalProperties: false
                    highlightedDetails:
                      type: array
                      items:
                        type: object
                        properties:
                          label:
                            type: string
                          value:
                            type: string
                        required:
                          - label
                        additionalProperties: false
                    effectiveDate:
                      type: string
                  additionalProperties: true
                notification:
                  oneOf:
                    - type: object
                      required:
                        - level
                        - title
                      properties:
                        level:
                          type: string
                          enum:
                            - info
                            - warn
                            - error
                        title:
                          type: string
                        message:
                          type: string
                        href:
                          type: string
                          format: uri
                    - type: string
                  description: >-
                    A notification to display to your customer. Send `null` to
                    clear the current notification.
              additionalProperties: false
      responses:
        '204':
          description: ''
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
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