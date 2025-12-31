# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/update-deployment-integration-action.md

# Update deployment integration action

> Updates the deployment integration action for the specified integration installation

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/integrations/{integrationConfigurationId}/resources/{resourceId}/actions/{action}
paths:
  path: >-
    /v1/deployments/{deploymentId}/integrations/{integrationConfigurationId}/resources/{resourceId}/actions/{action}
  method: patch
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
        deploymentId:
          schema:
            - type: string
              required: true
        integrationConfigurationId:
          schema:
            - type: string
              required: true
        resourceId:
          schema:
            - type: string
              required: true
        action:
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
              status:
                allOf:
                  - type: string
                    enum:
                      - running
                      - succeeded
                      - failed
              statusText:
                allOf:
                  - type: string
              statusUrl:
                allOf:
                  - type: string
                    format: uri
                    pattern: '^https?://|^sso:'
              outcomes:
                allOf:
                  - type: array
                    items:
                      oneOf:
                        - type: object
                          properties:
                            kind:
                              type: string
                            secrets:
                              type: array
                              items:
                                type: object
                                properties:
                                  name:
                                    type: string
                                  value:
                                    type: string
                                required:
                                  - name
                                  - value
                                additionalProperties: false
                          required:
                            - kind
                            - secrets
                          additionalProperties: false
            additionalProperties: false
        examples:
          example:
            value:
              status: running
              statusText: <string>
              statusUrl: <string>
              outcomes:
                - kind: <string>
                  secrets:
                    - name: <string>
                      value: <string>
    codeSamples:
      - label: update-integration-deployment-action
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.deployments.updateIntegrationDeploymentAction({
              deploymentId: "<id>",
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
              action: "<value>",
            });


          }

          run();
      - label: update-integration-deployment-action
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.integrations.updateIntegrationDeploymentAction({
              deploymentId: "<id>",
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
              action: "<value>",
            });


          }

          run();
  response:
    '202': {}
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
  deprecated: false
  type: path
components:
  schemas: {}

````