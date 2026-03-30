# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits-v2/renew-concurrency-lease.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Renew Concurrency Lease



## OpenAPI

````yaml post /v2/concurrency_limits/leases/{lease_id}/renew
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /v2/concurrency_limits/leases/{lease_id}/renew:
    post:
      tags:
        - Concurrency Limits V2
      summary: Renew Concurrency Lease
      operationId: >-
        renew_concurrency_lease_v2_concurrency_limits_leases__lease_id__renew_post
      parameters:
        - name: lease_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The ID of the lease to renew
            title: Lease Id
          description: The ID of the lease to renew
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_renew_concurrency_lease_v2_concurrency_limits_leases__lease_id__renew_post
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_renew_concurrency_lease_v2_concurrency_limits_leases__lease_id__renew_post:
      properties:
        lease_duration:
          type: number
          maximum: 86400
          minimum: 60
          title: Lease Duration
          description: The duration of the lease in seconds.
          default: 300
      type: object
      title: >-
        Body_renew_concurrency_lease_v2_concurrency_limits_leases__lease_id__renew_post
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).