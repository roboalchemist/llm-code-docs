# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-integration-resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Integration Resources

> Get all resources for a given installation ID.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/resources
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
  /v1/installations/{integrationConfigurationId}/resources:
    get:
      tags:
        - marketplace
      summary: Get Integration Resources
      description: Get all resources for a given installation ID.
      operationId: get-integration-resources
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  resources:
                    items:
                      properties:
                        partnerId:
                          type: string
                          description: >-
                            The ID provided by the partner for the given
                            resource
                        internalId:
                          type: string
                          description: The ID assigned by Vercel for the given resource
                        name:
                          type: string
                          description: The name of the resource as it is recorded in Vercel
                        status:
                          type: string
                          enum:
                            - error
                            - ready
                            - pending
                            - onboarding
                            - suspended
                            - resumed
                            - uninstalled
                          description: The current status of the resource
                        productId:
                          type: string
                          description: The ID of the product the resource is derived from
                        protocolSettings:
                          properties:
                            experimentation:
                              properties:
                                edgeConfigSyncingEnabled:
                                  type: boolean
                                  enum:
                                    - false
                                    - true
                                edgeConfigId:
                                  type: string
                                edgeConfigTokenId:
                                  type: string
                              type: object
                          type: object
                          description: >-
                            Any settings provided for the resource to support
                            its product's protocols
                        notification:
                          properties:
                            title:
                              type: string
                            level:
                              type: string
                              enum:
                                - error
                                - info
                                - warn
                            message:
                              type: string
                            href:
                              type: string
                          required:
                            - level
                            - title
                          type: object
                          description: >-
                            The notification, if set, displayed to the user when
                            viewing the resource in Vercel
                        billingPlanId:
                          type: string
                          description: >-
                            The ID of the billing plan the resource is
                            subscribed to, if applicable
                        metadata:
                          additionalProperties:
                            oneOf:
                              - type: string
                              - type: number
                              - items:
                                  type: string
                                type: array
                                description: >-
                                  The configured metadata for the resource as
                                  defined by its product's Metadata Schema
                              - items:
                                  type: number
                                type: array
                                description: >-
                                  The configured metadata for the resource as
                                  defined by its product's Metadata Schema
                              - type: boolean
                                enum:
                                  - false
                                  - true
                          type: object
                          description: >-
                            The configured metadata for the resource as defined
                            by its product's Metadata Schema
                      required:
                        - internalId
                        - name
                        - partnerId
                        - productId
                      type: object
                    type: array
                required:
                  - resources
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