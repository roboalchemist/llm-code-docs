# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-prepayment-balances.md

# Submit Prepayment Balances

> Sends the prepayment balances. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/balance
paths:
  path: /v1/installations/{integrationConfigurationId}/billing/balance
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
        integrationConfigurationId:
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
              timestamp:
                allOf:
                  - description: >-
                      Server time of your integration, used to determine the
                      most recent data for race conditions & updates. Only the
                      latest usage data for a given day, week, and month will be
                      kept.
                    type: string
                    format: date-time
              balances:
                allOf:
                  - type: array
                    items:
                      type: object
                      description: A credit balance for a particular token type
                      properties:
                        resourceId:
                          type: string
                          description: >-
                            Partner's resource ID, exclude if credits are tied
                            to the installation and not an individual resource.
                        credit:
                          type: string
                          description: >-
                            A human-readable description of the credits the user
                            currently has, e.g. \"2,000 Tokens\"
                        nameLabel:
                          type: string
                          description: >-
                            The name of the credits, for display purposes, e.g.
                            \"Tokens\"
                        currencyValueInCents:
                          type: number
                          description: >-
                            The dollar value of the credit balance, in USD and
                            provided in cents, which is used to trigger
                            automatic purchase thresholds.
                      required:
                        - currencyValueInCents
                      additionalProperties: false
            requiredProperties:
              - timestamp
              - balances
            additionalProperties: false
        examples:
          example:
            value:
              timestamp: '2023-11-07T05:31:56Z'
              balances:
                - resourceId: <string>
                  credit: <string>
                  nameLabel: <string>
                  currencyValueInCents: 123
    codeSamples:
      - label: submit-prepayment-balances
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.submitPrepaymentBalances({
              integrationConfigurationId: "<id>",
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
  deprecated: false
  type: path
components:
  schemas: {}

````