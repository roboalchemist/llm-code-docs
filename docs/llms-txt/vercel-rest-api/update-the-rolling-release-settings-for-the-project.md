# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/update-the-rolling-release-settings-for-the-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update the rolling release settings for the project

> Update (or disable) Rolling Releases for a project. When disabling with the resolve-on-disable feature flag enabled, any active rolling release document is resolved using the disableRolloutAction parameter: "abort" to roll back (default), or "complete" to promote the canary to production. When enabling or updating config, changes only affect the next production deployment and do not alter a rollout that's already in-flight. Note: Enabling Rolling Releases automatically enables skew protection on the project with the default value if it wasn't configured already.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/rolling-release/config
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
    patch:
      tags:
        - rolling-release
      summary: Update the rolling release settings for the project
      description: >-
        Update (or disable) Rolling Releases for a project. When disabling with
        the resolve-on-disable feature flag enabled, any active rolling release
        document is resolved using the disableRolloutAction parameter: "abort"
        to roll back (default), or "complete" to promote the canary to
        production. When enabling or updating config, changes only affect the
        next production deployment and do not alter a rollout that's already
        in-flight. Note: Enabling Rolling Releases automatically enables skew
        protection on the project with the default value if it wasn't configured
        already.
      operationId: updateRollingReleaseConfig
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
                oneOf:
                  - properties:
                      rollingRelease:
                        nullable: true
                    required:
                      - rollingRelease
                    type: object
                  - properties:
                      rollingRelease:
                        nullable: true
                        properties:
                          stages:
                            nullable: true
                            items:
                              properties:
                                targetPercentage:
                                  type: number
                                  description: >-
                                    The percentage of traffic to serve to the
                                    canary deployment (0-100)
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
                                    Duration in minutes for automatic
                                    advancement to the next stage
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
                                A stage object configured for a rolling release
                                once a new deployment is triggered the first
                                stage will be read in the proxy for first time
                                visitors, and if a RNG < targetPercentage then
                                it will serve the new deployment. Upon approval
                                the next stage will be read, etc.
                            type: array
                        type: object
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