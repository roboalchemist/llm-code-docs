# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/creates-a-new-integration-log-drain-deprecated.md

# Creates a new Integration Log Drain (deprecated)

> Creates an Integration log drain. This endpoint must be called with an OAuth2 client (integration), since log drains are tied to integrations. If it is called with a different token type it will produce a 400 error.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/integrations/log-drains
paths:
  path: /v2/integrations/log-drains
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
              name:
                allOf:
                  - description: The name of the log drain
                    example: My first log drain
                    maxLength: 100
                    pattern: ^[A-z0-9_ -]+$
                    type: string
              projectIds:
                allOf:
                  - minItems: 1
                    maxItems: 50
                    type: array
                    items:
                      pattern: ^[a-zA-z0-9_]+$
                      type: string
              secret:
                allOf:
                  - description: >-
                      A secret to sign log drain notification headers so a
                      consumer can verify their authenticity
                    example: a1Xsfd325fXcs
                    maxLength: 100
                    pattern: ^[A-z0-9_ -]+$
                    type: string
              deliveryFormat:
                allOf:
                  - description: The delivery log format
                    example: json
                    enum:
                      - json
                      - ndjson
              url:
                allOf:
                  - description: >-
                      The url where you will receive logs. The protocol must be
                      `https://` or `http://` when type is `json` and `ndjson`.
                    example: https://example.com/log-drain
                    format: uri
                    pattern: ^https?://
                    type: string
              sources:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - static
                        - lambda
                        - build
                        - edge
                        - external
                        - firewall
                    minItems: 1
              headers:
                allOf:
                  - description: Headers to be sent together with the request
                    type: object
                    additionalProperties:
                      type: string
              environments:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - preview
                        - production
                    minItems: 1
            required: true
            requiredProperties:
              - name
              - url
        examples:
          example:
            value:
              name: My first log drain
              projectIds:
                - <string>
              secret: a1Xsfd325fXcs
              deliveryFormat: json
              url: https://example.com/log-drain
              sources:
                - static
              headers: {}
              environments:
                - preview
    codeSamples:
      - label: createLogDrain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.CreateLogDrain(ctx, nil, nil, &operations.CreateLogDrainRequestBody{\n        Name: \"My first log drain\",\n        Secret: vercel.String(\"a1Xsfd325fXcs\"),\n        DeliveryFormat: operations.DeliveryFormatJSON.ToPointer(),\n        URL: \"https://example.com/log-drain\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createLogDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.createLogDrain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "My first log drain",
                secret: "a1Xsfd325fXcs",
                deliveryFormat: "json",
                url: "https://example.com/log-drain",
              },
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
              clientId:
                allOf:
                  - type: string
                    description: >-
                      The oauth2 client application id that created this log
                      drain
                    example: oac_xRhY4LAB7yLhUADD69EvV7ct
              configurationId:
                allOf:
                  - type: string
                    description: The client configuration this log drain was created with
                    example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              createdAt:
                allOf:
                  - type: number
                    description: A timestamp that tells you when the log drain was created
                    example: 1558531915505
              id:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier of the log drain. Always prefixed
                      with `ld_`
                    example: ld_nBuA7zCID8g4QZ8g
              deliveryFormat:
                allOf:
                  - type: string
                    enum:
                      - json
                      - ndjson
                      - syslog
                      - protobuf
                    description: The delivery log format
                    example: json
              name:
                allOf:
                  - type: string
                    description: The name of the log drain
                    example: My first log drain
              ownerId:
                allOf:
                  - type: string
                    description: >-
                      The identifier of the team or user whose events will
                      trigger the log drain
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              projectId:
                allOf:
                  - nullable: true
                    type: string
                    example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The identifier of the projects this log drain is
                      associated with
                    example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              url:
                allOf:
                  - type: string
                    description: The URL to call when logs are generated
                    example: https://example.com/log-drain
              sources:
                allOf:
                  - items:
                      type: string
                      enum:
                        - build
                        - edge
                        - lambda
                        - static
                        - external
                        - firewall
                        - redirect
                      description: >-
                        The sources from which logs are currently being
                        delivered to this log drain.
                      example:
                        - build
                        - edge
                    type: array
                    description: >-
                      The sources from which logs are currently being delivered
                      to this log drain.
                    example:
                      - build
                      - edge
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - integration
                      - self-served
                    description: >-
                      Whether the log drain was created by an integration or by
                      a user
                    example: integration
              headers:
                allOf:
                  - additionalProperties:
                      type: string
                    type: object
                    description: The headers to send with the request
                    example: '{"Authorization": "Bearer 123"}'
              environments:
                allOf:
                  - items:
                      type: string
                      enum:
                        - production
                        - preview
                      description: The environment of log drain
                      example:
                        - production
                    type: array
                    description: The environment of log drain
                    example:
                      - production
              branch:
                allOf:
                  - type: string
                    description: The branch regexp of log drain
                    example: feature/*
              samplingRate:
                allOf:
                  - type: number
                    description: The sampling rate of log drain
                    example: 0.5
              source:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - self-served
                        required:
                          - kind
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - integration
                          resourceId:
                            type: string
                          externalResourceId:
                            type: string
                          integrationId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - kind
                          - integrationId
                          - integrationConfigurationId
                        type: object
            requiredProperties:
              - createdAt
              - id
              - name
              - ownerId
              - url
              - source
        examples:
          example:
            value:
              clientId: oac_xRhY4LAB7yLhUADD69EvV7ct
              configurationId: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              createdAt: 1558531915505
              id: ld_nBuA7zCID8g4QZ8g
              deliveryFormat: json
              name: My first log drain
              ownerId: kr1PsOIzqEL5Xg6M4VZcZosf
              projectId: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              projectIds: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              url: https://example.com/log-drain
              sources:
                - build
                - edge
              createdFrom: integration
              headers: '{"Authorization": "Bearer 123"}'
              environments:
                - production
              branch: feature/*
              samplingRate: 0.5
              source:
                kind: self-served
        description: The log drain was successfully created
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              The provided token is not from an OAuth2 Client
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          The provided token is not from an OAuth2 Client
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