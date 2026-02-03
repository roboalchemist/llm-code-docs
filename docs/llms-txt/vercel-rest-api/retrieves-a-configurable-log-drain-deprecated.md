# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-configurable-log-drain-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves a Configurable Log Drain (deprecated)

> Retrieves a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be accessed.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/log-drains/{id}
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
  /v1/log-drains/{id}:
    get:
      tags:
        - logDrains
      summary: Retrieves a Configurable Log Drain (deprecated)
      description: >-
        Retrieves a Configurable Log Drain. This endpoint must be called with a
        team AccessToken (integration OAuth2 clients are not allowed). Only log
        drains owned by the authenticated team can be accessed.
      operationId: getConfigurableLogDrain
      parameters:
        - name: id
          in: path
          required: true
          schema:
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
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  createdFrom:
                    type: string
                  clientId:
                    type: string
                  configurationId:
                    type: string
                  projectsMetadata:
                    nullable: true
                    items:
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                        framework:
                          nullable: true
                          type: string
                          enum:
                            - blitzjs
                            - nextjs
                            - gatsby
                            - remix
                            - react-router
                            - astro
                            - hexo
                            - eleventy
                            - docusaurus-2
                            - docusaurus
                            - preact
                            - solidstart-1
                            - solidstart
                            - dojo
                            - ember
                            - vue
                            - scully
                            - ionic-angular
                            - angular
                            - polymer
                            - svelte
                            - sveltekit
                            - sveltekit-1
                            - ionic-react
                            - create-react-app
                            - gridsome
                            - umijs
                            - sapper
                            - saber
                            - stencil
                            - nuxtjs
                            - redwoodjs
                            - hugo
                            - jekyll
                            - brunch
                            - middleman
                            - zola
                            - hydrogen
                            - vite
                            - tanstack-start
                            - vitepress
                            - vuepress
                            - parcel
                            - fastapi
                            - flask
                            - fasthtml
                            - sanity-v3
                            - sanity
                            - storybook
                            - nitro
                            - hono
                            - express
                            - h3
                            - koa
                            - nestjs
                            - elysia
                            - fastify
                            - xmcp
                            - python
                            - ruby
                            - rust
                            - node
                            - services
                        latestDeployment:
                          type: string
                      required:
                        - id
                        - name
                      type: object
                    type: array
                  integrationIcon:
                    type: string
                  integrationConfigurationUri:
                    type: string
                  integrationWebsite:
                    type: string
                required:
                  - createdFrom
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