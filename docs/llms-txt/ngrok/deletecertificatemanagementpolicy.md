# Source: https://ngrok.com/docs/api-reference/reserveddomains/deletecertificatemanagementpolicy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Remove the certificate management policy from a specific reserved domain.

# DeleteCertificateManagementPolicy



## OpenAPI

````yaml delete /reserved_domains/{id}/certificate_management_policy
openapi: 3.0.0
info:
  title: ngrok OpenAPI
  version: 1.0.0
servers:
  - url: https://api.ngrok.com
security:
  - authentication: []
paths:
  /reserved_domains/{id}/certificate_management_policy:
    delete:
      tags:
        - ReservedDomains
      summary: DeleteCertificateManagementPolicy
      description: |
        Detach the certificate management policy attached to a reserved domain.
      operationId: ReservedDomainsDeleteCertificateManagementPolicy
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
          description: >
            Detach the certificate management policy attached to a reserved
            domain.
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