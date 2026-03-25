# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits-v2/bulk-decrement-active-slots-with-lease.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Decrement Active Slots With Lease



## OpenAPI

````yaml post /v2/concurrency_limits/decrement-with-lease
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /v2/concurrency_limits/decrement-with-lease:
    post:
      tags:
        - Concurrency Limits V2
      summary: Bulk Decrement Active Slots With Lease
      operationId: >-
        bulk_decrement_active_slots_with_lease_v2_concurrency_limits_decrement_with_lease_post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_bulk_decrement_active_slots_with_lease_v2_concurrency_limits_decrement_with_lease_post
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
    Body_bulk_decrement_active_slots_with_lease_v2_concurrency_limits_decrement_with_lease_post:
      properties:
        lease_id:
          type: string
          format: uuid
          title: Lease Id
          description: >-
            The ID of the lease corresponding to the concurrency limits to
            decrement.
      type: object
      required:
        - lease_id
      title: >-
        Body_bulk_decrement_active_slots_with_lease_v2_concurrency_limits_decrement_with_lease_post
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