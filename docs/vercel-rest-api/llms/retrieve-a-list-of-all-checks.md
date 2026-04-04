# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/retrieve-a-list-of-all-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a list of all checks

> List all of the checks created for a deployment.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks
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
  /v1/deployments/{deploymentId}/checks:
    get:
      tags:
        - checks
      summary: Retrieve a list of all checks
      description: List all of the checks created for a deployment.
      operationId: getAllChecks
      parameters:
        - name: deploymentId
          description: The deployment to get all checks for
          in: path
          required: true
          schema:
            description: The deployment to get all checks for
            example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
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
                properties:
                  checks:
                    items:
                      properties:
                        completedAt:
                          type: number
                        conclusion:
                          type: string
                          enum:
                            - canceled
                            - failed
                            - neutral
                            - succeeded
                            - skipped
                            - stale
                        createdAt:
                          type: number
                        detailsUrl:
                          type: string
                        id:
                          type: string
                        integrationId:
                          type: string
                        name:
                          type: string
                        output:
                          properties:
                            metrics:
                              properties:
                                FCP:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - source
                                    - value
                                  type: object
                                LCP:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - source
                                    - value
                                  type: object
                                CLS:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - source
                                    - value
                                  type: object
                                TBT:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - source
                                    - value
                                  type: object
                                virtualExperienceScore:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - source
                                    - value
                                  type: object
                              required:
                                - CLS
                                - FCP
                                - LCP
                                - TBT
                              type: object
                          type: object
                        path:
                          type: string
                        rerequestable:
                          type: boolean
                          enum:
                            - false
                            - true
                        blocking:
                          type: boolean
                          enum:
                            - false
                            - true
                        startedAt:
                          type: number
                        status:
                          type: string
                          enum:
                            - registered
                            - running
                            - completed
                        updatedAt:
                          type: number
                      required:
                        - blocking
                        - createdAt
                        - id
                        - integrationId
                        - name
                        - rerequestable
                        - status
                        - updatedAt
                      type: object
                    type: array
                required:
                  - checks
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