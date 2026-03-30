# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-capabilities/read-available-block-capabilities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Available Block Capabilities

> Get available block capabilities.

For more information, see https://docs.prefect.io/v3/concepts/blocks.



## OpenAPI

````yaml get /block_capabilities/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_capabilities/:
    get:
      tags:
        - Block capabilities
      summary: Read Available Block Capabilities
      description: |-
        Get available block capabilities.

        For more information, see https://docs.prefect.io/v3/concepts/blocks.
      operationId: read_available_block_capabilities_block_capabilities__get
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string
                title: >-
                  Response Read Available Block Capabilities Block Capabilities 
                  Get
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
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