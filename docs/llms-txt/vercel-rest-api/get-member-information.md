# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-member-information.md

# Get Member Information

> Returns the member role and other information for a given member ID ("user_id" claim in the SSO OIDC token).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/member/{memberId}
paths:
  path: /v1/installations/{integrationConfigurationId}/member/{memberId}
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
        integrationConfigurationId:
          schema:
            - type: string
              required: true
        memberId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-member
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getMember({
              integrationConfigurationId: "<id>",
              memberId: "<id>",
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
              id:
                allOf:
                  - type: string
              role:
                allOf:
                  - type: string
                    enum:
                      - ADMIN
                      - USER
                    description: >-
                      "The `ADMIN` role, by default, is provided to users
                      capable of installing integrations, while the `USER` role
                      can be granted to Vercel users with the Vercel `Billing`
                      or Vercel `Viewer` role, which are considered to be
                      Read-Only roles."
            requiredProperties:
              - id
              - role
        examples:
          example:
            value:
              id: <string>
              role: ADMIN
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