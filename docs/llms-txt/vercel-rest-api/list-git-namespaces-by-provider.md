# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-git-namespaces-by-provider.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List git namespaces by provider

> Lists git namespaces for a supported provider. Supported providers are `github`, `gitlab` and `bitbucket`. If the provider is not provided, it will try to obtain it from the user that authenticated the request.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/git-namespaces
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
  /v1/integrations/git-namespaces:
    get:
      tags:
        - integrations
      summary: List git namespaces by provider
      description: >-
        Lists git namespaces for a supported provider. Supported providers are
        `github`, `gitlab` and `bitbucket`. If the provider is not provided, it
        will try to obtain it from the user that authenticated the request.
      operationId: gitNamespaces
      parameters:
        - name: host
          description: >-
            The custom Git host if using a custom Git provider, like GitHub
            Enterprise Server
          in: query
          schema:
            description: >-
              The custom Git host if using a custom Git provider, like GitHub
              Enterprise Server
            type: string
            example: ghes-test.now.systems
        - name: provider
          in: query
          schema:
            enum:
              - github
              - github-limited
              - github-custom-host
              - gitlab
              - bitbucket
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                items:
                  properties:
                    provider:
                      type: string
                    slug:
                      type: string
                    id:
                      oneOf:
                        - type: string
                        - type: number
                    ownerType:
                      type: string
                    name:
                      type: string
                    isAccessRestricted:
                      type: boolean
                      enum:
                        - false
                        - true
                    installationId:
                      type: number
                    requireReauth:
                      type: boolean
                      enum:
                        - false
                        - true
                  required:
                    - id
                    - ownerType
                    - provider
                    - slug
                  type: object
                type: array
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '429':
          description: ''
        '500':
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