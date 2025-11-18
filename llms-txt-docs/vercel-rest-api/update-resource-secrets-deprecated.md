# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-resource-secrets-deprecated.md

# Update Resource Secrets (Deprecated)

> This endpoint is deprecated and replaced with the endpoint [Update Resource Secrets](#update-resource-secrets). <br/> This endpoint updates the secrets of a resource. If a resource has projects connected, the connected secrets are updated with the new secrets. The old secrets may still be used by existing connected projects because they are not automatically redeployed. Redeployment is a manual action and must be completed by the user. All new project connections will use the new secrets.<br/> <br/> Use cases for this endpoint:<br/> <br/> - Resetting the credentials of a database in the partner. If the user requests the credentials to be updated in the partner’s application, the partner post the new set of secrets to Vercel, the user should redeploy their application and the expire the old credentials.<br/>

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets
  method: put
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
        integrationProductIdOrSlug:
          schema:
            - type: string
              required: true
        resourceId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - name
                        - value
                      properties:
                        name:
                          type: string
                        value:
                          type: string
                        prefix:
                          type: string
                        environmentOverrides:
                          type: object
                          description: >-
                            A map of environments to override values for the
                            secret, used for setting different values across
                            deployments in production, preview, and development
                            environments. Note: the same value will be used for
                            all deployments in the given environment.
                          properties:
                            development:
                              type: string
                              description: Value used for development environment.
                            preview:
                              type: string
                              description: Value used for preview environment.
                            production:
                              type: string
                              description: Value used for production environment.
                      additionalProperties: false
              partial:
                allOf:
                  - type: boolean
                    description: If true, will only update the provided secrets
            required: true
            requiredProperties:
              - secrets
            additionalProperties: false
        examples:
          example:
            value:
              secrets:
                - name: <string>
                  value: <string>
                  prefix: <string>
                  environmentOverrides:
                    development: <string>
                    preview: <string>
                    production: <string>
              partial: true
    codeSamples:
      - label: update-resource-secrets
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateResourceSecrets({
              integrationConfigurationId: "<id>",
              integrationProductIdOrSlug: "<value>",
              resourceId: "<id>",
              requestBody: {
                secrets: [],
              },
            });


          }

          run();
  response:
    '201': {}
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
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '409': {}
    '422': {}
  deprecated: false
  type: path
components:
  schemas: {}

````