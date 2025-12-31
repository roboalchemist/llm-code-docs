# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logs/get-logs-for-a-deployment.md

# Get logs for a deployment

> Returns a stream of logs for a given deployment.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{projectId}/deployments/{deploymentId}/runtime-logs
paths:
  path: /v1/projects/{projectId}/deployments/{deploymentId}/runtime-logs
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
        projectId:
          schema:
            - type: string
              required: true
        deploymentId:
          schema:
            - type: string
              required: true
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
      - label: getRuntimeLogs
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logs.getRuntimeLogs({
              projectId: "<id>",
              deploymentId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/stream+json:
        schemaArray:
          - type: object
            properties:
              level:
                allOf:
                  - type: string
                    enum:
                      - error
                      - warning
                      - info
              message:
                allOf:
                  - type: string
              rowId:
                allOf:
                  - type: string
              source:
                allOf:
                  - type: string
                    enum:
                      - delimiter
                      - edge-function
                      - edge-middleware
                      - serverless
                      - request
              timestampInMs:
                allOf:
                  - type: number
              domain:
                allOf:
                  - type: string
              messageTruncated:
                allOf:
                  - type: boolean
              requestMethod:
                allOf:
                  - type: string
              requestPath:
                allOf:
                  - type: string
              responseStatusCode:
                allOf:
                  - type: number
            requiredProperties:
              - level
              - message
              - rowId
              - source
              - timestampInMs
              - domain
              - messageTruncated
              - requestMethod
              - requestPath
              - responseStatusCode
        examples:
          example:
            value:
              level: error
              message: <string>
              rowId: <string>
              source: delimiter
              timestampInMs: 123
              domain: <string>
              messageTruncated: true
              requestMethod: <string>
              requestPath: <string>
              responseStatusCode: 123
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
  deprecated: false
  type: path
components:
  schemas: {}

````