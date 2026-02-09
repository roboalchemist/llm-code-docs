# Source: https://docs.turso.tech/api-reference/organizations/invoices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# List Invoices

> Returns a list of invoices for the organization.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/invoices \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/invoices
openapi: 3.0.1
info:
  title: Turso Platform API
  description: API description here
  license:
    name: MIT
  version: 0.1.0
servers:
  - url: https://api.turso.tech
    description: Turso's Platform API
security: []
paths:
  /v1/organizations/{organizationSlug}/invoices:
    get:
      summary: List Invoices
      description: Returns a list of invoices for the organization.
      operationId: listOrganizationInvoices
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - name: type
          in: query
          schema:
            type: string
            enum:
              - all
              - upcoming
              - issued
          description: The type of invoice to retrieve.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  invoices:
                    type: array
                    description: The list of invoices for the organization.
                    items:
                      type: object
                      properties:
                        invoice_number:
                          type: string
                          description: The unique ID for the invoice.
                          example: LFONTK-00001
                        amount_due:
                          type: string
                          description: The formatted price in USD for the invoice.
                          example: '10.29'
                        due_date:
                          type: string
                          description: The due date for the invoice.
                          example: '2024-01-01T05:00:00+00:00'
                        paid_at:
                          type: string
                          description: The date the invoice was paid.
                          example: '2024-01-01T05:00:00+00:00'
                        payment_failed_at:
                          type: string
                          description: The date the invoice payment last failed.
                          example: '2024-01-01T05:00:00+00:00'
                        invoice_pdf:
                          type: string
                          description: The link to the invoice PDF you can download.
                          example: https://assets.withorb.com/invoice/...
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.

````