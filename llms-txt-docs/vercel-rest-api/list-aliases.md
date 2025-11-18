# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/list-aliases.md

# List aliases

> Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/aliases
paths:
  path: /v4/aliases
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        domain:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              description: Get only aliases of the given domain name
              maxItems: 20
              example: my-test-domain.com
            - type: string
              description: Get only aliases of the given domain name
              example: my-test-domain.com
        from:
          schema:
            - type: number
              description: Get only aliases created after the provided timestamp
              deprecated: true
              example: 1540095775951
        limit:
          schema:
            - type: number
              description: Maximum number of aliases to list from a request
              example: 10
        projectId:
          schema:
            - type: string
              description: Filter aliases from the given `projectId`
              example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
        since:
          schema:
            - type: number
              description: Get aliases created after this JavaScript timestamp
              example: 1540095775941
        until:
          schema:
            - type: number
              description: Get aliases created before this JavaScript timestamp
              example: 1540095775951
        rollbackDeploymentId:
          schema:
            - type: string
              description: Get aliases that would be rolled back for the given deployment
              example: dpl_XXX
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listAliases
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.ListAliases(ctx, operations.ListAliasesRequest{\n        Domain: vercel.Pointer(operations.CreateDomainStr(\n            \"my-test-domain.com\",\n        )),\n        From: vercel.Float64(1540095775951),\n        Limit: vercel.Float64(10),\n        ProjectID: vercel.String(\"prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB\"),\n        Since: vercel.Float64(1540095775941),\n        Until: vercel.Float64(1540095775951),\n        RollbackDeploymentID: vercel.String(\"dpl_XXX\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listAliases
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.listAliases({
              domain: "my-test-domain.com",
              from: 1540095775951,
              limit: 10,
              projectId: "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              since: 1540095775941,
              until: 1540095775951,
              rollbackDeploymentId: "dpl_XXX",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              aliases:
                allOf:
                  - items:
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
                            - uid
                            - email
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
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - access
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
                              properties:
                                projectId:
                                  type: string
                              required:
                                - projectId
                              type: object
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
                                      - fallbackHost
                                      - branchAlias
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
                            - defaultApp
                            - applications
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
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - aliases
              - pagination
        examples:
          example:
            value:
              aliases:
                - alias: my-alias.vercel.app
                  created: '2017-04-26T23:00:34.232Z'
                  createdAt: 1540095775941
                  creator:
                    uid: 96SnxkFiMyVKsK3pnoHfx3Hz
                    email: john-doe@gmail.com
                    username: john-doe
                  deletedAt: 1540095775941
                  deployment:
                    id: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                    url: my-instant-deployment-3ij3cxz9qr.now.sh
                    meta: {}
                  deploymentId: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                  projectId: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                  redirect: <string>
                  redirectStatusCode: 301
                  uid: <string>
                  updatedAt: 1540095775941
                  protectionBypass: {}
                  microfrontends:
                    defaultApp:
                      projectId: <string>
                    applications:
                      - fallbackHost: <string>
                        projectId: <string>
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
        description: The paginated list of aliases
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
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

````