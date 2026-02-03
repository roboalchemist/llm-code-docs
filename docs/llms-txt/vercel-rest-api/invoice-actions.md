# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/invoice-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoice Actions

> This endpoint allows the partner to request a refund for an invoice to Vercel. The invoice is created using the [Submit Invoice API](#submit-invoice-api).



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}/actions
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}/actions:
    post:
      tags:
        - marketplace
      summary: Invoice Actions
      description: >-
        This endpoint allows the partner to request a refund for an invoice to
        Vercel. The invoice is created using the [Submit Invoice
        API](#submit-invoice-api).
      operationId: update-invoice
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
        - name: invoiceId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - refund
                    reason:
                      type: string
                      description: Refund reason.
                    total:
                      description: >-
                        The total amount to be refunded. Must be less than or
                        equal to the total amount of the invoice.
                      type: string
                      pattern: ^[0-9]+(\\.[0-9]+)?$
                  required:
                    - action
                    - reason
                    - total
                  additionalProperties: false
        required: true
      responses:
        '204':
          description: ''
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '409':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````