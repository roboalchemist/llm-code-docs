# Source: https://docs.turso.tech/api-reference/organizations/invoices.md

# List Invoices

> Returns a list of invoices for the organization.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/invoices
paths:
  path: /v1/organizations/{organizationSlug}/invoices
  method: get
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        organizationSlug:
          schema:
            - type: string
              required: true
              description: The slug of the organization or user account.
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - all
                - upcoming
                - issued
              description: The type of invoice to retrieve.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              invoices:
                allOf:
                  - type: array
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
        examples:
          example:
            value:
              invoices:
                - invoice_number: LFONTK-00001
                  amount_due: '10.29'
                  due_date: '2024-01-01T05:00:00+00:00'
                  paid_at: '2024-01-01T05:00:00+00:00'
                  payment_failed_at: '2024-01-01T05:00:00+00:00'
                  invoice_pdf: https://assets.withorb.com/invoice/...
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````