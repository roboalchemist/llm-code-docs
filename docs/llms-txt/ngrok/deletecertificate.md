# Source: https://ngrok.com/docs/api-reference/reserveddomains/deletecertificate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Delete the TLS certificate associated with a specific reserved domain.

# DeleteCertificate



## OpenAPI

````yaml delete /reserved_domains/{id}/certificate
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /reserved_domains/{id}/certificate:
    delete:
      tags:
        - ReservedDomains
      summary: DeleteCertificate
      description: |
        Detach the certificate attached to a reserved domain.
      operationId: ReservedDomainsDeleteCertificate
      parameters:
        - $ref: '#/components/parameters/ngrokVersion'
        - name: id
          description: |
            a resource identifier
          in: path
          required: true
          schema:
            type: string
      responses:
        '204':
          description: |
            Detach the certificate attached to a reserved domain.
components:
  parameters:
    ngrokVersion:
      name: ngrok-version
      in: header
      required: true
      schema:
        type: integer
        default: 2
  securitySchemes:
    authentication:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).