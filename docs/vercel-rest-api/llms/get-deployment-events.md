# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/get-deployment-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get deployment events

> Get the build logs of a deployment by deployment ID and build ID. It can work as an infinite stream of logs or as a JSON endpoint depending on the input parameters.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/deployments/{idOrUrl}/events
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
  /v3/deployments/{idOrUrl}/events:
    get:
      tags:
        - deployments
      summary: Get deployment events
      description: >-
        Get the build logs of a deployment by deployment ID and build ID. It can
        work as an infinite stream of logs or as a JSON endpoint depending on
        the input parameters.
      operationId: getDeploymentEvents
      parameters:
        - name: idOrUrl
          description: The unique identifier or hostname of the deployment.
          in: path
          required: true
          schema:
            type: string
            example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
            description: The unique identifier or hostname of the deployment.
        - name: direction
          description: Order of the returned events based on the timestamp.
          in: query
          required: false
          schema:
            type: string
            enum:
              - backward
              - forward
            default: forward
            example: backward
            description: Order of the returned events based on the timestamp.
        - name: follow
          description: When enabled, this endpoint will return live events as they happen.
          in: query
          required: false
          schema:
            type: number
            enum:
              - 0
              - 1
            example: 1
            description: >-
              When enabled, this endpoint will return live events as they
              happen.
        - name: limit
          description: >-
            Maximum number of events to return. Provide `-1` to return all
            available logs.
          in: query
          required: false
          schema:
            type: number
            example: 100
            description: >-
              Maximum number of events to return. Provide `-1` to return all
              available logs.
        - name: name
          description: Deployment build ID.
          in: query
          required: false
          schema:
            type: string
            example: bld_cotnkcr76
            description: Deployment build ID.
        - name: since
          description: Timestamp for when build logs should be pulled from.
          in: query
          required: false
          schema:
            type: number
            example: 1540095775941
            description: Timestamp for when build logs should be pulled from.
        - name: until
          description: Timestamp for when the build logs should be pulled up until.
          in: query
          required: false
          schema:
            type: number
            example: 1540106318643
            description: Timestamp for when the build logs should be pulled up until.
        - name: statusCode
          description: HTTP status code range to filter events by.
          in: query
          required: false
          schema:
            example: 5xx
            description: HTTP status code range to filter events by.
            oneOf:
              - type: number
              - type: string
        - name: delimiter
          in: query
          required: false
          schema:
            type: number
            enum:
              - 0
              - 1
            example: 1
        - name: builds
          in: query
          required: false
          schema:
            type: number
            enum:
              - 0
              - 1
            example: 1
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
                type: array
                items:
                  oneOf:
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
                                - name
                                - type
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
                                - host
                                - method
                                - path
                                - referer
                                - region
                                - timestamp
                                - userAgent
                              type: object
                          required:
                            - date
                            - deploymentId
                            - id
                            - serial
                          type: object
                      required:
                        - created
                        - payload
                        - type
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
                            - name
                            - type
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
                nullable: true
            application/stream+json:
              schema:
                oneOf:
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
                              - name
                              - type
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
                              - host
                              - method
                              - path
                              - referer
                              - region
                              - timestamp
                              - userAgent
                            type: object
                        required:
                          - date
                          - deploymentId
                          - id
                          - serial
                        type: object
                    required:
                      - created
                      - payload
                      - type
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
                          - name
                          - type
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
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '500':
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