# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/get-rolling-release-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get rolling release configuration

> Get the Rolling Releases configuration for a project. The project-level config is simply a template that will be used for any future rolling release, and not the configuration for any active rolling release.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release/config
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
  /v1/projects/{idOrName}/rolling-release/config:
    get:
      tags:
        - rolling-release
      summary: Get rolling release configuration
      description: >-
        Get the Rolling Releases configuration for a project. The project-level
        config is simply a template that will be used for any future rolling
        release, and not the configuration for any active rolling release.
      operationId: getRollingReleaseConfig
      parameters:
        - name: idOrName
          description: Project ID or project name (URL-encoded)
          in: path
          required: true
          schema:
            description: Project ID or project name (URL-encoded)
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
                  rollingRelease:
                    nullable: true
                    properties:
                      target:
                        type: string
                        description: >-
                          The environment that the release targets, currently
                          only supports production. Adding in case we want to
                          configure with alias groups or custom environments.
                        example: production
                      stages:
                        nullable: true
                        items:
                          properties:
                            targetPercentage:
                              type: number
                              description: >-
                                The percentage of traffic to serve to the canary
                                deployment (0-100)
                              example: 25
                            requireApproval:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                Whether or not this stage requires manual
                                approval to proceed
                              example: false
                            duration:
                              type: number
                              description: >-
                                Duration in minutes for automatic advancement to
                                the next stage
                              example: 600
                            linearShift:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                Whether to linearly shift traffic over the
                                duration of this stage
                              example: false
                          required:
                            - targetPercentage
                          type: object
                          description: >-
                            An array of all the stages required during a
                            deployment release. Each stage defines a target
                            percentage and advancement rules. The final stage
                            must always have targetPercentage: 100.
                        type: array
                        description: >-
                          An array of all the stages required during a
                          deployment release. Each stage defines a target
                          percentage and advancement rules. The final stage must
                          always have targetPercentage: 100.
                      canaryResponseHeader:
                        type: boolean
                        enum:
                          - false
                          - true
                        description: >-
                          Whether the request served by a canary deployment
                          should return a header indicating a canary was served.
                          Defaults to `false` when omitted.
                        example: false
                    required:
                      - target
                    type: object
                    description: >-
                      Project-level rolling release configuration that defines
                      how deployments should be gradually rolled out
                required:
                  - rollingRelease
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
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````