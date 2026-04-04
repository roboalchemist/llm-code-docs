# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-resource-secrets-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Resource Secrets (Deprecated)

> This endpoint is deprecated and replaced with the endpoint [Update Resource Secrets](#update-resource-secrets). <br/> This endpoint updates the secrets of a resource. If a resource has projects connected, the connected secrets are updated with the new secrets. The old secrets may still be used by existing connected projects because they are not automatically redeployed. Redeployment is a manual action and must be completed by the user. All new project connections will use the new secrets.<br/> <br/> Use cases for this endpoint:<br/> <br/> - Resetting the credentials of a database in the partner. If the user requests the credentials to be updated in the partner’s application, the partner post the new set of secrets to Vercel, the user should redeploy their application and the expire the old credentials.<br/>



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets
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
  /v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets:
    put:
      tags:
        - marketplace
      summary: Update Resource Secrets (Deprecated)
      description: >-
        This endpoint is deprecated and replaced with the endpoint [Update
        Resource Secrets](#update-resource-secrets). <br/> This endpoint updates
        the secrets of a resource. If a resource has projects connected, the
        connected secrets are updated with the new secrets. The old secrets may
        still be used by existing connected projects because they are not
        automatically redeployed. Redeployment is a manual action and must be
        completed by the user. All new project connections will use the new
        secrets.<br/> <br/> Use cases for this endpoint:<br/> <br/> - Resetting
        the credentials of a database in the partner. If the user requests the
        credentials to be updated in the partner’s application, the partner post
        the new set of secrets to Vercel, the user should redeploy their
        application and the expire the old credentials.<br/>
      operationId: update-resource-secrets
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
        - name: integrationProductIdOrSlug
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
                partial:
                  type: boolean
                  description: If true, will only update the provided secrets
              additionalProperties: false
        required: true
      responses:
        '201':
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