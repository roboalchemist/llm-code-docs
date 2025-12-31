# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-firewall-actions-by-project.md

# Read Firewall Actions by Project

> Retrieve firewall actions for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/events
paths:
  path: /v1/security/firewall/events
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security: []
    parameters:
      path: {}
      query:
        projectId:
          schema:
            - type: string
              required: true
        startTimestamp:
          schema:
            - type: number
              required: false
        endTimestamp:
          schema:
            - type: number
              required: false
        hosts:
          schema:
            - type: string
              required: false
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get_/v1/security/firewall/events
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel();

          async function run() {
            const result = await vercel.security.getV1SecurityFirewallEvents({
              projectId: "<id>",
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
              actions:
                allOf:
                  - items:
                      properties:
                        startTime:
                          type: string
                        endTime:
                          type: string
                        isActive:
                          type: boolean
                        action_type:
                          type: string
                        host:
                          type: string
                        public_ip:
                          type: string
                        count:
                          type: number
                      required:
                        - startTime
                        - endTime
                        - isActive
                        - action_type
                        - host
                        - public_ip
                        - count
                      type: object
                    type: array
            requiredProperties:
              - actions
        examples:
          example:
            value:
              actions:
                - startTime: <string>
                  endTime: <string>
                  isActive: true
                  action_type: <string>
                  host: <string>
                  public_ip: <string>
                  count: 123
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````