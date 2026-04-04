# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/upload-client-certificate-for-egress-mtls.md

# Upload client certificate for egress mTLS

> Upload a client certificate for mTLS authentication to external origins.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/client-cert
paths:
  path: /v1/projects/{idOrName}/client-cert
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
      path:
        idOrName:
          schema:
            - type: string
              required: true
              description: The unique project identifier or the project name
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
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
              cert:
                allOf:
                  - description: The client certificate in PEM format
                    type: string
                    example: >-
                      -----BEGIN CERTIFICATE-----\\n...\\n-----END
                      CERTIFICATE-----
              key:
                allOf:
                  - description: The private key in PEM format
                    type: string
                    example: >-
                      -----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE
                      KEY-----
              ca:
                allOf:
                  - description: The certificate authority in PEM format
                    type: string
                    example: >-
                      -----BEGIN CERTIFICATE-----\\n...\\n-----END
                      CERTIFICATE-----
              origin:
                allOf:
                  - description: >-
                      The origin this certificate should be used for. If not
                      specified, the certificate will be project-wide.
                    type: string
                    example: https://api.example.com
              skipValidation:
                allOf:
                  - type: boolean
                    description: Skip validation of the certificate
            requiredProperties:
              - cert
              - key
              - ca
            additionalProperties: false
        examples:
          example:
            value:
              cert: '-----BEGIN CERTIFICATE-----\\n...\\n-----END CERTIFICATE-----'
              key: '-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----'
              ca: '-----BEGIN CERTIFICATE-----\\n...\\n-----END CERTIFICATE-----'
              origin: https://api.example.com
              skipValidation: true
    codeSamples:
      - label: uploadProjectClientCert
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.uploadProjectClientCert({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                cert: "-----BEGIN CERTIFICATE-----\\n...\\n-----END CERTIFICATE-----",
                key: "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----",
                ca: "-----BEGIN CERTIFICATE-----\\n...\\n-----END CERTIFICATE-----",
                origin: "https://api.example.com",
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
              updated:
                allOf:
                  - type: boolean
              origin:
                allOf:
                  - type: string
              certId:
                allOf:
                  - type: string
            requiredProperties:
              - updated
              - origin
              - certId
        examples:
          example:
            value:
              updated: true
              origin: <string>
              certId: <string>
        description: Client certificate uploaded successfully
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
    '402':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The account was soft-blocked for an unhandled reason.
              The account is missing a payment so payment method must be updated
        examples: {}
        description: |-
          The account was soft-blocked for an unhandled reason.
          The account is missing a payment so payment method must be updated
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The project is being transferred and uploading certificates is not
              possible
        examples: {}
        description: >-
          The project is being transferred and uploading certificates is not
          possible
    '500':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              Failed to upload the client certificate
              Failed to encrypt the private key
        examples: {}
        description: |-
          Failed to upload the client certificate
          Failed to encrypt the private key
  deprecated: false
  type: path
components:
  schemas: {}

````