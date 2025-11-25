# Source: https://polar.sh/docs/api-reference/orders/get-invoice.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/get-invoice.md

# Source: https://polar.sh/docs/api-reference/orders/get-invoice.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/get-invoice.md

# Get Order Invoice

> Get an order's invoice data.

**Scopes**: `customer_portal:read` `customer_portal:write`

## OpenAPI

````yaml get /v1/customer-portal/orders/{id}/invoice
paths:
  path: /v1/customer-portal/orders/{id}/invoice
  method: get
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
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"os\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.CustomerPortal.Orders.Invoice(ctx, operations.CustomerPortalOrdersInvoiceSecurity{\n        CustomerSession: os.Getenv(\"POLAR_CUSTOMER_SESSION\"),\n    }, \"<value>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.CustomerOrderInvoice != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          import polar_sdk
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_portal.orders.invoice(security=polar_sdk.CustomerPortalOrdersInvoiceSecurity(
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
            const result = await polar.customerPortal.orders.invoice({
              customerSession: process.env["POLAR_CUSTOMER_SESSION"] ?? "",
            }, {
              id: "<value>",
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;
          use Polar\Models\Operations;

          $sdk = Polar\Polar::builder()->build();


          $requestSecurity = new Operations\CustomerPortalOrdersInvoiceSecurity(
              customerSession: '<YOUR_BEARER_TOKEN_HERE>',
          );

          $response = $sdk->customerPortal->orders->invoice(
              security: $requestSecurity,
              id: '<value>'

          );

          if ($response->customerOrderInvoice !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              url:
                allOf:
                  - type: string
                    title: Url
                    description: The URL to the invoice.
            title: CustomerOrderInvoice
            description: Order's invoice data.
            refIdentifier: '#/components/schemas/CustomerOrderInvoice'
            requiredProperties:
              - url
        examples:
          example:
            value:
              url: <string>
        description: Successful Response
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
        description: Order not found.
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