# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-resource.md

# Update Resource

> This endpoint updates an existing resource in the installation. All parameters are optional, allowing partial updates.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/resources/{resourceId}
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
        integrationConfigurationId:
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
              ownership:
                allOf:
                  - type: string
                    enum:
                      - owned
                      - linked
                      - sandbox
              name:
                allOf:
                  - type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - ready
                      - pending
                      - onboarding
                      - suspended
                      - resumed
                      - uninstalled
                      - error
              metadata:
                allOf:
                  - type: object
                    additionalProperties: true
              billingPlan:
                allOf:
                  - type: object
                    required:
                      - id
                      - type
                      - name
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                        enum:
                          - prepayment
                          - subscription
                      name:
                        type: string
                      description:
                        type: string
                      paymentMethodRequired:
                        type: boolean
                      cost:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      highlightedDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      effectiveDate:
                        type: string
                    additionalProperties: true
              notification:
                allOf:
                  - type: object
                    required:
                      - level
                      - title
                    properties:
                      level:
                        type: string
                        enum:
                          - info
                          - warn
                          - error
                      title:
                        type: string
                      message:
                        type: string
                      href:
                        type: string
                        format: uri
              extras:
                allOf:
                  - type: object
                    additionalProperties: true
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
            additionalProperties: false
        examples:
          example:
            value:
              ownership: owned
              name: <string>
              status: ready
              metadata: {}
              billingPlan:
                id: <string>
                type: prepayment
                name: <string>
                description: <string>
                paymentMethodRequired: true
                cost: <string>
                details:
                  - label: <string>
                    value: <string>
                highlightedDetails:
                  - label: <string>
                    value: <string>
                effectiveDate: <string>
              notification:
                level: info
                title: <string>
                message: <string>
                href: <string>
              extras: {}
              secrets:
                - name: <string>
                  value: <string>
                  prefix: <string>
                  environmentOverrides:
                    development: <string>
                    preview: <string>
                    production: <string>
    codeSamples:
      - label: update-resource
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.updateResource({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
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
              name:
                allOf:
                  - type: string
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: <string>
        description: ''
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