# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/validate-drain-delivery-configuration.md

# Validate Drain delivery configuration

> Validate the delivery configuration of a Drain using sample events.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains/test
paths:
  path: /v1/drains/test
  method: post
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
              schemas:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - version
                      properties:
                        version:
                          type: string
              delivery:
                allOf:
                  - type: object
                    oneOf:
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - traces
                                properties:
                                  traces:
                                    type: string
                          encoding:
                            type: string
                            enum:
                              - proto
                              - json
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - secret
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          secret:
                            type: string
            requiredProperties:
              - schemas
              - delivery
            additionalProperties: false
        examples:
          example:
            value:
              schemas: {}
              delivery:
                type: <string>
                endpoint: <string>
                compression: gzip
                encoding: json
                headers: {}
                secret: <string>
    codeSamples:
      - label: testDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.testDrain({
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
            properties: {}
          - type: object
            properties:
              status:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
              endpoint:
                allOf:
                  - type: string
            requiredProperties:
              - status
              - error
              - endpoint
        examples:
          example:
            value: {}
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
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
  deprecated: false
  type: path
components:
  schemas: {}

````