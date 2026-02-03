# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/import-resource.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Import Resource

> This endpoint imports (upserts) a resource to Vercel's installation. This may be needed if resources can be independently created on the partner's side and need to be synchronized to Vercel.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}
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
  /v1/installations/{integrationConfigurationId}/resources/{resourceId}:
    put:
      tags:
        - marketplace
      summary: Import Resource
      description: >-
        This endpoint imports (upserts) a resource to Vercel's installation.
        This may be needed if resources can be independently created on the
        partner's side and need to be synchronized to Vercel.
      operationId: import-resource
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
        - name: resourceId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - productId
                - name
                - status
              properties:
                ownership:
                  type: string
                  enum:
                    - owned
                    - linked
                    - sandbox
                productId:
                  type: string
                name:
                  type: string
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
                metadata:
                  additionalProperties: true
                  type: object
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
                  type: object
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
                extras:
                  additionalProperties: true
                  type: object
                secrets:
                  type: array
                  items:
                    type: object
                    required:
                      - name
                      - value
                    properties:
                      name:
                        type: string
                      value:
                        type: string
                      prefix:
                        type: string
                      environmentOverrides:
                        type: object
                        description: >-
                          A map of environments to override values for the
                          secret, used for setting different values across
                          deployments in production, preview, and development
                          environments. Note: the same value will be used for
                          all deployments in the given environment.
                        properties:
                          development:
                            type: string
                            description: Value used for development environment.
                          preview:
                            type: string
                            description: Value used for preview environment.
                          production:
                            type: string
                            description: Value used for production environment.
                    additionalProperties: false
              additionalProperties: false
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  name:
                    type: string
                required:
                  - name
                type: object
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
        '409':
          description: ''
        '422':
          description: ''
        '429':
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