# Source: https://polar.sh/docs/api-reference/orders/post-invoice.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/post-invoice.md

# Generate Order Invoice

> Trigger generation of an order's invoice.

**Scopes**: `customer_portal:read` `customer_portal:write`

## OpenAPI

````yaml post /v1/customer-portal/orders/{id}/invoice
paths:
  path: /v1/customer-portal/orders/{id}/invoice
  method: post
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: customer session
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Customer session tokens are specific tokens that are used to
                authenticate customers on your organization. You can create
                those sessions programmatically using the [Create Customer
                Session
                endpoint](/api-reference/customer-portal/sessions/create).
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              title: Id
              description: The order ID.
              format: uuid4
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"os\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.CustomerPortal.Orders.GenerateInvoice(ctx, operations.CustomerPortalOrdersGenerateInvoiceSecurity{\n        CustomerSession: os.Getenv(\"POLAR_CUSTOMER_SESSION\"),\n    }, \"<value>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Any != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          import polar_sdk
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_portal.orders.generate_invoice(security=polar_sdk.CustomerPortalOrdersGenerateInvoiceSecurity(
                  customer_session="<YOUR_BEARER_TOKEN_HERE>",
              ), id="<value>")

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.customerPortal.orders.generateInvoice({
              customerSession: process.env["POLAR_CUSTOMER_SESSION"] ?? "",
            }, {
              id: "<value>",
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: >-
          declare(strict_types=1);


          require 'vendor/autoload.php';


          use Polar;

          use Polar\Models\Operations;


          $sdk = Polar\Polar::builder()->build();



          $requestSecurity = new
          Operations\CustomerPortalOrdersGenerateInvoiceSecurity(
              customerSession: '<YOUR_BEARER_TOKEN_HERE>',
          );


          $response = $sdk->customerPortal->orders->generateInvoice(
              security: $requestSecurity,
              id: '<value>'

          );


          if ($response->any !== null) {
              // handle response
          }
  response:
    '202':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: MissingInvoiceBillingDetails
                    title: Error
                    examples:
                      - MissingInvoiceBillingDetails
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: MissingInvoiceBillingDetails
            refIdentifier: '#/components/schemas/MissingInvoiceBillingDetails'
            requiredProperties:
              - error
              - detail
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: NotPaidOrder
                    title: Error
                    examples:
                      - NotPaidOrder
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: NotPaidOrder
            refIdentifier: '#/components/schemas/NotPaidOrder'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: MissingInvoiceBillingDetails
              detail: <string>
        description: Order is not paid or is missing billing name or address.
  deprecated: false
  type: path
components:
  schemas: {}

````