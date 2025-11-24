# Source: https://polar.sh/docs/api-reference/customers/delete-external.md

# Delete Customer by External ID

> Delete a customer by external ID.

Immediately cancels any active subscriptions and revokes any active benefits.

**Scopes**: `customers:write`

## OpenAPI

````yaml delete /v1/customers/external/{external_id}
paths:
  path: /v1/customers/external/{external_id}
  method: delete
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: access token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                You can generate an **Organization Access Token** from your
                organization's settings.
          cookie: {}
    parameters:
      path:
        external_id:
          schema:
            - type: string
              required: true
              title: External Id
              description: The customer external ID.
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Customers.DeleteExternal(ctx, \"<id>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              polar.customers.delete_external(external_id="<id>")

              # Use the SDK ...
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            await polar.customers.deleteExternal({
              externalId: "<id>",
            });


          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();



          $response = $sdk->customers->deleteExternal(
              externalId: '<id>'
          );

          if ($response->statusCode === 200) {
              // handle response
          }
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Customer deleted.
        examples: {}
        description: Customer deleted.
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: ResourceNotFound
                    title: Error
                    examples:
                      - ResourceNotFound
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: ResourceNotFound
            refIdentifier: '#/components/schemas/ResourceNotFound'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: ResourceNotFound
              detail: <string>
        description: Customer not found.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````