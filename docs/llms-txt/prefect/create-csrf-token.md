# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/create-csrf-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Csrf Token

> Create or update a CSRF token for a client



## OpenAPI

````yaml get /csrf-token
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /csrf-token:
    get:
      summary: Create Csrf Token
      description: Create or update a CSRF token for a client
      operationId: create_csrf_token_csrf_token_get
      parameters:
        - name: client
          in: query
          required: true
          schema:
            type: string
            description: The client to create a CSRF token for
            title: Client
          description: The client to create a CSRF token for
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
                $ref: '#/components/schemas/CsrfToken'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    CsrfToken:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        token:
          type: string
          title: Token
          description: The CSRF token
        client:
          type: string
          title: Client
          description: The client id associated with the CSRF token
        expiration:
          type: string
          format: date-time
          title: Expiration
          description: The expiration time of the CSRF token
      type: object
      required:
        - token
        - client
        - expiration
        - id
        - created
        - updated
      title: CsrfToken
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