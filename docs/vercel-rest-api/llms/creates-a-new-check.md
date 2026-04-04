# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/creates-a-new-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Creates a new Check

> Creates a new check. This endpoint must be called with an OAuth2 or it will produce a 400 error.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks
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
    post:
      tags:
        - checks
      summary: Creates a new Check
      description: >-
        Creates a new check. This endpoint must be called with an OAuth2 or it
        will produce a 400 error.
      operationId: createCheck
      parameters:
        - name: deploymentId
          description: The deployment to create the check for.
          in: path
          required: true
          schema:
            description: The deployment to create the check for.
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
      requestBody:
        content:
          application/json:
            schema:
              properties:
                name:
                  description: The name of the check being created
                  maxLength: 100
                  example: Performance Check
                  type: string
                path:
                  description: Path of the page that is being checked
                  type: string
                  maxLength: 255
                  example: /
                blocking:
                  description: Whether the check should block a deployment from succeeding
                  type: boolean
                  example: true
                detailsUrl:
                  description: URL to display for further details
                  type: string
                  example: http://example.com
                externalId:
                  description: An identifier that can be used as an external reference
                  type: string
                  example: 1234abc
                rerequestable:
                  description: >-
                    Whether a user should be able to request for the check to be
                    rerun if it fails
                  type: boolean
                  example: true
              required:
                - name
                - blocking
              type: object
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                    example: chk_1a2b3c4d5e6f7g8h9i0j
                  name:
                    type: string
                    example: Performance Check
                  path:
                    type: string
                    example: /api/users
                  status:
                    type: string
                    enum:
                      - registered
                      - running
                      - completed
                    example: completed
                  conclusion:
                    type: string
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
                      - stale
                    example: succeeded
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
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
            Cannot create check for finished deployment
            The provided token is not from an OAuth2 Client
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