# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/delete-client-certificate-for-egress-mtls.md

# Delete client certificate for egress mTLS

> Delete a client certificate for mTLS authentication to external origins.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/projects/{idOrName}/client-cert/{certId}
paths:
  path: /v1/projects/{idOrName}/client-cert/{certId}
  method: delete
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
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
        certId:
          schema:
            - type: string
              required: true
              description: The certificate identifier
              example: cert_a1b2c3d4e5f6g7h8
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
      - label: deleteProjectClientCert
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.deleteProjectClientCert({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              certId: "cert_a1b2c3d4e5f6g7h8",
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
              origin:
                allOf:
                  - type: string
              certId:
                allOf:
                  - type: string
            requiredProperties:
              - origin
              - certId
        examples:
          example:
            value:
              origin: <string>
              certId: <string>
        description: Client certificate deleted successfully
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The certificate could not be found
        examples: {}
        description: The certificate could not be found
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The project is being transferred and deleting certificates is not
              possible
        examples: {}
        description: >-
          The project is being transferred and deleting certificates is not
          possible
  deprecated: false
  type: path
components:
  schemas: {}

````