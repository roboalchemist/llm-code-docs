# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/connect/configures-static-ips-for-a-project.md

# Configures Static IPs for a project

> Allows configuring Static IPs for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/shared-connect-links
paths:
  path: /v1/projects/{idOrName}/shared-connect-links
  method: patch
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
              description: The unique project identifier or the project name
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              builds:
                allOf:
                  - &ref_0
                    type: boolean
                    description: Whether to use Static IPs for builds.
              regions:
                allOf:
                  - &ref_1
                    type: array
                    items:
                      type: string
                      maxLength: 4
                      description: The region in which to enable Static IPs.
                      example: iad1
                    minItems: 0
                    maxItems: 3
                    uniqueItems: true
            requiredProperties:
              - builds
          - type: object
            properties:
              builds:
                allOf:
                  - *ref_0
              regions:
                allOf:
                  - *ref_1
            requiredProperties:
              - regions
        examples:
          example:
            value:
              builds: true
              regions:
                - iad1
    codeSamples:
      - label: updateStaticIps
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.connect.updateStaticIps({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                regions: [
                  "iad1",
                ],
              },
            });

            console.log(result);
          }

          run();
      - label: updateStaticIps
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.staticIps.updateStaticIps({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                regions: [
                  "iad1",
                ],
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - properties:
                    envId:
                      oneOf:
                        - type: string
                        - type: string
                          enum:
                            - preview
                            - production
                    connectConfigurationId:
                      type: string
                    dc:
                      type: string
                    passive:
                      type: boolean
                    buildsEnabled:
                      type: boolean
                    aws:
                      properties:
                        subnetIds:
                          items:
                            type: string
                          type: array
                        securityGroupId:
                          type: string
                      required:
                        - subnetIds
                        - securityGroupId
                      type: object
                    createdAt:
                      type: number
                    updatedAt:
                      type: number
                  required:
                    - envId
                    - connectConfigurationId
                    - passive
                    - buildsEnabled
                    - createdAt
                    - updatedAt
                  type: object
        examples:
          example:
            value:
              - envId: <string>
                connectConfigurationId: <string>
                dc: <string>
                passive: true
                buildsEnabled: true
                aws:
                  subnetIds:
                    - <string>
                  securityGroupId: <string>
                createdAt: 123
                updatedAt: 123
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '402': {}
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````