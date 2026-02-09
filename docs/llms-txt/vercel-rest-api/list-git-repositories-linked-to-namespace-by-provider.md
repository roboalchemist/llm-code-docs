# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-git-repositories-linked-to-namespace-by-provider.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List git repositories linked to namespace by provider

> Lists git repositories linked to a namespace `id` for a supported provider. A specific namespace `id` can be obtained via the `git-namespaces`  endpoint. Supported providers are `github`, `gitlab` and `bitbucket`. If the provider or namespace is not provided, it will try to obtain it from the user that authenticated the request.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/search-repo
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
  /v1/integrations/search-repo:
    get:
      tags:
        - integrations
      summary: List git repositories linked to namespace by provider
      description: >-
        Lists git repositories linked to a namespace `id` for a supported
        provider. A specific namespace `id` can be obtained via the
        `git-namespaces`  endpoint. Supported providers are `github`, `gitlab`
        and `bitbucket`. If the provider or namespace is not provided, it will
        try to obtain it from the user that authenticated the request.
      operationId: searchRepo
      parameters:
        - name: query
          in: query
          schema:
            type: string
        - name: namespaceId
          in: query
          schema:
            nullable: true
            oneOf:
              - type: string
              - type: number
        - name: provider
          in: query
          schema:
            enum:
              - github
              - github-limited
              - github-custom-host
              - gitlab
              - bitbucket
        - name: installationId
          in: query
          schema:
            type: string
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
                oneOf:
                  - type: object
                  - properties:
                      gitAccount:
                        properties:
                          provider:
                            type: string
                            enum:
                              - github
                              - github-limited
                              - github-custom-host
                              - gitlab
                              - bitbucket
                          namespaceId:
                            nullable: true
                            oneOf:
                              - type: string
                              - type: number
                        required:
                          - namespaceId
                          - provider
                        type: object
                      repos:
                        items:
                          properties:
                            id:
                              oneOf:
                                - type: string
                                - type: number
                            provider:
                              type: string
                              enum:
                                - github
                                - github-limited
                                - github-custom-host
                                - gitlab
                                - bitbucket
                            url:
                              type: string
                            name:
                              type: string
                            slug:
                              type: string
                            namespace:
                              type: string
                            owner:
                              properties:
                                id:
                                  oneOf:
                                    - type: string
                                    - type: number
                                name:
                                  type: string
                              required:
                                - id
                                - name
                              type: object
                            ownerType:
                              type: string
                              enum:
                                - user
                                - team
                            private:
                              type: boolean
                              enum:
                                - false
                                - true
                            defaultBranch:
                              type: string
                            updatedAt:
                              type: number
                          required:
                            - defaultBranch
                            - id
                            - name
                            - namespace
                            - owner
                            - ownerType
                            - private
                            - provider
                            - slug
                            - updatedAt
                            - url
                          type: object
                        type: array
                    required:
                      - gitAccount
                      - repos
                    type: object
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