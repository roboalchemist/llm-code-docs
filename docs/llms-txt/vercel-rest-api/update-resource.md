# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-resource.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Resource

> This endpoint updates an existing resource in the installation. All parameters are optional, allowing partial updates.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}
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
    patch:
      tags:
        - marketplace
      summary: Update Resource
      description: >-
        This endpoint updates an existing resource in the installation. All
        parameters are optional, allowing partial updates.
      operationId: update-resource
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
              properties:
                ownership:
                  type: string
                  enum:
                    - owned
                    - linked
                    - sandbox
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
                extras:
                  additionalProperties: true
                  type: object
                secrets:
                  oneOf:
                    - type: array
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
                              deployments in production, preview, and
                              development environments. Note: the same value
                              will be used for all deployments in the given
                              environment.
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
                    - type: object
                      required:
                        - secrets
                      properties:
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
                                  A map of environments to override values for
                                  the secret, used for setting different values
                                  across deployments in production, preview, and
                                  development environments. Note: the same value
                                  will be used for all deployments in the given
                                  environment.
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
                        partial:
                          type: boolean
                          description: >-
                            If true, will only overwrite the provided secrets
                            instead of replacing all secrets.
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
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````