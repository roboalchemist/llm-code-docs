# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-list-of-integration-log-drains-deprecated.md

# Retrieves a list of Integration log drains (deprecated)

> Retrieves a list of all Integration log drains that are defined for the authenticated user or team. When using an OAuth2 token, the list is limited to log drains created by the authenticated integration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/integrations/log-drains
paths:
  path: /v2/integrations/log-drains
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
    body: {}
    codeSamples:
      - label: getIntegrationLogDrains
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.GetIntegrationLogDrains(ctx, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseBodies != nil {\n        // handle response\n    }\n}"
      - label: getIntegrationLogDrains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.getIntegrationLogDrains({
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
          - type: array
            items:
              allOf:
                - properties:
                    clientId:
                      type: string
                      description: >-
                        The oauth2 client application id that created this log
                        drain
                      example: oac_xRhY4LAB7yLhUADD69EvV7ct
                    configurationId:
                      type: string
                      description: The client configuration this log drain was created with
                      example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                    createdAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the log drain was
                        created
                      example: 1558531915505
                    id:
                      type: string
                      description: >-
                        The unique identifier of the log drain. Always prefixed
                        with `ld_`
                      example: ld_nBuA7zCID8g4QZ8g
                    deliveryFormat:
                      type: string
                      enum:
                        - json
                        - ndjson
                        - syslog
                        - protobuf
                      description: The delivery log format
                      example: json
                    name:
                      type: string
                      description: The name of the log drain
                      example: My first log drain
                    ownerId:
                      type: string
                      description: >-
                        The identifier of the team or user whose events will
                        trigger the log drain
                      example: kr1PsOIzqEL5Xg6M4VZcZosf
                    projectId:
                      nullable: true
                      type: string
                      example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                    projectIds:
                      items:
                        type: string
                      type: array
                      description: >-
                        The identifier of the projects this log drain is
                        associated with
                      example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                    url:
                      type: string
                      description: The URL to call when logs are generated
                      example: https://example.com/log-drain
                    sources:
                      items:
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
                        The sources from which logs are currently being
                        delivered to this log drain.
                      example:
                        - build
                        - edge
                    createdFrom:
                      type: string
                      enum:
                        - integration
                        - self-served
                      description: >-
                        Whether the log drain was created by an integration or
                        by a user
                      example: integration
                    headers:
                      additionalProperties:
                        type: string
                      type: object
                      description: The headers to send with the request
                      example: '{"Authorization": "Bearer 123"}'
                    environments:
                      items:
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
                      type: string
                      description: The branch regexp of log drain
                      example: feature/*
                    samplingRate:
                      type: number
                      description: The sampling rate of log drain
                      example: 0.5
                    source:
                      oneOf:
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
                  required:
                    - createdAt
                    - id
                    - name
                    - ownerId
                    - url
                    - source
                  type: object
        examples:
          example:
            value:
              - clientId: oac_xRhY4LAB7yLhUADD69EvV7ct
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
        description: A list of log drains
    '400': {}
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