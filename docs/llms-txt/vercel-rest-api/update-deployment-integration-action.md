# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/update-deployment-integration-action.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update deployment integration action

> Updates the deployment integration action for the specified integration installation



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/integrations/{integrationConfigurationId}/resources/{resourceId}/actions/{action}
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
  /v1/deployments/{deploymentId}/integrations/{integrationConfigurationId}/resources/{resourceId}/actions/{action}:
    patch:
      tags:
        - deployments
        - integrations
      summary: Update deployment integration action
      description: >-
        Updates the deployment integration action for the specified integration
        installation
      operationId: update-integration-deployment-action
      parameters:
        - name: deploymentId
          in: path
          required: true
          schema:
            type: string
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
        - name: action
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
                    - running
                    - succeeded
                    - failed
                statusText:
                  type: string
                statusUrl:
                  type: string
                  format: uri
                  pattern: '^https?://|^sso:'
                outcomes:
                  type: array
                  items:
                    oneOf:
                      - type: object
                        properties:
                          kind:
                            type: string
                          secrets:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                value:
                                  type: string
                              required:
                                - name
                                - value
                              additionalProperties: false
                        required:
                          - kind
                          - secrets
                        additionalProperties: false
              additionalProperties: false
      responses:
        '202':
          description: ''
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````