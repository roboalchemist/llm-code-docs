# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/get-rolling-release-configuration.md

# Get rolling release configuration

> Get the Rolling Releases configuration for a project. The project-level config is simply a template that will be used for any future rolling release, and not the configuration for any active rolling release.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release/config
paths:
  path: /v1/projects/{idOrName}/rolling-release/config
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
      path:
        idOrName:
          schema:
            - type: string
              required: true
              description: Project ID or project name (URL-encoded)
      query:
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
      - label: getRollingReleaseConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.rollingRelease.getRollingReleaseConfig({
              idOrName: "<value>",
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
              rollingRelease:
                allOf:
                  - nullable: true
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
            requiredProperties:
              - rollingRelease
        examples:
          example:
            value:
              rollingRelease:
                target: production
                stages:
                  - targetPercentage: 25
                    requireApproval: false
                    duration: 600
                    linearShift: false
                canaryResponseHeader: false
        description: ''
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
  schemas: {}

````