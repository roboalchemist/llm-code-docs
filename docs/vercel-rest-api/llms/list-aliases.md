# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/list-aliases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List aliases

> Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/aliases
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
  /v4/aliases:
    get:
      tags:
        - aliases
      summary: List aliases
      description: >-
        Retrieves a list of aliases for the authenticated User or Team. When
        `domain` is provided, only aliases for that domain will be returned.
        When `projectId` is provided, it will only return the given project
        aliases.
      operationId: listAliases
      parameters:
        - name: domain
          description: Get only aliases of the given domain name
          in: query
          schema:
            description: Get only aliases of the given domain name
            example: my-test-domain.com
            maxItems: 20
            oneOf:
              - items:
                  type: string
                type: array
              - type: string
        - name: from
          description: Get only aliases created after the provided timestamp
          in: query
          schema:
            deprecated: true
            description: Get only aliases created after the provided timestamp
            example: 1540095775951
            type: number
        - name: limit
          description: Maximum number of aliases to list from a request
          in: query
          schema:
            description: Maximum number of aliases to list from a request
            example: 10
            type: number
        - name: projectId
          description: Filter aliases from the given `projectId`
          in: query
          schema:
            description: Filter aliases from the given `projectId`
            example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            type: string
        - name: since
          description: Get aliases created after this JavaScript timestamp
          in: query
          schema:
            description: Get aliases created after this JavaScript timestamp
            example: 1540095775941
            type: number
        - name: until
          description: Get aliases created before this JavaScript timestamp
          in: query
          schema:
            description: Get aliases created before this JavaScript timestamp
            example: 1540095775951
            type: number
        - name: rollbackDeploymentId
          description: Get aliases that would be rolled back for the given deployment
          in: query
          schema:
            description: Get aliases that would be rolled back for the given deployment
            example: dpl_XXX
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
          description: The paginated list of aliases
          content:
            application/json:
              schema:
                properties:
                  aliases:
                    items:
                      properties:
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
                        createdAt:
                          type: number
                          description: >-
                            The date when the alias was created in milliseconds
                            since the UNIX epoch
                          example: 1540095775941
                        creator:
                          properties:
                            uid:
                              type: string
                              description: ID of the user who created the alias
                              example: 96SnxkFiMyVKsK3pnoHfx3Hz
                            email:
                              type: string
                              description: Email of the user who created the alias
                              example: john-doe@gmail.com
                            username:
                              type: string
                              description: Username of the user who created the alias
                              example: john-doe
                          required:
                            - email
                            - uid
                            - username
                          type: object
                          description: Information of the user who created the alias
                        deletedAt:
                          type: number
                          description: >-
                            The date when the alias was deleted in milliseconds
                            since the UNIX epoch
                          example: 1540095775941
                          nullable: true
                        deployment:
                          properties:
                            id:
                              type: string
                              description: The deployment unique identifier
                              example: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                            url:
                              type: string
                              description: The deployment unique URL
                              example: my-instant-deployment-3ij3cxz9qr.now.sh
                            meta:
                              type: string
                              description: The deployment metadata
                              example: {}
                          required:
                            - id
                            - url
                          type: object
                          description: A map with the deployment ID, URL and metadata
                        deploymentId:
                          nullable: true
                          type: string
                          description: The deployment ID
                          example: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                        projectId:
                          nullable: true
                          type: string
                          description: The unique identifier of the project
                          example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                        redirect:
                          nullable: true
                          type: string
                          description: >-
                            Target destination domain for redirect when the
                            alias is a redirect
                        redirectStatusCode:
                          nullable: true
                          type: number
                          enum:
                            - 301
                            - 302
                            - 307
                            - 308
                          description: Status code to be used on redirect
                        uid:
                          type: string
                          description: The unique identifier of the alias
                        updatedAt:
                          type: number
                          description: >-
                            The date when the alias was updated in milliseconds
                            since the UNIX epoch
                          example: 1540095775941
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
                        microfrontends:
                          properties:
                            defaultApp:
                              type: object
                              required:
                                - projectId
                              properties:
                                projectId:
                                  type: string
                            applications:
                              oneOf:
                                - items:
                                    properties:
                                      fallbackHost:
                                        type: string
                                        description: >-
                                          This is always set. In production it is
                                          used as a pointer to each apps
                                          production deployment. For
                                          pre-production, it's used as the
                                          fallback if there is no deployment for
                                          the branch.
                                      projectId:
                                        type: string
                                        description: >-
                                          The project ID of the microfrontends
                                          application.
                                    required:
                                      - fallbackHost
                                      - projectId
                                    type: object
                                    description: >-
                                      A list of the deployment routing
                                      information for each project.
                                  type: array
                                  description: >-
                                    A list of the deployment routing information
                                    for each project.
                                - items:
                                    properties:
                                      fallbackHost:
                                        type: string
                                        description: >-
                                          This is always set. For branch aliases,
                                          it's used as the fallback if there is no
                                          deployment for the branch.
                                      branchAlias:
                                        type: string
                                        description: >-
                                          Could point to a branch without a
                                          deployment if the project was never
                                          deployed. The proxy will fallback to the
                                          fallbackHost if there is no deployment.
                                      projectId:
                                        type: string
                                        description: >-
                                          The project ID of the microfrontends
                                          application.
                                    required:
                                      - branchAlias
                                      - fallbackHost
                                      - projectId
                                    type: object
                                    description: >-
                                      A list of the deployment routing
                                      information for each project.
                                  type: array
                                  description: >-
                                    A list of the deployment routing information
                                    for each project.
                                - items:
                                    properties:
                                      deploymentId:
                                        type: string
                                        description: >-
                                          This is the deployment for the same
                                          commit, it could be a cancelled
                                          deployment. The proxy will fallback to
                                          the branchDeploymentId and then the
                                          fallbackDeploymentId.
                                      branchDeploymentId:
                                        type: string
                                        description: >-
                                          This is the latest non-cancelled
                                          deployment of the branch alias at the
                                          time the commit alias was created. It is
                                          possible there is no deployment for the
                                          branch, or this was set before the
                                          deployment was canceled, in which case
                                          this will point to a cancelled
                                          deployment, in either case the proxy
                                          will fallback to the
                                          fallbackDeploymentId.
                                      fallbackDeploymentId:
                                        type: string
                                        description: >-
                                          This is the deployment of the fallback
                                          host at the time the commit alias was
                                          created. It is possible for this to be a
                                          deleted deployment, in which case the
                                          proxy will show that the deployment is
                                          deleted. It will not use the
                                          fallbackHost, as a future deployment on
                                          the fallback host could be invalid for
                                          this deployment, and it could lead to
                                          confusion / incorrect behavior for the
                                          commit alias.
                                      fallbackHost:
                                        type: string
                                        description: >-
                                          Temporary for backwards compatibility.
                                          Can remove when metadata change is
                                          released
                                      branchAlias:
                                        type: string
                                      projectId:
                                        type: string
                                        description: >-
                                          The project ID of the microfrontends
                                          application.
                                    required:
                                      - projectId
                                    type: object
                                    description: >-
                                      A list of the deployment routing
                                      information for each project.
                                  type: array
                                  description: >-
                                    A list of the deployment routing information
                                    for each project.
                          required:
                            - applications
                            - defaultApp
                          type: object
                          description: >-
                            The microfrontends for the alias including the
                            routing configuration
                      required:
                        - alias
                        - created
                        - deploymentId
                        - projectId
                        - uid
                      type: object
                    type: array
                  pagination:
                    $ref: '#/components/schemas/Pagination'
                required:
                  - aliases
                  - pagination
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
  schemas:
    Pagination:
      properties:
        count:
          type: number
          description: Amount of items in the current page.
          example: 20
        next:
          nullable: true
          type: number
          description: Timestamp that must be used to request the next page.
          example: 1540095775951
        prev:
          nullable: true
          type: number
          description: Timestamp that must be used to request the previous page.
          example: 1540095775951
      required:
        - count
        - next
        - prev
      type: object
      description: >-
        This object contains information related to the pagination of the
        current request, including the necessary parameters to get the next or
        previous page of data.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````