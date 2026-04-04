# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/update-a-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a check

> Update an existing check. This endpoint must be called with an OAuth2 or it will produce a 400 error.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/checks/{checkId}
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
    patch:
      tags:
        - checks
      summary: Update a check
      description: >-
        Update an existing check. This endpoint must be called with an OAuth2 or
        it will produce a 400 error.
      operationId: updateCheck
      parameters:
        - name: deploymentId
          description: The deployment to update the check for.
          in: path
          required: true
          schema:
            description: The deployment to update the check for.
            example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
            type: string
        - name: checkId
          description: The check being updated
          in: path
          required: true
          schema:
            description: The check being updated
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
                status:
                  description: The current status of the check
                  enum:
                    - running
                    - completed
                conclusion:
                  description: The result of the check being run
                  enum:
                    - canceled
                    - failed
                    - neutral
                    - succeeded
                    - skipped
                detailsUrl:
                  description: >-
                    A URL a user may visit to see more information about the
                    check
                  type: string
                  example: https://example.com/check/run/1234abc
                output:
                  description: The results of the check Run
                  type: object
                  properties:
                    metrics:
                      type: object
                      description: Metrics about the page
                      required:
                        - FCP
                        - LCP
                        - CLS
                        - TBT
                      additionalProperties: false
                      properties:
                        FCP:
                          type: object
                          required:
                            - value
                            - source
                          properties:
                            value:
                              type: number
                              example: 1200
                              description: First Contentful Paint value
                              nullable: true
                            previousValue:
                              type: number
                              example: 900
                              description: >-
                                Previous First Contentful Paint value to display
                                a delta
                            source:
                              type: string
                              enum:
                                - web-vitals
                        LCP:
                          type: object
                          required:
                            - value
                            - source
                          properties:
                            value:
                              type: number
                              example: 1200
                              description: Largest Contentful Paint value
                              nullable: true
                            previousValue:
                              type: number
                              example: 1000
                              description: >-
                                Previous Largest Contentful Paint value to
                                display a delta
                            source:
                              type: string
                              enum:
                                - web-vitals
                        CLS:
                          type: object
                          required:
                            - value
                            - source
                          properties:
                            value:
                              type: number
                              example: 4
                              description: Cumulative Layout Shift value
                              nullable: true
                            previousValue:
                              type: number
                              example: 2
                              description: >-
                                Previous Cumulative Layout Shift value to
                                display a delta
                            source:
                              type: string
                              enum:
                                - web-vitals
                        TBT:
                          type: object
                          required:
                            - value
                            - source
                          properties:
                            value:
                              type: number
                              example: 3000
                              description: Total Blocking Time value
                              nullable: true
                            previousValue:
                              type: number
                              example: 3500
                              description: >-
                                Previous Total Blocking Time value to display a
                                delta
                            source:
                              enum:
                                - web-vitals
                        virtualExperienceScore:
                          type: object
                          required:
                            - value
                            - source
                          properties:
                            value:
                              type: integer
                              maximum: 100
                              minimum: 0
                              example: 30
                              description: >-
                                The calculated Virtual Experience Score value,
                                between 0 and 100
                              nullable: true
                            previousValue:
                              type: integer
                              maximum: 100
                              minimum: 0
                              example: 35
                              description: >-
                                A previous Virtual Experience Score value to
                                display a delta, between 0 and 100
                            source:
                              enum:
                                - web-vitals
                externalId:
                  description: An identifier that can be used as an external reference
                  type: string
                  example: 1234abc
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
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
            The provided token is not from an OAuth2 Client
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: |-
            Check was not found
            The deployment was not found
        '413':
          description: The output provided is too large
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````