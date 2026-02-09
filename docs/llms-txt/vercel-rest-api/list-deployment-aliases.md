# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/list-deployment-aliases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List Deployment Aliases

> Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/deployments/{id}/aliases
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
  /v2/deployments/{id}/aliases:
    get:
      tags:
        - aliases
      summary: List Deployment Aliases
      description: >-
        Retrieves all Aliases for the Deployment with the given ID. The
        authenticated user or team must own the deployment.
      operationId: listDeploymentAliases
      parameters:
        - name: id
          description: The ID of the deployment the aliases should be listed for
          in: path
          required: true
          schema:
            example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
            description: The ID of the deployment the aliases should be listed for
            type: string
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
          description: The list of aliases assigned to the deployment
          content:
            application/json:
              schema:
                properties:
                  aliases:
                    items:
                      properties:
                        uid:
                          type: string
                          description: The unique identifier of the alias
                          example: 2WjyKQmM8ZnGcJsPWMrHRHrE
                        alias:
                          type: string
                          description: >-
                            The alias name, it could be a `.vercel.app`
                            subdomain or a custom domain
                          example: my-alias.vercel.app
                        created:
                          type: string
                          format: date-time
                          description: The date when the alias was created
                          example: '2017-04-26T23:00:34.232Z'
                        redirect:
                          nullable: true
                          type: string
                          description: >-
                            Target destination domain for redirect when the
                            alias is a redirect
                        protectionBypass:
                          additionalProperties:
                            oneOf:
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - shareable-link
                                  expires:
                                    type: number
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  access:
                                    type: string
                                    enum:
                                      - requested
                                      - granted
                                  scope:
                                    type: string
                                    enum:
                                      - user
                                required:
                                  - access
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - alias-protection-override
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - email_invite
                                required:
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                          type: object
                          description: The protection bypass for the alias
                      required:
                        - alias
                        - created
                        - uid
                      type: object
                      description: A list of the aliases assigned to the deployment
                    type: array
                    description: A list of the aliases assigned to the deployment
                required:
                  - aliases
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: The deployment was not found
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````