# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/delete.md

# Source: https://polar.sh/docs/api-reference/files/delete.md

# Source: https://polar.sh/docs/api-reference/discounts/delete.md

# Source: https://polar.sh/docs/api-reference/customers/delete.md

# Source: https://polar.sh/docs/api-reference/custom-fields/delete.md

# Source: https://polar.sh/docs/api-reference/checkout-links/delete.md

# Source: https://polar.sh/docs/api-reference/benefits/delete.md

# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/delete.md

# Source: https://polar.sh/docs/api-reference/files/delete.md

# Source: https://polar.sh/docs/api-reference/discounts/delete.md

# Source: https://polar.sh/docs/api-reference/customers/delete.md

# Source: https://polar.sh/docs/api-reference/custom-fields/delete.md

# Source: https://polar.sh/docs/api-reference/checkout-links/delete.md

# Source: https://polar.sh/docs/api-reference/benefits/delete.md

# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/delete.md

# Source: https://polar.sh/docs/api-reference/files/delete.md

# Source: https://polar.sh/docs/api-reference/discounts/delete.md

# Source: https://polar.sh/docs/api-reference/customers/delete.md

# Source: https://polar.sh/docs/api-reference/custom-fields/delete.md

# Source: https://polar.sh/docs/api-reference/checkout-links/delete.md

# Source: https://polar.sh/docs/api-reference/benefits/delete.md

# Source: https://polar.sh/docs/api-reference/checkout-links/delete.md

# Source: https://polar.sh/docs/api-reference/benefits/delete.md

# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/delete.md

# Source: https://polar.sh/docs/api-reference/files/delete.md

# Source: https://polar.sh/docs/api-reference/discounts/delete.md

# Source: https://polar.sh/docs/api-reference/customers/delete.md

# Source: https://polar.sh/docs/api-reference/custom-fields/delete.md

# Source: https://polar.sh/docs/api-reference/checkout-links/delete.md

# Source: https://polar.sh/docs/api-reference/benefits/delete.md

# Delete Benefit

> Delete a benefit.

> [!WARNING]
> Every grants associated with the benefit will be revoked.
> Users will lose access to the benefit.

**Scopes**: `benefits:write`

## OpenAPI

````yaml delete /v1/benefits/{id}
paths:
  path: /v1/benefits/{id}
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
        id:
          schema:
            - type: string
              required: true
              title: Id
              description: The benefit ID.
              format: uuid4
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Benefits.Delete(ctx, \"<value>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              polar.benefits.delete(id="<value>")

              # Use the SDK ...
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            await polar.benefits.delete({
              id: "<value>",
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



          $response = $sdk->benefits->delete(
              id: '<value>'
          );

          if ($response->statusCode === 200) {
              // handle response
          }
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Benefit deleted.
        examples: {}
        description: Benefit deleted.
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: NotPermitted
                    title: Error
                    examples:
                      - NotPermitted
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: NotPermitted
            refIdentifier: '#/components/schemas/NotPermitted'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: NotPermitted
              detail: <string>
        description: This benefit is not deletable.
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
        description: Benefit not found.
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