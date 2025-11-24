# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/get-deployment-events.md

# Get deployment events

> Get the build logs of a deployment by deployment ID and build ID. It can work as an infinite stream of logs or as a JSON endpoint depending on the input parameters.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/deployments/{idOrUrl}/events
paths:
  path: /v3/deployments/{idOrUrl}/events
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
        idOrUrl:
          schema:
            - type: string
              required: true
              description: The unique identifier or hostname of the deployment.
              example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
      query:
        direction:
          schema:
            - type: enum<string>
              enum:
                - backward
                - forward
              required: false
              description: Order of the returned events based on the timestamp.
              default: forward
              example: backward
        follow:
          schema:
            - type: enum<number>
              enum:
                - 0
                - 1
              required: false
              description: >-
                When enabled, this endpoint will return live events as they
                happen.
              example: 1
        limit:
          schema:
            - type: number
              required: false
              description: >-
                Maximum number of events to return. Provide `-1` to return all
                available logs.
              example: 100
        name:
          schema:
            - type: string
              required: false
              description: Deployment build ID.
              example: bld_cotnkcr76
        since:
          schema:
            - type: number
              required: false
              description: Timestamp for when build logs should be pulled from.
              example: 1540095775941
        until:
          schema:
            - type: number
              required: false
              description: Timestamp for when the build logs should be pulled up until.
              example: 1540106318643
        statusCode:
          schema:
            - type: number
              required: false
              description: HTTP status code range to filter events by.
              example: 5xx
            - type: string
              required: false
              description: HTTP status code range to filter events by.
              example: 5xx
        delimiter:
          schema:
            - type: enum<number>
              enum:
                - 0
                - 1
              required: false
              example: 1
        builds:
          schema:
            - type: enum<number>
              enum:
                - 0
                - 1
              required: false
              example: 1
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
      - label: getDeploymentEvents
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.GetDeploymentEvents(ctx, operations.GetDeploymentEventsRequest{\n        IDOrURL: \"dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd\",\n        Direction: operations.DirectionBackward.ToPointer(),\n        Follow: vercel.Float64(1),\n        Limit: vercel.Float64(100),\n        Name: vercel.String(\"bld_cotnkcr76\"),\n        Since: vercel.Float64(1540095775941),\n        Until: vercel.Float64(1540106318643),\n        StatusCode: vercel.Pointer(operations.CreateStatusCodeStr(\n            \"5xx\",\n        )),\n        Delimiter: vercel.Float64(1),\n        Builds: vercel.Float64(1),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: getDeploymentEvents
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.getDeploymentEvents({
              idOrUrl: "dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd",
              direction: "backward",
              follow: 1,
              limit: 100,
              name: "bld_cotnkcr76",
              since: 1540095775941,
              until: 1540106318643,
              statusCode: "5xx",
              delimiter: 1,
              builds: 1,
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
                - oneOf:
                    - properties:
                        type:
                          type: string
                          enum:
                            - delimiter
                            - command
                            - stdout
                            - stderr
                            - exit
                            - deployment-state
                            - middleware
                            - middleware-invocation
                            - edge-function-invocation
                            - metric
                            - report
                            - fatal
                        created:
                          type: number
                        payload:
                          properties:
                            deploymentId:
                              type: string
                            info:
                              properties:
                                type:
                                  type: string
                                name:
                                  type: string
                                entrypoint:
                                  type: string
                                path:
                                  type: string
                                step:
                                  type: string
                                readyState:
                                  type: string
                              required:
                                - type
                                - name
                              type: object
                            text:
                              type: string
                            id:
                              type: string
                            date:
                              type: number
                            serial:
                              type: string
                            created:
                              type: number
                            statusCode:
                              type: number
                            requestId:
                              type: string
                            proxy:
                              properties:
                                timestamp:
                                  type: number
                                method:
                                  type: string
                                host:
                                  type: string
                                path:
                                  type: string
                                statusCode:
                                  type: number
                                userAgent:
                                  items:
                                    type: string
                                  type: array
                                referer:
                                  type: string
                                clientIp:
                                  type: string
                                region:
                                  type: string
                                scheme:
                                  type: string
                                responseByteSize:
                                  type: number
                                cacheId:
                                  type: string
                                pathType:
                                  type: string
                                pathTypeVariant:
                                  type: string
                                vercelId:
                                  type: string
                                vercelCache:
                                  type: string
                                  enum:
                                    - MISS
                                    - HIT
                                    - STALE
                                    - BYPASS
                                    - PRERENDER
                                    - REVALIDATED
                                lambdaRegion:
                                  type: string
                                wafAction:
                                  type: string
                                  enum:
                                    - log
                                    - challenge
                                    - deny
                                    - bypass
                                    - rate_limit
                                wafRuleId:
                                  type: string
                              required:
                                - timestamp
                                - method
                                - host
                                - path
                                - userAgent
                                - referer
                                - region
                              type: object
                          required:
                            - deploymentId
                            - id
                            - date
                            - serial
                          type: object
                      required:
                        - type
                        - created
                        - payload
                      type: object
                    - properties:
                        created:
                          type: number
                        date:
                          type: number
                        deploymentId:
                          type: string
                        id:
                          type: string
                        info:
                          properties:
                            type:
                              type: string
                            name:
                              type: string
                            entrypoint:
                              type: string
                            path:
                              type: string
                            step:
                              type: string
                            readyState:
                              type: string
                          required:
                            - type
                            - name
                          type: object
                        serial:
                          type: string
                        text:
                          type: string
                        type:
                          type: string
                          enum:
                            - delimiter
                            - command
                            - stdout
                            - stderr
                            - exit
                            - deployment-state
                            - middleware
                            - middleware-invocation
                            - edge-function-invocation
                            - metric
                            - report
                            - fatal
                        level:
                          type: string
                          enum:
                            - error
                            - warning
                      required:
                        - created
                        - date
                        - deploymentId
                        - id
                        - info
                        - serial
                        - type
                      type: object
                  nullable: true
          - type: 'null'
        examples:
          example:
            value:
              - type: delimiter
                created: 123
                payload:
                  deploymentId: <string>
                  info:
                    type: <string>
                    name: <string>
                    entrypoint: <string>
                    path: <string>
                    step: <string>
                    readyState: <string>
                  text: <string>
                  id: <string>
                  date: 123
                  serial: <string>
                  created: 123
                  statusCode: 123
                  requestId: <string>
                  proxy:
                    timestamp: 123
                    method: <string>
                    host: <string>
                    path: <string>
                    statusCode: 123
                    userAgent:
                      - <string>
                    referer: <string>
                    clientIp: <string>
                    region: <string>
                    scheme: <string>
                    responseByteSize: 123
                    cacheId: <string>
                    pathType: <string>
                    pathTypeVariant: <string>
                    vercelId: <string>
                    vercelCache: MISS
                    lambdaRegion: <string>
                    wafAction: log
                    wafRuleId: <string>
        description: ''
      application/stream+json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - delimiter
                      - command
                      - stdout
                      - stderr
                      - exit
                      - deployment-state
                      - middleware
                      - middleware-invocation
                      - edge-function-invocation
                      - metric
                      - report
                      - fatal
              created:
                allOf:
                  - type: number
              payload:
                allOf:
                  - properties:
                      deploymentId:
                        type: string
                      info:
                        properties:
                          type:
                            type: string
                          name:
                            type: string
                          entrypoint:
                            type: string
                          path:
                            type: string
                          step:
                            type: string
                          readyState:
                            type: string
                        required:
                          - type
                          - name
                        type: object
                      text:
                        type: string
                      id:
                        type: string
                      date:
                        type: number
                      serial:
                        type: string
                      created:
                        type: number
                      statusCode:
                        type: number
                      requestId:
                        type: string
                      proxy:
                        properties:
                          timestamp:
                            type: number
                          method:
                            type: string
                          host:
                            type: string
                          path:
                            type: string
                          statusCode:
                            type: number
                          userAgent:
                            items:
                              type: string
                            type: array
                          referer:
                            type: string
                          clientIp:
                            type: string
                          region:
                            type: string
                          scheme:
                            type: string
                          responseByteSize:
                            type: number
                          cacheId:
                            type: string
                          pathType:
                            type: string
                          pathTypeVariant:
                            type: string
                          vercelId:
                            type: string
                          vercelCache:
                            type: string
                            enum:
                              - MISS
                              - HIT
                              - STALE
                              - BYPASS
                              - PRERENDER
                              - REVALIDATED
                          lambdaRegion:
                            type: string
                          wafAction:
                            type: string
                            enum:
                              - log
                              - challenge
                              - deny
                              - bypass
                              - rate_limit
                          wafRuleId:
                            type: string
                        required:
                          - timestamp
                          - method
                          - host
                          - path
                          - userAgent
                          - referer
                          - region
                        type: object
                    required:
                      - deploymentId
                      - id
                      - date
                      - serial
                    type: object
            requiredProperties:
              - type
              - created
              - payload
          - type: object
            properties:
              created:
                allOf:
                  - type: number
              date:
                allOf:
                  - type: number
              deploymentId:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              info:
                allOf:
                  - properties:
                      type:
                        type: string
                      name:
                        type: string
                      entrypoint:
                        type: string
                      path:
                        type: string
                      step:
                        type: string
                      readyState:
                        type: string
                    required:
                      - type
                      - name
                    type: object
              serial:
                allOf:
                  - type: string
              text:
                allOf:
                  - type: string
              type:
                allOf:
                  - type: string
                    enum:
                      - delimiter
                      - command
                      - stdout
                      - stderr
                      - exit
                      - deployment-state
                      - middleware
                      - middleware-invocation
                      - edge-function-invocation
                      - metric
                      - report
                      - fatal
              level:
                allOf:
                  - type: string
                    enum:
                      - error
                      - warning
            requiredProperties:
              - created
              - date
              - deploymentId
              - id
              - info
              - serial
              - type
        examples:
          example:
            value:
              type: delimiter
              created: 123
              payload:
                deploymentId: <string>
                info:
                  type: <string>
                  name: <string>
                  entrypoint: <string>
                  path: <string>
                  step: <string>
                  readyState: <string>
                text: <string>
                id: <string>
                date: 123
                serial: <string>
                created: 123
                statusCode: 123
                requestId: <string>
                proxy:
                  timestamp: 123
                  method: <string>
                  host: <string>
                  path: <string>
                  statusCode: 123
                  userAgent:
                    - <string>
                  referer: <string>
                  clientIp: <string>
                  region: <string>
                  scheme: <string>
                  responseByteSize: 123
                  cacheId: <string>
                  pathType: <string>
                  pathTypeVariant: <string>
                  vercelId: <string>
                  vercelCache: MISS
                  lambdaRegion: <string>
                  wafAction: log
                  wafRuleId: <string>
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````