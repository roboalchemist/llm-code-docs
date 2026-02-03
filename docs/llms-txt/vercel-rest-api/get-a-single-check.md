# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/get-a-single-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a single check

> Return a detailed response for a single check.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks/{checkId}
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
  /v1/deployments/{deploymentId}/checks/{checkId}:
    get:
      tags:
        - checks
      summary: Get a single check
      description: Return a detailed response for a single check.
      operationId: getCheck
      parameters:
        - name: deploymentId
          description: The deployment to get the check for.
          in: path
          required: true
          schema:
            description: The deployment to get the check for.
            example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
            type: string
        - name: checkId
          description: The check to fetch
          in: path
          required: true
          schema:
            description: The check to fetch
            example: check_2qn7PZrx89yxY34vEZPD31Y9XVj6
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
                  id:
                    type: string
                  name:
                    type: string
                  path:
                    type: string
                  status:
                    type: string
                    enum:
                      - registered
                      - running
                      - completed
                  conclusion:
                    type: string
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
                      - stale
                  blocking:
                    type: boolean
                    enum:
                      - false
                      - true
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
                  detailsUrl:
                    type: string
                  integrationId:
                    type: string
                  deploymentId:
                    type: string
                  externalId:
                    type: string
                  createdAt:
                    type: number
                  updatedAt:
                    type: number
                  startedAt:
                    type: number
                  completedAt:
                    type: number
                  rerequestable:
                    type: boolean
                    enum:
                      - false
                      - true
                required:
                  - blocking
                  - createdAt
                  - deploymentId
                  - id
                  - integrationId
                  - name
                  - status
                  - updatedAt
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: >-
            You do not have permission to access this resource.

            The provided token is not from an OAuth2 Client that created the
            Check
        '404':
          description: |-
            Check was not found
            The deployment was not found
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````