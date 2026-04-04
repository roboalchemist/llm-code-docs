# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/variables/update-variable-by-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Variable By Name



## OpenAPI

````yaml patch /variables/name/{name}
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
    patch:
      tags:
        - Variables
      summary: Update Variable By Name
      operationId: update_variable_by_name_variables_name__name__patch
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VariableUpdate'
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
    VariableUpdate:
      properties:
        name:
          anyOf:
            - type: string
              maxLength: 255
              description: The name of the variable
              examples:
                - my_variable
            - type: 'null'
          title: Name
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
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Tags
          description: A list of variable tags
          examples:
            - - tag-1
              - tag-2
      additionalProperties: false
      type: object
      title: VariableUpdate
      description: Data used by the Prefect REST API to update a Variable.
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