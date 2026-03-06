# Source: https://io.net/docs/reference/sub-keys/revoke-sub-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke Sub-API Key

> Immediately revokes a sub-API key. All subsequent requests using the revoked key receive 401 Unauthorized.

<Warning>
  Revocation is **permanent and immediate**. Once revoked, the key cannot be restored. Issue a new sub-key if access needs to be reinstated.
</Warning>

Any in-flight request that was authenticated before revocation may still complete. Revocation takes effect for all new authentication attempts.


## OpenAPI

````yaml openapi/sub-keys/revoke-sub-key.json delete /v1/api-keys/sub-keys/{key_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.io.solutions
security:
  - sec0: []
paths:
  /v1/api-keys/sub-keys/{key_id}:
    delete:
      tags:
        - Sub-API Keys
      summary: Revoke Sub-API Key
      description: >-
        Immediately revokes a sub-API key by setting its expiry to the current
        time. Any subsequent request made with the revoked key will receive a
        401 Unauthorized response. This action cannot be undone.
      operationId: revoke_sub_key
      parameters:
        - name: key_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Key ID
          description: UUID of the sub-key to revoke.
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: Admin API key (io.net Intelligence)
            title: X-Api-Key
          description: Admin API key that owns the sub-key.
      responses:
        '200':
          description: Sub-key revoked successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
              example:
                status: succeeded
        '401':
          description: Unauthorized — invalid or missing API key
        '404':
          description: Sub-API key not found or not owned by this admin
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    SuccessResponse:
      type: object
      title: SuccessResponse
      properties:
        status:
          type: string
          example: succeeded
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
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````