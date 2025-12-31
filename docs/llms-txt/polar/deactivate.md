# Source: https://polar.sh/docs/api-reference/license-keys/deactivate.md

# Source: https://polar.sh/docs/api-reference/customer-portal/license-keys/deactivate.md

# Source: https://polar.sh/docs/api-reference/license-keys/deactivate.md

# Source: https://polar.sh/docs/api-reference/customer-portal/license-keys/deactivate.md

# Source: https://polar.sh/docs/api-reference/license-keys/deactivate.md

# Source: https://polar.sh/docs/api-reference/customer-portal/license-keys/deactivate.md

# Source: https://polar.sh/docs/api-reference/license-keys/deactivate.md

# Source: https://polar.sh/docs/api-reference/customer-portal/license-keys/deactivate.md

# Deactivate License Key

> Deactivate a license key instance.

> This endpoint doesn't require authentication and can be safely used on a public
> client, like a desktop application or a mobile app.
> If you plan to validate a license key on a server, use the `/v1/license-keys/deactivate`
> endpoint instead.

## OpenAPI

````yaml post /v1/customer-portal/license-keys/deactivate
paths:
  path: /v1/customer-portal/license-keys/deactivate
  method: post
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              key:
                allOf:
                  - type: string
                    title: Key
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
              activation_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Activation Id
            required: true
            title: LicenseKeyDeactivate
            refIdentifier: '#/components/schemas/LicenseKeyDeactivate'
            requiredProperties:
              - key
              - organization_id
              - activation_id
        examples:
          example:
            value:
              key: <string>
              organization_id: <string>
              activation_id: <string>
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.CustomerPortal.LicenseKeys.Deactivate(ctx, components.LicenseKeyDeactivate{\n        Key: \"<key>\",\n        OrganizationID: \"<value>\",\n        ActivationID: \"<value>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar() as polar:

              polar.customer_portal.license_keys.deactivate(request={
                  "key": "<key>",
                  "organization_id": "<value>",
                  "activation_id": "<value>",
              })

              # Use the SDK ...
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            await polar.customerPortal.licenseKeys.deactivate({
              key: "<key>",
              organizationId: "<value>",
              activationId: "<value>",
            });


          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;
          use Polar\Models\Components;

          $sdk = Polar\Polar::builder()->build();

          $request = new Components\LicenseKeyDeactivate(
              key: '<key>',
              organizationId: '<value>',
              activationId: '<value>',
          );

          $response = $sdk->customerPortal->licenseKeys->deactivate(
              request: $request
          );

          if ($response->statusCode === 200) {
              // handle response
          }
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: License key activation deactivated.
        examples: {}
        description: License key activation deactivated.
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
        description: License key not found.
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