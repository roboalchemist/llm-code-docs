# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/variables/read-variable-by-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Variable By Name



## OpenAPI

````yaml get /variables/name/{name}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /variables/name/{name}:
    get:
      tags:
        - Variables
      summary: Read Variable By Name
      operationId: read_variable_by_name_variables_name__name__get
      parameters:
        - name: name
          in: path
          required: true
          schema:
            type: string
            title: Name
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
                $ref: '#/components/schemas/Variable'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Variable:
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
        name:
          type: string
          maxLength: 255
          title: Name
          description: The name of the variable
          examples:
            - my-variable
        value:
          anyOf:
            - type: string
            - type: integer
            - type: boolean
            - type: number
            - additionalProperties: true
              type: object
            - items: {}
              type: array
            - type: 'null'
          title: Value
          description: The value of the variable
          examples:
            - my-value
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of variable tags
          examples:
            - - tag-1
              - tag-2
      type: object
      required:
        - name
        - value
        - id
        - created
        - updated
      title: Variable
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